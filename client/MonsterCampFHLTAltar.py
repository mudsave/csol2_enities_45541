# -*- coding: gb18030 -*-

from Monster import Monster
import csdefine
from bwdebug import *

class MonsterCampFHLTAltar( Monster ):
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
			if entity.getCamp() == self.ownCamp:
				return csdefine.RELATION_FRIEND
			else:
				return csdefine.RELATION_ANTAGONIZE
		
		if entity.isEntityType( csdefine.ENTITY_TYPE_CAMP_XIAN_FENG ):
			if entity.ownCamp == self.ownCamp:
				return csdefine.RELATION_FRIEND
			else:
				return csdefine.RELATION_ANTAGONIZE

		return csdefine.RELATION_NEUTRALLY