# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/11/22 15:13
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: product_b_info.py

BASE_PRODUCT_DESCRIPTION = """
【宠物责任险】
1、保险产品名称：
宠物责任险
产品分为三个版本：基础版、升级版、尊享版

2、保险险种名称：
一级分类名称：宠物保险
二级分类名称：宠物责任险
"""

A = """
3、投/被保险人：
在中华人民共和国境内（不包括港、澳、台地区）合法饲养宠物，且具有完全民事行为能力的自然人，可作为本保险合同的投保人和被保险人。
"""

B = """
4、被保险宠物：
本保险合同承保的宠物（以下简称“被保险宠物”）为被保险人以玩赏、陪伴为目的而合法饲养、可明确鉴别身份的犬类或猫类宠物，犬类或猫类年龄无限制。
流浪且未被收养的宠物不得作为本保险合同的被保险宠物。
"""

C = """
5、投保份数：
本产品仅限宠物主本人购买，同一时间段同一宠物犬或宠物猫限投一份，多投无效。同一投保人累计限购3份。
"""

D = """
6、保险期限：
本产品保险期限为一年，保单生效时间为投保并成功缴纳保费的第三日零时。
"""

E = """
7、保障责任：
    a.保险期限：本产品保险期限为一年，保单生效时间为投保并成功缴纳保费的第三日零时。
    b.保障详情：
    【基础版方案】
        1. 三者责任
        保障详情:
            在保险期间内，因本保险合同载明的被保险宠物自主的袭击、撕咬，直接造成第三者的人身伤亡，依照中华人民共和国法律（不包括港、澳、台地区法律）应由被保险人承担的经济赔偿责任，保险人按照本保险合同的约定在保险合同载明的赔偿限额内负责赔偿。
            保险事故发生后，被保险人因保险事故而被提起仲裁或者诉讼的，对应由被保险人支付的仲裁或诉讼费用以及事先经保险人书面同意支付的其他必要的、合理的费用（简称“法律费用”），保险人按照本保险合同的约定负责赔偿。
    【升级版方案】
        1. 三者责任，保障详情同基础版
        2. 增加宠物伤害宠物主或同住家属责任
        保障详情:
            本保险合同扩展承保被保险人及同住家属（配偶、父母、子女）遭受宠物猫或宠物犬袭击、撕咬导致身故、伤残及医疗费用支出，保险人按下列约定给付保险金。
            （一）身故保险责任
            在保险期间内，被保险人或其同住家属因遭受宠物猫或宠物犬袭击、撕咬，并自该事故发生之日起180日（含第180日）内因该事故导致身故的，保险人按照本保险合同载明的保险金额给付身故保险金。
            如果被保险人或其同住家属在给付身故保险金前已依本保险合同给付过伤残保险金，在给付身故保险金时，需扣除已给付的伤残保险金。
            （二）伤残保险责任
            在保险期间内，被保险人或其同住家属因遭受宠物猫或宠物犬袭击、撕咬，并自事故发生之日起180日内因该事故造成《人身保险伤残评定标准及代码》（以下简称“《伤残评定标准》”）所列伤残程度之一者，保险人按《伤残评定标准》所列伤残程度对应的保险金给付比例乘以本保险合同载明的保险金额给付伤残保险金。如第180日治疗仍未结束的，按第180日的身体情况进行伤残鉴定，并据此给付伤残保险金。
            被保险人或其同住家属如在本次伤害事故之前已有伤残，保险人按合并后的伤残程度在《伤残评定标准》中所对应的给付比例给付伤残保险金，但应扣除原有伤残程度在《伤残评定标准》中所对应的伤残保险金。
            当同一保险事故造成两处或两处以上伤残时，应首先对各处伤残程度分别进行评定，如果几处伤残等级不同，以最重的伤残等级作为最终的评定结论；如果两处或两处以上伤残等级相同，伤残等级在原评定基础上最多晋升一级，最高晋升至第一级。同一部位和性质的伤残，不应采用《伤残评定标准》条文两条以上或者同一条文两次以上进行评定。
            （三）医疗费用保险责任
            在保险期间内，被保险人或其同住家属因遭受宠物猫或宠物犬袭击、撕咬，并因该事故导致在医院接受治疗而实际发生的合理且必要的医疗费用，保险人在扣除本保险合同约定的免赔额后，按本保险合同约定的赔付比例给付医疗费用保险金。
            在保险期间内，保险人承担给付医疗费用保险金的责任以本保险合同约定的医疗费用保险金额为限，对一次或者累计给付医疗费用保险金之和达到该保险金额时，本保险合同的医疗费用保险责任终止。
            被保险人或其同住家属如果已从其他途径获得补偿，则保险人只承担合理医疗费用剩余部分的保险责任。
    【尊享版方案】
        1. 三者责任，保障详情同基础版。
        2. 宠物伤害宠物主或同住家属责任，保障详情同升级版。
        3. 扩展人畜共患病医疗费用责任
        保障详情:
            在保险期间内，在本保险合同约定的等待期届满后，被保险宠物罹患本保险合同约定的人畜共患传染病且宠物饲养人或其同住家属受到感染，针对宠物饲养人或其同住家属在二级及以上公立医院治疗该人畜共患传染病而产生的合理且必要的、超过当地社会基本医疗保险范围的医疗费用，保险人按照本保险合同的约定负责赔偿。
"""

F = """
8、缴费方式及金额：
本产品可支持趸交一次性付清和月缴分为12期交付两种方式：保费分期缴付周期为每月，未缴付首期保费，保险合同不成立。
"""

G = """
9、产品犹豫期：
本产品无犹豫期。
"""

H = """
10、产品合同解除（退保）规则：
（1）保单未生效：
保单未生效申请退保并递交齐全退保资料的，将全额退还已缴纳的保险费；
（2）保单已生效：
A、年缴保单：
在保单生效后申请退保的，将退还未满期净保险费，计算公式为：未满期净保险费=保险费x（1-保险单已经过天数/保险期间天数）。
B、月缴保单：
在保单生效后申请退保的，将退还未满期净保险费，计算公式为：退还未满期净保险费=本合同当期月度保险费*（1-当月实际经过天数/当月实际天数）。
对于月缴保单用户，缴费宽限期为15天，若超过缴费宽限期仍未能完成保费缴纳，保单及增值服务均自动失效，保单终止日期为上一缴费期最后一天。
"""

I = """
11、续保规则：
保险续保服务由用户选择投保的保险公司提供。续保功能目前仅支持部分险种，用户可以在明确标识可续保的保险产品页面或保单详情页面开通续保功能。
"""

J = """
12、增值服务：
无
"""

K = """
13、责任免除：
三者责任：
下列情形或因下列原因造成的损失、费用和责任，保险人不承担赔偿责任：
（一）被保险人不具有动物饲养所在地人民政府规定的动物饲养条件，或违反动物饲养所在地人民政府颁布的管理规定；
（二）投保人、被保险人或其家庭成员（见释义）、家庭雇佣人员、暂居人员（见释义）的人身伤亡；
（三）被保险宠物对第三者造成的人身伤亡是由于第三者的挑逗、戏耍等故意或重大过失行为或违法、犯罪行为引发宠物袭击、撕咬所导致的；
（四）投保人、被保险人或其家庭成员、家庭雇佣人员、暂居人员的故意行为造成的第三者的人身伤亡；
（五）被保险宠物本身的损失、治疗或相关处置费用；
（六）携带被保险宠物进入公共领域或公共场所时未配置或未合理使用安全装置（狗绳、宠物笼）造成的第三者的人身伤亡；
（七）被保险宠物造成其他动物或植物的损失；
（八）因保险事故引起的任何精神损害赔偿或间接损失；
（九）罚款、罚金或惩罚性赔偿；
（十）任何违反《中华人民共和国动物防疫法》的情形所造成的损失；
（十一）被保险宠物在被遗弃或逃逸期间造成的第三者的人身伤亡；
（十二）未经保险人同意，被保险人与第三者或第三者家属签订的赔偿协议约定的超出保险人应承担责任部分的赔偿金额；
（十三）宠物造成的大气、土地、水污染及其他各种污染所引起的赔偿责任；
（十四）任何财产损失。

宠物伤害宠物主或同住家属责任：
由于下列原因造成的损失，保险人不负给付或赔偿保险金的责任：
（一）投保前已有的伤病；
（二）投保人、被保险人或同住家属的故意行为；
（三）被保险人或同住家属故意挑逗、挑畔衅宠物导致其遭受宠物的袭击、撕咬；
（四）未遵医嘱，私自服用、涂用、注射药物；
（五）被保险人或同住家属因精神错乱或失常而导致的意外；
（六）宠物饲养人或同住家属猝死（见释义）。

下列费用，保险人不负给付或赔偿保险金的责任：
（一）营养费、辅助器具费、修复手术费、牙齿整形费、牙齿修复费、镶牙费、护理费、
交通费、伙食费、误工费、丧葬费、疗养费、康复治疗费、心理治疗费、美容费、矫形费、
视力矫正手术费、非意外事故所致的整容手术费，但本保险合同另有约定的不在此限；
（二）任何违反《中华人民共和国动物防疫法》的情形所造成的损失；
（三）因保险事故引起的任何精神损書赔偿或间接损失；
（四）保险单中约定的免赔额范围内的损失或责任；
（五）不必要的转院治疗引发的额外费用；
（六）在非附加本保险合同约定的医院进行治疗而发生的费用。

人畜共患病医疗费用责任：
因下列情形之一，造成被保险人支出医疗费用，保险人不承担保险金给付责任：
（一）被保险人或其同住家属在等待期内罹患人畜共患传染病并因此产生的医疗费用；
（二）被保险宠物的任何医疗费用；
（三）在保险期间开始前被确定为人畜共患传染病例并因此产生的医疗费用；
（四）在不符合本附加保险合同约定的医院就诊发生的医疗费用；
（五）康复治疗或训练、休养或疗养、健康体检、非处方药物、保健食品及用品、各种康复治疗器械、假体、义肢、自用的按摩保健和治疗用品、所有非处方医疗器械；
（六）接受矫形、视力矫正手术、美容、变性手术、以美容为目的的整形手术、牙科治疗、牙科保健，及所有前述的手术导致的并发症或医疗事故；
（七）交通费、伙食费、误工费、取暖费等费用。

下列原因造成的损失、费用和责任，保险人不负责赔偿：
（一）授保人、被保险人及其代表的故意、重大过失或犯罪行为；
（二）战争、敌对行为、军事行为、武装冲实、罢工、骚乱、暴动、恐怖活动；
（三）核辐射、核爆炸、核污染及其他放射性污染；
（四）大气污染、土地污染、水污染及其他各种污染：
（五）行政行为或司法行为。
下列损失、费用和责任，保险人不负责赔偿：
（一）罚款、罚金及惩罚性赔偿；
（二）精神损害赔偿；
（三）保险单载明的免赔额或按照保险单载明的免赔率计算的免赔额；
（四）超过保险单载明的各项责任限额之外的超额损失。
"""

L = """
13、责任免除：
三者责任：
下列情形或因下列原因造成的损失、费用和责任，保险人不承担赔偿责任：
（一）被保险人不具有动物饲养所在地人民政府规定的动物饲养条件，或违反动物饲养所在地人民政府颁布的管理规定；
（二）投保人、被保险人或其家庭成员（见释义）、家庭雇佣人员、暂居人员（见释义）的人身伤亡；
（三）被保险宠物对第三者造成的人身伤亡是由于第三者的挑逗、戏耍等故意或重大过失行为或违法、犯罪行为引发宠物袭击、撕咬所导致的；
（四）投保人、被保险人或其家庭成员、家庭雇佣人员、暂居人员的故意行为造成的第三者的人身伤亡；
（五）被保险宠物本身的损失、治疗或相关处置费用；
（六）携带被保险宠物进入公共领域或公共场所时未配置或未合理使用安全装置（狗绳、宠物笼）造成的第三者的人身伤亡；
（七）被保险宠物造成其他动物或植物的损失；
（八）因保险事故引起的任何精神损害赔偿或间接损失；
（九）罚款、罚金或惩罚性赔偿；
（十）任何违反《中华人民共和国动物防疫法》的情形所造成的损失；
（十一）被保险宠物在被遗弃或逃逸期间造成的第三者的人身伤亡；
（十二）未经保险人同意，被保险人与第三者或第三者家属签订的赔偿协议约定的超出保险人应承担责任部分的赔偿金额；
（十三）宠物造成的大气、土地、水污染及其他各种污染所引起的赔偿责任；
（十四）任何财产损失。

宠物伤害宠物主或同住家属责任：
由于下列原因造成的损失，保险人不负给付或赔偿保险金的责任：
（一）投保前已有的伤病；
（二）投保人、被保险人或同住家属的故意行为；
（三）被保险人或同住家属故意挑逗、挑畔衅宠物导致其遭受宠物的袭击、撕咬；
（四）未遵医嘱，私自服用、涂用、注射药物；
（五）被保险人或同住家属因精神错乱或失常而导致的意外；
（六）宠物饲养人或同住家属猝死（见释义）。

下列费用，保险人不负给付或赔偿保险金的责任：
（一）营养费、辅助器具费、修复手术费、牙齿整形费、牙齿修复费、镶牙费、护理费、
交通费、伙食费、误工费、丧葬费、疗养费、康复治疗费、心理治疗费、美容费、矫形费、
视力矫正手术费、非意外事故所致的整容手术费，但本保险合同另有约定的不在此限；
（二）任何违反《中华人民共和国动物防疫法》的情形所造成的损失；
（三）因保险事故引起的任何精神损書赔偿或间接损失；
（四）保险单中约定的免赔额范围内的损失或责任；
（五）不必要的转院治疗引发的额外费用；
（六）在非附加本保险合同约定的医院进行治疗而发生的费用。

人畜共患病医疗费用责任：
因下列情形之一，造成被保险人支出医疗费用，保险人不承担保险金给付责任：
（一）被保险人或其同住家属在等待期内罹患人畜共患传染病并因此产生的医疗费用；
（二）被保险宠物的任何医疗费用；
（三）在保险期间开始前被确定为人畜共患传染病例并因此产生的医疗费用；
（四）在不符合本附加保险合同约定的医院就诊发生的医疗费用；
（五）康复治疗或训练、休养或疗养、健康体检、非处方药物、保健食品及用品、各种康复治疗器械、假体、义肢、自用的按摩保健和治疗用品、所有非处方医疗器械；
（六）接受矫形、视力矫正手术、美容、变性手术、以美容为目的的整形手术、牙科治疗、牙科保健，及所有前述的手术导致的并发症或医疗事故；
（七）交通费、伙食费、误工费、取暖费等费用。

下列原因造成的损失、费用和责任，保险人不负责赔偿：
（一）授保人、被保险人及其代表的故意、重大过失或犯罪行为；
（二）战争、敌对行为、军事行为、武装冲实、罢工、骚乱、暴动、恐怖活动；
（三）核辐射、核爆炸、核污染及其他放射性污染；
（四）大气污染、土地污染、水污染及其他各种污染：
（五）行政行为或司法行为。
下列损失、费用和责任，保险人不负责赔偿：
（一）罚款、罚金及惩罚性赔偿；
（二）精神损害赔偿；
（三）保险单载明的免赔额或按照保险单载明的免赔率计算的免赔额；
（四）超过保险单载明的各项责任限额之外的超额损失。
"""

M = """
7、保障责任：
等待期：本产品保单生效后无等待期。
【基础版方案】
	1. 三者责任
	保障详情:
	    在保险期间内，因本保险合同载明的被保险宠物自主的袭击、撕咬，直接造成第三者的人身伤亡，依照中华人民共和国法律（不包括港、澳、台地区法律）应由被保险人承担的经济赔偿责任，保险人按照本保险合同的约定在保险合同载明的赔偿限额内负责赔偿。
	    保险事故发生后，被保险人因保险事故而被提起仲裁或者诉讼的，对应由被保险人支付的仲裁或诉讼费用以及事先经保险人书面同意支付的其他必要的、合理的费用（简称“法律费用”），保险人按照本保险合同的约定负责赔偿。
【升级版方案】
	1. 三者责任，保障详情同基础版
	2. 扩展宠物伤害宠物主或同住家属责任
	保障详情:
        本保险合同扩展承保被保险人及同住家属（配偶、父母、子女）遭受宠物猫或宠物犬袭击、撕咬导致身故、伤残及医疗费用支出，保险人按下列约定给付保险金。
        （一）身故保险责任
        在保险期间内，被保险人或其同住家属因遭受宠物猫或宠物犬袭击、撕咬，并自该事故发生之日起180日（含第180日）内因该事故导致身故的，保险人按照本保险合同载明的保险金额给付身故保险金。
        如果被保险人或其同住家属在给付身故保险金前已依本保险合同给付过伤残保险金，在给付身故保险金时，需扣除已给付的伤残保险金。
        （二）伤残保险责任
        在保险期间内，被保险人或其同住家属因遭受宠物猫或宠物犬袭击、撕咬，并自事故发生之日起180日内因该事故造成《人身保险伤残评定标准及代码》（以下简称“《伤残评定标准》”）所列伤残程度之一者，保险人按《伤残评定标准》所列伤残程度对应的保险金给付比例乘以本保险合同载明的保险金额给付伤残保险金。如第180日治疗仍未结束的，按第180日的身体情况进行伤残鉴定，并据此给付伤残保险金。
        被保险人或其同住家属如在本次伤害事故之前已有伤残，保险人按合并后的伤残程度在《伤残评定标准》中所对应的给付比例给付伤残保险金，但应扣除原有伤残程度在《伤残评定标准》中所对应的伤残保险金。
        当同一保险事故造成两处或两处以上伤残时，应首先对各处伤残程度分别进行评定，如果几处伤残等级不同，以最重的伤残等级作为最终的评定结论；如果两处或两处以上伤残等级相同，伤残等级在原评定基础上最多晋升一级，最高晋升至第一级。同一部位和性质的伤残，不应采用《伤残评定标准》条文两条以上或者同一条文两次以上进行评定。
        （三）医疗费用保险责任
        在保险期间内，被保险人或其同住家属因遭受宠物猫或宠物犬袭击、撕咬，并因该事故导致在医院接受治疗而实际发生的合理且必要的医疗费用，保险人在扣除本保险合同约定的免赔额后，按本保险合同约定的赔付比例给付医疗费用保险金。
        在保险期间内，保险人承担给付医疗费用保险金的责任以本保险合同约定的医疗费用保险金额为限，对一次或者累计给付医疗费用保险金之和达到该保险金额时，本保险合同的医疗费用保险责任终止。
        被保险人或其同住家属如果已从其他途径获得补偿，则保险人只承担合理医疗费用剩余部分的保险责任。
【尊享版方案】
	1. 三者责任，保障详情同基础版。
	2. 扩展宠物伤害宠物主或同住家属责任，保障详情同升级版。
	3. 扩展人畜共患病医疗费用责任
	保障详情:
        在保险期间内，在本保险合同约定的等待期届满后，被保险宠物罹患本保险合同约定的人畜共患传染病且宠物饲养人或其同住家属受到感染，针对宠物饲养人或其同住家属在二级及以上公立医院治疗该人畜共患传染病而产生的合理且必要的、超过当地社会基本医疗保险范围的医疗费用，保险人按照本保险合同的约定负责赔偿。
"""

PRODUCT_DESCRIPTION_MAP = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J, "K": K,
                           "L": L, "M": M}
