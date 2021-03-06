# -*- coding: gb18030 -*-
#
# $Id: FuncContestFamilyNPC.py,v 1.3 2008-07-31 04:14:37 kebiao Exp $

"""
"""
from Function import Function
import BigWorld
import csstatus
import csdefine
import csconst

class FuncContestFamilyNPC( Function ):
	"""
	争夺家族NPC
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
		if player.iskitbagsLocked():	# 背包上锁，by姜毅
			player.client.onStatusMessage( csstatus.CIB_MSG_KITBAG_LOCKED_MISSION, "" )
			player.endGossip( talkEntity )
			return
		player.setTemp( "family_warNPC_ClassName", talkEntity.className )
		player.setTemp( "family_warNPC_Name", talkEntity.uname )
		player.setTemp( "family_warNPC_POS", talkEntity.position )
		player.setTemp( "family_warNPC_MAP", player.getCurrentSpaceData( csconst.SPACE_SPACEDATA_KEY ) )
		player.getFamilyManager().requestWar( talkEntity.className, player.base, player.money, player.level, player.family_grade, player.family_dbID )
		player.endGossip( talkEntity )

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
		return True


#
# $Log: not supported by cvs2svn $
# Revision 1.2  2008/07/19 03:53:07  kebiao
# no message
#
# Revision 1.1  2008/07/18 06:23:15  kebiao
# no message
#
# Revision 1.4  2008/06/09 01:22:12  fangpengjun
# no message
#
# Revision 1.3  2008/06/05 07:54:14  fangpengjun
# no message
#
# Revision 1.2  2008/06/05 02:03:14  kebiao
# no message
#
#
