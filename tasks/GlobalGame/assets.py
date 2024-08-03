from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class GlobalGameAssets: 


	# Image Rule Assets
	# 接受 
	I_G_ACCEPT = RuleImage(roi_front=(830,407,56,46), roi_back=(798,369,117,110), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_g_accept.png")
	# 拒绝 
	I_G_REJECT = RuleImage(roi_front=(832,508,53,51), roi_back=(808,480,108,101), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_g_reject.png")
	# 勾玉 
	I_G_JADE = RuleImage(roi_front=(661,466,43,46), roi_back=(661,466,43,46), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_g_jade.png")
	# 猫粮 
	I_G_CAT_FOOD = RuleImage(roi_front=(565,463,59,65), roi_back=(565,463,59,65), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_g_cat_food.png")
	# 狗粮 
	I_G_DOG_FOOD = RuleImage(roi_front=(565,464,60,63), roi_back=(565,464,60,63), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_g_dog_food.png")
	# 忽略 
	I_G_IGNORE = RuleImage(roi_front=(773,116,21,21), roi_back=(759,102,48,48), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_g_ignore.png")
	# 网络异常 
	I_NETWORK_ABNORMAL = RuleImage(roi_front=(583,330,221,67), roi_back=(583,330,221,67), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_network_abnormal.png")
	# 已端口游戏服务器，需要重新连接，这种情况一般是断开很久了 
	I_NETWORK_ERROR = RuleImage(roi_front=(431,253,416,208), roi_back=(431,253,416,208), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_network_error.png")
	# 我还没有碰到这个情况没能截图 
	I_CLIENT_CLEAR = RuleImage(roi_front=(578,369,151,72), roi_back=(578,369,151,72), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_client_clear.png")
	# description 
	I_CHAT_CLOSE_BUTTON = RuleImage(roi_front=(632,343,49,103), roi_back=(632,343,49,103), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/gg/gg_chat_close_button.png")


	# Click Rule Assets
	# description 
	C_UI_REWARD = RuleClick(roi_front=(330,277,208,368), roi_back=(73,203,244,503), name="ui_reward")


	# Image Rule Assets
	# 长一点的确认 
	I_UI_CONFIRM = RuleImage(roi_front=(667,398,179,66), roi_back=(667,398,179,66), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_confirm.png")
	# 长一点的取消 
	I_UI_CANCEL = RuleImage(roi_front=(432,403,177,62), roi_back=(432,403,177,62), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_cancel.png")
	# '获得奖励' 四个大字 
	I_UI_REWARD = RuleImage(roi_front=(481,185,317,42), roi_back=(464,142,350,145), threshold=0.73, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_reward.png")
	# description 
	I_UI_BACK_RED = RuleImage(roi_front=(1041,111,34,38), roi_back=(834,15,427,200), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_back_red.png")
	# description 
	I_UI_BACK_YELLOW = RuleImage(roi_front=(26,17,47,46), roi_back=(0,0,100,100), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_back_yellow.png")
	# description 
	I_UI_BACK_BLUE = RuleImage(roi_front=(32,37,51,45), roi_back=(2,1,133,119), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_back_blue.png")
	# description 
	I_UI_AWARD = RuleImage(roi_front=(577,499,100,100), roi_back=(530,408,199,220), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_award.png")
	# 短一点的确认 
	I_UI_CONFIRM_SAMLL = RuleImage(roi_front=(677,390,130,62), roi_back=(677,390,130,62), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_confirm_samll.png")
	# 短一点的取消 
	I_UI_CANCEL_SAMLL = RuleImage(roi_front=(472,389,128,62), roi_back=(472,389,128,62), threshold=0.8, method="Template matching", file="./tasks/GlobalGame/ui/ui_ui_cancel_samll.png")


