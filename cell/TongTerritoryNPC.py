# -*- coding: gb18030 -*-
#
# $Id: NPC.py,v 1.65 2008-09-03 07:04:17 kebiao Exp $

"""
NPC����
"""

import BigWorld
from bwdebug import *
import csdefine
import csstatus
from NPC import NPC

class TongTerritoryNPC( NPC ):
	"""
	������NPC����
	"""
	def __init__( self ):
		"""
		��ʼ����XML��ȡ��Ϣ
		"""
		NPC.__init__( self )
		
	def lock( self ):
		"""
		define method.
		NPC����ס�� ����Ա�޷���������
		"""
		self.locked = True

	def unlock( self ):
		"""
		define method.
		NPC�������� ����Ա�ָ���������
		"""
		self.locked = False
		
# NPC.py