# -*- coding:gb18030 -*-

from bwdebug import *
import csdefine
from SpellBase import *
from Buff_Normal import Buff_Normal

class Buff_70001( Buff_Normal ):
	"""
	防御姿态
	
	物理防御力提高%，进入防御姿态
	"""
	def __init__( self ):
		Buff_Normal.__init__( self )
		self.posture = csdefine.ENTITY_POSTURE_DEFENCE
		
	def init( self, data ):
		"""
		"""
		Buff_Normal.init( self, data )
		# 物理防御力提高%
		self.param1 = float( data["Param1"] if data["Param1"] > 0 else 0 ) * 100
		self.param2 = int( data[ "Param2" ] if len( data[ "Param2" ] ) > 0 else 0 )
		
	def doBegin( self, receiver, buffData ):
		"""
		virtual method.
		"""
		Buff_Normal.doBegin( self, receiver, buffData )
		receiver.changePosture( self.posture )
		receiver.armor_percent += self.param1
		receiver.armor_value += self.param2
		receiver.calcArmor()
		
	def doReload( self, receiver, buffData ):
		"""
		virtual method.
		"""
		Buff_Normal.doReload( self, receiver, buffData )
		receiver.changePosture( self.posture )
		receiver.armor_percent += self.param1
		receiver.armor_value += self.param2
		
	def doEnd( self, receiver, buffData ):
		"""
		virtual method.
		"""
		Buff_Normal.doEnd( self, receiver, buffData )
		receiver.changePosture( csdefine.ENTITY_POSTURE_NONE )
		receiver.armor_percent -= self.param1
		receiver.armor_value -= self.param2
		receiver.calcArmor()
		
		