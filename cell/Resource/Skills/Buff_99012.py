# -*- coding: gb18030 -*-
#
# $Id: Buff_1003.py,v 1.2 2007-12-13 04:59:55 huangyongwei Exp $

"""
持续性效果
"""

import BigWorld
import csconst
import csstatus
import csdefine
import time
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal
import Const

class Buff_99012( Buff_Normal ):
	"""
	双人舞蹈buff，不断增加经验
	"""
	def __init__( self ):
		"""
		构造函数。
		"""
		Buff_Normal.__init__( self )
		self._p1 = 0

	def init( self, dict ):
		"""
		读取技能配置
		@param dict: 配置数据
		@type  dict: python dict
		"""
		Buff_Normal.init( self, dict )
		self._p1 = float( dict[ "Param1" ] ) 						# 增加经验的公式

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
		increaseEXP = self.getIncreaseEXP( receiver.level )
		buffIncreaseEXP = 0

		if not receiver.actionSign( csdefine.ACTION_ALLOW_DANCE ):		# 判断角色是否在舞厅中
			return Buff_Normal.doLoop( self, receiver, buffData )

		# 判断是否跳舞时间中。。。
		if len( receiver.findBuffsByBuffID( Const.JING_WU_SHI_KE_DANCE_BUFF ) ) == 0:		# 判断角色是否在跳舞时间中
			return Buff_Normal.doLoop( self, receiver, buffData )

		buffIncreaseEXP += increaseEXP * ( 1 + 20.0/100 )		# 双人舞，经验加成20%
		
		if receiver.hasCouple():	# 如果共舞夫妻，获得夫妻经验加成,gexp * %25
			loverBaseMB = receiver.getCoupleMB()
			if loverBaseMB and loverBaseMB.id == receiver.dancePartnerID:
				buffIncreaseEXP += increaseEXP * 25.0/100

		if len( receiver.findBuffsByBuffID( Const.JING_WU_SHI_KE_TIAO_WU_YAO_JUE_BUFF ) ) > 0:		# 判断角色是否有跳舞要诀
			buffIncreaseEXP += increaseEXP * 5

		if len( receiver.findBuffsByBuffID( Const.JING_WU_SHI_KE_WU_WANG_MI_JUE_BUFF ) ) > 0:		# 判断角色是否有舞王秘诀
			buffIncreaseEXP += increaseEXP * 10

		if buffIncreaseEXP > 0:
			receiver.addExp ( int(buffIncreaseEXP), csdefine.CHANGE_EXP_DOUBLEDANCE )
		else:
			receiver.addExp ( int(increaseEXP), csdefine.CHANGE_EXP_DOUBLEDANCE )
		return Buff_Normal.doLoop( self, receiver, buffData )

	def getIncreaseEXP( self, level ):
		"""
		根据公式获得增加的Exp
		"""
		return int( 134.66 + 26.9 * pow( level, 1.2 ) )
