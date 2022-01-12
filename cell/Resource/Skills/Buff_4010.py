# -*- coding: gb18030 -*-
#
# $Id: Buff_4010.py,v 1.3 2008-09-04 07:46:27 kebiao Exp $

"""
������Ч��
"""

import BigWorld
import csconst
import csstatus
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal

class Buff_4010( Buff_Normal ):
	"""
	example:��λ����������A������������%

	"""
	def __init__( self ):
		"""
		���캯����
		"""
		Buff_Normal.__init__( self )
		self._p0 = 0
		self._p1 = 0
		
	def init( self, dict ):
		"""
		��ȡ��������
		@param dict: ��������
		@type  dict: python dict
		"""
		Buff_Normal.init( self, dict )
		self._p0 = int( dict[ "Param1" ] if len( dict[ "Param1" ] ) > 0 else 0 ) 	
		self._p1 = int( dict[ "Param2" ] if len( dict[ "Param2" ] ) > 0 else 0 )  * 100	
		
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
		receiver.magic_armor_value += self._p0
		receiver.calcMagicArmor()
		receiver.armor_value += self._p0
		receiver.calcArmor()
		receiver.armor_reduce_damage_percent += self._p1 #���˺����������в�������ֵ�ļ���
		receiver.magic_armor_reduce_damage_percent += self._p1 #���˺����������в�������ֵ�ļ���
		
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
		receiver.magic_armor_value += self._p0
		receiver.armor_value += self._p0
		receiver.armor_reduce_damage_percent += self._p1 #���˺����������в�������ֵ�ļ���
		receiver.magic_armor_reduce_damage_percent += self._p1 #���˺����������в�������ֵ�ļ���
		
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
		receiver.magic_armor_value -= self._p0
		receiver.calcMagicArmor()
		receiver.armor_value -= self._p0
		receiver.calcArmor()
		receiver.armor_reduce_damage_percent -= self._p1 #���˺����������в�������ֵ�ļ���
		receiver.magic_armor_reduce_damage_percent += self._p1 #���˺����������в�������ֵ�ļ���
		
#
# $Log: not supported by cvs2svn $
# Revision 1.2  2007/12/05 01:19:12  kebiao
# ͳһ�ӳ�ʹ������
#
# Revision 1.1  2007/11/30 07:11:50  kebiao
# no message
#
# 
#