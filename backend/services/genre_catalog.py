"""受控题材与子风格目录 — 所有题材相关配置的唯一数据源。

skill_executor.py 中的题材分支逻辑全部从这里读取，不再硬编码。
新增/修改题材只需编辑本文件，无需改动 Python 逻辑。
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# 核心目录
# ---------------------------------------------------------------------------

GENRE_CATALOG: List[Dict[str, Any]] = [
    # ======================== 玄幻 ========================
    {
        "id": "玄幻",
        "name": "玄幻",
        "bucket": "xuanhuan",
        "aliases": ["修仙", "仙侠", "奇幻", "玄幻流", "修仙文", "xuanhuan", "xianxia"],
        "default_substyle": "热血升级流",
        "substyles": [
            {
                "id": "热血升级流",
                "name": "热血升级流",
                "description": "主角主动出击，升级、夺宝、打脸与突破要连续兑现。",
                "keywords": ["热血", "升级", "逆袭", "越级", "突破", "打脸", "大比", "试炼", "夺宝", "斗法"],
                "focus": [
                    "尽快进入修炼、斗法、夺宝、试炼等玄幻行动场景",
                    "让主角主动反击，爽点落在实力和筹码增长",
                    "阶段收益要可量化，如境界、资源、贡献、法器、词条强化",
                ],
                "avoid": [
                    "长篇契文辩论或程序正确型爽点",
                    "阴冷潮湿的惊悚求生腔",
                    "整章都在低头忍耐、没有正面推进",
                ],
            },
            {
                "id": "凡人流",
                "name": "凡人流",
                "description": "底层开局，资源稀缺，靠判断、耐心与积累稳步逆袭。",
                "keywords": ["凡人", "底层", "资源稀缺", "稳扎稳打", "积累", "机缘", "算计", "谨慎"],
                "focus": [
                    "保留底层生存压力，但必须指向稳步变强",
                    "机缘、资源与信息差要成为真正筹码",
                    "谨慎不等于阴森，重点是冷静与成长回报",
                ],
                "avoid": [
                    "纯惊悚压抑氛围",
                    "只写忍耐而没有成长兑现",
                    "全靠契约条款或口头辩论解决冲突",
                ],
            },
            {
                "id": "苟道流",
                "name": "苟道流",
                "description": "主角审慎藏锋、预判风险、暗中发育，关键时刻一击制胜。",
                "keywords": ["苟", "藏拙", "稳健", "底牌", "布局", "预判", "避险", "后手"],
                "focus": [
                    "隐藏实力和预埋后手必须服务于最终反制",
                    "稳健发育要和资源积累、功法精进绑定",
                    "关键出手时要体现碾压感和准备充分",
                ],
                "avoid": [
                    "把谨慎写成畏缩无能",
                    "整章都是惊悚旁白或不敢行动",
                    "靠程序条款赢而不是靠布局和底牌赢",
                ],
            },
            {
                "id": "宗门成长流",
                "name": "宗门成长流",
                "description": "宗门层级、试炼大比、资源分配与门内晋升并行推进。",
                "keywords": ["宗门", "外门", "内门", "长老", "大比", "试炼", "贡献", "晋升", "洞府", "师承"],
                "focus": [
                    "宗门规矩要服务于资源争夺和实力晋升",
                    "多写大比、任务、试炼、传承、师门关系",
                    "主角要不断向更高层级跃迁",
                ],
                "avoid": [
                    "把宗门写成纯文书机构",
                    "用法条对线替代修炼与竞争",
                    "只写底层压迫不写晋升通道",
                ],
            },
        ],
        # ---------- 风格配置 ----------
        "conflict_examples": "势力斗法、境界压制、资源争夺、秘境风险、宗门博弈",
        "extra_prohibitions": (
            "1. 除非大纲明确要求，禁止把正文重心写成条款辩论/证据链/程序审理。\n"
            "2. 禁止连续两个以上段落只谈契文细则而无修炼、战力或机缘推进。\n"
            '3. 禁止把核心爽点写成"程序正确"而非"实力与筹码增长"。'
        ),
        "positive_style": (
            "1. 文风必须是昂扬、果断、锋利的玄幻成长爽文，不写冷湿压抑求生腔。\n"
            "2. 每章至少出现2类玄幻硬锚点并参与剧情：修炼/功法/境界/灵气/法器/丹药/秘境/宗门资源。\n"
            '3. 本章前40%必须出现一次"玄幻行动推进"（修炼、斗法、夺宝、试炼、突破其一）。\n'
            "4. 本章必须兑现至少1个可量化收益：境界进度、词力提升、资源到手、贡献点、战力筹码。\n"
            "5. 本章必须有1次主动反制/布局动作，禁止全程被动挨压。\n"
            "6. 程序条款、契文辩驳类段落总占比不得超过30%（除非大纲明确要求）。\n"
            '7. 结尾必须把悬念落在"下一步变强或对抗升级"，不能落在纯文书流程。'
        ),
        "genre_anchors": [
            "修炼", "境界", "突破", "功法", "灵气", "灵石",
            "宗门", "外门", "内门", "词条", "机缘", "法器",
            "丹药", "秘境", "经脉", "真元", "剑诀", "斗法",
        ],
        "rewrite_target": (
            "1. 叙事语气：改为玄幻成长爽文的昂扬起势感\n"
            "2. 描写重心：聚焦修炼推进、战力筹码、机缘争夺\n"
            "3. 结构调整：压缩条款/契文辩论段，转为行动、对抗与收益兑现\n"
            "4. 镜头语言：把死寂、阴风、诡异安静、未知呼吸感改写为矿脉、灵纹、机缘、资源、翻盘筹码"
        ),
        "trope_keywords": ["修仙题材套路"],
        "knowledge_preferred_files": [
            "xuanhuan-plot-patterns.md",
            "xuanhuan-cool-points.md",
            "cultivation-levels.md",
        ],
        "template_preferred_files": [
            "power-systems.md",
            "cultivation-levels.md",
            "xuanhuan-plot-patterns.md",
            "xuanhuan-cool-points.md",
        ],
        "template_aliases": {
            "玄幻": ["修仙"], "仙侠": ["修仙"], "奇幻": ["修仙"],
            "武侠": ["修仙"], "系统流": ["系统流", "修仙"],
        },
        "drift_detection": {
            "suppressive_lexicon": [
                "忍住", "不敢", "不动声色", "只求活着", "先忍", "藏好", "压下去", "窒息",
                "阴冷", "潮湿", "霉味", "发冷", "麻木", "绝望",
            ],
            "suspense_lexicon": [
                "死寂", "诡异的安静", "像有什么在呼吸", "不对劲",
                "阴风", "死地", "不该看见", "今晚别动", "活命", "藏好",
            ],
            "growth_lexicon": [
                "修炼", "突破", "境界", "灵气", "功法", "词条", "掠夺",
                "资源", "贡献点", "灵石", "机缘", "反制", "破局", "法器", "丹药", "斗法",
            ],
            "legal_lexicon": [
                "契文", "词契", "条款", "第九条", "白纸黑字", "公示", "见证", "作证",
                "证据链", "核查", "按印", "告示牌", "契堂", "呈告", "程序",
            ],
            "payoff_words": [
                "突破", "反制", "收益", "提升", "获得", "到手", "拿回", "逆转", "压制",
                "晋升", "升阶", "进阶", "凝聚", "领悟", "掌握", "吞噬", "吸收",
                "夺", "抢", "赢", "胜", "碾压", "击败", "斩杀", "收服",
                "入手", "炼成", "激活", "觉醒", "解锁", "强化", "翻盘", "破局",
            ],
            "substyle_checks": {
                "热血升级流": {
                    "timid_lexicon": [
                        "先苟住", "活命", "藏好", "忍一夜", "别动", "不该看见",
                        "低头", "先忍", "按住念头", "不要出头", "求稳",
                    ],
                    "hotblood_anchors": ["突破", "反击", "夺宝", "斗法", "出手", "大比", "试炼", "镇压", "斩", "逆袭"],
                },
            },
        },
        "opening_instruction": (
            "1. 开篇应尽快进入本章大纲已给出的首个困境、冲突或目标，禁止额外扩写与大纲无关的慢热氛围。\n"
            "2. 若大纲前段安排了主角主动动作、试探、反制或布局，必须尽早写出；若未安排，不得硬加新反击，只能强化主角判断、准备或代价承受。\n"
            "3. 若大纲里有矿脉异动、秘境异象、未知声响，必须在1-2段内转成灵纹、矿性、机缘、资源或战力线索；若大纲没有，禁止自行添加。\n"
            "4. 若本章大纲安排了收益、筹码、发现或能力确认，必须在对应位置清晰兑现；若这些内容属于后章，禁止提前写出。\n"
            "5. 章末悬念必须停在本章大纲允许的边界内，优先挂钩下一步行动、资源争夺或对抗升级，不能额外制造不属于大纲的阴悬感。"
        ),
    },

    # ======================== 规则怪谈 ========================
    {
        "id": "规则怪谈",
        "name": "规则怪谈",
        "bucket": "rules-mystery",
        "aliases": ["怪谈", "悬疑", "惊悚", "恐怖", "rules-mystery"],
        "default_substyle": "规则生存流",
        "substyles": [
            {
                "id": "规则生存流",
                "name": "规则生存流",
                "description": "重规则压迫、试错成本与求生决策。",
                "keywords": ["规则", "守则", "生存", "试错", "污染", "禁忌", "求生"],
                "focus": ["规则要具体可触发", "代价必须真实", "每次判断都影响生死"],
                "avoid": ["热血升级流", "宗门修炼体系", "轻松插科打诨"],
            },
            {
                "id": "诡局推演流",
                "name": "诡局推演流",
                "description": "重信息差、逻辑推演与规则互证。",
                "keywords": ["推演", "线索", "信息差", "诡局", "推理", "验证"],
                "focus": ["线索回收", "多轮试探", "推理链闭环"],
                "avoid": ["无根据硬反转", "单纯堆砌怪物描写", "爽文打脸模板"],
            },
            {
                "id": "密室调查流",
                "name": "密室调查流",
                "description": "重封闭空间、调查推进与异象真相。",
                "keywords": ["密室", "封闭", "调查", "异常", "现场", "真相"],
                "focus": ["现场感", "调查步骤", "真相逼近"],
                "avoid": ["大地图升级冒险", "玄幻修炼体系", "无调查直接揭底"],
            },
        ],
        "conflict_examples": "规则压迫、认知错位、试错代价、信息差推理、禁忌触发",
        "extra_prohibitions": (
            "1. 禁止写成热血升级打怪流，冲突必须围绕规则和认知展开。\n"
            "2. 禁止用玄幻修炼体系（境界/灵气/功法）替代怪谈规则体系。\n"
            "3. 禁止轻松插科打诨消解恐怖张力。"
        ),
        "positive_style": (
            "1. 文风必须是紧绷、克制、充满认知压迫的怪谈氛围，每句话都藏着不对劲的细节。\n"
            "2. 每章必须出现至少2条具体规则/守则/禁忌，并让角色直面规则的约束。\n"
            "3. 本章前30%必须建立一个认知错位（看似正常的表象下藏着异常）。\n"
            "4. 每章至少1次试错或违规后果展示：有人触犯规则后，发生不可逆的事。\n"
            "5. 信息揭露节奏：每章揭示1个线索，同时制造1个新疑问，保持推理驱动力。\n"
            "6. 环境描写服务于规则感：封闭空间、不自然的秩序、看似日常却处处约束。\n"
            '7. 结尾必须落在"新的规则威胁逼近"或"旧线索指向更深的真相"。'
        ),
        "genre_anchors": [],  # 规则怪谈用专门的 rule_anchors 检测，见 drift_detection
        "rewrite_target": (
            "1. 叙事语气：改为紧绷克制的怪谈认知压迫感\n"
            "2. 描写重心：聚焦规则约束、试错代价、信息差与认知错位\n"
            "3. 结构调整：增加规则细节和违规后果展示，减少热血打斗描写"
        ),
        "trope_keywords": ["规则怪谈套路", "怪谈题材套路"],
        "knowledge_preferred_files": [
            "core-elements.md",
            "structure-pacing.md",
            "clue-design.md",
        ],
        "template_preferred_files": [
            "core-elements.md",
            "structure-pacing.md",
            "clue-design.md",
        ],
        "drift_detection": {
            "xuanhuan_leak": ["修炼", "境界", "突破", "功法", "灵气", "灵石", "宗门", "丹药", "法器"],
            "romance_leak": ["心动", "暧昧", "告白", "甜蜜", "脸红", "拥抱"],
            "rule_anchors": ["规则", "守则", "禁忌", "违规", "异常", "不对劲", "线索", "真相", "副本"],
        },
    },

    # ======================== 现代言情 ========================
    {
        "id": "现代言情",
        "name": "现代言情",
        "bucket": "dog-blood-romance",
        "aliases": ["狗血言情", "替身文", "言情", "现代言情文", "dog-blood-romance", "romance"],
        "default_substyle": "高甜拉扯",
        "substyles": [
            {
                "id": "追妻火葬场",
                "name": "追妻火葬场",
                "description": "先虐后追，情绪报复与关系反转是核心。",
                "keywords": ["追妻火葬场", "后悔", "追妻", "虐恋", "回头", "挽回"],
                "focus": ["情绪反噬", "关系逆转", "报复与心软拉扯"],
                "avoid": ["平铺直叙生活流水账", "古风腔", "悬疑惊悚腔"],
            },
            {
                "id": "高甜拉扯",
                "name": "高甜拉扯",
                "description": "高频互动、暧昧升级、甜中带刺。",
                "keywords": ["暧昧", "心动", "拉扯", "高甜", "试探", "吃醋"],
                "focus": ["互动密度", "情绪升温", "甜点及时兑现"],
                "avoid": ["冷硬说明文", "惊悚腔", "纯事业线压过感情线"],
            },
            {
                "id": "豪门修罗场",
                "name": "豪门修罗场",
                "description": "身份、利益与情感纠缠并进。",
                "keywords": ["豪门", "修罗场", "联姻", "误会", "争宠", "身份"],
                "focus": ["身份张力", "多方拉扯", "利益与情感冲突"],
                "avoid": ["纯职场纪实", "平淡恋爱流水账", "玄幻打怪升级"],
            },
        ],
        "conflict_examples": "情感误会、身份反转、感情拉扯、吃醋争风、深情告白",
        "extra_prohibitions": (
            "1. 禁止用冷硬说明文写情感场景，对话和内心必须有情绪温度。\n"
            "2. 禁止长篇事业线/职场描写挤占感情线篇幅（除非大纲要求）。\n"
            "3. 禁止写成惊悚氛围或悬疑推理，保持恋爱甜虐基调。"
        ),
        "positive_style": (
            "1. 文风必须是细腻、撩拨、情绪张力饱满的言情文，每一段都推进情感温度。\n"
            "2. 每章至少出现2类言情硬锚点：心动/暧昧/吃醋/误会/告白/拥抱/泪目/甜蜜互动。\n"
            '3. 本章前40%必须出现一次"情感触发事件"（偶遇、误会、醋意、暧昧接触其一）。\n'
            "4. 每章必须有至少1个情绪高光时刻：心跳加速、脸红、眼眶泛红、心软动摇。\n"
            "5. 男女主互动占比不低于40%，对话要有潜台词和情绪暗涌。\n"
            "6. 环境描写服务于情感氛围：暖光、花香、雨夜、咖啡店等浪漫场景意象。\n"
            '7. 结尾必须落在"关系推进一步"或"情感悬念升级"（心动未说出口、误会加深、新对手出现）。'
        ),
        "genre_anchors": [
            "心动", "吃醋", "告白", "误会", "甜蜜", "暧昧",
            "深情", "拥抱", "眼泪", "心疼", "温柔", "脸红",
            "心跳", "牵手", "拉扯", "心软", "撩", "宠",
        ],
        "rewrite_target": (
            "1. 叙事语气：改为言情文的细腻撩拨感\n"
            "2. 描写重心：聚焦情感拉扯、心动暧昧、甜虐交织\n"
            "3. 段落密度：增加角色互动与情感交锋"
        ),
        "trope_keywords": ["替身文", "言情", "狗血"],
        "knowledge_preferred_files": [
            "romance-pacing.md",
            "emotional-tension.md",
            "sweet-moments.md",
        ],
        "template_preferred_files": [
            "romance-pacing.md",
            "emotional-tension.md",
            "plot-templates.md",
        ],
        "template_aliases": {"现代言情": ["狗血言情"]},
        "drift_detection": {
            "emotion_lexicon": [
                "心动", "心跳", "脸红", "暧昧", "吃醋", "误会", "告白",
                "拥抱", "牵手", "甜蜜", "撩", "心软", "眼泪", "心疼",
                "温柔", "宠", "深情", "拉扯",
            ],
            "cold_lexicon": [
                "阴森", "诡异", "规则", "守则", "修炼", "境界", "灵气",
                "功法", "副本", "杀伐", "灵石", "斗法",
            ],
        },
    },

    # ======================== 古代言情 ========================
    {
        "id": "古代言情",
        "name": "古代言情",
        "bucket": "period-drama",
        "aliases": ["古言", "宫斗", "古代言情文", "period-drama"],
        "default_substyle": "宫斗权谋",
        "substyles": [
            {
                "id": "宫斗权谋",
                "name": "宫斗权谋",
                "description": "宫廷秩序、人心试探与权势博弈并行。",
                "keywords": ["宫斗", "权谋", "后宫", "圣宠", "布局", "试探"],
                "focus": ["权力位置变化", "试探回击", "含蓄锋利的语言"],
                "avoid": ["现代口语腔", "爽文打怪模板", "悬疑惊悚氛围"],
            },
            {
                "id": "宅斗逆袭",
                "name": "宅斗逆袭",
                "description": "家宅秩序、嫡庶冲突与名分争夺。",
                "keywords": ["宅斗", "嫡庶", "掌家", "内宅", "逆袭", "姨娘"],
                "focus": ["内宅规则", "关系压制与反制", "地位稳步提升"],
                "avoid": ["纯宫廷政变", "现代法条逻辑", "玄幻体系"],
            },
            {
                "id": "朝堂联姻",
                "name": "朝堂联姻",
                "description": "婚约、朝堂与家族利益捆绑推进。",
                "keywords": ["朝堂", "联姻", "门第", "婚约", "家族", "站队"],
                "focus": ["政治与婚姻绑定", "家族筹码", "话中机锋"],
                "avoid": ["纯后宫争宠", "甜宠无冲突", "惊悚腔"],
            },
        ],
        "conflict_examples": "朝堂博弈、后宫争宠、家族倾轧、权谋暗斗、联姻利益",
        "extra_prohibitions": (
            "1. 禁止使用现代口语和网络用语，对话必须有古典韵味。\n"
            "2. 禁止用玄幻打怪升级模板替代宫廷/家族博弈。\n"
            "3. 禁止直白表达情感和意图，人物言行必须含蓄有机锋。"
        ),
        "positive_style": (
            "1. 文风必须是典雅含蓄、暗藏锋芒的古典叙事，对话要有古韵和机锋。\n"
            "2. 每章至少出现2类古言硬锚点：朝堂博弈/后宫争宠/家族暗斗/联姻试探/请安布局。\n"
            '3. 本章前40%必须出现一次"权力或关系的试探动作"（请安暗示、送礼试探、话中机锋其一）。\n'
            "4. 每章必须推进至少1条权力线或情感线：恩宠变化、阵营松动、新的威胁或盟友。\n"
            "5. 角色对话要有弦外之音：表面客气、内里交锋，用规矩和礼仪包裹真实意图。\n"
            "6. 环境描写服务于宫廷/府邸氛围：宫灯、檀香、屏风、庭院、绫罗、丝竹。\n"
            '7. 结尾必须落在"局势更进一步"或"新的博弈开启"（圣意难测、新敌入局、心机初见成效）。'
        ),
        "genre_anchors": [
            "皇上", "娘娘", "府上", "宫中", "朝堂", "联姻",
            "嫡庶", "请安", "宫灯", "侍女", "布局", "恩宠",
            "圣旨", "府邸", "嬷嬷", "规矩", "赐", "跪",
        ],
        "rewrite_target": (
            "1. 叙事语气：改为古典典雅的宫廷/权谋语感\n"
            "2. 描写重心：聚焦朝堂暗流、人心博弈、含蓄试探\n"
            "3. 段落密度：增加布局与反制推进"
        ),
        "trope_keywords": ["古言", "宫斗", "古代言情"],
        "knowledge_preferred_files": [
            "plot-patterns.md",
            "palace-intrigue.md",
            "ancient-dialogue.md",
        ],
        "template_preferred_files": [
            "plot-patterns.md",
            "palace-intrigue.md",
            "historical-setting.md",
        ],
        "template_aliases": {"古代言情": ["古言"], "历史": ["古言"]},
        "drift_detection": {
            "ancient_lexicon": [
                "皇上", "陛下", "娘娘", "府上", "宫中", "朝堂", "联姻",
                "嫡庶", "请安", "侍女", "恩宠", "规矩", "赐", "圣旨",
                "嬷嬷", "布局", "试探", "机锋",
            ],
            "modern_leak": [
                "手机", "微信", "公司", "领导", "外卖", "地铁", "加班",
                "客户", "合同", "工资",
            ],
        },
    },

    # ======================== 都市现实 ========================
    {
        "id": "都市现实",
        "name": "都市现实",
        "bucket": "realistic",
        "aliases": ["都市", "都市异能", "现实题材", "现实", "现实向", "realistic"],
        "default_substyle": "都市成长",
        "substyles": [
            {
                "id": "都市成长",
                "name": "都市成长",
                "description": "现实压力下的个人成长与逆袭。",
                "keywords": ["成长", "现实", "逆袭", "家庭", "生活", "压力"],
                "focus": ["现实细节", "成长路径", "关系与选择的代价"],
                "avoid": ["玄幻术法", "怪谈守则", "空泛鸡汤"],
            },
            {
                "id": "职场逆袭",
                "name": "职场逆袭",
                "description": "竞争、晋升、资源争夺与办公室博弈。",
                "keywords": ["职场", "晋升", "客户", "方案", "竞争", "公司"],
                "focus": ["职业目标", "项目推进", "人际博弈"],
                "avoid": ["悬浮爽文", "古风腔", "玄幻战斗"],
            },
            {
                "id": "都市异能",
                "name": "都市异能",
                "description": "都市生活与异能能力双线并进。",
                "keywords": ["异能", "都市", "能力", "觉醒", "调查", "组织"],
                "focus": ["都市语境", "能力规则", "现实关系碰撞"],
                "avoid": ["仙侠宗门语言", "纯校园流水账", "惊悚守则腔"],
            },
        ],
        "conflict_examples": "职场竞争、社会压力、人际冲突、道德两难、阶层碰撞",
        "extra_prohibitions": (
            "1. 禁止出现超自然元素（异能/修炼/灵气/规则怪谈），保持现实基底。\n"
            "2. 禁止用古风/书面腔写对话，必须口语化、接地气。\n"
            "3. 禁止空泛鸡汤说教，冲突和成长必须落在具体事件和选择上。"
        ),
        "positive_style": (
            "1. 文风必须是真实、接地气、有烟火气的现实主义叙事，读者要有代入感。\n"
            "2. 每章至少出现2类现实硬锚点：职场压力/家庭矛盾/经济困境/人际冲突/社会现象。\n"
            '3. 本章前40%必须出现一次"现实冲突触发"（领导施压、家人争吵、经济危机、同事背刺其一）。\n'
            "4. 每章必须有至少1个情绪共鸣点：打工人的无奈、小人物的坚持、生活中的温暖或残酷。\n"
            "5. 对话必须像真实对话：口语化、有情绪、有潜台词，杜绝书面腔和说教感。\n"
            "6. 环境描写服务于现实感：地铁、写字楼、出租屋、菜市场、医院、学校等日常场景。\n"
            '7. 结尾必须落在"现实困境推进"或"人物选择面临新考验"（升职还是跳槽、要不要妥协、关系走向十字路口）。'
        ),
        "genre_anchors": [
            "公司", "领导", "工资", "合同", "客户", "同事",
            "家庭", "孩子", "房贷", "地铁", "加班", "辞职",
            "手机", "微信", "外卖", "出租屋", "医院", "学校",
        ],
        "rewrite_target": (
            "1. 叙事语气：改为现实主义质感\n"
            "2. 描写重心：聚焦生活细节、人际冲突、社会压力\n"
            "3. 段落密度：增加真实场景与自然对话"
        ),
        "trope_keywords": ["都市", "现实", "现代"],
        "knowledge_preferred_files": [
            "dialogue-authenticity.md",
            "plot-logic.md",
            "reality-anchoring.md",
        ],
        "template_preferred_files": [
            "plot-logic.md",
            "dialogue-authenticity.md",
            "reality-anchoring.md",
        ],
        "template_aliases": {
            "都市现实": ["都市异能", "现实题材"],
            "都市": ["都市异能", "现实题材"],
            "科幻": ["现实题材"],
        },
        "drift_detection": {
            "reality_lexicon": [
                "公司", "领导", "工资", "合同", "客户", "同事", "家庭",
                "孩子", "房贷", "地铁", "加班", "辞职", "手机", "微信",
                "外卖", "出租屋", "医院", "学校",
            ],
            "fantasy_leak": [
                "修炼", "境界", "灵气", "功法", "灵石", "法器", "宗门",
                "秘境", "突破", "丹药", "规则怪谈", "守则", "副本",
            ],
        },
    },

    # ======================== 知乎短篇 ========================
    {
        "id": "知乎短篇",
        "name": "知乎短篇",
        "bucket": "zhihu-short",
        "aliases": ["短篇", "反转短文", "zhihu-short"],
        "default_substyle": "高能反转",
        "substyles": [
            {
                "id": "高能反转",
                "name": "高能反转",
                "description": "开门见钩子，结尾反转要猛。",
                "keywords": ["反转", "钩子", "真相", "揭穿", "打脸", "结局"],
                "focus": ["高信息密度", "反转回收", "叙述克制"],
                "avoid": ["长线升级", "冗长世界观", "慢热铺垫"],
            },
            {
                "id": "情感反杀",
                "name": "情感反杀",
                "description": "利用关系误判完成情绪层面的反转。",
                "keywords": ["情感", "误判", "反杀", "背叛", "揭露", "关系"],
                "focus": ["情绪爆点", "信息差", "结尾回刺"],
                "avoid": ["平淡叙述", "无钩子开头", "大段背景介绍"],
            },
            {
                "id": "悬念揭秘",
                "name": "悬念揭秘",
                "description": "先埋谜面，再用关键细节一击揭底。",
                "keywords": ["悬念", "揭秘", "线索", "细节", "误导", "揭底"],
                "focus": ["伏笔组织", "线索密度", "揭底瞬间"],
                "avoid": ["空洞煽情", "无解谜过程", "玄幻战斗"],
            },
        ],
        "conflict_examples": "认知反转、人性暗面、信息差揭露、选择两难、逻辑陷阱",
        "extra_prohibitions": (
            "1. 禁止冗长世界观铺垫和慢热开头，第一段就要抓人。\n"
            "2. 禁止无伏笔的硬反转，每个反转必须有前文线索支撑。\n"
            "3. 禁止水字数的环境描写和情绪铺排，保持信息密度。"
        ),
        "positive_style": (
            "1. 文风必须是冷静克制、高信息密度的知乎体，每句话都有用，没有注水。\n"
            "2. 每章必须出现至少2个信息钩子：悬念、伏笔、反常细节、未解释的行为。\n"
            '3. 开头必须在3段内抛出核心钩子，让读者产生"这不对劲/我想知道为什么"的冲动。\n'
            "4. 每章必须铺设至少1条后续可回收的伏笔线索（人物反常行为、矛盾细节、话中有话）。\n"
            "5. 叙述视角必须有信息差控制：读者知道的和角色知道的不同，制造认知落差。\n"
            "6. 对话要精炼有力：每句话推进信息量或暴露人物立场，杜绝寒暄废话。\n"
            '7. 结尾必须落在"反转揭露"或"更大的悬念打开"（真相反转、认知颠覆、新谜面出现）。'
        ),
        "genre_anchors": [
            "反转", "真相", "线索", "逻辑", "伏笔", "揭穿",
            "聪明", "推理", "细节", "证据", "发现", "恍然",
            "信息差", "认知", "隐瞒", "谎言", "揭底", "钩子",
        ],
        "rewrite_target": (
            "1. 叙事语气：改为冷静克制的知乎体\n"
            "2. 描写重心：聚焦信息差铺设、逻辑伏笔、认知反转\n"
            "3. 段落密度：提升信息量与节奏推进"
        ),
        "trope_keywords": ["短篇", "反转", "知乎"],
        "knowledge_preferred_files": [
            "hook-techniques.md",
            "pacing-rhythm.md",
            "ending-patterns.md",
        ],
        "template_preferred_files": [
            "hook-techniques.md",
            "pacing-rhythm.md",
            "ending-patterns.md",
        ],
        "drift_detection": {
            "info_lexicon": [
                "反转", "真相", "线索", "逻辑", "伏笔", "揭穿",
                "发现", "恍然", "信息差", "隐瞒", "谎言", "证据", "推理",
            ],
            "padding_indicators": ["忽然", "突然", "不禁", "不由得", "缓缓地", "慢慢地"],
        },
    },

    # ======================== 黑暗题材 ========================
    {
        "id": "黑暗题材",
        "name": "黑暗题材",
        "bucket": "dark",
        "aliases": ["黑暗", "黑暗向", "dark"],
        "default_substyle": "权谋倾轧",
        "substyles": [
            {
                "id": "黑暗修仙",
                "name": "黑暗修仙",
                "description": "修仙法则残酷，资源与人命一起被吞噬。",
                "keywords": ["黑暗修仙", "残酷", "资源", "杀伐", "背叛", "代价"],
                "focus": ["代价真实", "法则残酷", "强者秩序"],
                "avoid": ["轻松热血", "程序正义", "甜宠互动"],
            },
            {
                "id": "权谋倾轧",
                "name": "权谋倾轧",
                "description": "利益、权力与背叛层层交织。",
                "keywords": ["权谋", "倾轧", "背叛", "利益", "野心", "掌控"],
                "focus": ["多方算计", "筹码交换", "人性阴影"],
                "avoid": ["单纯惊悚堆氛围", "直白鸡血升级", "法条辩论"],
            },
            {
                "id": "末路求生",
                "name": "末路求生",
                "description": "世界失序后，在残酷环境里争取活路。",
                "keywords": ["求生", "末路", "残存", "绝境", "秩序崩坏", "代价"],
                "focus": ["生存代价", "极限选择", "残酷回报"],
                "avoid": ["轻松吐槽", "无代价的好运", "玄幻宗门晋升模板"],
            },
        ],
        "conflict_examples": "势力倾轧、黑暗法则、弱肉强食、背叛阴谋、绝地求生",
        "extra_prohibitions": (
            "1. 禁止把黑暗写成单纯的恐怖氛围堆砌，重点是权力和利益的残酷。\n"
            "2. 禁止轻松化处理代价（主角总是轻松脱险/无代价获胜）。\n"
            "3. 禁止用热血爽文的打脸套路替代黑暗题材的利益博弈。"
        ),
        "positive_style": (
            "1. 文风必须是冷峻、残酷、充满压迫感的黑暗叙事，弱肉强食是底色。\n"
            "2. 每章至少出现2类黑暗硬锚点：权力倾轧/背叛算计/生存代价/弱肉强食/利益交换。\n"
            '3. 本章前40%必须出现一次"残酷现实展示"（被背叛、被剥夺、被迫做选择其一）。\n'
            '4. 每章必须有至少1个"代价兑现"：角色的选择必须有真实后果，没有免费的午餐。\n'
            "5. 人物关系建立在利益之上：盟友可以随时翻脸，信任是最昂贵的奢侈品。\n"
            "6. 环境描写服务于残酷氛围：荒芜、铁幕、血色、废墟、弱者的尸骨铺路。\n"
            '7. 结尾必须落在"新的威胁逼近"或"主角为下一步付出了代价"（筹码消耗、新敌浮现、盟友反水）。'
        ),
        "genre_anchors": [
            "势力", "背叛", "阴谋", "权力", "利益", "手段",
            "残酷", "代价", "野心", "筹码", "杀伐", "臣服",
            "倾轧", "弱肉强食", "铁幕", "血腥", "牺牲", "算计",
        ],
        "rewrite_target": (
            "1. 叙事语气：改为黑暗残酷的斗争语感\n"
            "2. 描写重心：聚焦人心险恶、弱肉强食、利益倾轧\n"
            "3. 段落密度：增加势力角逐与阴谋推进"
        ),
        "trope_keywords": ["黑暗题材套路"],
        "knowledge_preferred_files": [
            "power-struggle.md",
            "dark-plot-patterns.md",
            "survival-cost.md",
        ],
        "template_preferred_files": [
            "power-struggle.md",
            "dark-plot-patterns.md",
            "survival-cost.md",
        ],
        "drift_detection": {
            "dark_lexicon": [
                "背叛", "阴谋", "代价", "残酷", "利益", "野心", "筹码",
                "杀伐", "倾轧", "弱肉强食", "牺牲", "算计", "权力",
            ],
            "soft_leak": [
                "甜蜜", "暧昧", "心动", "脸红", "温柔", "宠", "告白",
            ],
        },
    },
]


# ---------------------------------------------------------------------------
# 通用漂移检测词表（非题材特有，所有非怪谈题材共用）
# ---------------------------------------------------------------------------

DRIFT_LEXICON: List[str] = [
    "不该看见", "今晚别动", "活命", "藏好", "毛骨悚然", "后颈发凉",
    "规则怪谈", "诡异", "污染", "理智值", "san", "守则", "副本", "不可名状",
]

SUPPRESSIVE_HORROR_LEXICON: List[str] = [
    "阴冷", "潮湿", "霉味", "窒息", "麻木", "绝望",
    "发冷", "不寒而栗", "毛骨悚然", "诡异的笑", "阴森",
]


# ---------------------------------------------------------------------------
# 通用回退（未命中任何已知题材时使用）
# ---------------------------------------------------------------------------

GENERIC_POSITIVE_STYLE: str = (
    "1. 文风、冲突组织、氛围意象必须贴合当前题材特征。\n"
    "2. 每章的冲突和张力必须来自题材内部逻辑。\n"
    "3. 环境描写、角色对话、情绪渲染必须符合题材的阅读期待。\n"
    "4. 结尾必须落在题材核心矛盾的推进上。"
)

GENERIC_REWRITE_TARGET: str = (
    "1. 叙事语气：改为贴合当前题材的正确文风\n"
    "2. 描写重心：聚焦题材内的核心矛盾与冲突\n"
    "3. 段落密度：提升题材核心元素的出场密度"
)

GENERIC_OPENING_INSTRUCTION: str = (
    "1. 开篇应尽快进入本章大纲给出的首个困境、目标或关键冲突，禁止慢热铺陈。\n"
    "2. 若大纲前段安排了主角主动动作或主动选择，必须尽早写出；若未安排，不能硬加本章没有的反击或收益。\n"
    "3. 若大纲存在异常、风险、诱因、发现或收益，必须尽快写清其与本章目标的关系；若没有，禁止自行添加。\n"
    "4. 章末悬念必须停在本章大纲允许的边界内，指向下一步行动或冲突升级，不能另起一条与大纲无关的新悬念。"
)


# ---------------------------------------------------------------------------
# 公共 API — skill_executor.py 等外部模块通过这些函数读取配置
# ---------------------------------------------------------------------------

def _normalize_text(value: Any) -> str:
    return str(value or "").strip()


def get_genre_entry(genre: Any) -> Optional[Dict[str, Any]]:
    query = _normalize_text(genre)
    if not query:
        return None
    query_l = query.lower()
    for entry in GENRE_CATALOG:
        names = [entry["id"], entry["name"], *entry.get("aliases", [])]
        for name in names:
            if query == name or query_l == str(name).lower():
                return entry
    return None


def _entry_by_bucket(bucket: str) -> Optional[Dict[str, Any]]:
    for entry in GENRE_CATALOG:
        if entry.get("bucket") == bucket:
            return entry
    return None


def canonical_genre_id(genre: Any) -> str:
    entry = get_genre_entry(genre)
    if entry:
        return entry["id"]
    return _normalize_text(genre)


def get_genre_bucket(genre: Any) -> str:
    entry = get_genre_entry(genre)
    if entry:
        return entry.get("bucket", "")
    return ""


def get_substyle_entry(genre: Any, substyle: Any = "") -> Optional[Dict[str, Any]]:
    entry = get_genre_entry(genre)
    if not entry:
        return None

    query = _normalize_text(substyle)
    substyles = entry.get("substyles", [])
    if not query:
        default_id = entry.get("default_substyle", "")
        return next((item for item in substyles if item.get("id") == default_id), substyles[0] if substyles else None)

    query_l = query.lower()
    for item in substyles:
        names = [item.get("id", ""), item.get("name", ""), *(item.get("aliases", []) or [])]
        for name in names:
            if query == name or query_l == str(name).lower():
                return item

    default_id = entry.get("default_substyle", "")
    return next((item for item in substyles if item.get("id") == default_id), substyles[0] if substyles else None)


def canonical_substyle_id(genre: Any, substyle: Any = "") -> str:
    item = get_substyle_entry(genre, substyle)
    if item:
        return item.get("id", "")
    return _normalize_text(substyle)


def list_supported_genres() -> List[Dict[str, Any]]:
    return deepcopy(GENRE_CATALOG)


# ---------- 风格配置读取 ----------

def _get_field(bucket: str, field: str, default: Any = "") -> Any:
    """按 bucket key 读取题材配置字段。"""
    entry = _entry_by_bucket(bucket)
    if entry:
        return entry.get(field, default)
    return default


def get_conflict_examples(bucket: str) -> str:
    return _get_field(bucket, "conflict_examples", "当前题材内的冲突与矛盾")


def get_extra_prohibitions(bucket: str) -> str:
    return _get_field(bucket, "extra_prohibitions", "")


def get_positive_style(bucket: str) -> str:
    return _get_field(bucket, "positive_style", GENERIC_POSITIVE_STYLE)


def get_genre_anchors(bucket: str) -> List[str]:
    return _get_field(bucket, "genre_anchors", [])


def get_rewrite_target(bucket: str) -> str:
    return _get_field(bucket, "rewrite_target", GENERIC_REWRITE_TARGET)


def get_trope_keywords(bucket: str) -> List[str]:
    return _get_field(bucket, "trope_keywords", [])


def get_knowledge_preferred_files(bucket: str) -> List[str]:
    return _get_field(bucket, "knowledge_preferred_files", [])


def get_template_preferred_files(bucket: str) -> List[str]:
    return _get_field(bucket, "template_preferred_files", [])


def get_drift_detection(bucket: str) -> Dict[str, Any]:
    return _get_field(bucket, "drift_detection", {})


def get_opening_instruction(bucket: str) -> str:
    return _get_field(bucket, "opening_instruction", "")


def get_template_aliases() -> Dict[str, List[str]]:
    """汇总所有题材的模板名称别名映射。"""
    merged: Dict[str, List[str]] = {}
    for entry in GENRE_CATALOG:
        aliases = entry.get("template_aliases")
        if isinstance(aliases, dict):
            merged.update(aliases)
    return merged
