# -*- coding: UTF-8 -*-

# 神机匣
main = { 'lbTitle'	 : { 'text' : "神机匣" },
		'tab_0'		 : { 'text' : "装备打造" },
		'tab_1'		 : { 'text' : "属性抽取" },
		'tab_2'		 : { 'text' : "属性灌注" },
		'tab_3'		 : { 'text' : "装备强化" },
		'tab_4'		 : { 'text' : "特殊合成" },
		'tab_5'		 : { 'text' : "装备认主" },
		'btnOk'		 : { 'text' : "确 定" },
		}

#装备打造
EquipBuildPanel = { 'draw'		 	: { 'text' : "图 纸" },
					'stuff'		 	: { 'text' : "材 料" },
					'whiteEquip'  	: { 'text' : "白 装" },
					'wireStuff'			: { 'text' : "线 材" },
					'mainStuff'			: { 'text' : "主 材" },
					'aidStuff'			: { 'text' : "辅 材" },
					'buy'			: { 'text' : "购 买" },
					'obliv'			: { 'text' : "遗 忘" },
					'build'			: { 'text' : "点我打造" },
					'drawDsp'		: { 'text' : "此处为你所习得的装备制作配方。" },
					'proDsp'		: { 'text' : "成功打造后,成品装备将出现在这里。" },
					"rtMoney"		: { "text": "花费:%s" },
					"fixedAttr"		: { "text": "固定属性:" },
					"randomAttr" 	: {"text": "随机属性:"},
		}

#属性抽取
AttrExtractPanel = { 'specProps'		 	: { 'text' : "特殊道具" },
					'sucRateText'		: { 'text' : "本次抽取成功率为" },
					'reqMoney'		 	: { 'text' : "所需金钱" },
					'tokenInfo'			: { 'text' : "@F{fc = ( 230, 227, 185, 255 )}额外使用神征令，能将抽取成功率提升至100%。" },
					'token'				: { 'text' : "@F{fc = ( 127, 127, 127, 200 )}神征令" },
					'crysDsp'			: { 'text' : "放置封灵石于此,它们是用来抽取装备属性的必要道具,成功后,封灵石将变为韵灵琥珀，暂存住装备属性。" },
					'equipDsp'			: { 'text' : "放置需要被抽取属性的装备于此，当装备拥有多条属性时，使用1个封灵石，将随机抽取装备的1条属必须是60级以上。" },
		}

#装备强化
EquipIntensifyPanel = { 'inputEquip'		 	: { 'text' : "请放入装备" },
					   'reqDragon'		 	: { 'text' : "所需龙珠" },
					   'putSymbol'	: { 'text' : "放入幸运石" },
					   'sucRate'		 	: { 'text' : "成功率:%d%%" },
					   'insTitle'		: { 'text' : "强化说明" },
					   'instInfo'		: { 'text' : "@F{fc = ( 230, 227, 185, 255 )}@S{4}装备有九个星级。通过装备强化提高装备星级，增加装备基础属性。将欲强化的装备和龙珠放入神机匣就可以强化了！确定按钮上方会显示成功率，装备星级越高升下一级的成功率越低。强化时加入幸运宝石可以提高成功率。@B@S{4}@F{fc=c4}白色龙珠针对1-30级的装备。@B@S{4}蓝色龙珠针对31-50级的装备。@B@S{4}黄色龙珠针对51-90级的装备。@B@S{4}粉色龙珠针对91-120级的装备。@B@S{4}绿色龙珠针对121-150级的装备。@F{fc=( 230, 227, 185, 255 )}@B@S{4}每块初级幸运宝石可以提高@F{fc=c29}4%@F{fc=( 230, 227, 185, 255 )}成功率。@B@S{4}每块高级幸运宝石可以提高@F{fc=c29}10%@F{fc=( 230, 227, 185, 255 )}成功率。@B@S{4}可以放入多颗龙珠和多块幸运宝石，但每次只会使用@F{fc=c3}一颗@F{fc=( 230, 227, 185, 255 )}龙珠和@F{fc=c3}一块@F{fc=( 230, 227, 185, 255 )}幸运宝石。@B@S{4}通过任务也许会奖励少量白色龙珠。主要获得龙珠和幸运宝石的途径是在道具商城中购买。" },
		}

#特殊合成
SpeComPanel = { 'comTitle':{ 'text' : "特殊合成说明" },
				 'compose':{ 'text' : "合 成" },
				'compInfo':{ 'text' : "@F{fc = ( 230, 227, 185, 255 )}@S{4}特殊合成是合成各种必要的任务物品、特殊道具和特殊装备的功能。@B@S{4}将配方和材料放进神机匣选择“合成”，就可以进行合成。配方有可能是怪物掉落，有可能是NPC传授，也可能需要玩家自己摸索。特殊合成可能使用各种材料，除了正规的铁、玉、丝绸等还有可能使用各种看似没用的杂物或任务物品。@B@S{4}大部分材料和杂物由怪物掉落，还有部分需要在商城中购买。" },
		}

#属性灌注
AttrPourPanel = { 'stoneDsp':{ 'text' : "放置韵灵琥珀于此，它是属性灌注的必要道具，成功后，韵灵琥珀上的属性会转移到装备上，韵灵琥珀消失。" },
				'equipDsp':{ 'text' : "放置被灌注属性的装备于此，配合韵灵琥珀成功灌注后，装备将获得相关属性加成。被灌注属性的装备品质必须是粉色或以上的。" },
		}


#装备认主
EquipBindPanel = { 'bindTitle':{ 'text' : "装备认主说明" },
					'bind':{ 'text' : "认 主" },
					'putChain'	: { 'text' : "放入灵魂锁链" },
					'bindInfo':{ 'text' : "@F{fc = ( 230, 227, 185, 255 )}@S{4}装备认主可以让这件装备不会因为死亡等原因掉落。将“灵魂锁链”和期望认主的装备一起放进神机匣，支付一定的金钱就能完成装备和当前角色的认主。认主后装备属性也会得到增强。@B@S{4}@F{fc=c3}装备等级越高需要花费的金钱越多@F{fc=( 230, 227, 185, 255 )}。同时“灵魂锁链”需要在道具商城中购买。",}
		}
