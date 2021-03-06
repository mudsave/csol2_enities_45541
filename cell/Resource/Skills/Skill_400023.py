# -*- coding: gb18030 -*-
#


from SpellBase import *
from Skill_Normal import Skill_Normal
import csdefine
import random

class Skill_400023( Skill_Normal ):
	"""
	使你受到物理爆击的几率降低1%。

	"""
	def __init__( self ):
		"""
		构造函数。
		"""
		Skill_Normal.__init__( self )
	
	def init( self, dict ):
		"""
		读取技能配置
		@param dict: 配置数据
		@type  dict: python dict
		"""
		Skill_Normal.init( self, dict )
		self._param = int( dict[ "param1" ] if len( dict[ "param1" ] ) > 0 else 0 )  * 100	
		
	def attach( self, ownerEntity ):
		"""
		virtual method = 0;
		为目标附上一个效果，通常被附上的效果是实例自身，它可以通过detach()去掉这个效果。具体效果由各派生类自行决定。
		
		@param ownerEntity:	拥有者实体
		@type ownerEntity:	BigWorld.Entity
		"""
		ownerEntity.be_double_hit_probability -= self._param
		
	def detach( self, ownerEntity ):
		"""
		virtual method
		执行与attach()的反向操作

		@param ownerEntity:	拥有者实体
		@type ownerEntity:	BigWorld.Entity
		"""
		ownerEntity.be_double_hit_probability += self._param