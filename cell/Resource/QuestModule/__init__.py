# -*- coding: gb18030 -*-

from Quest import Quest
from QuestRandom import QuestRandom
from QuestRandomGroup import QuestRandomGroup
from QuestDirectFinish import QuestDirectFinish
from QuestFixedLoop import QuestFixedLoop
from QuestPotential import QuestPotential
from QuestLoopGroup import QuestLoopGroup
from QuestDart import QuestDart
from QuestRob import QuestRob
from QuestMemberDart import QuestMemberDart
from QuestMerchant import QuestMerchant
from QuestTongNormal import QuestTongNormalLoopGroup
from QuestImperialExamination import QuestImperialExamination
from QuestTongNormal import QuestTongFeteGroup
from QuestTongNormal import QuestTongBuildGroup
from Quest108Star import Quest108Star
from QuestFamilyDart import QuestFamilyDart
from QuestTongDart import QuestTongDart
from QuestNewYearGroup import QuestNewYearGroup
from QuestCompleteFixCount import QuestCompleteFixCount
from QuestTongSpaceCopyGroup import QuestTongSpaceCopyGroup
from QuestTongFuBen import QuestTongFuBen
from QuestPotentialSpecial import QuestPotentialSpecial
from QuestAbandonAtNPC import QuestAbandonAtNPC
from QuestNormal import QuestNormal
from QuestCampActivity import QuestCampActivity
from QuestCampDaily import QuestCampDaily
from QuestAuto import QuestAuto

#from QuestRandom import QuestRandom
#from QuestRandomGroup import QuestRandomGroup

map_type = {
		""						: Quest,
		"normal"				: Quest,										#普通任务
		"random"				: QuestRandom,									#子任务
		"random_group"			: QuestRandomGroup,								#赏金讨伐任务
		"fixed_loop"			: QuestFixedLoop,								#固定次数任务
		"direct_finish" 		: QuestDirectFinish,							#直接完成的任务
		"potential"				: QuestPotential,								#潜能任务
		"loop_group"			: QuestLoopGroup,								#环任务
		"quest_dart"			: QuestDart,									#运镖任务
		"quest_rob"				: QuestRob,										#劫镖任务
		"quest_member_dart"		: QuestMemberDart,								#成员运镖任务
		"quest_merchant" 		: QuestMerchant,
		"quest_tongnormal"		: QuestTongNormalLoopGroup,						#帮会日常任务
		"questimperialexamination" : QuestImperialExamination,					#科举
		"quest_tongfete" 		: QuestTongFeteGroup,							#帮会建筑任务
		"quest_tongbuild"		: QuestTongBuildGroup,
		"quest_108star"			: Quest108Star,									#固定次数任务
		"quest_family_dart"		: QuestFamilyDart,								#家族运镖
		"quest_tong_dart"		: QuestTongDart,								# 帮会运镖
		"quest_new_year"		: QuestNewYearGroup,							#新年机缘任务
		"complete_fixed"		: QuestCompleteFixCount,						#完成任务次数
		"tong_space_copy"		: QuestTongFuBen,								# 帮会副本子任务
		"tong_space_copy_grp"	: QuestTongSpaceCopyGroup,						# 帮会副本任务组
		"potential_special"		: QuestPotentialSpecial,						# 潜能副本特殊任务
		"quest_abandonatnpc"	: QuestAbandonAtNPC,							# 只能到指定NPC处放弃的任务
		"normal1"				: QuestNormal,									# 普通任务1( 等级差超过10级，依然会显示绿色感叹号的接取任务提示 )
		"quest_campactivity"	: QuestCampActivity,							# 阵营活动任务
		"quest_campdaily"		: QuestCampDaily,								# 阵营日常任务
		"auto"					: QuestAuto,									# 自动任务
	}

def getQuestModule( questType ):
	return map_type.get( questType, Quest )