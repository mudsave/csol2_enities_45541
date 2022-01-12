# -*- coding: gb18030 -*-

# $Id: AIEAISet.py,v 1.1 2008-04-22 04:16:47 kebiao Exp $

import csstatus
import csdefine
import BigWorld
from bwdebug import *
from AIAction import AIAction

class AIEAISet( AIAction ):
	"""
	����EAI
	"""
	def __init__( self ):
		AIAction.__init__( self )
		self._eaiData = []
		
	def init( self, section ):
		"""
		virtual method
		@param	section	: 	�洢���ݵ����ݶ�
		@type	section	:	PyDataSection
		"""
		#AIAction.init( self, section )
		for s in section.values():
			self._eaiData.append( s.asInt )
				
	def do( self, ai, entity ):
		"""
		vitural method
		@param	ai		: 	ӵ�д�������AI ( ����֧����Ϊ�˵õ���дAI�Ķ�̬���� )
		@type	ai		:	AI of instance, AIBase
		@param	entity	: 	ִ�д�AICondition��entity
		@type	entity	:	entity
		"""
		for aiID in self._eaiData:
			entity.addEAI( aiID )

#
# $Log: not supported by cvs2svn $
#