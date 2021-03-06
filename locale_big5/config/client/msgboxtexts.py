# -*- coding: cp950 -*-

Datas = {
# GameMgr.py( 0x0000∼0x0020 )
0x0000 : "你確實要退出遊戲嗎？",
0x0001 : "請用 Launcher.exe 登錄遊戲！",

# LoginMgr.py（0x0021∼0x0060）
0x0021 : "登錄失敗: %s",
0x0022 : "登錄失敗: 未知錯誤: ( %d, %d )",
0x0023 : "你的賬號已經被封鎖，封存時間為%s！",
0x0024 : "永久",
0x0025 : "%Y年%m月%d日%H時%M分%S秒",
0x0031 : "The connection could not be initiated as either the client was already connected to a server!",
0x0032 : "登錄成功。",
0x0033 : "無法連接到服務器。",
0x0034 : "無法連接到服務器。",
0x0035 : "CLIENT ERROR: An unknown client-side error has occurred.",
0x0036 : "客戶端主動取消登錄。",
0x0037 : "CLIENT ERROR: The client is already online locally (i.e. exploring a space offline).",
0x0038 : "非法登錄數據。",
0x0039 : "版本不匹配，請升級到最新版本。",
0x003a : "帳號或密碼不正確。",
0x003b : "帳號或密碼不正確。",
0x003c : "此帳號已登錄。",
0x003d : "版本不匹配，請升級到最新版本。",
0x003e : "服務器未啟動（1, -70）。",
0x003f : "服務器未啟動（1, -71）。",
0x0040 : "帳號或密碼不正確。",
0x0041 : "服務器未啟動（1, -73）。",
0x0042 : "SERVER ERROR: The updater is not ready yet.",
0x0043 : "服務器未啟動（1, -75）。",
0x0044 : "服務器負載過重，請稍後再試(1, -76)。",
0x0045 : "服務器繁忙，請稍後再試(1, -77)。",
0x0046 : "服務器未啟動（1, -78）。",
0x0047 : "服務器負載過重(1, -79)。",
0x0048 : "服務器未啟動(1, -80)。",
0x0049 : "賬號已被 GM 托管！",
0x004a : "自動激活隊列已滿，請稍後再試。",
0x004b : "登錄成功，開始接受數據（2, 1）。",
0x004c : "從服務器斷開（6, 1）。",
0x0050 : "名字長度不能超過 14 個字節",
0x0051 : "您輸入的用戶名無效，請重新輸入",
0x0052 : "名稱不合法！",
0x0053 : "輸入的名字有禁用詞匯！",
0x0054 : "存在角色數量已經達到上限！",

# FamilyInterface.py（0x0061∼0x0080）
0x0061 : "你確認要花費20金幣爭奪該NPC嗎?",
0x0062 : "您真的要放棄對這個NPC占領麼？如果放棄，貴家族將不再占領任何NPC！",

# HyperlinkMgr.py（0x0081∼0x00a0）
0x0081 : "是否使用引路蜂傳送?",
0x0082 : "是否同意收對方為徒?",

# ItemsBag.py（0x00a1∼0x00c0）
0x00a1 : "您的騎寵技能已滿，是否隨機替換其中一個技能？",
0x00a2 : "裝備後將綁定，是否裝備？",
0x00a3 : "強製解鎖背包需要%s，解鎖後密碼將被清空，你確定要申請嗎？",

# Const.py（0x00c1∼0x00e0）
0x00c1 : "你確定要將正在出戰的寵物進行還童操作麼？",
0x00c2 : "使用忘憂丹會讓你的寵物遺忘所有技能，真的要這樣做麼？",
0x00c3 : "是否確定使用潛能天書？",
0x00c4 : "確定要將正在出戰的寵物進行還童操作麼？@B還童後寵物和其天賦技能都將變為1級，主動技能也會有損失！",
0x00c5 : "您確認要使用北冥爐遺忘所有技能麼？",
0x00c6 : "是否使用天工槌修理所有裝備？",
0x00c7 : "您已經沒有可用的歸命符籙，是否從商城購買？",
0x00c8 : "是否使用司辰沙漏？",
0x00c9 : "要延長司辰沙漏的時間麼？",
0x00ca : "您已經沒有可用的天工槌，是否從商店購買？",

# LivingSystem.py（0x00e1∼0x0100）
0x00e1 : "是否確認遺忘%s技能（等級%i）？",
0x00e2 : "是否花費%s將%s技能升級到等級%i？",

# love3.py（0x0101∼0x0120）
0x0101 : "遊戲資源數據損壞，請重新安裝遊戲客戶端。(1)",
0x0102 : "遊戲資源數據損壞，請重新安裝遊戲客戶端。(2)",
0x0103 : "版本不匹配，請升級到最新版本。",

# Role.py（0x0121∼0x0140）
0x0121 : "真的要花費%s捐獻麼？",
0x0122 : "是否花費1金幣來保存獎勵時間？",
0x0123 : "凍結的勁舞時間無法保持到下一天，請問您是否確認凍結。",
0x0124 : "你所登錄的場景已經滿員了，請稍後登陸。",
0x0125 : "%s邀請您進行切磋。",
0x0126 : "遊戲資源數據損壞，請重新安裝遊戲客戶端",
0x0127 : "是否使用鳳凰引原地復活？",

# RoleRelation.py（0x0141∼0x0160）
0x0141 : "[%s]希望加你為好友一起遊戲，您是否同意？",
0x0142 : "如果刪除了友好關係好友度也會清除，真的要和[%s]決裂麼？",
0x0143 : "是否刪除黑名單[%s]？",
0x0144 : "%s 邀請你成為戀人，你是否接受？",
0x0145 : "%s 邀請你成為夫妻，你是否接受？",
0x0146 : "是否同意離婚",
0x0147 : "單方面的強製離婚可馬上生效，但需要付出50金的離婚手續費，你確定要離嗎？",
0x0148 : "是否解除與%s的師徒關係?",
0x0149 : "%s希望能拜你為師，接受你的教導，你是否接受？",
0x014a : "結拜需要大家組隊，並且由隊長交納%i金和結拜儀式必要的黃紙、桃花酒。是否要結拜？",
0x014b : "更改結拜稱號需要結拜的所有兄弟一起組隊，並且交納%i金手續費，真的要更改結拜稱號麼？",
0x014d : "結拜增加新成員需要原有所有人和新人組隊，並且由隊長交納%i金和結拜儀式必要的黃紙、桃花酒。是否要結拜？",
0x014e : "結拜稱號改名",
0x014f : "名字長度不能超過 14 個字節",
0x0150 : "您輸入的用戶名無效，請重新輸入。",
0x0151 : "結拜稱號只能由漢字和字母組成！",
0x0152 : "名稱不合法！",
0x0153 : "輸入的名字有禁用詞匯!",
0x0154 : "多年情義就這樣完結，你真的想好了麼？真的要解除結拜關係麼？",
0x0155 : "您的徒弟%s希望您到他的身邊，是否接受召喚？",
0x0156 : "%s希望能收你為徒，你是否接受？",

# StatusMgr.py（0x0161∼0x0180）
0x0161 : "服務器斷開，請重新登錄！",
0x0162 : "提示",
0x0163 : "伺服器已斷線，請重新登入",

# Team.py（0x0181∼0x01a0）
0x0181 : "您的隊員%s欲邀請%s加入隊伍，您是否同意？",
0x0182 : "你已不在該副本的隊伍中，將在%s秒後離開此副本。點擊確定可以立刻離開。",
0x0183 : "是否要跟隨隊長行動?",

# FamilyFacade.py（0x01a1∼0x01c0）
0x01a1 : "%s邀請你加入%s家族, 是否接受?",
0x01a2 : "族長使用了集結令.你願意跟隨族長嗎?",

# TongFacade.py（0x01c1∼0x01e0）
0x01c1 : "【%s】邀請您加入其幫會【%s】一同開天辟地，降妖除魔。您是否願意？",
0x01c2 : "%s幫會邀請你的幫會結為同盟, 是否接受?",
0x01c3 : "幫主使用了集結令.你願意跟隨幫主嗎?",

# AntiRabotWindow.py（0x01e1∼0x0200）
0x01e1 : "請先點擊選出不相同的形狀！",

# BigMap.py（0x0201∼0x0220）
0x0201 : "該地圖暫時沒開放！",
0x0202 : "你當前所在的區域不允許查看地圖",

# bigmap\NPCLister.py（0x0221∼0x0240）
0x0221 : "請輸入要搜索的 NPC 名字！",
0x0222 : "NPC：%s 不存在！",
0x0223 : "請選擇一個 NPC！",

# chatwindow\ChatLogViewer.py（0x0241∼0x0260）
0x0241 : "聊天記錄已成功保存到%s文件中。",
0x0242 : "保存文件失敗！%s",
0x0243 : "文件%s已存在，是否覆蓋？",
0x0244 : "名字已經存在！",

# chatwindow\rolebroadcaster\Sender.py（0x0261∼0x0270）
0x0261 : "請輸入廣播信息",

# chatwindow\playmatechat\PLMChatWindow.py（0x0271∼0x0280）
0x0271 : "%s不是您的好友，不能進行好友聊天！",

# commissionsale\ModelPanel.py（0x0281∼0x02a0）
0x0281 : "創建模型失敗！",

# commissionviewer\GoodsPanel.py（0x02a1∼0x02c0）
0x02a1 : "等級上限不能低於等級下限，請重新輸入！",
0x02a2 : "您的金錢不足以購買該物品！",

# commissionviewer\PetPanel.py（0x02c1∼0x02e0）
0x02c1 : "等級上限不能低於等級下限，請重新輸入！",
0x02c2 : "您的金錢不足以購買該寵物！",

# commissionsale\pointcardwindow\PCSellWindow.py（0x02e1∼0x0300）
0x02e1 : "密碼不能為空！",
0x02e2 : "點卡未定價！",
0x02e3 : "您輸入的卡號不正確，請核實後再輸入！",

# tishouwindow\sellwindow\GoodsPanel.py（0x0301∼0x0320）
0x0301 : "請先暫停寄售再進行該操作！",
0x0302 : "價格超出了上限！",
0x0303 : "該物品不允許出售!",
0x0304 : "該物品還沒有定價!",
0x0305 : "寄售界面已裝滿!",

# tishouwindow\sellwindow\PetsPanel.py（0x0321∼0x0340）
0x0321 : "您的寵物攜帶數量已滿。",
0x0322 : "價格超出了上限！",
0x0323 : "未找到寄售NPC！",
0x0324 : "請先暫停寄售再進行該操作！",
0x0325 : "該寵物還沒有定價!",

# TiShouSellWindow.py（0x0341∼0x0360）
0x0341 : "未找到替售NPC！",
0x0342 : "您還沒有開始寄售物品，是否開始寄售？",

# StuffsPanel.py（0x0361∼0x0380）
0x0361 : "確定移除材料%s?",

# StatWindow.py（0x0381∼0x03a0）
0x0381 : "是否確定離開戰鬥？",

# GameQuiz.py（0x03a1∼0x03c0）
0x03a1 : "是否確定退出知識問答？",
0x03a2 : "想獲得大量經驗和潛能嗎？知識答題簡單又有趣，快點擊確定參與吧。",
0x03a3 : "是否需要傳送回覆活點進行答題？",
0x03a4 : "知識答題活動正在進行，您是否參加活動？",
0x03a5 : "知識答題活動正在進行，是否需要傳送回覆活點進行答題？",

# KitBag.py（0x03c1∼0x03e0）
0x03c1 : "包裹密碼已經成功設定，請牢記您的密碼",
0x03c2 : "包裹已經成功永久解鎖",
0x03c3 : "包裹密碼已經成功修改，請牢記您的密碼",
0x03c4 : "您輸入的密碼不正確，請重新輸入",
0x03c5 : "背包上鎖成功。",
0x03c6 : "背包解鎖成功。",
0x03c7 : "您已經輸入密碼錯誤三次，請稍候再試",
0x03c8 : "成功進行永久開鎖，之前的密碼已被清空。",
0x03c9 : "給包裹上鎖會導致交易取消,確定嗎?",
0x03ca : "您輸入的舊密碼不正確，請重新輸入",

# kitbag\ObjectItem.py（0x03e1∼0x0400）
0x03e1 : "您是否要使用金絲木為你的倉庫開啟下一頁空間?",
0x03e2 : "確定銷毀%s?",
0x03e3 : "你要花費%s購買%s個%s麼?",
0x03e4 : "確定花費%d天幣購買%d個%s?",

# kitbag\KitbagItem.py（0x0401∼0x0420）
0x0401 : "擺攤時不能使用神機匣功能。",
# kitbag\AritRefine.py
0x0411: "只有50級以上的綠色武器才能煉製神器。",

# knowledgeQandA\QandAWindow.py（0x0421∼0x0440）
0x0421 : "您還未答題，是否確定退出？",
0x0422 : "答錯了，不要氣餒哦，您可以再次回答。",
0x0423 : "退出回答，您需要重新對話開始。",

# MailBox.py（0x0441∼0x0460）
0x0441 : "郵件%s含有物品或金錢，確定刪除?",

# MiniMap.py（0x0461∼0x0480）
0x0461 : "您低於30級，無法查看商城。",

# Exp2PotWindow.py（0x0481∼0x04a0）
0x0481 : "確定要將%d點經驗兌換成%d點潛能嗎?",

# UnchainPrentice.py（0x04a1∼0x04c0）
0x04a1 : "你是否要解除徒弟%s",

# PetCombine.py（0x04c1∼0x04e0）
0x04c1 : "必須選擇一個材料寵物！",

# PetModelRender.py（0x04e1∼0x0500）
0x04e1 : "創建模型失敗！",

# PetPanel.py（0x0501∼0x0520）
0x0501 : "確定把寵物%s放生?",

# VehicleRender.py（0x0521∼0x0540）
0x0521 : "創建模型失敗！",
0x0522 : "騎寵模型\'%i\'不存在！",

# PetTrade.py（0x0541∼0x0560）
0x0541 : "%s請求與你寵物交易",
0x0542 : "取消交易",

# TalismanModelRender.py（0x0561∼0x0580）
0x0561 : "創建模型失敗！",
0x0562 : "法寶模型不存在！",

# QuestList.py（0x0581∼0x05a0）
0x0581 : "是否放棄任務%s?",
0x0582 : "族長邀請你參與運鏢任務，你是否接受？",
0x0583 : "是否繼續已保存的環任務？",

# relationship\family\AfficheEdit.py（0x05a1∼0x05e0）
0x05a1 : "家族公告必須在1000字節內",
0x05a2 : "輸入的內容有禁用詞匯!",

# relationship\family\FamilyPanel.py（0x05e1∼0x0600）
0x05e1 : "確定將%s請出家族？",

# relationship\family\MenuItem.py（0x0601∼0x0620）
0x0601 : "確定提升%s為家族族長?",
0x0602 : "確定解散家族：%s?",
0x0603 : "確定退出家族：%s?",

# relationship\family\ChangeNameBox.py（0x0621∼0x0640）
0x0621 : "名字長度不能超過 14 個字節",
0x0622 : "您輸入的用戶名無效，請重新輸入。",
0x0623 : "家族名稱只能由漢字和字母組成！",
0x0624 : "名稱不合法！",
0x0625 : "輸入的名字有禁用詞匯!",

# relationship\family\FoundFamily.py（0x0641∼0x0660）
0x0641 : "對不起，你已經有一個家族了。",
0x0642 : "名字長度不能超過 14 個字節",
0x0643 : "您輸入的用戶名無效，請重新輸入。",
0x0644 : "家族名稱只能由漢字和字母組成！",
0x0645 : "名稱不合法！",
0x0646 : "輸入的名字有禁用詞匯!",
0x0647 : "對不起，創建家族至少需要10金幣,您的金錢不足。",
0x0648 : "對不起，創建家族需要至少30級。",

# relationship\relationship\RelationPanel.py（0x0661∼0x0680）
0x0661 : "是否確定將玩家%s添加進好友名單?",
0x0662 : "是否確定將玩家%s加為戀人?",
0x0663 : "是否確定將玩家%s添加進仇人列表?",
0x0664 : "是否確定將玩家%s添加進黑名單?",
0x0665 : "是否確認刪除戀人:%s?",
0x0666 : "是否確認刪除仇人:%s?",

# relationship\RelationWindow.py（0x0681∼0x06a0）
0x0681 : "您還沒有家族",
0x0682 : "你還沒有幫會",

# relationship\tong\AffichePanel.py（0x06a1∼0x06c0）
0x06a1 : "幫會公告必須在200字節內",
0x06a2 : "輸入的內容有禁用詞匯!",

# relationship\tong\ManagerPanel.py（0x06c1∼0x06e0）
0x06c1 : "確定將%s請出幫會？",
0x06c2 : "幫會沒有該成員！",
0x06c3 : "不能添加自己幫會為同盟！",
0x06c4 : "已存在該同盟幫會！",
0x06c5 : "沒有該同盟幫會！",
0x06c6 : "確定與%s幫會解除同盟關係？",

# relationship\tong\MenuItem.py（0x06e1∼0x0700）
0x06e1 : "必須先將幫主職位轉讓給幫會裡的其他族長，才可以退出幫會。",
0x06e2 : "確定退出幫會：%s?",
0x06e3 : "確定將幫主之位讓給%s?",

# relationship\tong\ChangeNameBox.py（0x0701∼0x0720）
0x0701 : "名字長度不能超過 14 個字節",
0x0702 : "您輸入的幫會名無效，請重新輸入。",
0x0703 : "名稱不合法！",
0x0704 : "幫會名稱只能由漢字和字母組成！",
0x0705 : "輸入的名稱有禁用詞匯!",

# relationship\tong\DutyPanel.py（0x0721∼0x0740）
0x0721 : "備注不能超過7個字符!",
0x0722 : "輸入的備注有禁用詞匯!",

# relationship\tong\DutySetting.py（0x0741∼0x0760）
0x0741 : "名稱長度不能超過 10 個字節",
0x0742 : "您輸入的用戶名無效，請重新輸入。",
0x0743 : "名稱不合法！",
0x0744 : "輸入的名字有禁用詞匯!",
0x0745 : "已存在相同的職務名稱!",

# relationship\tong\FoundTong.py（0x0761∼0x0780）
0x0761 : "對不起，你已經有一個幫會了。",
0x0762 : "名字長度不能超過 14 個字節",
0x0763 : "您輸入的用戶名無效，請重新輸入。",
0x0764 : "名稱不合法！",
0x0765 : "幫會名稱只能由漢字和字母組成！",
0x0766 : "輸入的名稱有禁用詞匯!",
0x0767 : "對不起，創建幫會至少需要30金幣,您的金錢不足。",
0x0768 : "對不起，創建幫會需要至少45級。",

# rolestrading\TradingWindow.py（0x0781∼0x07a0）
0x0781 : "取消交易",
0x0782 : "%s請求與你交易",

# specialshop\FittingModelRender.py（0x07a1∼0x07c0）
0x07a1 : "創建模型失敗！",
0x07a2 : "騎寵模型\'%i\'不存在！",

# specialshop\SpecialItem.py（0x07c1∼0x07e0）
0x07c1 : "確定花費%d天幣購買%d個%s?",

# specialshop\SpecialShop.py（0x07e1∼0x0800）
0x07e1 : "遊戲商城正在更新，商城界面需關閉。",
0x07e2 : "確定花費%d天幣購買%s?",
0x07e3 : "你確定要撤銷該求購訂單嗎？",
0x07e4 : "本次掛單將收取%s作為保管費不退還，確定以單價%s/100@I{p=guis/general/specialshop/yuanbao.gui}出售%d@I{p=guis/general/specialshop/yuanbao.gui}?",
0x07e5 : "本次掛單將收取%s作為保管費不退還，確定以單價%s/100@I{p=guis/general/specialshop/yuanbao.gui}求購%d@I{p=guis/general/specialshop/yuanbao.gui}?",
0x07e6 : "寄售單價不能超過250@I{p=guis/controls/goldicon.gui}。",
0x07e7 : "單筆寄售數量不能超過1000x100@I{p=guis/general/specialshop/yuanbao.gui}。",
0x07e8 : "您身上的金天幣不足。",
0x07e9 : "單筆求購數量不能超過1000x100@I{p=guis/general/specialshop/yuanbao.gui}。",
0x07ea : "求購單價不能低於20@I{p=guis/controls/goldicon.gui}。",
0x07eb : "本次操作將取出您的交易系統賬戶內所有的遊戲幣，是否確認取出？",
0x07ec : "本次操作將取出您的交易系統賬戶內所有的金天幣，是否確認取出？",
0x07ed : "你確定要撤銷該寄售訂單嗎？",
0x07ee : "該訂單最大出售天幣數量為%d，購買天幣數超過該數量。",
0x07ef : "該訂單最大購買天幣數量為%d，出售天幣數超過該數量。",

# storewindow\ItemsPanel.py（0x0801∼0x0820）
0x0801 : "您輸入的名稱無效，請重新輸入。",
0x0802 : "名稱不合法！",
0x0803 : "輸入的名稱有禁用詞匯！",
0x0804 : "您輸入的名稱超過8字節，請重新輸入。",

# storewindow\StoreItem.py（0x0821∼0x0840）
0x0821 : "確定丟棄%s？",

# storewindow\StoreWindow.py（0x0841∼0x0880）
0x0841 : "您是否要將錢莊中剩餘的存款%d金%d銀%d銅全部取出？",
0x0842 : "您需要%d個金絲木才可以獲得這一空間,確定麼?",
0x0843 : "是否確定將%d天幣兌換為天幣票?",
0x0844 : "錢莊密碼已經成功設定，請牢記您的密碼",
0x0845 : "錢莊密碼已經成功修改，請牢記您的密碼",
0x0846 : "您輸入的密碼不正確，請重新輸入",
0x0847 : "您輸入的舊密碼不正確，請重新輸入",
0x0848 : "錢莊上鎖成功。",
0x0849 : "錢莊解鎖成功。",
0x084a : "您已經輸入密碼錯誤三次，請稍候再試",
0x084b : "成功進行永久開鎖，之前的密碼已被清空。",
0x084c : "一次可兌換的天幣票最大數量為%d。",
0x084d : "一次可兌換的天幣票最小數量為%d。",
0x084e : "要兌換天幣數超過攜帶天幣數！",

# syssetting\AVPanel.py（0x0881∼0x08a0）
0x0881 : "部分圖形設置需要重新啟動，將於下次客戶端運行時生效。",

# syssetting\KeySetter.py（0x08a1∼0x08c0）
0x08a1 : "當前已經設置為該按鍵，重復設置將會清除該設置，是否繼續？",
0x08a2 : "按鍵重復，導致“%s”變為未設置。",

# tongabout\BiddingBox.py（0x08c1∼0x08e0）
0x08c1 : "請輸入數字",
0x08c2 : "幫會可用資金不足。",
0x08c3 : "最低競拍價格要為10金的整數倍，您的競價不滿足要求。",
0x08c4 : "最低追加競拍價要為10金的整數倍，您的追加價不滿足要求。",

# tongabout\ModelRender.py（0x08e1∼0x0900）
0x08e1 : "創建模型失敗！",

# tongabout\SkillReSearch.py（0x0901∼0x0920）
0x0901 : "你確定研發技能%s?",
0x0902 : "你確定研發%s, 同時放棄正在研發的%s?",

# tongabout\WarIntergral.py（0x0921∼0x0940）
0x0921 : "是否確定離開幫會戰場？",

# tongabout\tongstorage\StorageItem.py（0x0941∼0x0960）
0x0941 : "確定丟棄%s？",

# tongabout\ApplyRobWar.py（0x0961∼0x0980）
0x0961 : "名字長度不能超過 14 個字節",
0x0962 : "您輸入的幫會名無效，請重新輸入。",
0x0963 : "名稱不合法！",
0x0964 : "幫會名稱只可能由漢字和字母組成！",
0x0965 : "輸入的名稱有禁用詞匯!",

# tongabout\BuildReSearch.py（0x0981∼0x09a0）
0x0981 : "該建築正在升級過程中！",
0x0982 : "你確定升級建築%s？",
0x0983 : "你確定升級建築%s，同時取消%s的升級嗎？",

# tongabout\ShenShouBeckon.py（0x09a1∼0x09c0）
0x09a1 : "該神獸已經存在!",
0x09a2 : "你沒有選擇神獸的權限!",
0x09a3 : "幫會資金不足,選擇或者更換神獸需要%d金幫會資金。",
0x09a4 : "幫會行動力不足,選擇或者更換神獸需要%d點幫會行動力。",

# tongabout\TaxRateSetBox.py（0x09c1∼0x09e0）
0x09c1 : "稅率只能為1%-50%，請輸入一個1-50的整數，請重新輸入。",

# tongabout\TongQuery.py（0x09e1∼0x0a00）
0x09e1 : "對不起，您還沒有幫會。",
0x09e2 : "幫會宣傳內容不合法！",
0x09e3 : "幫會宣傳含有禁用詞匯!",

# tradewindow\BuyPanel.py（0x0a01∼0x0a20）
0x0a01 : "%s，是否確定需要修理?",

# tradewindow\TradeWindow.py（0x0a21∼0x0a40）
0x0a21 : "釣魚中...",

# tradewindow\Repairer.py（0x0a41∼0x0a60）
0x0a41 : "該裝備不需要修理",
0x0a42 : "請選擇需要修理的裝備",
0x0a43 : "%s，是否確定需要修理?",

# vendwindow\buywindow\ItemsPanel.py（0x0a61∼0x0a80）
0x0a61 : "你要花費%s購買%s個%s麼?",

# vendwindow\buywindow\PurchasePanel.py（0x0a81∼0x0aa0）
0x0a81 : "成功出售XXX",
0x0a82 : "確定出售%s個%s？",
0x0a91 : "您沒有足夠的物品出售！",

# vendwindow\sellwindow\GoodsPanel.py（0x0aa1∼0x0ac0）
0x0aa1 : "請先停止擺攤再進行該操作！",
0x0aa2 : "該物品不允許出售!",
0x0aa3 : "該物品還沒有定價!",
0x0aa4 : "物品界面已裝滿!",
0x0aa5 : "價格超出了上限！",

# vendwindow\sellwindow\PurchasePanel.py（0x0ac1∼0x0ae0）
0x0ac1 : "該物品不支持收購!",
0x0ac2 : "請先停止擺攤再進行該操作！",
0x0ac3 : "您沒有足夠的金錢收購物品。",
0x0ac4 : "請先選擇一個收購物品!",
0x0ac5 : "收購界面已裝滿!",
0x0ac6 : "該物品還沒有定價!",
0x0ac7 : "界面空位不足!",

# tishouwindow\buywindow\ItemsPanel.py（0x0ae1∼0x0b00）
0x0ae1 : "店家還沒開始擺攤",
0x0ae2 : "你要花費%s購買%s個%s麼?",

# tishouwindow\sellwindow\PurchasePanel.py（0x0b01∼0x0b20）
0x0b01 : "未找到寄售NPC！",
0x0b02 : "請先停止寄售再進行該操作！",
0x0b03 : "收購界面已裝滿!",
0x0b04 : "該物品還沒有定價!",
0x0b05 : "界面空位不足!",
0x0b06 : "物品未定價！",
0x0b07 : "你的背包處於上鎖狀態，請解鎖後再進行此操作。",

# loginuis\logindialog\LoginDialog.py（0x0b21∼0x0b40）
0x0b21 : "錯誤的密保卡號!",
0x0b22 : "你輸入密保號 %i 次，將重新申請矩陣組，請認準組號重新輸入！",

# loginuis\logindialog\LoginDialog.py（0x0b41∼0x0b60）
0x0b41 : "確定要放棄排隊嗎？",
0x0b42 : "已提交您的登入申請。目前你排在第%i位，等待時間少於一分鐘。",
0x0b43 : "已提交您的登入申請。目前你排在第%i位，大概需要等待%i分鐘。",
0x0b44 : "請輸入賬號和密碼!",
0x0b45 : "找不到 launcher",
0x0b46 : "此功能未開通",

# loginuis\roleselector\RoleSelector.py（0x0b61∼0x0b80）
0x0b61 : "角色成功改名為：%s",
0x0b62 : "存在角色數量已經達到上限！",
0x0b63 : "請選擇一個角色！",
0x0b64 : "輸入錯誤，刪除取消",
0x0b65 : "角色需要改名",

# passwordbox\PasswordOperate.py（0x0b81∼0x0ba0）
0x0b81 : "您還沒有設置密碼",
0x0b82 : "密碼必須為4-6位數字",
0x0b83 : "忘記密碼請到鳳鳴城錢莊的解鎖師那裡，可以強製解除密碼。",

# passwordbox\PasswordSetting.py（0x0ba1∼0x0bc0）
0x0ba1 : "密碼必須為4-6位數字",
0x0ba2 : "兩次輸入密碼不一致，請重新輸入新密碼",

# T_SoundSetter.py（0x0bc1∼0x0be0）
0x0bc1 : "路徑“res/entities/common/tempconfigs”不存在，保存失敗",
0x0bc2 : "保存以下事件聲音失敗：%s原因可能是該控件不支持設置事件聲音，請與程序聯繫！",
0x0bc3 : "保存成功！",
0x0bc4 : "聲音 \'%s\' 不存在!",

# T_UIColorTester.py（0x0be1∼0x0c00）
0x0be1 : "不是可測試的文本標簽（滑鼠必須擊中一段文本）",

# T_UIModelAdjuster.py（0x0c01∼0x0c20）
0x0c01 : "有的模型更改了還沒保存，你要保存嗎？",
0x0c02 : "保存成功!",
0x0c03 : "保存失敗，路徑“%s”不存在",
0x0c04 : "@A{C}我是大懶人，網站還沒建設好，@B哈哈@I{p=maps/emote/emote_13.gui}",
0x0c05 : "沒有可調整的模型",
0x0c06 : "模型觀察器不包含“__config”屬性，不能調整",

# Account.py（0x0c21∼0x0c40）
0x0c21 : "創建角色成功",
0x0c22 : "提示",

# TongInterface.py（0x0c41∼0x0c60）
0x0c41 : "[%s]希望加入貴幫，是否同意？",
0x0c42 : "你確定要取消當前會標？",

# helper\Searcher.py（0x0c61∼0x0c80）
0x0c61 : "請輸入關鍵字！",
0x0c62 : "找不到相關主題！",

# npctalk\QuestTalkWindow.py（0x0c81∼0x0ca0）
0x0c81 : "請選擇一個獎勵的物品",

# petswindow\aboutnpc\StorageTenancy.py（0x0ca1∼0x0cc0）
0x0ca1 : "金天幣不足",

# petswindow\petpanel\ChangeNamePanel.py（0x0cc1∼0x0ce0）
0x0cc1 : "名字長度不能超過 14 個字節",
0x0cc2 : "您輸入的用戶名無效，請重新輸入。",
0x0cc3 : "名稱不合法！",
0x0cc4 : "輸入的名字有禁用詞匯!",

# petswindow\petpanel\PetPanel.py（0x0ce1∼0x0d00）
0x0ce1 : "寵物處於戰鬥中不能放生！",
0x0ce2 : "寵物正在出售，不能放生！",

# petswindow\vehiclepanel\VehiclePanel.py（0x0d01∼0x0d20）
0x0d01 : "輸入錯誤，不能放生",

# playerprowindow\PlayProWindow.py（0x0d21∼0x0d40）
0x0d21 : "您未裝備法寶",
0x0d22 : "您的經驗代練界面尚未激活",

# targetinfo\TargetInfo.py（0x0d41∼0x0d60）
0x0d41 : "%s 邀請你共舞，你是否接受？",
0x0d42 : "武道大會第%s輪比賽開始,請盡快進入比賽場地！",
0x0d43 : "想要祈福需要花費%d金，真的要祈福麼？",

# teammateinfo\TeammateArray.py（0x0d61∼0x0d80）
0x0d61 : "%s 邀請你加入他的隊伍，你是否接受？",
0x0d62 : "%s 請求加入你的隊伍，你是否同意？",
0x0d63 : "%s 邀請你跟隨他，你是否接受？",

# chatwindow\YellVerifyBox.py（0x0d81∼0x0da0）
0x0d81 : "在世界頻道發言需要耗 %i 銀幣，確定要發言嗎！",

# tongabout\ItemReSearch.py（0x0da1∼0x0dc0）
0x0da1 : "你確定生產%d個%s, 同時放棄正在生產的%s？",
0x0da2 : "你確定生產%d個%s？",

# tooluis\fixrewardbox\FixRewardBox.py（0x0dc1∼0x0de0）
0x0dc1 : "歡迎來到天上人間，聽說新手導師慕雪有事找你呢，正前方頭頂問號的就是她啦，快去看看吧。",
0x0dc2 : "恭喜您獲得第%s份大禮:%s。%s後將獲得第%s份禮物，請千萬不要錯過哦。",
0x0dc3 : "明天0：00前，您還可以領取%d份禮物。",

# vendwindow\sellwindow\PetsPanel.py（0x0de1∼0x0e00）
0x0de1 : "該寵物已是待售寵物！",
0x0de2 : "該寵物還沒有定價!",

# vendwindow\sellwindow\SellPanel.py（0x0e01∼0x0e20）
0x0e01 : "商品(%s)標價超過上限!",
0x0e02 : "寵物標價超過上限!",
0x0e03 : "你有商品尚未標價!",
0x0e04 : "沒有出售或收購的商品!",
0x0e05 : "您沒有足夠的金錢收購物品!",
0x0e06 : "名字長度不能超過 20個字節！",
0x0e07 : "您輸入的名稱無效！",
0x0e08 : "名稱不合法！",
0x0e09 : "輸入的名稱有禁用詞匯!",

# loginuis\rolecreator\RoleCreator.py（0x0e21∼0x0e40）
0x0e21 : "請輸入角色名字",

# tools\__init__.py（0x0e41∼0x0e50）
0x0e41 : "找不到合適的控件",
0x0e42 : "請首先關閉 %s",

# damagestatic\StatisWindow.py（0x0e51∼0x0e60）
0x0e51 : "您希望重置傷害統計數據麼？",

# general\tanabata\(0x0e61∼0x0e80)
0x0e61 : "請先選擇一項",
0x0e62 : "請選擇一個好友。",
0x0e63 : "請輸入留言內容。",
0x0e64 : "每條留言不得少於10個字符。",
0x0e65 : "要發送消息不合法。",
0x0e66 : "要發送消息含有禁用詞匯。",
0x0e67 : "您的投票發送成功。",
# Bank.py( 0x0e81∼0x0e90 )
0x0e81 : "強製解鎖倉庫需要%s，解鎖後密碼將被清空，你確定要申請嗎？",

#general\equipextract\( 0x0ea1∼0x0ec0 )
0x0ea1 : "請放入一件裝備。",
0x0ea2 : "請至少放入一顆封靈石或超級封靈石。",
0x0ea3 : "灌注的屬性不能被抽取，是否繼續？",
0x0ea4 : "您的封靈石數量不足，不能把所有屬性都抽取，只能隨機抽取其中的屬性，是否繼續？",
0x0ea5 : "使用已綁定的裝備抽取屬性，所有封靈石都將變為綁定的，是否繼續？",
0x0ea6 : "請放入封靈石或超級封靈石。",
0x0ea7 : "封靈石不能混用。",
0x0ea8 : "請放入60級以上且品質在粉色以上的裝備。",
0x0ea9 : "只能放入神徵令。神徵令可將抽取成功率提高到100%，在副本掉落，也可在道具商城購買到。",
0x0eab : "請放入一個韻靈琥珀。",
0x0eac : "使用已綁定的韻靈琥珀灌注裝備，裝備將會變為綁定的，是否繼續？",
0x0ead : "請放入韻靈琥珀。",
0x0eae : "請放入一個飛升靈玉",
0x0eaf : "使用已綁定的飛升靈玉提升裝備品質，裝備將會變為綁定的，是否繼續？",
0x0eb0 : "您放入的飛升靈玉與裝備等級不符",
0x0eb1 : "您放入裝備的等級與飛升靈玉不符",
0x0eb2 : "請放入%i級以上的%s裝備。",

# PlayerInfo.py( 0x0ec1∼0x0ed0 )
0x0ec1 : "您確定新建裝備組合，並將現在穿著的裝備保存其中麼？",
0x0ec2 : "您輸入的名稱過長。",
0x0ec3 : "只能對已經保存過的組合重新命名。",

}