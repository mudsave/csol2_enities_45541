# -*- coding: gb18030 -*-
#
# $Id: Spell_TeamDancing.py,v 1.28 2009.11.04 10:02:41 pengju Exp $

"""
���鹲��
2009.11.04: by pengju
"""

import random
import BigWorld
import csdefine
import csstatus
from SpellBase import *
from bwdebug import *

class Spell_TeamDancing( Spell ):
	def __init__( self ):
		Spell.__init__( self )

	def init( self, dict ):
		"""
		��ȡ��������
		@param dict: ��������
		@type  dict: python dict
		"""
		Spell.init( self, dict )

	def getType( self ):
		"""
		ȡ�û�����������
		��Щֵ��BASE_SKILL_TYPE_*֮һ
		"""
		return csdefine.BASE_SKILL_TYPE_ACTION

	def useableCheck( self, caster, target ):
		"""
		virtual method.
		У�鼼���Ƿ����ʹ�á�
		return: SkillDefine::SKILL_*;Ĭ�Ϸ���SKILL_UNKNOW
		ע���˽ӿ��Ǿɰ��е�validUse()

		@param target: ʩչ����
		@type  target: һ����װ���Ķ���entity ����װ��������� (λ�ã�entity, item)��ϸ�뿴SkillTargetObjImpl.py
		@return:           INT��see also csdefine.SKILL_*
		@rtype:            INT
		"""
		if caster.isTeamFollowing():
			return csstatus.JING_WU_SHI_KE_DANCE_NO_FOLLOWING
		
		state = caster.getState()
		# ֻ�д��ڵ����衢˫�����������״̬����ʩ�ż���
		if state == csdefine.ENTITY_STATE_DANCE and caster.dancePartnerID == 0 or \
			state == csdefine.ENTITY_STATE_DOUBLE_DANCE or \
			state == csdefine.ENTITY_STATE_FREE :
			return Spell.useableCheck( self, caster, target )
		return csstatus.JING_WU_SHI_KE_NOT_FREE

	def receive( self, caster, receiver ) :
		"""
		���ڸ�Ŀ��ʩ��һ��buff�����е�buff�Ľ��ն�����ͨ���˽ӿڣ�
		�˽ӿڱ����жϽ������Ƿ�ΪrealEntity��
		����������Ҫͨ��receiver.receiveOnReal()�ӿڴ�����

		@param   caster: ʩ����
		@type    caster: Entity
		@param receiver: �ܻ���
		@type  receiver: Entity
		"""
		caster.teamDance()