# -*- coding: gb18030 -*-
#
# $Id: Spell_Item_Tong_Money.py by jy
"""
ʹ����Ʒ�ı����ʽ�
"""

from bwdebug import *
from Spell_Item import Spell_Item
import csstatus
import csdefine

class Spell_Item_Tong_Money( Spell_Item ):
	"""
	"""
	def __init__( self ):
		"""
		���캯����
		"""
		Spell_Item.__init__( self )

	def init( self, dict ):
		"""
		��ȡ��������
		@param dict: ��������
		@type  dict: python dict
		"""
		self._addMoney = int(dict[ "param1" ]) if len( dict[ "param1" ] ) > 0 else 0
		Spell_Item.init( self, dict )

	def receive( self, caster, receiver ):
		"""
		virtual method.
		����������Ҫ��������
		"""
		if caster.tong_dbID <= 0:
			return
		tong = caster.tong_getTongEntity( caster.tong_dbID )
		if tong is None:
			return
		tong.addMoney( self._addMoney, csdefine.TONG_CHANGE_MONEY_ITEM )
		INFO_MSG( "Change tong(%d) money by %s."%( caster.tong_dbID, caster.getName() ) )
		Spell_Item.receive( self, caster, receiver )

	def useableCheck( self, caster, target ):
		"""
		virtual method.
		"""
		if caster.tong_dbID <= 0:
			return csstatus.TONG_NO_TONG
		tong = caster.tong_getTongEntity( caster.tong_dbID )
		if tong is None:
			return csstatus.TONG_TARGET_NOT_EXIST
		
		return Spell_Item.useableCheck( self, caster, target )