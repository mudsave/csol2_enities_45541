# -*- coding: gb18030 -*-
#
# 2009-05-25 SongPeifang
#
"""
JuLingMo��
"""

from Monster import Monster
import Love3
import csdefine
import BigWorld

class JuLingMo( Monster ):
	"""
	�������ű�
	"""
	def __init__( self ):
		"""
		��ʼ����XML��ȡ��Ϣ
		"""
		Monster.__init__( self )

	def onFrogDieNotify( self, notifyStr ):
		"""
		����֪ͨ
		"""
		Love3.g_baseApp.anonymityBroadcast( notifyStr, [] )
		if BigWorld.globalData.has_key( "JuLingMoAlive" ):
			del BigWorld.globalData[ "JuLingMoAlive" ]