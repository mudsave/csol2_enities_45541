# -*- coding: gb18030 -*-
#
# $Id: Buff_108003.py,v 1.12 2008-07-04 03:50:57 kebiao Exp $

"""
������Ч��
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
	example:ʹĿ�걻�־壬�޷�ʹ�ü��ܣ��޷��ƶ������Ա�����

	"""
	def __init__( self ):
		"""
		���캯����
		"""
		Buff_Normal.__init__( self )
		
	def init( self, dict ):
		"""
		��ȡ��������
		@param dict: ��������
		@type  dict: python dict
		"""
		Buff_Normal.init( self, dict )
		
	def doBegin( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		Ч����ʼ�Ĵ�����

		@param receiver: Ч��ҪӰ���ʵ��
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: None
		"""
		Buff_Normal.doBegin( self, receiver, buffData )
		if receiver.attrIntonateTimer > 0 and receiver.attrIntonateSkill.getType() in Const.INTERRUPTED_BASE_TYPE or\
			( receiver.attrHomingSpell and receiver.attrHomingSpell.getType() in Const.INTERRUPTED_BASE_TYPE ) :
			receiver.interruptSpell( csstatus.SKILL_IN_BLACKOUT )
		# ִ�и���Ч��
		receiver.actCounterInc( STATES )
		receiver.effectStateInc( csdefine.EFFECT_STATE_VERTIGO )
		if receiver.isMoving():
			# �����ƶ����ƣ���ȷ��buff���ƶ�����Ч����Ч by����
			receiver.stopMoving()

	def doReload( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		Ч�����¼��صĴ�����

		@param receiver: Ч��ҪӰ���ʵ��
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: None
		"""
		Buff_Normal.doReload( self, receiver, buffData )
		# ִ�и���Ч��
		receiver.actCounterInc( STATES )
		receiver.effectStateInc( csdefine.EFFECT_STATE_VERTIGO )
		if receiver.isMoving():
			# �����ƶ����ƣ���ȷ��buff���ƶ�����Ч����Ч by����
			receiver.stopMoving()
		
	def doEnd( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		Ч�������Ĵ�����

		@param receiver: Ч��ҪӰ���ʵ��
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		"""
		Buff_Normal.doEnd( self, receiver, buffData )
		receiver.effectStateDec( csdefine.EFFECT_STATE_VERTIGO )
		receiver.actCounterDec( STATES )
		
#
#