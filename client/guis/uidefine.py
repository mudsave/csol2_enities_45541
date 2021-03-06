# -*- coding: gb18030 -*-
#
# $Id: uidefine.py,v 1.8 2008-09-02 10:01:08 fangpengjun Exp $

"""
macros defination
2005/03/07 : writen by huangyongwei
"""


# --------------------------------------------------------------------
# 全局常量
# --------------------------------------------------------------------
ELEM_CHILD_WARP = 1.0								# GUI.Texture 的距离计算要比 Child 的距离计算短（因为两个组件的修正算法不一样）

# --------------------------------------------------------------------
# ui 状态信息宏
# --------------------------------------------------------------------
class UIState :
	# 状态
	COMMON						= 0					# 普通状态
	HIGHLIGHT 					= 1					# 高亮状态
	PRESSED						= 2					# 按下状态
	SELECTED					= 3					# 选中状态
	DISABLE						= 4					# 无效状态
	LOCKED						= 5					# 锁定状态

	# 状态贴图模式（行数，列数）
	MODE_R1C1					= ( 1, 1 )			# 一行一列
	MODE_R1C2					= ( 1, 2 )			# 一行两列
	MODE_R1C3					= ( 1, 3 )			# 一行三列
	MODE_R1C4					= ( 1, 4 )			# 一行四列
	MODE_R2C1					= ( 2, 1 )			# 两行一列
	MODE_R2C2 					= ( 2, 2 )			# 两行两列
	MODE_R3C1					= ( 3, 1 )			# 三行一列
	MODE_R4C1					= ( 4, 1 )			# 四行一列

	# 选择的状态
	ST_R1C1 					= ( 1, 1 )			# 选中第一行第一列
	ST_R1C2						= ( 1, 2 )			# 选中第一行第二列
	ST_R1C3						= ( 1, 3 )			# 选中第一行第三列
	ST_R1C4						= ( 1, 4 )			# 选中第一行第四列
	ST_R2C1						= ( 2, 1 )			# 选中第二行第一列
	ST_R2C2 					= ( 2, 2 )			# 选中第二行第二列
	ST_R3C1						= ( 3, 1 )			# 选中第三行第一列
	ST_R4C1						= ( 4, 1 )			# 选中第四行第一列


# --------------------------------------------------------------------
# ui 停靠方式，该方式一般应用于 GUI.Text，或没有子 UI 的 UI 中
# --------------------------------------------------------------------
class UIAnchor :
	LEFT						= "LEFT"			# 靠左，宽度增加时，宽度往右边延伸
	CENTER						= "CENTER"			# 靠中，宽度增加时，宽度往左右两边等比延伸
	RIGHT						= "RIGHT"			# 靠右，宽度增加时，宽度往左延伸
	TOP							= "TOP"				# 靠顶，高度增加时，高度往下延伸
	MIDDLE						= "CENTER"			# 靠中，高度增加时，高度往上下两边等比延伸
	BOTTOM						= "BOTTOM"			# 靠下，高度增加时，高度往上延伸


# --------------------------------------------------------------------
# 是否显示滚动条
# --------------------------------------------------------------------
class ScrollBarST :
	AUTO 						= 0					# 自动（能显示得下所有内容时显示，否则不显示）
	SHOW						= 1					# 一直显示
	HIDE						= 2					# 一直不显示


# --------------------------------------------------------------------
# 菜单选项样式
# --------------------------------------------------------------------
class MIStyle :
	COMMON						= 0					# 普通样式
	CHECKABLE					= 1					# 可选样式
	SPLITTER					= 2					# 分隔条样式


# --------------------------------------------------------------------
# 文本输入模式
# --------------------------------------------------------------------
class InputMode :
	COMMON						= 0					# 允许输入任何字符
	INTEGER						= 1					# 只允许输入整数值
	FLOAT						= 2					# 允许输入整数和浮点数
	NATURALNUM					= 3					# 自然数
	PASSWORD					= 4					# 输入密码


# --------------------------------------------------------------------
# UI 的层次关系，层次越低越靠上层
# --------------------------------------------------------------------
class ZSegs :
	L1							= 1					# 第一层，即最上层( 用于像信息提示框之类的顶层UI )
	L2							= 2					# 第二层( 用于菜单之类 )
	L3							= 3					# 第三层( 用于 always on top UI )
	L4							= 4					# 第四层( 用于常规 UI )
	L5							= 5					# 第五层( 用于一直处于底层的 UI )
	LMAX						= 5


# --------------------------------------------------------------------
# 拖放标记，这些标记用于拖起一个对象时，赋予拖放对象，当放下时，再通过检查该标记来判断放下的对象能否被目标接纳
# --------------------------------------------------------------------
class DragMark :
	NONE						= 0					# 未知对象
	QUICK_BAR					= 1					# 快捷栏上的图标
	PET_QUICK_BAR				= 2					# 宠物快捷栏
	KITBAG_BAG					= 3					# 背包里的背包图标
	KITBAG_WND					= 4					# 背包上的物品图标
	EQUIP_WND					= 5					# 装备栏上的图标
	SKILL_WND					= 6					# 技能栏上的图标
	ROLES_TRADING_WND			= 7					# 玩家之间交易的图标
	EQUIP_REPAIR_WND			= 8					# 装备修理中的图标
	NPC_TRADE_BUY				= 9					# 贩卖物品中的图标
	BANK_WND_BAG				= 10				# 仓库里的背包图标
	BANK_WND_ITEM				= 11				# 仓库力的物品图标
	NPC_TRADE_REDEEM			= 12				# 赎回物品窗口
	PETSKILL_BAR					= 13				# 宠物仅能栏
	MY_PET_PANEL				= 14				# 自己的宠物仓库
	STORAGE_PET_PANEL			= 15				# 寄存处的宠物仓库
	VEND_SELL_WND				= 16				# 摆摊卖家窗口
	VEND_BUY_WND				= 17				# 摆摊买家窗口
	SPECIAL_SHOP_WND			= 18 				# 道具商城窗口
	RACE_BAG						= 19				# 赛马道具背包
	VEHICLES_PANEL				= 20				# 玩家骑宠栏
	VEHICLE_SKILL_BAR			= 21				# 骑宠技能栏
	TONG_STORAGE_ITEM			= 22				# 帮会仓库图标
	MAIL_SEND_ITEM				= 23				# 发信物品图标
	MAIL_RECEIVE_ITEM			= 24				# 收信物品图标
	TISHOU_SELL_PANEL			= 25				# NPC替售商品出售面板
	TISHOU_BUY_PANEL			= 26				# NPC替售商品购买面板
	VEND_PURCHASE_PANEL		= 27				# 摆摊收购界面
	GUARD_LIST_PANEL			= 28				# 盘古守护面板
	GUARD_QUICK_BAR			= 29				# 守护召唤技能栏
	LoLCOPY_TRADE_WND			= 30 			# 英雄副本交易界面
	SERMON_COMMON_WND			= 31 			# 普通道心背包
	SERMON_EQUIP_WND			= 32 				# 装备道心背包
	SERMON_SHOP_WND			= 33				# 证道积分兑换界面
	SPACE_SKILL				= 34				# 副本技能图标
	TONG_SPECIAL_ITEM		= 35				# 帮会特殊商品

# --------------------------------------------------------------------
# 对话框返回值
# --------------------------------------------------------------------
class DialogResult :
	OK							= 0x01				# 点击了确定按钮
	CANCEL						= 0x02				# 点击的取消按钮
	YES							= 0x04				# 点击了是按钮
	NO							= 0x08				# 点击了否按钮


# ----------------------------------------------------
# 密码锁窗口返回结果
# ----------------------------------------------------
class PassResult:
	LOCK						=	0x01			# 上锁按钮
	UNLOCK						=	0x02			# 开锁按钮
	FOREUNLOCK					=	0x04			# 永久开锁按钮
	SETRESULT					=	0x08			# 设置密码确定按钮
	CHANGERESULT				=	0x10			# 修改密码确定按钮


# ----------------------------------------------------
# 窗口互斥显示组
# 注意，由于生成互斥组是没有显示说明的，所以每新增一个互斥组或者
# 添加一个新的UI到互斥组时，为了方便后续的维护和添加新的互斥窗口，
# 请务必在这里添加备注：
# ----------------------------------------------------
class MutexGroup :
	TRADE1						= 1					# 互斥交易分组1，其中包括以下窗口：
	# --------------------------------------------------------------------------
	# TiShouSellWindow, EquipProduce, CasketWindow, PetFoster, PetTrade,
	# StoreWindow, TradingWindow, StorageWindow, TradeWindow, VendBuyWindow,
	# TiShouBuyWindow, VendSellWindow, CommissionViewer, EQExtractWnd, EQPourWnd
	# --------------------------------------------------------------------------

	TRADE2						= 2					# 互斥交易分组2，其中包括以下窗口：
	# --------------------------------------------------------------------------
	# QuestTalkWindow, PetTrade, TradingWindow, GroupRewards
	# --------------------------------------------------------------------------

	PET1						= 3					# 互斥宠物分组1，其中包括以下窗口：
	# --------------------------------------------------------------------------
	# PetStorage, PetTrade, PetFoster
	# --------------------------------------------------------------------------

	TANABATA1					= 4					# 互斥七夕活动窗口，其中包括以下窗口：
	# --------------------------------------------------------------------------
	# MsgBoard，TbExplainWnd，TbVoteWnd
	# --------------------------------------------------------------------------
