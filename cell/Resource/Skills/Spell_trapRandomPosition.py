# -*- coding: gb18030 -*-

# 系统技能，生成一个AreaRestrictTransducer的entity(陷阱功能entity)，在一定范围内随机找一点

import BigWorld
import csdefine
import csstatus
from SpellBase import *
import random

class Spell_trapRandomPosition( Spell ):
	"""
	系统技能
	生成一个AreaRestrictTransducer的entity(陷阱功能entity)
	"""
	def __init__( self ):
		"""
		构造函数。
		"""
		Spell.__init__( self )
		self.lifetime = 0				# 陷阱销毁时间
		self.radius = 0.0				# 陷阱半径
		self.enterSpell = 0				# 进入陷阱施放的技能
		self.leaveSpell = 0				# 离开陷阱施放的技能
		self.randomRadius = 0			# 创建陷阱的随机范围半径
		self.modelNumber =  ""			# 陷阱对应的模型(带光效的)

	def init( self, dict ):
		"""
		读取技能配置
		@param dict: 配置数据
		@type  dict: python dict
		"""
		Spell.init( self, dict )
		self.lifetime = int( dict[ "param1" ] )
		self.radius = float( dict[ "param2" ] )
		spellStr = str( dict["param3"] )
		self.enterSpell = int( spellStr.split(";")[0] )
		self.leaveSpell = int( spellStr.split(";")[1] )
		self.randomRadius = int( dict[ "param4" ] )
		self.modelNumber = str( dict[ "param5" ] )

	def receive( self, caster, receiver ):
		"""
		virtual method.
		技能实现的目的
		"""
		if receiver.isReal():
			dict = { \
				"radius" : self.radius,
				"enterSpell" : self.enterSpell,
				"leaveSpell" : self.leaveSpell,
				"destroySpell" : self.leaveSpell,
				"modelNumber" : self.modelNumber,
				"lifetime" : self.lifetime,
				"uname" : self.getName()\
			}
			pos = caster.position + ( random.randint(-self.randomRadius, self.randomRadius), 0, random.randint(-self.randomRadius, self.randomRadius) )
			trap = receiver.createEntityNearPlanes( "SkillTrap", pos, (0, 0, 0), dict )
		else:	# 加入对ghost的支持。17:31 2009-1-16，wsf
			receiver.receiveOnReal( caster.id, self )
