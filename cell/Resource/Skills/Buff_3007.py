# -*- coding: gb18030 -*-
#
# $Id: Buff_3007.py,v 1.2 2007-12-05 01:19:12 kebiao Exp $

"""
持续性效果
"""

import BigWorld
import csconst
import csstatus
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal

class Buff_3007( Buff_Normal ):
	"""
	example:
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
		self._p1 = int( float(dict[ "Param1" ] if len( dict[ "Param1" ] ) > 0 else 0 ) * csconst.FLOAT_ZIP_PERCENT / 100 )
		
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
		receiver.magic_hitProbability_value += self._p1
		receiver.calcMagicHitProbability()
		
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
		receiver.magic_hitProbability_value += self._p1
		
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
		receiver.magic_hitProbability_value -= self._p1
		receiver.calcMagicHitProbability()
		
#
# $Log: not supported by cvs2svn $
# Revision 1.1  2007/11/30 07:11:50  kebiao
# no message
#
# 
#