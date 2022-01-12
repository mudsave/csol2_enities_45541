# -*- coding: gb18030 -*-
#
# $Id: Buff_107008.py,v 1.9 2008-08-11 07:55:59 kebiao Exp $

"""
������Ч��
"""

import BigWorld
import csdefine
import csstatus
from bwdebug import *
from SpellBase import *
from Buff_Normal import Buff_Normal


class Buff_107008( Buff_Normal ):
	"""
	example:��ʧ����A���ܵ�%�����˺�	DEBUFF	��������ʧ����/�����˺�	��һ����ֵ����ħ��ֵ�����ܵ�һ�������ķ����˺���

	"""
	def __init__( self ):
		"""
		���캯����
		"""
		Buff_Normal.__init__( self )
		self._p1 = 0 # ������hPֵ 

	def init( self, dict ):
		"""
		��ȡ��������
		@param dict: ��������
		@type  dict: python dict
		"""
		Buff_Normal.init( self, dict )
		self._p1 = int( int( dict[ "Param1" ] if len( dict[ "Param1" ] ) > 0 else 0 )  / ( self._persistent / self._loopSpeed ) )	
			
	def doLoop( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		����buff����ʾbuff��ÿһ������ʱӦ����ʲô��

		@param receiver: Ч��ҪӰ���ʵ��
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: BOOL��������������򷵻�True�����򷵻�False
		@rtype:  BOOL
		"""
		SkillMessage.buff_ConsumeMP( buffData, receiver, self._p1 )
		receiver.setMP( receiver.MP - self._p1 )
		damage = self.calcDotDamage( receiver, receiver, csdefine.DAMAGE_TYPE_VOID, int( self._p1 ) )
		receiver.receiveSpell( buffData["caster"], self.getID(), csdefine.DAMAGE_TYPE_FLAG_BUFF|csdefine.DAMAGE_TYPE_VOID, damage, 0 )
		receiver.receiveDamage( buffData["caster"], self.getID(), csdefine.DAMAGE_TYPE_FLAG_BUFF|csdefine.DAMAGE_TYPE_VOID, damage )
		return Buff_Normal.doLoop( self, receiver, buffData )

#
# $Log: not supported by cvs2svn $
# Revision 1.8  2008/04/10 04:08:26  kebiao
# ��Ϊ�ڽ����˺�֮ǰ֪ͨ�ͻ��˽��ܼ��ܴ���
#
# Revision 1.7  2008/04/10 03:25:50  kebiao
# modify to receiveSpell pertinent.
#
# Revision 1.6  2008/03/31 09:04:02  kebiao
# �޸�receiveDamage��֪ͨ�ͻ��˽���ĳ���ܽ���ֿ�
# ����ͨ��receiveSpell֪ͨ�ͻ���ȥ���֣�֧�ָ����ܲ�ͬ�ı���
#
# Revision 1.5  2008/02/13 08:41:04  kebiao
# ���������ʾ��Ϣ
#
# Revision 1.4  2007/12/21 08:56:32  kebiao
# no message
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