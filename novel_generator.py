#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小说生成器 - Novel Generator
一个基于模板和随机组合的小说生成工具
"""

import random
import json
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict


@dataclass
class Character:
    """角色类"""
    name: str
    age: int
    gender: str
    occupation: str
    personality: str
    background: str
    goal: str
    flaw: str


@dataclass
class Setting:
    """场景设定类"""
    location: str
    time_period: str
    atmosphere: str
    weather: str


@dataclass
class PlotPoint:
    """情节点类"""
    title: str
    description: str
    conflict: str
    emotion: str


class NovelGenerator:
    """小说生成器主类"""
    
    def __init__(self):
        # 初始化各种素材库
        self.character_names = {
            'male': ['李明', '王强', '张伟', '刘洋', '陈杰', '杨帆', '赵宇', '孙涛', '周磊', '吴斌'],
            'female': ['李娜', '王芳', '张敏', '刘静', '陈丽', '杨雪', '赵婷', '孙梅', '周琳', '吴燕']
        }
        
        self.occupations = [
            '程序员', '医生', '教师', '律师', '记者', '艺术家', '企业家', '科学家',
            '警察', '厨师', '作家', '音乐家', '摄影师', '设计师', '研究员', '飞行员'
        ]
        
        self.personalities = [
            '开朗乐观', '内向沉思', '果断坚决', '温柔体贴', '幽默风趣',
            '严肃认真', '热情奔放', '冷静理性', '敏感细腻', '勇敢无畏'
        ]
        
        self.backgrounds = [
            '出身普通家庭，通过自己的努力取得成功',
            '来自富裕家庭，但渴望证明自己的价值',
            '经历过重大挫折，从中重新站起来',
            '从小失去父母，由祖父母抚养长大',
            '在国外生活多年， recently 回国发展',
            '曾经是某个领域的天才，但因意外失去能力',
            '隐藏着一个不为人知的秘密身份',
            '背负着家族的使命和期望'
        ]
        
        self.goals = [
            '寻找失散多年的亲人',
            '实现自己的梦想',
            '揭露一个巨大的阴谋',
            '拯救濒临破产的家族企业',
            '找到真爱',
            '证明自己的清白',
            '完成一项重要的使命',
            '寻求内心的平静和解脱'
        ]
        
        self.flaws = [
            '过于固执，不愿听取他人意见',
            '容易冲动，缺乏耐心',
            '过度完美主义',
            '害怕承诺和亲密关系',
            '过于信任他人',
            '自卑，不敢追求自己想要的',
            '工作狂，忽视生活和健康',
            '过去创伤导致的心理阴影'
        ]
        
        self.locations = [
            '繁华的都市中心', '宁静的小镇', '古老的村庄', '海滨城市',
            '山区度假村', '历史古城', '现代化的科技园区', '艺术区',
            '大学城', '工业区', '金融中心', '文化街区'
        ]
        
        self.time_periods = [
            '现代', '近未来', '民国时期', '改革开放初期',
            '千禧年代', '疫情后时代', '人工智能普及时代'
        ]
        
        self.atmospheres = [
            '温馨浪漫', '紧张悬疑', '轻松幽默', '悲伤沉重',
            '充满希望', '神秘诡异', '激烈冲突', '平静祥和'
        ]
        
        self.weathers = [
            '阳光明媚', '阴雨绵绵', '雪花纷飞', '微风和煦',
            '雷电交加', '雾气弥漫', '秋高气爽', '闷热潮湿'
        ]
        
        self.plot_templates = [
            {
                'title': '意外的相遇',
                'description': '两个陌生人在{location}偶然相遇，这次相遇将改变他们的命运。',
                'conflict': '社会地位的差异/过去的恩怨/误解',
                'emotion': '惊讶、好奇、紧张'
            },
            {
                'title': '真相的揭露',
                'description': '主角发现了隐藏在{location}的秘密，这个秘密可能会颠覆一切。',
                'conflict': '道德困境/忠诚与正义的选择/个人利益与他人安危',
                'emotion': '震惊、愤怒、困惑'
            },
            {
                'title': '艰难的抉择',
                'description': '在{location}，主角面临人生中最艰难的决定。',
                'conflict': '爱情与事业/家庭与梦想/安全与冒险',
                'emotion': '痛苦、犹豫、决心'
            },
            {
                'title': '危机降临',
                'description': '{location}突然陷入危机，主角必须挺身而出。',
                'conflict': '时间紧迫/资源有限/内部矛盾',
                'emotion': '恐惧、勇敢、绝望中的希望'
            },
            {
                'title': '重逢的时刻',
                'description': '在{location}，主角与重要的人重逢，但一切都已不同。',
                'conflict': '时间的隔阂/未解的心结/新的障碍',
                'emotion': '喜悦、伤感、复杂的情感'
            },
            {
                'title': '梦想的起点',
                'description': '主角在{location}迈出了追逐梦想的第一步。',
                'conflict': '现实的阻力/他人的质疑/自身的怀疑',
                'emotion': '兴奋、紧张、充满期待'
            },
            {
                'title': '背叛与原谅',
                'description': '在{location}，主角遭遇了信任之人的背叛。',
                'conflict': '信任与怀疑/报复与宽恕/真相与谎言',
                'emotion': '痛苦、愤怒、最终的释然'
            },
            {
                'title': '最后的对决',
                'description': '一切在{location}迎来高潮，主角必须面对最终的挑战。',
                'conflict': '正邪对抗/内心挣扎/生死抉择',
                'emotion': '紧张、悲壮、胜利的喜悦'
            }
        ]
        
        self.chapter_openings = [
            "清晨的阳光透过窗帘的缝隙，洒在{character}的脸上。",
            "{character}站在{location}，心中思绪万千。",
            "没有人想到，这一天会成为{character}人生的转折点。",
            "雨已经下了整整三天，就像{character}此刻的心情。",
            "故事要从{time}年前的那个{season}说起。",
            "{character}从未想过，自己会再次回到这个地方。",
            "电话铃声在寂静的房间里显得格外刺耳。",
            "当{character}推开那扇门时，命运的齿轮开始转动。"
        ]
        
        self.transitions = [
            "时光飞逝，转眼已是数月之后。",
            "与此同时，在城市的另一端...",
            "几天后，当一切尘埃落定...",
            "然而，事情并没有那么简单。",
            "就在这个关键时刻...",
            "回忆如潮水般涌来。",
            "夜幕降临，城市华灯初上。",
            "第二天清晨，阳光依旧灿烂。"
        ]
        
        self.endings = [
            "这就是{character}的故事，一个关于{theme}的故事。",
            "生活还在继续，而{character}已经不再是当初的那个人。",
            "在这个充满变数的世界里，唯一不变的是心中的信念。",
            "夕阳西下，{character}踏上了新的旅程。",
            "有些问题可能永远没有答案，但这正是生活的魅力所在。",
            "故事结束了，但属于{character}的生活才刚刚开始。",
            "回首往事，{character}明白了一切都有它的意义。",
            "未来的路还很长，但至少现在，{character}找到了方向。"
        ]
        
        self.themes = [
            '爱与成长', '梦想与坚持', '救赎与原谅', '勇气与牺牲',
            '家庭与责任', '友情与背叛', '命运与选择', '真实与虚幻'
        ]
        
        self.seasons = ['春天', '夏天', '秋天', '冬天']

    def generate_character(self, gender: Optional[str] = None) -> Character:
        """生成一个随机角色"""
        if gender is None:
            gender = random.choice(['male', 'female'])
        
        name = random.choice(self.character_names[gender])
        age = random.randint(20, 45)
        occupation = random.choice(self.occupations)
        personality = random.choice(self.personalities)
        background = random.choice(self.backgrounds)
        goal = random.choice(self.goals)
        flaw = random.choice(self.flaws)
        
        return Character(
            name=name,
            age=age,
            gender='男' if gender == 'male' else '女',
            occupation=occupation,
            personality=personality,
            background=background,
            goal=goal,
            flaw=flaw
        )

    def generate_setting(self) -> Setting:
        """生成一个随机场景设定"""
        return Setting(
            location=random.choice(self.locations),
            time_period=random.choice(self.time_periods),
            atmosphere=random.choice(self.atmospheres),
            weather=random.choice(self.weathers)
        )

    def generate_plot_point(self, setting: Setting) -> PlotPoint:
        """生成一个情节点"""
        template = random.choice(self.plot_templates)
        return PlotPoint(
            title=template['title'],
            description=template['description'].format(location=setting.location),
            conflict=template['conflict'],
            emotion=template['emotion']
        )

    def generate_chapter(self, chapter_num: int, characters: List[Character], 
                        setting: Setting, plot_points: List[PlotPoint]) -> str:
        """生成一个章节"""
        main_char = random.choice(characters)
        plot = random.choice(plot_points)
        
        opening = random.choice(self.chapter_openings).format(
            character=main_char.name,
            location=setting.location,
            time=random.randint(1, 10),
            season=random.choice(self.seasons)
        )
        
        # 生成章节内容
        content = f"第{chapter_num}章：{plot.title}\n\n"
        content += f"{opening}\n\n"
        content += f"{plot.description}\n\n"
        content += f"当前的氛围是{setting.atmosphere}，天气{setting.weather}。\n\n"
        content += f"主要冲突：{plot.conflict}\n"
        content += f"情感基调：{plot.emotion}\n\n"
        
        # 添加一些细节描写
        details = [
            f"{main_char.name}深吸一口气，{main_char.personality}的性格让他/她迅速做出了决定。",
            f"作为一名{main_char.occupation}，{main_char.name}深知这个决定的重要性。",
            f"{main_char.goal}的目标一直驱动着他/她前进，尽管{main_char.flaw}常常成为阻碍。",
            f"回想起{main_char.background}，{main_char.name}更加坚定了现在的选择。"
        ]
        
        content += "\n".join(random.sample(details, min(2, len(details))))
        content += "\n\n"
        
        if chapter_num > 1:
            transition = random.choice(self.transitions)
            content += f"{transition}\n\n"
        
        return content

    def generate_novel(self, title: str, num_chapters: int = 5, 
                      num_characters: int = 2) -> Dict:
        """生成完整的小说"""
        print(f"正在生成小说：《{title}》...")
        print(f"章节数：{num_chapters}")
        print(f"角色数：{num_characters}")
        print("-" * 50)
        
        # 生成角色
        characters = []
        for i in range(num_characters):
            char = self.generate_character()
            characters.append(char)
            print(f"生成角色 {i+1}: {char.name} ({char.gender}, {char.age}岁, {char.occupation})")
        
        # 生成场景设定
        setting = self.generate_setting()
        print(f"\n场景设定：{setting.location}, {setting.time_period}")
        print(f"氛围：{setting.atmosphere}, 天气：{setting.weather}")
        
        # 生成情节点
        plot_points = []
        for i in range(num_chapters):
            plot = self.generate_plot_point(setting)
            plot_points.append(plot)
        
        # 生成主题
        theme = random.choice(self.themes)
        
        # 生成章节
        chapters = []
        print("\n生成章节内容:")
        for i in range(1, num_chapters + 1):
            chapter_content = self.generate_chapter(i, characters, setting, plot_points)
            chapters.append(chapter_content)
            print(f"  ✓ 第{i}章生成完成")
        
        # 生成结尾
        main_char = characters[0]
        ending_template = random.choice(self.endings)
        ending = ending_template.format(character=main_char.name, theme=theme)
        
        novel = {
            'title': title,
            'theme': theme,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'characters': [asdict(c) for c in characters],
            'setting': asdict(setting),
            'chapters': chapters,
            'ending': ending
        }
        
        print("\n" + "=" * 50)
        print(f"小说《{title}》生成完成！")
        print(f"主题：{theme}")
        print("=" * 50)
        
        return novel

    def save_novel(self, novel: Dict, filename: Optional[str] = None):
        """保存小说到文件"""
        if filename is None:
            filename = f"novel_{novel['title']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"《{novel['title']}》\n")
            f.write(f"主题：{novel['theme']}\n")
            f.write(f"生成时间：{novel['created_at']}\n")
            f.write("=" * 80 + "\n\n")
            
            # 角色介绍
            f.write("【角色介绍】\n")
            for char in novel['characters']:
                f.write(f"\n{char['name']} ({char['gender']}, {char['age']}岁)\n")
                f.write(f"职业：{char['occupation']}\n")
                f.write(f"性格：{char['personality']}\n")
                f.write(f"背景：{char['background']}\n")
                f.write(f"目标：{char['goal']}\n")
                f.write(f"缺点：{char['flaw']}\n")
            
            # 场景设定
            f.write(f"\n\n【场景设定】\n")
            f.write(f"地点：{novel['setting']['location']}\n")
            f.write(f"时代：{novel['setting']['time_period']}\n")
            f.write(f"氛围：{novel['setting']['atmosphere']}\n")
            f.write(f"天气：{novel['setting']['weather']}\n")
            
            f.write("\n" + "=" * 80 + "\n\n")
            
            # 章节内容
            for i, chapter in enumerate(novel['chapters'], 1):
                f.write(chapter)
                f.write("\n" + "-" * 40 + "\n\n")
            
            # 结尾
            f.write("【结局】\n")
            f.write(novel['ending'])
            f.write("\n\n")
            f.write("=" * 80 + "\n")
            f.write("【完】\n")
        
        print(f"小说已保存到文件：{filename}")
        return filename

    def display_novel(self, novel: Dict):
        """在控制台显示小说"""
        print("\n" + "=" * 80)
        print(f"《{novel['title']}》")
        print(f"主题：{novel['theme']}")
        print(f"生成时间：{novel['created_at']}")
        print("=" * 80)
        
        print("\n【角色介绍】")
        for char in novel['characters']:
            print(f"\n• {char['name']} ({char['gender']}, {char['age']}岁)")
            print(f"  职业：{char['occupation']}")
            print(f"  性格：{char['personality']}")
            print(f"  目标：{char['goal']}")
        
        print(f"\n【场景】{novel['setting']['location']} - {novel['setting']['time_period']}")
        print(f"氛围：{novel['setting']['atmosphere']}")
        
        print("\n" + "-" * 80)
        print("【章节预览】")
        print("-" * 80)
        
        for i, chapter in enumerate(novel['chapters'], 1):
            lines = chapter.split('\n')
            print(f"\n第{i}章")
            # 显示前几行作为预览
            for line in lines[:8]:
                print(line)
            if len(lines) > 8:
                print("  ...")
        
        print("\n" + "-" * 80)
        print("【结局】")
        print(novel['ending'])
        print("=" * 80)


def main():
    """主函数"""
    print("=" * 60)
    print("       欢迎使用小说生成器")
    print("=" * 60)
    
    generator = NovelGenerator()
    
    # 获取用户输入
    print("\n请输入小说信息（直接回车使用默认值）：")
    title = input("小说标题 [默认：星辰之约]: ").strip() or "星辰之约"
    
    try:
        num_chapters = int(input("章节数量 [默认：5]: ").strip() or "5")
    except ValueError:
        num_chapters = 5
    
    try:
        num_characters = int(input("主要角色数量 [默认：2]: ").strip() or "2")
    except ValueError:
        num_characters = 2
    
    # 生成小说
    novel = generator.generate_novel(title, num_chapters, num_characters)
    
    # 显示小说
    generator.display_novel(novel)
    
    # 询问是否保存
    save = input("\n是否保存到文件？(y/n) [默认：y]: ").strip().lower()
    if save != 'n':
        filename = input("文件名 [默认：自动生成]: ").strip() or None
        generator.save_novel(novel, filename if filename else None)
    
    print("\n感谢使用小说生成器！再见！")


if __name__ == "__main__":
    main()
