# -*- coding: gb18030 -*-
#
# $Id: Buff_107001.py,v 1.7 2008-08-11 07:55:59 kebiao Exp $

"""
持续性效果
"""

import BigWorld
import csdefine
import csstatus
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal
from Function import newUID
from Domain_Fight import g_fightMgr

class Buff_21002( Buff_Normal ):
	"""
	example:群近攻，增法攻	对自身使用，持续15秒，每3秒一次对5米范围内的最多10个敌对目标造成一次伤害

	"""
	def __init__( self ):
		"""
		构造函数。
		"""
		Buff_Normal.__init__( self )
		self._param = { "p1" : 0 }#攻击力

	def init( self, dict ):
		"""
		读取技能配置
		@param dict: 配置数据
		@type  dict: python dict
		"""
		Buff_Normal.init( self, dict )
		self._param["p1"] = int( int( dict[ "Param1" ] if len( dict[ "Param1" ] ) > 0 else 0 ) )
		self._radius = float( dict[ "Param2" ] )
		self._maxCount = int( dict[ "Param3" ] )
		
	def doBegin( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		效果开始的处理。

		@param receiver: 效果要影响的实体
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: None
		"""
		Buff_Normal.doBegin( self, receiver, buffData )
		id = buffData["caster"]
		if BigWorld.entities.has_key( id ):
			caster = BigWorld.entities[ id ]
			p = self.initMagicDotDamage( caster, receiver, self._param[ "p1" ] )
			buffData[ "skill" ] = self.createFromDict( { "param":{ "p1":p } } )
			
	def doLoop( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		用于buff，表示buff在每一次心跳时应该做什么。

		@param receiver: 效果要影响的实体
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: BOOL；如果允许继续则返回True，否则返回False
		@rtype:  BOOL
		"""
		maxCount = self._maxCount
		entityList = receiver.entitiesInRangeExt( self._radius, None, receiver.position )	
		for e in entityList:
			if receiver.queryRelation( e ) == csdefine.RELATION_ANTAGONIZE:
				damage = self.calcDotDamage( receiver, e, csdefine.DAMAGE_TYPE_MAGIC, int( self._param[ "p1" ] ) )
				g_fightMgr.buildEnemyRelation( e, receiver )
				e.receiveSpell( receiver.id, self.getID(), csdefine.DAMAGE_TYPE_FLAG_BUFF|csdefine.DAMAGE_TYPE_MAGIC, damage, 0 )
				e.receiveDamage( receiver.id, self.getID(), csdefine.DAMAGE_TYPE_FLAG_BUFF|csdefine.DAMAGE_TYPE_MAGIC, damage )
				maxCount -= 1
			
				if maxCount <= 0:
					break
					
		return Buff_Normal.doLoop( self, receiver, buffData )

	def addToDict( self ):
		"""
		virtual method.
		打包自身需要传输的数据，数据必须是一个dict，具体参数详看SkillTypeImpl；
		此接口默认返回：{"id":self._id, "param":None}，即表示无动态数据。
		
		@return: 返回一个SKILL类型的字典。SKILL类型详细定义请参照defs/alias.xml文件
		"""
		return { "param" : self._param }

	def createFromDict( self, data ):
		"""
		virtual method.
		根据给定的字典数据创建一个与自身相同id号的技能。详细字典数据格式请参数SkillTypeImpl。
		此函数默认返回实例自身，这样在一些不需要保存动态数据的技能中就能以更高的效率进行数据还原，
		如果哪些技能需要保存动态数据，则只要重载此接口即可。
		
		@type data: dict
		"""
		obj = Buff_21002()
		obj.__dict__.update( self.__dict__ )
		obj._param = data["param"]
		if not data.has_key( "uid" ) or data[ "uid" ] == 0:
			obj.setUID( newUID() )		
		else:
			obj.setUID( data[ "uid" ] )		
		return obj

#
# $Log: not supported by cvs2svn $
# Revision 1.6  2008/04/10 04:08:26  kebiao
# 改为在接受伤害之前通知客户端接受技能处理
#
# Revision 1.5  2008/04/10 03:25:50  kebiao
# modify to receiveSpell pertinent.
#
# Revision 1.4  2008/03/31 09:04:02  kebiao
# 修改receiveDamage和通知客户端接受某技能结果分开
# 技能通过receiveSpell通知客户端去表现，支持各技能不同的表现
#
# Revision 1.3  2007/12/21 08:43:14  kebiao
# no message
#
# Revision 1.2  2007/12/21 07:28:00  kebiao
# no message
#
# Revision 1.1  2007/11/30 07:11:50  kebiao
# no message
#
# 
#