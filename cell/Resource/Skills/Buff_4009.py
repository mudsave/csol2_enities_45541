# -*- coding: gb18030 -*-
#
# $Id: Buff_4009.py,v 1.3 2008-09-04 07:46:27 kebiao Exp $

"""
持续性效果
"""

import BigWorld
import csconst
import csstatus
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal

class Buff_4009( Buff_Normal ):
	"""
	example:无双效果R	BUFF	防御率/闪避率/招架率	效果存在时单位得到防御率，闪避率，招架率的提升。

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
		self._p1 = int( dict[ "Param1" ] if len( dict[ "Param1" ] ) > 0 else 0 )  * 100	
		#self._p2 = dict[ "Param2" ].asInt / 100.0
		#self._p3 = dict[ "Param3" ].asInt / 100.0
		
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
		receiver.resist_hit_probability_percent += self._p1
		receiver.calcResistHitProbability()
		receiver.dodge_probability_percent += self._p1
		receiver.calcDodgeProbability()
		receiver.armor_reduce_damage_percent += self._p1 #在伤害计算流程中参与最终值的计算
		receiver.magic_armor_reduce_damage_percent += self._p1 #在伤害计算流程中参与最终值的计算
		
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
		receiver.resist_hit_probability_percent += self._p1
		receiver.dodge_probability_percent += self._p1
		receiver.armor_reduce_damage_percent += self._p1 #在伤害计算流程中参与最终值的计算
		receiver.magic_armor_reduce_damage_percent += self._p1 #在伤害计算流程中参与最终值的计算
		
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
		receiver.resist_hit_probability_percent -= self._p1
		receiver.calcResistHitProbability()
		receiver.dodge_probability_percent -= self._p1
		receiver.calcDodgeProbability()
		receiver.armor_reduce_damage_percent -= self._p1 #在伤害计算流程中参与最终值的计算
		receiver.magic_armor_reduce_damage_percent -= self._p1 #在伤害计算流程中参与最终值的计算
#
# $Log: not supported by cvs2svn $
# Revision 1.2  2007/12/05 01:19:12  kebiao
# 统一加成使用整数
#
# Revision 1.1  2007/11/30 07:11:50  kebiao
# no message
#
# 
#