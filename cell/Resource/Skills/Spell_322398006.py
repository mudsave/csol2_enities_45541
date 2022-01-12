# -*- coding: gb18030 -*-


import Const

from bwdebug import *
from Spell_Item import Spell_Item
from Love3 import g_itemDropLuckyBoxZhaocai
import csdefine
import ItemTypeEnum
import csstatus

class Spell_322398006( Spell_Item ):
	"""
	��Ʒ���ܣ��в�����
	"""
	def __init__( self ):
		"""
		"""
		Spell_Item.__init__( self )


	def init( self, dict ):
		"""
		��ȡ��������
		@param dict: ��������
		@type  dict: python dict
		"""
		Spell_Item.init( self, dict )


	def receive( self, caster, receiver ):
		"""
		virtual method.
		���ÿһ�������߽�������������������˺����ı����Եȵȡ�ͨ������´˽ӿ�����onArrive()���ã�
		�������п�����SpellUnit::receiveOnreal()�������ã����ڴ���һЩ��Ҫ�������ߵ�real entity�����������顣
		�������Ƿ���Ҫ��real entity���Ͻ��գ��ɼ����������receive()�������жϣ������ṩ��ػ��ơ�
		ע���˽ӿ�Ϊ�ɰ��е�onReceive()

		@param   caster: ʩ����
		@type    caster: Entity
		@param receiver: �ܻ���
		@type  receiver: Entity
		"""
		# ����caster���ϵı�����Ʒ�������Ҽ��ϻ�õ���Ʒ
		uid = caster.queryTemp( "item_using" )
		item = caster.getByUid( uid )
		if item is None:
			ERROR_MSG( "ʥ�����ӣ�player( %s )'s item is None.uid:%i." % ( caster.getName(), uid ) )
			return

		dropType, dropInstance = g_itemDropLuckyBoxZhaocai.getDropData( item.getLevel() )
		if dropType == Const.LUCKY_BOX_DROP_MONEY:
			caster.addMoney( dropInstance, csdefine.CHANGE_MONEY_CMS_SOCKS )
		elif dropType == Const.LUCKY_BOX_DROP_POTENTIAL:
			caster.addPotential( dropInstance, csdefine.CHANGE_POTENTIAL_CMS_SOCKS )
		elif dropType == Const.LUCKY_BOX_DROP_EXP:
			caster.addExp( dropInstance, csdefine.CHANGE_EXP_CMS_SOCKS )
		else:
			dropInstance.setBindType( ItemTypeEnum.CBT_PICKUP )
			caster.addItem( dropInstance, csdefine.ADD_ITEM_CMS_SOCKS )


	def useableCheck( self, caster, target ):
		"""
		��Ҫ��һ���ո�ſ��Դ�ʥ�����ӡ������޷������Ʒ
		"""
		if caster.getNormalKitbagFreeOrderCount() < 1:
			caster.client.onStatusMessage( csstatus.CMS_SOCKS_NEED_SPACE, "" )
			return csstatus.SKILL_USE_ITEM_NEED_ONE_BLANK
		return Spell_Item.useableCheck( self, caster, target )