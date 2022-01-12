# -*- coding: gb18030 -*-

import BigWorld
from bwdebug import *
import csdefine
import csstatus
from NPC import NPC

from Resource.SkillTrainerLoader import SkillTrainerLoader
g_skillTrainerList = SkillTrainerLoader.instance()

from Resource.GoodsLoader import GoodsLoader
g_goods = GoodsLoader.instance()

import items
g_items = items.instance()

class EidolonNPC( NPC ):
	"""
	小精灵
	"""
	def __init__( self ):
		"""
		初始化从XML读取信息
		"""
		NPC.__init__( self )
		self.attrTrainInfo = set()	# 技能学习数据
		self.attrInvoices = {}
		
	def load( self, section ):
		"""
		读取商品列表配置文件，初始化商品及相关数值

		@param section: 配置文件的section
		@type  section: Language.PyDataSection
		@return: 		无
		"""
		NPC.load( self, section )	# 先加载基层的配置
		self.attrTrainInfo = g_skillTrainerList.get( self.className )
		self.initGoods()
	
	def onLoadEntityProperties_( self, section ):
		"""
		virtual method. template method, call by GameObject::load().
		根据给定的section，初始化（读取）entity属性。
		注：只有在createEntity()时需要把值自动对entity进行初始化时才有必要放到此函数初始化，
		也就是说，这里初始化的所有属性都必须是在相应的.def中声明过的。

		@param section: PyDataSection, 根据一定的格式存储了entity属性的section
		"""
		NPC.onLoadEntityProperties_( self, section )

		self.setEntityProperty( "invSellPercent",	section["invSellPercent"].asFloat )		# 出售比例；商人NPC专用
		self.setEntityProperty( "invBuyPercent",	section["invBuyPercent"].asFloat )		# 回收比例；商人NPC专用
		self.setEntityProperty( "invRestoreTime",	section["invRestoreTime"].asFloat )		# 商品恢复时间；商人NPC专用
		self.setEntityProperty( "isJoinRevenue",	section.readInt("isJoinRevenue") )		# 是否参与税收
		
	def validLearn( self, player, skillID ):
		"""
		"""
		return skillID in self.attrTrainInfo
		
	def gossipWith( self, selfEntity, playerEntity, dlgKey ):
		"""
		与玩家对话；未声明(不能声明)的方法，因此重载此方法的上层如果需要访问自己的私有属性请自己判断self.isReal()。

		@param   selfEntity: 与自己对应的Entity实例，传这个参数是为了方便以后的扩充
		@type    selfEntity: Entity
		@param playerEntity: 说话的玩家
		@type  playerEntity: Entity
		@param       dlgKey: 对话关键字
		@type        dlgKey: str
		@return: 无
		"""
		NPC.gossipWith( self, selfEntity, playerEntity, dlgKey )
		
	def canUseBank( self, srcEntity, roleEntity ):
		"""
		在此验证玩家的vip级别和是否能够使用相关功能
		
		@param srcEntity : 此脚本对应的entity
		@param roleEntity : 玩家entity，目前只有玩家才能使用钱庄
		"""
		return csstatus.BANK_CAN_USE
	
	# --------------------------------------------------------------------------
	# 商人功能
	# --------------------------------------------------------------------------
		
	def initGoods( self ):
		"""
		初始化每个商人的商品
		"""
		g_goods.initGoods( self, self.className )

	def sellTo( self, selfEntity, playerEntity, argIndex, argAmount ):
		"""
		商人把东西卖给玩家

		@param 	 selfEntity	 : NPC自身实例
		@param   playerEntity: 玩家
		@param   argIndex	 : 要买第几个货物
		@param   argAmount	 : 要买的数量
		@return: 			无
		"""
		# 取得所要买的商品
		try:
			objInvoice = self.attrInvoices[argIndex]
		except:
			ERROR_MSG( "%s(%i): srcEntityId = %i, no such invoice(argIndex = %i)." % (selfEntity.getName(), selfEntity.id, playerEntity.id, argIndex) )
			return

		srcItem = objInvoice.getSrcItem()

		if srcItem.getStackable() < argAmount:
			# 无论是否可叠加的物品，如果数量大于叠加上限则出错
			ERROR_MSG( "stackable less then sell amount" )
			return

		# 现在开始卖商品了
		if objInvoice.getMaxAmount() > 0 and argAmount > objInvoice.getAmount():	# 商品有数量限制
			playerEntity.client.onStatusMessage( csstatus.GOODS_IS_NONE_1, "" )
			ERROR_MSG( "%s(%i): %s(%i) buy %i '%s', %i only." % ( selfEntity.getName(), selfEntity.id, playerEntity.playerName, playerEntity.id, srcItem.id, argAmount, objInvoice.getAmount() ) )
			return	# 没这么多货，不卖

		newInvoice = objInvoice.copy()
		#itemData.setAmount( argAmount )
		self.onSellItem( selfEntity, playerEntity, newInvoice, argIndex, argAmount )


	def onSellItem( self, selfEntity, playerEntity, newInvoice, argIndex, argAmount ):
		"""
		销售某物品事件
		"""
		playerEntity.buyFromNPC( selfEntity, newInvoice, argIndex, argAmount )

	def sellArrayTo( self, selfEntity, playerEntity, argIndices, argAmountList ):
		"""
		Exposed method
		商人把东西卖给玩家

		@param 	 selfEntity	  : NPC自身实例
		@param   playerEntity : 玩家
		@param   argIndices  : 要买的哪个商品
		@type    argIndices  : ARRAY <of> UINT16	</of>
		@param   argAmountList: 要买的数量
		@type    argAmountList: ARRAY <of> UINT16	</of>
		@return: 			无
		"""
		# 取得所要买的商品
		if playerEntity.actionSign( csdefine.ACTION_FORBID_TALK ):				#判断是否能跟NPC对话 完成操作
			return
		invoiceItems = []
		indices = []
		amountList = []
		totalAmount = {}

		for argIndex, argAmount in zip(argIndices, argAmountList):
			try:
				objInvoice = self.attrInvoices[argIndex]
			except:
				ERROR_MSG( "%s(%i): srcEntityId = %i, no such invoice(argIndex = %i)." % (selfEntity.getName(), selfEntity.id, playerEntity.id, argIndex) )
				return
			# 统计各类物品的购买总数
			if argIndex in totalAmount:
				totalAmount[argIndex] += argAmount
			else:
				totalAmount[argIndex] = argAmount
			srcItem = objInvoice.getSrcItem()
			if srcItem.getStackable() < argAmount:
				# 无论是否可叠加的物品，如果数量大于叠加上限则出错
				ERROR_MSG( "stackable less then sell amount" )
				return

			INFO_MSG("%s try to buy %d '%s'from'%s', %d remain.it's maxAmount is %d." % ( playerEntity.getName(), totalAmount[argIndex], srcItem.name(), selfEntity.getName(), objInvoice.getAmount(), objInvoice.getMaxAmount() ) )
			if objInvoice.getMaxAmount() > 0:	# 商品有数量限制
				if objInvoice.getAmount() <= 0:
					playerEntity.client.onStatusMessage( csstatus.GOODS_IS_NONE_2, str(( srcItem.name(), )) )
					selfEntity.sellToCB( argIndex, 0, playerEntity.id )	# 添加这句是为了通知客户端商品已被别人买光
					ERROR_MSG( "%s(%i): %s(%i) buy %i '%s', %i only." % ( selfEntity.getName(), selfEntity.id, playerEntity.playerName, playerEntity.id, srcItem.id, argAmount, objInvoice.getAmount() ) )
					return	# 没货，不卖
				elif totalAmount[argIndex] > objInvoice.getAmount():
					playerEntity.client.onStatusMessage( csstatus.GOODS_NOT_ENOUGH, str(( srcItem.name(), )) )
					ERROR_MSG( "%s(%i): %s(%i) buy %i '%s', %i only." % ( selfEntity.getName(), selfEntity.id, playerEntity.playerName, playerEntity.id, srcItem.id, argAmount, objInvoice.getAmount() ) )
					return	# 没这么多货，不卖

			invoiceData = objInvoice.copy()
			#itemData.setAmount( argAmount )
			invoiceItems.append( invoiceData )
			indices.append( argIndex )
			amountList.append( argAmount )


		if len( invoiceItems ) > 0:
			self.onSellItems( selfEntity, playerEntity, invoiceItems, indices, amountList )

	def onSellItems( self, selfEntity, playerEntity, invoiceItems, argIndices, argAmountList ):
		"""
		销售某类物品事件
		"""
		playerEntity.buyArrayFromNPC( selfEntity, invoiceItems, argIndices, argAmountList )

	def buyFrom( self, selfEntity, playerEntity, argUid, argAmount ):
		"""
		商人从玩家身上收购东西

		@param 	 selfEntity	  	: NPC自身实例
		@param   playerEntity	: 玩家
		@param   argUid			: 要买的哪个商品
		@type    argUid			: INT64
		@param   argAmount		: 要买的数量
		@type    argAmount		: UINT16
		@return					: 无
		"""
		playerEntity.sellToNPC( selfEntity, argUid, argAmount )

	def buyArrayFrom( self, selfEntity, playerEntity, argUidList, argAmountList ):
		"""
		Exposed method
		商人从玩家身上收购大量东西；
		参数列表里的每一个元素对应一个物品所在背包、标识和数量。
		收购规则：所有物品都存在且可以卖以及卖出总价值与玩家身上金钱总和不会超过玩家允许携带的金钱总数时，允许出售，否则不允许出售。

		@param 	 selfEntity	  : NPC自身实例
		@param   playerEntity : 玩家
		@param  argUidList: 要买的哪个商品
		@type   argUidList: ARRAY OF UINT64
		@param  argAmountList: 要买的数量
		@type   argAmountList: ARRAY OF UINT16
		@return:               无
		"""
		if playerEntity.actionSign( csdefine.ACTION_FORBID_TALK ):				#判断是否能跟NPC对话 完成操作
			return
		playerEntity.sellArrayToNPC( selfEntity, argUidList, argAmountList )