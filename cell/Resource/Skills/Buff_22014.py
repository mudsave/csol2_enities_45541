# -*- coding: gb18030 -*-
#
# $Id: Exp $

"""
持续性效果
"""

import BigWorld
import csconst
import csstatus
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal

class Buff_22014( Buff_Normal ):
	"""
	仙羽灵气
	"""
	def __init__( self ):
		"""
		构造函数。
		"""
		Buff_Normal.__init__( self )
		self._p1 = 0 #移动速度提高百分比
		self._p2 = 0 #自然回蓝回血提高百分比		
		
	def init( self, dict ):
		"""
		读取技能配置
		@param dict: 配置数据
		@type  dict: python dict
		"""
		Buff_Normal.init( self, dict )
		self._p1 = int( dict[ "Param1" ] if len( dict[ "Param1" ] ) > 0 else 0 )  * 100	
		self._p2 = int( dict[ "Param2" ] if len( dict[ "Param2" ] ) > 0 else 0 )  * 100	
		
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
		receiver.move_speed_percent += self._p1
		receiver.calcMoveSpeed()		
		receiver.HP_regen_percent += self._p2
		receiver.calcHPCureSpeed()
		receiver.MP_regen_percent += self._p2
		receiver.calcMPCureSpeed()


	def doReload( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		效果重新加载的处理。

		@param receiver: 效果要影响的实体
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: None
		"""
		Buff_Normal.doReload( self, receiver, buffData )
		receiver.move_speed_percent += self._p1
		receiver.HP_regen_percent += self._p2
		receiver.MP_regen_percent += self._p2
		
	def doEnd( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		效果结束的处理。

		@param receiver: 效果要影响的实体
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		"""
		Buff_Normal.doEnd( self, receiver, buffData )
		receiver.move_speed_percent -= self._p1
		receiver.calcMoveSpeed()		
		receiver.HP_regen_percent -= self._p2
		receiver.calcHPCureSpeed()
		receiver.MP_regen_percent -= self._p2
		receiver.calcMPCureSpeed()