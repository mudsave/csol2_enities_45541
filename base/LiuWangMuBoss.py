# -*- coding: gb18030 -*-
#
# 2009-05-25 SongPeifang
#
"""
ToxinFrog类
"""
from Monster import Monster

class LiuWangMuBoss( Monster ):
	"""
	地宫六王墓Boss
	"""
	def __init__( self ):
		"""
		初始化从XML读取信息
		"""
		Monster.__init__( self )
		
	def onLiuWangMuMonsterDieNotify( self, notifyStr ):
		"""
		死后通知
		"""
		self.getScript().onLiuWangMuMonsterDieNotify( notifyStr )
		
