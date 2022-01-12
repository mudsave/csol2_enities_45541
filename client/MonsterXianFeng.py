# -*- coding: gb18030 -*-

from Monster import Monster
import csdefine
from bwdebug import *

class MonsterXianFeng( Monster ):
	def __init__( self ):
		Monster.__init__( self )
	
	def queryRelation( self, entity ):
		if not self.isNeedQueryRelation( entity ):
			return csdefine.RELATION_FRIEND
			
		if self.isUseCombatCamp and entity.isUseCombatCamp:
			return Monster.queryRelation( self, entity )
		
		if entity.isEntityType( csdefine.ENTITY_TYPE_MONSTER ):
			return csdefine.RELATION_NEUTRALLY

		if entity.isEntityType( csdefine.ENTITY_TYPE_ROLE ):
			if entity.tong_dbID == self.ownTongDBID:
				return csdefine.RELATION_FRIEND
			else:
				return csdefine.RELATION_ANTAGONIZE
		
		if entity.isEntityType( csdefine.ENTITY_TYPE_XIAN_FENG ) or entity.isEntityType( csdefine.ENTITY_TYPE_FENG_HUO_LIAN_TIAN_TOWER ) or \
			entity.isEntityType( csdefine.ENTITY_TYPE_FENG_HUO_LIAN_TIAN_ALTAR ) or entity.isEntityType( csdefine.ENTITY_TYPE_FENG_HUO_LIAN_TIAN_BASE_TOWER ):
			if entity.ownTongDBID == self.ownTongDBID:
				return csdefine.RELATION_FRIEND
			else:
				return csdefine.RELATION_ANTAGONIZE

		return csdefine.RELATION_NEUTRALLY