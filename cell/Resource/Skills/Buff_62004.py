# -*- coding: gb18030 -*-
#
# $Id: Buff_62004.py,v 1.2 2008-09-04 07:46:27 kebiao Exp $

"""
持续性效果
"""

import BigWorld
import csconst
import csdefine
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal

class Buff_62004( Buff_Normal ):
	"""
	example:物理攻击力提高40%,法术攻击力提高40%。
				<Param1>	40	</Param1>
				<Param2>	40	</Param2>
				<Param3>	</Param3>
	"""
	def __init__( self ):
		"""
		构造函数。
		"""
		Buff_Normal.__init__( self )

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
		receiver.damage_min_percent += self._p1
		receiver.damage_max_percent += self._p1
		receiver.magic_damage_percent += self._p2
		receiver.calcDamageMin()
		receiver.calcDamageMax()
		receiver.calcMagicDamage()
		
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
		receiver.damage_min_percent += self._p1
		receiver.damage_max_percent += self._p1
		receiver.magic_damage_percent += self._p2
		
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
		receiver.damage_min_percent -= self._p1
		receiver.damage_max_percent -= self._p1
		receiver.magic_damage_percent -= self._p2
		receiver.calcDamageMin()
		receiver.calcDamageMax()
		receiver.calcMagicDamage()
		if not receiver.queryTemp( "buffBeInteruptFromTuteng", False ):
			receiver.setTemp("allBuffInteruptFromTuteng", False )
		
		receiver.removeTemp( "buffBeInteruptFromTuteng" )
		receiver.removeTemp( "CUMULATION_COUNT" )
		
#
# $Log: not supported by cvs2svn $
# Revision 1.1  2008/07/14 04:05:32  kebiao
# no message
#
# 
#