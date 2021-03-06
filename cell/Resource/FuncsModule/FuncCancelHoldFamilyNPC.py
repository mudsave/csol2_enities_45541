# -*- coding: gb18030 -*-
#
#$Id:$

import BigWorld
import csdefine
from bwdebug import *

class FuncCancelHoldFamilyNPC:
	"""
	取消占领某个家族NPC
	"""
	def __init__( self, section ):
		"""
		@param param: 由实现类自己解释格式; param1 - param5
		@type  param: pyDataSection
		"""
		pass
		
		
	def do( self, player, talkEntity = None ):
		"""
		执行一个功能

		@param player: 玩家
		@type  player: Entity
		@param  talkEntity: 一个扩展的参数
		@type   talkEntity: entity
		@return: None
		"""
		if talkEntity is None:
			WARNING_MSG( "talkEntity cannot be None." )
			return
		player.endGossip( talkEntity )
		player.client.family_askForCancelFamilyNPC()
		
	def valid( self, player, talkEntity = None ):
		"""
		检查一个功能是否可以使用

		@param player: 玩家
		@type  player: Entity
		@param  talkEntity: 一个扩展的参数
		@type   talkEntity: entity
		@return: True/False
		@rtype:	bool
		"""
		if player.family_grade == csdefine.FAMILY_GRADE_SHAIKH:
			key = "flyNPC." + talkEntity.className
			if BigWorld.globalData.has_key( key ):		
				dbid, name = BigWorld.globalData[ key ]
				if player.family_dbID == dbid:
					return True
		return False



#$Log:$
#
# 