# -*- coding: gb18030 -*-

# $Id: CYDRoleMP.py

from CYaoDing import CYaoDing
import ItemTypeEnum
from bwdebug import *

class CYDRoleMP( CYaoDing ):
	"""
	蓝灵药鼑
	"""
	def __init__( self, srcData ):
		CYaoDing.__init__( self, srcData )

	def checkItem( self, item, owner, target ):
		"""
		检查物品是否是想要的类型
		@type  item : ITEM
		@param item : 要检查的物品
		"""
		if item.getType() != ItemTypeEnum.ITEM_DRUG_ROLE_MP:
			return False
		return CYaoDing.checkItem( self, item, owner, target )