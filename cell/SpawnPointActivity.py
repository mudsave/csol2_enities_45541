# -*- coding: gb18030 -*-
from SpawnPointNormal import SpawnPointNormal

class SpawnPointActivity( SpawnPointNormal ):
	def __init__( self ):
		SpawnPointNormal.__init__( self )
	
	def onActivityEnd( self ):
		"""
		define method
		�����
		"""
		self.getScript().onActivityEnd( self )