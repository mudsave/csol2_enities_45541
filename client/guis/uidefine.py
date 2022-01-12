# -*- coding: gb18030 -*-
#
# $Id: uidefine.py,v 1.8 2008-09-02 10:01:08 fangpengjun Exp $

"""
macros defination
2005/03/07 : writen by huangyongwei
"""


# --------------------------------------------------------------------
# ȫ�ֳ���
# --------------------------------------------------------------------
ELEM_CHILD_WARP = 1.0								# GUI.Texture �ľ������Ҫ�� Child �ľ������̣���Ϊ��������������㷨��һ����

# --------------------------------------------------------------------
# ui ״̬��Ϣ��
# --------------------------------------------------------------------
class UIState :
	# ״̬
	COMMON						= 0					# ��ͨ״̬
	HIGHLIGHT 					= 1					# ����״̬
	PRESSED						= 2					# ����״̬
	SELECTED					= 3					# ѡ��״̬
	DISABLE						= 4					# ��Ч״̬
	LOCKED						= 5					# ����״̬

	# ״̬��ͼģʽ��������������
	MODE_R1C1					= ( 1, 1 )			# һ��һ��
	MODE_R1C2					= ( 1, 2 )			# һ������
	MODE_R1C3					= ( 1, 3 )			# һ������
	MODE_R1C4					= ( 1, 4 )			# һ������
	MODE_R2C1					= ( 2, 1 )			# ����һ��
	MODE_R2C2 					= ( 2, 2 )			# ��������
	MODE_R3C1					= ( 3, 1 )			# ����һ��
	MODE_R4C1					= ( 4, 1 )			# ����һ��

	# ѡ���״̬
	ST_R1C1 					= ( 1, 1 )			# ѡ�е�һ�е�һ��
	ST_R1C2						= ( 1, 2 )			# ѡ�е�һ�еڶ���
	ST_R1C3						= ( 1, 3 )			# ѡ�е�һ�е�����
	ST_R1C4						= ( 1, 4 )			# ѡ�е�һ�е�����
	ST_R2C1						= ( 2, 1 )			# ѡ�еڶ��е�һ��
	ST_R2C2 					= ( 2, 2 )			# ѡ�еڶ��еڶ���
	ST_R3C1						= ( 3, 1 )			# ѡ�е����е�һ��
	ST_R4C1						= ( 4, 1 )			# ѡ�е����е�һ��


# --------------------------------------------------------------------
# ui ͣ����ʽ���÷�ʽһ��Ӧ���� GUI.Text����û���� UI �� UI ��
# --------------------------------------------------------------------
class UIAnchor :
	LEFT						= "LEFT"			# ���󣬿�������ʱ���������ұ�����
	CENTER						= "CENTER"			# ���У���������ʱ���������������ߵȱ�����
	RIGHT						= "RIGHT"			# ���ң���������ʱ��������������
	TOP							= "TOP"				# �������߶�����ʱ���߶���������
	MIDDLE						= "CENTER"			# ���У��߶�����ʱ���߶����������ߵȱ�����
	BOTTOM						= "BOTTOM"			# ���£��߶�����ʱ���߶���������


# --------------------------------------------------------------------
# �Ƿ���ʾ������
# --------------------------------------------------------------------
class ScrollBarST :
	AUTO 						= 0					# �Զ�������ʾ������������ʱ��ʾ��������ʾ��
	SHOW						= 1					# һֱ��ʾ
	HIDE						= 2					# һֱ����ʾ


# --------------------------------------------------------------------
# �˵�ѡ����ʽ
# --------------------------------------------------------------------
class MIStyle :
	COMMON						= 0					# ��ͨ��ʽ
	CHECKABLE					= 1					# ��ѡ��ʽ
	SPLITTER					= 2					# �ָ�����ʽ


# --------------------------------------------------------------------
# �ı�����ģʽ
# --------------------------------------------------------------------
class InputMode :
	COMMON						= 0					# ���������κ��ַ�
	INTEGER						= 1					# ֻ������������ֵ
	FLOAT						= 2					# �������������͸�����
	NATURALNUM					= 3					# ��Ȼ��
	PASSWORD					= 4					# ��������


# --------------------------------------------------------------------
# UI �Ĳ�ι�ϵ�����Խ��Խ���ϲ�
# --------------------------------------------------------------------
class ZSegs :
	L1							= 1					# ��һ�㣬�����ϲ�( ��������Ϣ��ʾ��֮��Ķ���UI )
	L2							= 2					# �ڶ���( ���ڲ˵�֮�� )
	L3							= 3					# ������( ���� always on top UI )
	L4							= 4					# ���Ĳ�( ���ڳ��� UI )
	L5							= 5					# �����( ����һֱ���ڵײ�� UI )
	LMAX						= 5


# --------------------------------------------------------------------
# �Ϸű�ǣ���Щ�����������һ������ʱ�������ϷŶ��󣬵�����ʱ����ͨ�����ñ�����жϷ��µĶ����ܷ�Ŀ�����
# --------------------------------------------------------------------
class DragMark :
	NONE						= 0					# δ֪����
	QUICK_BAR					= 1					# ������ϵ�ͼ��
	PET_QUICK_BAR				= 2					# ��������
	KITBAG_BAG					= 3					# ������ı���ͼ��
	KITBAG_WND					= 4					# �����ϵ���Ʒͼ��
	EQUIP_WND					= 5					# װ�����ϵ�ͼ��
	SKILL_WND					= 6					# �������ϵ�ͼ��
	ROLES_TRADING_WND			= 7					# ���֮�佻�׵�ͼ��
	EQUIP_REPAIR_WND			= 8					# װ�������е�ͼ��
	NPC_TRADE_BUY				= 9					# ������Ʒ�е�ͼ��
	BANK_WND_BAG				= 10				# �ֿ���ı���ͼ��
	BANK_WND_ITEM				= 11				# �ֿ�������Ʒͼ��
	NPC_TRADE_REDEEM			= 12				# �����Ʒ����
	PETSKILL_BAR					= 13				# ���������
	MY_PET_PANEL				= 14				# �Լ��ĳ���ֿ�
	STORAGE_PET_PANEL			= 15				# �Ĵ洦�ĳ���ֿ�
	VEND_SELL_WND				= 16				# ��̯���Ҵ���
	VEND_BUY_WND				= 17				# ��̯��Ҵ���
	SPECIAL_SHOP_WND			= 18 				# �����̳Ǵ���
	RACE_BAG						= 19				# �������߱���
	VEHICLES_PANEL				= 20				# ��������
	VEHICLE_SKILL_BAR			= 21				# ��輼����
	TONG_STORAGE_ITEM			= 22				# ���ֿ�ͼ��
	MAIL_SEND_ITEM				= 23				# ������Ʒͼ��
	MAIL_RECEIVE_ITEM			= 24				# ������Ʒͼ��
	TISHOU_SELL_PANEL			= 25				# NPC������Ʒ�������
	TISHOU_BUY_PANEL			= 26				# NPC������Ʒ�������
	VEND_PURCHASE_PANEL		= 27				# ��̯�չ�����
	GUARD_LIST_PANEL			= 28				# �̹��ػ����
	GUARD_QUICK_BAR			= 29				# �ػ��ٻ�������
	LoLCOPY_TRADE_WND			= 30 			# Ӣ�۸������׽���
	SERMON_COMMON_WND			= 31 			# ��ͨ���ı���
	SERMON_EQUIP_WND			= 32 				# װ�����ı���
	SERMON_SHOP_WND			= 33				# ֤�����ֶһ�����
	SPACE_SKILL				= 34				# ��������ͼ��
	TONG_SPECIAL_ITEM		= 35				# ���������Ʒ

# --------------------------------------------------------------------
# �Ի��򷵻�ֵ
# --------------------------------------------------------------------
class DialogResult :
	OK							= 0x01				# �����ȷ����ť
	CANCEL						= 0x02				# �����ȡ����ť
	YES							= 0x04				# ������ǰ�ť
	NO							= 0x08				# ����˷�ť


# ----------------------------------------------------
# ���������ڷ��ؽ��
# ----------------------------------------------------
class PassResult:
	LOCK						=	0x01			# ������ť
	UNLOCK						=	0x02			# ������ť
	FOREUNLOCK					=	0x04			# ���ÿ�����ť
	SETRESULT					=	0x08			# ��������ȷ����ť
	CHANGERESULT				=	0x10			# �޸�����ȷ����ť


# ----------------------------------------------------
# ���ڻ�����ʾ��
# ע�⣬�������ɻ�������û����ʾ˵���ģ�����ÿ����һ�����������
# ����һ���µ�UI��������ʱ��Ϊ�˷��������ά���������µĻ��ⴰ�ڣ�
# ��������������ӱ�ע��
# ----------------------------------------------------
class MutexGroup :
	TRADE1						= 1					# ���⽻�׷���1�����а������´��ڣ�
	# --------------------------------------------------------------------------
	# TiShouSellWindow, EquipProduce, CasketWindow, PetFoster, PetTrade,
	# StoreWindow, TradingWindow, StorageWindow, TradeWindow, VendBuyWindow,
	# TiShouBuyWindow, VendSellWindow, CommissionViewer, EQExtractWnd, EQPourWnd
	# --------------------------------------------------------------------------

	TRADE2						= 2					# ���⽻�׷���2�����а������´��ڣ�
	# --------------------------------------------------------------------------
	# QuestTalkWindow, PetTrade, TradingWindow, GroupRewards
	# --------------------------------------------------------------------------

	PET1						= 3					# ����������1�����а������´��ڣ�
	# --------------------------------------------------------------------------
	# PetStorage, PetTrade, PetFoster
	# --------------------------------------------------------------------------

	TANABATA1					= 4					# ������Ϧ����ڣ����а������´��ڣ�
	# --------------------------------------------------------------------------
	# MsgBoard��TbExplainWnd��TbVoteWnd
	# --------------------------------------------------------------------------