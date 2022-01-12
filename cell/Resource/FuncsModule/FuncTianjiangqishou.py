# -*- coding: gb18030 -*-

"""
��콵����
"""
import time
import BigWorld
from Function import Function
import csdefine
import csstatus
import utils
from bwdebug import *

TEAM_MEMBER_NEED 	= 3																	#��Ҫ�Ķ����Ա
MAX_LEVEL 			= 110																#���ȼ�

class FuncTianjiangqishou( Function ):
	"""
	�����콵����
	(fu_ben_hun_dun_ru_qin)
	"""
	def __init__( self, section ):
		"""
		"""
		self.__mapName 		= section["param1"].asString								#��ͼ��
		self.__level		= section["param2"].asInt									#��Ҫ�ȼ�
		
		self.__pos = None																#����λ��
		position = section.readString( "param3" )
		pos = utils.vector3TypeConvert( position )
		if pos is None:
			ERROR_MSG( "Vector3 Type Error��%s Bad format '%s' in section param3 " % ( self.__class__.__name__, position ) )
		else:
			self.__pos = pos
		
		self.__direction = None
		direction = section.readString( "param4" )										#���볯��
		dir = utils.vector3TypeConvert( direction )
		if dir is None:
			ERROR_MSG( "Vector3 Type Error��%s Bad format '%s' in section param4 " % ( self.__class__.__name__, direction ) )
		else:
			self.__direction = dir
				
		self.__distance		= section["param5"].asFloat									#��Ա����

	def do( self, player, talkEntity = None ):
		"""
		"""
		player.endGossip( talkEntity )

		if talkEntity.hasFlag( csdefine.ENTITY_FLAG_COPY_STARTING ):
			player.client.onStatusMessage( csstatus.NPC_IS_BUSY, "" )
			return


		if player.level < self.__level or player.level > MAX_LEVEL:
			player.client.onStatusMessage( csstatus.TIANJIANGQISHOU_FORBID_LEVEL, str(( self.__level, MAX_LEVEL )) )
			return
			
		if not player.isInTeam():
			player.client.onStatusMessage( csstatus.TALK_FORBID_TEAM, "" )
			return
			
		if not player.isTeamCaptain():
			player.client.onStatusMessage( csstatus.TIANJIANGQISHOU_FORBID_CAPTAIN, "" )
			return
		
		members = player.getAllMemberInRange( self.__distance )
		
		if len( members ) < TEAM_MEMBER_NEED :
			player.client.onStatusMessage( csstatus.TIANJIANGQISHOU_FORBID_MEMBER_AMOUNT, str(( TEAM_MEMBER_NEED, )) )
			return
		if len( members ) < len( player.teamMembers ):
			player.client.onStatusMessage( csstatus.TIANJIANGQISHOU_FORBID_MEMBER_NEAR, "" )
			return
		for teamMate in members:
			if teamMate.level < self.__level:
				player.client.onStatusMessage( csstatus.TIANJIANGQISHOU_FORBID_MEMBER_LEVEL_LESS, str(( teamMate.getName(), self.__level )) )
				return

			if teamMate.level > MAX_LEVEL:
				player.client.onStatusMessage( csstatus.TIANJIANGQISHOU_FORBID_MEMBER_LEVEL_MORE, str(( teamMate.getName(), MAX_LEVEL )) )
				return

		BigWorld.cellAppData["TJQS_%i"%player.teamMailbox.id] = talkEntity.id

		#player.setTemp("copySpaceEnterMonsterID", talkEntity.id )
		player.gotoSpace( self.__mapName, self.__pos, self.__direction )
		members.remove( player )
		
		
		for teamMate in members:
			teamMate.set("lastDragonTeamID", player.getTeamMailbox().id )
			teamMate.gotoSpace( self.__mapName, self.__pos, self.__direction )
		#talkEntity.destroy()
		talkEntity.addFlag( csdefine.ENTITY_FLAG_COPY_STARTING )

	def valid( self, player, talkEntity = None ):
		"""
		���һ�������Ƿ����ʹ��
		@param player: ���
		@type  player: Entity
		@param  talkEntity: һ����չ�Ĳ���
		@type   talkEntity: entity
		@return: True/False
		@rtype:	bool
		"""
		return BigWorld.globalData.has_key( "AS_Tianjiangqishou" )