# -*- coding: gb18030 -*-
#
# $Id: NPC.py,v 1.65 2008-09-03 07:04:17 kebiao Exp $

"""
NPC基类
"""

import BigWorld
from bwdebug import *
import csdefine
import csstatus
from NPC import NPC

class Chapman( NPC ):
	"""
	商人 
	"""
	def __init__( self ):
		"""
		初始化从XML读取信息
		"""
		NPC.__init__( self )
		
# NPC.py
