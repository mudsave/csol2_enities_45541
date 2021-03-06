# -*- coding: gb18030 -*-

import math
from Buff_Normal import Buff_Normal
from Function import newUID

class Buff_99033( Buff_Normal ):
	"""
	增加敏捷（英雄王座副本使用）
	公式 X=A*(Lv+C)+B
	"""
	def __init__( self ):
		"""
		构造函数
		"""
		Buff_Normal.__init__( self )
		self._pA1 = 0.0
		self._pB1 = 0.0
		self._pC1 = 0.0
		self._level = 0	# 副本等级

	def init( self, dict ):
		"""
		读取技能配置
		@param dict: 配置数据
		@type  dict: python dict
		"""
		Buff_Normal.init( self, dict )
		p1 = dict["Param1"].split( ";" )
		if len( p1 ) >= 3:
			self._pA1 = float( p1[0] )
			self._pB1 = float( p1[1] )
			self._pC1 = float( p1[2] )

	def doBegin( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		效果开始的处理。

		@param receiver: 效果要影响的实体
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: None
		"""
		Buff_Normal.doBegin( self, receiver, buffData )
		self._level = receiver.getSpaceCopyLevel()
		dexterity_value = int( math.ceil( self._pA1 * ( self._level + self._pC1 ) + self._pB1 ) )
		receiver.dexterity_value += dexterity_value
		receiver.calcDynamicProperties()

	def doReload( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		效果重新加载的处理。

		@param receiver: 效果要影响的实体
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		@return: None
		"""
		Buff_Normal.doReload( self, receiver, buffData )
		self._level = receiver.getSpaceCopyLevel()
		dexterity_value = int( math.ceil( self._pA1 * ( self._level + self._pC1 ) + self._pB1 ) )
		receiver.dexterity_value += dexterity_value

	def doEnd( self, receiver, buffData ):
		"""
		Virtual method; call only by real entity.
		效果结束的处理。

		@param receiver: 效果要影响的实体
		@type  receiver: BigWorld.Entity
		@param buffData: BUFF
		@type  buffData: BUFF
		"""
		Buff_Normal.doEnd( self, receiver, buffData )
		dexterity_value = int( math.ceil( self._pA1 * ( self._level + self._pC1 ) + self._pB1 ) )
		receiver.dexterity_value -= dexterity_value
		receiver.calcDynamicProperties()

	def addToDict( self ):
		"""
		virtual method.
		打包自身需要传输的数据，数据必须是一个dict，具体参数详看SkillTypeImpl；
		此接口默认返回：{"id":self._id, "param":None}，即表示无动态数据。
		
		@return: 返回一个SKILL类型的字典。SKILL类型详细定义请参照defs/alias.xml文件
		"""
		return { "param" : self._level }

	def createFromDict( self, data ):
		"""
		virtual method.
		根据给定的字典数据创建一个与自身相同id号的技能。详细字典数据格式请参数SkillTypeImpl。
		此函数默认返回实例自身，这样在一些不需要保存动态数据的技能中就能以更高的效率进行数据还原，
		如果哪些技能需要保存动态数据，则只要重载此接口即可。
		
		@type data: dict
		""" 
		obj = Buff_99033()
		obj.__dict__.update( self.__dict__ )
		obj._level = data["param"]
		if not data.has_key( "uid" ) or data[ "uid" ] == 0:
			obj.setUID( newUID() )
		else:
			obj.setUID( data[ "uid" ] )
		return obj