# -*- coding: gb18030 -*-
#
# $Id: Buff_108003.py,v 1.12 2008-07-04 03:50:57 kebiao Exp $

"""
持续性效果
"""
import random
import BigWorld

import csstatus
import csdefine
from bwdebug import *

import Const
from SpellBase import *
from Buff_Normal import Buff_Normal

STATES = csdefine.ACTION_FORBID_MOVE | csdefine.ACTION_FORBID_ATTACK | csdefine.ACTION_FORBID_SPELL | csdefine.ACTION_FORBID_JUMP
				 
class Buff_108004( Buff_Normal ):
	"""
	example:使目标被恐惧，无法使用技能，无法移动，可以被攻击

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
		if receiver.attrIntonateTimer > 0 and receiver.attrIntonateSkill.getType() in Const.INTERRUPTED_BASE_TYPE or\
			( receiver.attrHomingSpell and receiver.attrHomingSpell.getType() in Const.INTERRUPTED_BASE_TYPE ) :
			receiver.interruptSpell( csstatus.SKILL_IN_BLACKOUT )
		# 执行附加效果
		receiver.actCounterInc( STATES )
		receiver.effectStateInc( csdefine.EFFECT_STATE_VERTIGO )
		if receiver.isMoving():
			# 加入移动限制，以确保buff对移动限制效果生效 by姜毅
			receiver.stopMoving()

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
		# 执行附加效果
		receiver.actCounterInc( STATES )
		receiver.effectStateInc( csdefine.EFFECT_STATE_VERTIGO )
		if receiver.isMoving():
			# 加入移动限制，以确保buff对移动限制效果生效 by姜毅
			receiver.stopMoving()
		
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
		receiver.effectStateDec( csdefine.EFFECT_STATE_VERTIGO )
		receiver.actCounterDec( STATES )
		
#
#