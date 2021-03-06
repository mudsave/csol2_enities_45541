# -*- coding: utf-8 -*-

# --------------------------------------------------------------------
# 各职业玩家各类属性的说明描述信息
# add by ganjinxing 2009-3-18
#---------------------------------------------------------------------
import csdefine

playerPropertyDescription = {
	# 战士属性描述
	csdefine.CLASS_FIGHTER :{
		"Force":"影响物理攻击力和招架率",								# 力量
		"Brains":"影响法力值、法术攻击力、法术致命率",					# 智力
		"Agility":"影响闪避率和物理致命率",								# 敏捷
		"Habitus":"影响生命值",											# 体质
		"Ditheism":"您拥有的善良值，当pk值等于0时，善良值才会增加，当您的善良值为100时便可成为善人。",	# 善良值
		"Potential": "当您拥有的潜能点不足时，您将无法学习技能。",		# 潜能
		"PK": "当您的pk值达到18时，您便会成为红名。",						# PK值
		"Damage":"您当前的物理攻击力。",								# 物理伤害
		"Hit": "您的物理攻击能够击中同等级目标的几率。实际物理命中率还受“目标闪避率”、“双方等级差距”等影响。",						# 物理命中率
		"Dead": "您的物理攻击能够造成更大伤害的几率。",					# 物理致命率
		"Dodge": "闪避敌人的攻击，能让您不受到任何伤害。实际闪避率还受“攻方命中率”、“双方等级差距”等影响。",				# 闪避率
		"Resisit": "招架能让您本次受到的物理伤害降低一半。",			# 招架率
		"Amor": "提高物理防御能够减少敌人对您的物理攻击带来的伤害。",	# 物理防御率
		"MagDam":"您当前的法术攻击力。",								# 法术伤害
		"MagHit":"您的法术攻击能够击中同等级目标的几率。实际法术命中率还受“目标闪避率”、“双方等级差距”等影响。",					# 法术命中率
		"MagDead":"您的法术攻击能够造成更大伤害的几率。",				# 法术致命率
		"MagAmor":"提高法术防御能够减少敌人对您的法术攻击带来的伤害。",	# 法术防御
		"Credit": "功勋值可用于兑换“师父”称号。",						# 功勋
		"Honor": "参加个人竞技等竞技活动获得的积分。可以用来换取奖励。"	,# 荣誉
		"Vim" : "每天凌晨自动恢复到上限，用来进行生活技能的能量。"		# 活力值
	},
	# 剑客属性描述
	csdefine.CLASS_SWORDMAN :{
		"Force":"影响物理攻击力和招架率",								# 力量
		"Brains":"影响法力值、法术攻击力、法术致命率",					# 智力
		"Agility":"影响物理攻击力，闪避率和物理致命率",					# 敏捷
		"Habitus":"影响生命值",											# 体质
		"Ditheism":"您拥有的善良值，当pk值等于0时，善良值才会增加，当您的善良值为100时便可成为善人。",	# 善良值
		"Potential": "当您拥有的潜能点不足时，您将无法学习技能。",		# 潜能
		"PK": "当您的pk值达到18时，您便会成为红名。",						# PK值
		"Damage":"您当前的物理攻击力。",								# 物理伤害
		"Hit": "您的物理攻击能够击中同等级目标的几率。实际物理命中率还受“目标闪避率”、“双方等级差距”等影响。",						# 物理命中率
		"Dead": "您的物理攻击能够造成更大伤害的几率。",					# 物理致命率
		"Dodge": "闪避敌人的攻击，能让您不受到任何伤害。实际闪避率还受“攻方命中率”、“双方等级差距”等影响。",				# 闪避率
		"Resisit": "招架能让您本次受到的物理伤害降低一半。",			# 招架率
		"Amor": "提高物理防御能够减少敌人对您的物理攻击带来的伤害。",	# 物理防御率
		"MagDam":"您当前的法术攻击力。",								# 法术伤害
		"MagHit":"您的法术攻击能够击中同等级目标的几率。实际法术命中率还受“目标闪避率”、“双方等级差距”等影响。",					# 法术命中率
		"MagDead":"您的法术攻击能够造成更大伤害的几率。",				# 法术致命率
		"MagAmor":"提高法术防御能够减少敌人对您的法术攻击带来的伤害。",	# 法术防御
		"Credit": "功勋值可用于兑换“师父”称号。",						# 功勋
		"Honor": "参加个人竞技等竞技活动获得的积分。可以用来换取奖励。"	,# 荣誉
		"Vim" : "每天凌晨自动恢复到上限，用来进行生活技能的能量。"		# 活力值
	},
	# 射手属性描述
	csdefine.CLASS_ARCHER :{
		"Force":"影响物理攻击力和招架率",								# 力量
		"Brains":"影响法力值、法术攻击力、法术致命率",					# 智力
		"Agility":"影响物理攻击力，闪避率和物理致命率",					# 敏捷
		"Habitus":"影响生命值",											# 体质
		"Ditheism":"您拥有的善良值，当pk值等于0时，善良值才会增加，当您的善良值为100时便可成为善人。",	# 善良值
		"Potential": "当您拥有的潜能点不足时，您将无法学习技能。",		# 潜能
		"PK": "当您的pk值达到18时，您便会成为红名。",						# PK值
		"Damage":"您当前的物理攻击力。",								# 物理伤害
		"Hit": "您的物理攻击能够击中同等级目标的几率。实际物理命中率还受“目标闪避率”、“双方等级差距”等影响。",						# 物理命中率
		"Dead": "您的物理攻击能够造成更大伤害的几率。",					# 物理致命率
		"Dodge": "闪避敌人的攻击，能让您不受到任何伤害。实际闪避率还受“攻方命中率”、“双方等级差距”等影响。",				# 闪避率
		"Resisit": "招架能让您本次受到的物理伤害降低一半。",			# 招架率
		"Amor": "提高物理防御能够减少敌人对您的物理攻击带来的伤害。",	# 物理防御率
		"MagDam":"您当前的法术攻击力。",								# 法术伤害
		"MagHit":"您的法术攻击能够击中同等级目标的几率。实际法术命中率还受“目标闪避率”、“双方等级差距”等影响。",					# 法术命中率
		"MagDead":"您的法术攻击能够造成更大伤害的几率。",				# 法术致命率
		"MagAmor":"提高法术防御能够减少敌人对您的法术攻击带来的伤害。",	# 法术防御
		"Credit": "功勋值可用于兑换“师父”称号。",						# 功勋
		"Honor": "参加个人竞技等竞技活动获得的积分。可以用来换取奖励。",	# 荣誉
		"Vim" : "每天凌晨自动恢复到上限，用来进行生活技能的能量。"		# 活力值
	},
	# 法师属性描述
	csdefine.CLASS_MAGE :{
		"Force":"影响物理攻击力和招架率",								# 力量
		"Brains":"影响法力值、法术攻击力、法术致命率",					# 智力
		"Agility":"影响闪避率和物理致命率",								# 敏捷
		"Habitus":"影响生命值",											# 体质
		"Ditheism":"您拥有的善良值，当pk值等于0时，善良值才会增加，当您的善良值为100时便可成为善人。",	# 善良值
		"Potential": "当您拥有的潜能点不足时，您将无法学习技能。",		# 潜能
		"PK": "当您的pk值达到18时，您便会成为红名。",						# PK值
		"Damage":"您当前的物理攻击力。",								# 物理伤害
		"Hit": "您的物理攻击能够击中同等级目标的几率。实际物理命中率还受“目标闪避率”、“双方等级差距”等影响。",				# 物理命中率
		"Dead": "您的物理攻击能够造成更大伤害的几率。",					# 物理致命率
		"Dodge": "闪避敌人的攻击，能让您不受到任何伤害。实际闪避率还受“攻方命中率”、“双方等级差距”等影响。",				# 闪避率
		"Resisit": "招架能让您本次受到的物理伤害降低一半。",			# 招架率
		"Amor": "提高物理防御能够减少敌人对您的物理攻击带来的伤害。",	# 物理防御率
		"MagDam":"您当前的法术攻击力。",								# 法术伤害
		"MagHit":"您的法术攻击能够击中同等级目标的几率。实际法术命中率还受“目标闪避率”、“双方等级差距”等影响。",					# 法术命中率
		"MagDead":"您的法术攻击能够造成更大伤害的几率。",				# 法术致命率
		"MagAmor":"提高法术防御能够减少敌人对您的法术攻击带来的伤害。",	# 法术防御
		"Credit": "功勋值可用于兑换“师父”称号。",						# 功勋
		"Honor": "参加个人竞技等竞技活动获得的积分。可以用来换取奖励。",# 荣誉
		"Vim" : "每天凌晨自动恢复到上限，用来进行生活技能的能量。"		# 活力值
	},
}