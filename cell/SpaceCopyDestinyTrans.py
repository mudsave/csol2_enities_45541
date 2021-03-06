# -*- coding: gb18030 -*-

import Const
from bwdebug import *
from SpaceCopy import SpaceCopy
from interface.SpaceCopyYeWaiInterface import SpaceCopyYeWaiInterface

DESTROY_SPACE_AFTER_LEAVE_SPACE_TIME = 3.0

class SpaceCopyDestinyTrans( SpaceCopy, SpaceCopyYeWaiInterface ):
	"""
	天命轮回副本
	"""
	def __init__( self ):
		"""
		初始化
		"""
		SpaceCopy.__init__( self )
		SpaceCopyYeWaiInterface.__init__( self )

	def onEnterCommon( self, baseMailbox, params ):
		"""
		define method
		"""
		SpaceCopy.onEnterCommon( self, baseMailbox, params )

	def onLeaveCommon( self, baseMailbox, params ):
		"""
		define method.
		一个entity准备离开space时的通知；
		此接口在base的ObjectScripts/Space.py中也同样存在，用于处理base收到onLeave()消息时（如果有的话）的处理。
		@param selfEntity: 与自身相匹配的Space Entity
		@param baseMailbox: 要离开此space的entity mailbox
		@param params: dict; 离开此space时需要的附加数据。此数据由当前脚本的packedDataOnLeave()接口根据当前脚本需要而获取并传输
		"""
		SpaceCopy.onLeaveCommon( self, baseMailbox, params )
		
		if len( self._players ) == 0:
			self.addTimer( DESTROY_SPACE_AFTER_LEAVE_SPACE_TIME, 0, Const.SPACE_COPY_CLOSE_CBID )

	def shownDetails( self ):
		"""
		shownDetails 副本内容显示规则：
		[ 
			0: 剩余时间
			1: 剩余小怪
			2: 剩余小怪批次
			3: 剩余BOSS
			4: 蒙蒙数量
			5: 剩余魔纹虎数量
			6: 剩余真鬼影狮数量
		]
		"""
		return [ 0, 1, 3 ]

	def checkSpaceIsFull( self ):
		"""
		覆盖SpaceCopyYeWaiInterface的该方法
		"""
		return False