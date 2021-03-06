# -*- coding: gb18030 -*-
#
# $Id: BankFacade.py,v 1.9 2008-05-30 03:07:39 yangkai Exp $

"""
implement bank facade
2006/10/25 : writen by huangyongwei
"""

import BigWorld
from bwdebug import *
from ItemsFactory import ObjectItem
from event.EventCenter import *
import csdefine
import ItemTypeEnum
import csstatus

class BankFacade :
	@staticmethod
	def reset() :
		pass

# --------------------------------------------------------------------
# called by base
# --------------------------------------------------------------------

def onHideBankWindow() :
	"""
	request for hiding bank window
	"""
	fireEvent( "EVT_ON_HIDE_STORE_WINDOW" )

# -----------------------------------------------------
def onUpdateBankItem( itemIndex, item ) :
	"""
	when an item had been updated, it will be called
	@type			index : int
	@param			index : item index in bank window
	@type			item  : instance
	@param			item  : object item instance
	@return				  : None
	"""
	itemInfo = None
	if item is not None :
		tamount = item.getAmount()
		ticon = item.icon()
		tid = item.id
		itemInfo = ObjectItem( item )
	fireEvent( "EVT_ON_UPDATE_STORE_ITEM",itemIndex, itemInfo )

def onBankMoneyChanged( amount ) :
	"""
	when store money changed, it will be changed
	@type			amount : int
	@param			amount : the number of store money
	@return				   : None
	"""
	fireEvent( "EVT_ON_STORE_MONEY_CHANGED", amount )

# --------------------------------------------------------------------
# called by ui
# --------------------------------------------------------------------
def tradeOverInventory():
	"""
	when Inventory over it will called
	"""
	player = BigWorld.player()
	player.cell.leaveTradeIV()

def getBankItemDescription( index ) :
	"""
	get item description
	@type			index : int
	@param			index : the item index
	@return				  : None
	"""
	player = BigWorld.player()
	return player.getItemDescriptionIV( index )

# -----------------------------------------------------
def storeBankItem( indexInBank, kitbagID, indexInBag, amount ) :
	"""
	store items
	@type			indexInBank : int
	@param			indexInBank : destanation in bank
	@type			kitBagID	: int
	@param			kitBagID	: kit bag index
	@type			indexInKit	: int
	@param			indexInKit	: source index in kit bag
	@type			amount		: int
	@param			amount		: the number of item you will be stored
	@return						: None
	"""
	player = BigWorld.player()
	player.storeItemIV( indexInBank, kitbagID, indexInBag, amount )

def storeBankMoney( amount ) :
	"""
	store money
	@type			money 		: int32
	@param			money		: amount of money you want to store
	@return						: None
	"""
	player = BigWorld.player()
	BigWorld.player().storeMoneyIV( amount )

# -------------------------------------------
def takeBankItem( indexInBank, kitbagID, indexInBag, amount ) :
	"""
	store items
	@type			indexInBank : int
	@param			indexInBank : destanation in bank
	@type			kitBagID	: int
	@param			kitBagID	: kit bag index
	@type			indexInKit	: int
	@param			indexInKit	: source index in kit bag
	@type			amount		: int
	@param			amount		: the number of item you will be stored
	@return						: None
	"""
	player = BigWorld.player()
	player.takeItemIV( indexInBank, kitbagID, indexInBag, amount )

def takeBankMoney( amount ) :
	"""
	store money
	@type			money 		: int32
	@param			money		: amount of money you want to take
	@return						: None
	"""
	BigWorld.player().takeMoneyIV( amount )

def getHireMoney( index, time ):
# ????????????????????????????????????????????
	money = 12345
	return money

def getRemain( index, time ): # ????????????
	return 0
#	remainTime =

# -----------------------------------------------------
def swapBankItem( srcIdx, dstIdx ) :
	"""
	exchange two items' sits
	@type			srcIndex : int
	@param			srcIndex : the source index
	@type			dstIndex : int
	@param			dstIndex : the distance index
	@return 				 : None
	"""
	player = BigWorld.player()
	player.swapItemIV( srcIdx, dstIdx )

def splitBankItem( index, amount ) :
	"""
	@type			srcIndex : int
	@param			srcIndex : the source index
	@type			amount	 : int
	@param			amount	 : the number of splitting
	@return 				 : None
	"""
	player = BigWorld.player()
	player.splitItemIV( index, amount )

def changePassword( password ):
	"""
	@type			password : string
	@param			suitIndex : the password string
	@return						: None
	"""
	pass

def settingPassword( password ):
	"""
	@type			password : string
	@param			suitIndex : the password string
	@return						: None
	"""
	pass

def hirePacks( packsIndex, timeStr ):
	#????????????????????????????????????????????????????????????
	"""
	@type			suitIndex : int
	@param			suitIndex : the packs index
	@type			timeStr	 : string
	@param			timeStr	 : the hire time
	@return 				 : None
	"""
	time = int( timeStr )
	hireMoney = getHireMoney( packsIndex, time )#????????????????????????????
	player = BigWorld.player()
	if player.money < hireMoney:
		player.statusMessage( csstatus.MONEY_HIRE_NOT_ENOUGH )
		return
	# ????????????????????????????????????????????????????????????????
	remainTime = getRemain( packsIndex, timeStr )
	fireEvent( "EVT_ON_UPDATE_STORE_PACKS", packsIndex, remainTime )

def getHires( packsIndex ):
	# ????????????????????????????????????
	"""
	@type			packsIndex : int
	@param			packsIndex : the packs index
	@return					: None
	"""
	pass

def isHasPassword( ):
# ??????????????????????????
	"""
	@type			id : int
	@param			id : the bank or the kitbag index
	@return				: bool
	"""
	return True

def isLocked( ):
#????????????????????????
	"""
	@type			id : int
	@param			id : the bank or the kitbag index
	@return				: bool
	"""
	return True

def getPassword( ):
#??????????????????????
	"""
	@type			id : int
	@param			id : the bank or the kitbag index
	@return				: int
	"""
	psw  = "123456" #????????????
	return  psw

def freezeUnlock( ):
# ????????????????24????????????
	"""
	@type			id : int
	@param			id : the bank or the kitbag index
	@return				: None
	"""
	pass

def dropItemFromKitbag( srcBagIndex, gbIndex, packIndex ): #??????????????????????
# ??????????????????????????????????????????
	"""
	@type			srcBagIndex : int
	@param			srcBagIndex : the kitbag index
	@type			gbIndex : int
	@param			gbIndex : the package globel index
	@type			packIndex : int
	@param			packIndex : the target pack index
	@return				: None
	"""
	player = BigWorld.player()
	orderID = srcBagIndex * csdefine.KB_MAX_SPACE + gbIndex
	item = player.getItem_( orderID )
	amount = item.amount
	if item is None:
		player.statusMessage( csstatus.EQUIP_ANALYZE_NOT_EXIST )
		return
	storeBankItem( packIndex, srcBagIndex, gbIndex, amount )

def dropPackFromKitbag( srcBagIndex, index, packIndex ): # ??????????????????
	player = BigWorld.player()
	orderID = srcBagIndex * csdefine.KB_MAX_SPACE + index
	item = player.getItem_( orderID )
	itemInfo = ObjectItem( item )
	amount = item.amount
	if item is None:
		player.statusMessage( csstatus.EQUIP_ANALYZE_NOT_EXIST )
		return
	fireEvent( "EVT_ON_UPDATE_STORE_PACK", packIndex, itemInfo )# ??????????????
