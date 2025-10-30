#首先，能看到代码的大家应该是都拆包了……
#我不会弄加密啊，所以你们随便拆吧
#这个代码其实挺石山的，bug会有很多，素材也都是1代2代的素材以及部分由汐澪（凉鸢是谁，不认识）提供
#但是还是希望大家玩的开心





#nvl区域
define gn = Character(None,kind=nvl,what_color="#3852c7")
define bn = Character(None,kind=nvl,what_color="#973acc")
define n = Character(None,kind=nvl)




define t = Character("test")

define gui.nvl_borders = Borders(100,100,100,100)
define gui.nvl_height = None
define gui.nvl_spacing = None
define gui.nvl_text_xpos = 0
define nvl_bg_img = "images/nvl_bg1.png"  # 默认NVL背景
define config.nvl_list_length = None

#这里好像只有n常用，无所谓了，还有一些nvl设置

define config.say_attribute_transition = dissolve

image sbx = "images/sbx/sbx_1.png"
image sbxshock = "images/sbx/bx_shocked.png"
image sbxmianq = "images/sbx/bx_mianq.png"
image sbxsmile = "images/sbx/bx_smile.png"
image sbxworried = "images/sbx/bx_worried.png"
image sbxcry = "images/sbx/bx_cry.png"
#一些人物素材（全景）



label start:
    
    jump ch0
    return


image dpxmovie = Movie(play="<from 21 to 68>video/dpx.avi",mask=True) #地平线视频，ch2用的

label ch0:

    stop music


    pause 0.5
    #t "welcome to {a=https://space.bilibili.com/36977194}never knows best!{/a}"


    show expression "c00.png" at truecenter with dissolve
    pause 2.0
    hide expression "c00.png" with fade


    play music "audio/neibour.wav" fadein 1.0
    show expression "bg0.png" at truecenter with dissolve
    nvl clear
    show expression "bg_2/bgnvl.png" at topleft with dissolve
    gn "「小心！」"
    n "突然，一股大力将少女拉离了原地。"
    n "巨大的鱼头招牌掉在少女刚刚站的地方，"
    n "有个人，帮他挡住了四处飞溅的塑料碎片。"
    gn "「没事吧，没有哪里受伤吧。」"
    gn "「刚刚好危险。」"
    play sound "bx/bx1.wav"
    bn "「没……没事。」"
    play sound "bx/bx2.wav"
    bn "「我完全没有看到那个。」"
    nvl clear
    n "拉开少女的，是不久前给少女结账的店员。"
    gn "「啊，那家店关门了，这招牌一直没人修。」"
    gn "「起风时还和店长聊，说这起大风肯定要砸到人的。」"
    gn "「然后就看到你站在下面了。」"
    gn "「你被吓到了吧，要不要去店里坐一下。」"
    play sound "bx/bx3.wav"
    bn "「嗯……」"
    n "少女犹豫了一下，"
    n "她其实没有被突然掉下来的招牌吓到，"
    n "暑假在这边的老楼探险时，更可怕的景象都遇到过。"
    nvl clear
    n "不过……"
    play sound "bx/bx4.wav"
    bn "「他的手好暖。」"
    n "少女在心里对自己说道，"
    n "她不是一个随便的人，也不是一个警惕性低的人。"
    n "她的包里放着辣椒喷雾，她的衣服里藏着防狼电击枪。"
    n "如果是平时，她绝对不会这么随便答应对方的，也不会产生这种奇怪的想法。"
    n "可是今天……"
    n "或许是除夕，或许是吊桥效应，或许是别的什么冥冥之中的原因。"
    n "她觉得，对方的确实好意，他也应该接受对方的好意。"
    nvl clear
    n "\n\n\n\n\n\n\n"
    play sound "bx/bx5.wav"
    bn "「好。」"
    play sound "bx/bx6.wav"
    bn "「那个，我叫苏半夏，谢谢你救了我。」"
    nvl clear
    stop music fadeout 1.0
    play music "audio/op.wav" fadein 1.0
    n "\n\n\n\n\n"
    
    gn "「没事，这有啥好谢的。」"
    gn "「我叫顾韦。」"
    gn "「回顾的顾，芦苇去掉草字头的韦。」"
    gn "「是苹果湖中学的学生，在这里打工。」"
    
    nvl clear

    hide expression "bg_2/bgnvl.png" 
    stop music fadeout 1.0
    hide expression "bg0.png" with dissolve
    
    jump ch1
    return





label ch1:
    


    
    stop music
    pause 1
    show expression "bg_1/c01.png" at truecenter with dissolve
    pause 2
    hide expression "bg_1/c01.png" with fade
    #c01为章节图


    nvl clear
    show expression "bg_1/bg_1n.png" at truecenter 
    with dissolve
    play music "audio/1_1.wav" fadein 1.0
    $ style.say_dialogue.color = "#000000"
    #我为什么要写这行，不知道
    show expression "bg_1/bg_1.png" at truecenter 
    gn "「我叫顾韦。回顾的顾，芦苇去掉草字头那个韦，是苹果湖中学的学生，在这里打工。」\n"
    show sbx at lcg(1520) with dissolve
    hide expression "bg_1/bg_1n.png"
    
    n "顾……韦……我是不是，在哪里听过这个名字。"

    n "被紧握住的手传来阵阵温度。"

    n "他的手，好温暖，"

    n "令人熟悉，无比怀念的温度。\n"
    
    n "贴在衣服里的暖贴没由来地让我有些燥热，"

    n "奇怪，明明前一瞬身子才稍稍暖和了些，现在额头上怎么已经渗出涔涔汗液。"

    n "与模糊的记忆中一样的燥热，遇到危险时，同样有人挡在我的身前。"

    n "既视感……还有违和感。"
    # hide sbx with dissolve
    hide sbx 
    nvl clear
    hide expression "bg_1/bg_1.png" with dissolve
    
    
    
    
    show expression "bg_1/bg_1.png" at truecenter with dissolve
    nvl clear

    gn "「要不还是先去店里面吧，招牌的支架还没掉下来，说不定还会有危险。」\n"

    n "顾韦指着摇摇欲坠的金属支架,"

    gn "\n「我等会打电话给街道办，让他们来处理一下。」"

    n "\n「嗯。」我随意地答应道，思绪停留在原地。"

    n "顾韦拉着我的手，往森罗万象里走去。"
    nvl clear
    hide expression "bg_1/bg_1.png"
    show expression "bg_1/bg_2.png" at truecenter with dissolve
    n "\n\n\n\n\n"
    
    n "孱陵路……一来到这里，就有熟悉的感觉，刚刚的既视感也是。"

    n "想起来了，虽然只有一点点，但我一定和那个人在这里经历过非常重要的事情。"

    n "......可是那个人，是谁？那个理应被我呼唤过千百遍的名字，到底是什么？"
    nvl clear
    n "\n\n\n\n\n"
    n "……"

    n "这是我第一次主动去牵女生的手。事出紧急，容不得我多想，身体比脑袋更快反应过来，"

    n "我一把拉住她，向着旁边躲闪而去。"

    n "在我平凡的人生中，我从未有过如此强烈的冲动——想要保护一个人。"

    
    show expression "bg_1/bg_3.png" at truecenter with dissolve
    hide expression "bg_1/bg_2.png"
    nvl clear
    show sbxshock at lcg with dissolve
    n "「哐当！」铁质招牌砸落在地面，锈红色的粉尘裹挟着碎玻璃扬起阵阵烟雾。"
    n "行人纷纷侧目，又收回目光，只当做是回家路上的一个小插曲。"
    n "每个人都期待着今夜与家人的团聚，没人在意他们受伤与否。"
    #zc
    n "呛人的铁腥味顺着鼻腔被吸进肺部，我不由得咳嗽了几声，好在少女没有被招牌砸到。"
    gn "\n「你没事吧，没有哪里受伤吧？」\n"
    hide sbxshock
    show sbxmianq at lcg 
    bn "\n「没，没事。」"

    bn "「刚才真的好危险。」"

    bn "「我完全没有看到那个。」\n"
    nvl clear
    n "\n\n\n\n"
    n "有那么一瞬间，我恍惚觉得找到了已经失踪许多年的朋友。"
    n "暮光温柔地铺洒在她的身上，如瀑的白色长发闪耀着淡金色的光芒，胸口的蝴蝶挂饰伴着寒风轻轻振翅。"
    n "红宝石般的眼睛里藏着十二月的寒风都吹不散的热忱，以及，眼底那一抹淡淡的悲伤。"
    n "少女的眼睛，是罕见的双色瞳，左眼虽与我失联多年的朋友无比相似，但右眼却是金黄色的。"
    nvl clear
    gn "「要去店里坐一会吗？」\n"

    n "望着她的右眼，我冷不丁地冒出这样一句话。"
    n "我这是在干什么，我跟她不熟吧？别人已经脱离危险了，我还关心她干什么。"
    n "今天是除夕，她要回家和家人团聚吧。"
    n "但是，好在意啊，真的好在意，她的异色瞳。为什么在记忆里，会多出一只不存在的黄金瞳呢。"
    hide sbxmianq
    show sbxsmile at lcg
    bn "\n「嗯……好。」\n"

    n "意料之外的，少女同意了我的邀请，并告诉了我她的名字。"

    bn "\n「我的名字叫苏半夏，谢谢你救了我。」\n"

    n "半夏……只有一半的夏天，永不完结的夏天。"

    nvl clear

    n "\n\n\n\n\n\n\n\n"
    n "可是那个夏天，已经结束了啊……"

    hide sbxsmile
    show expression "bg_1/bg_4.png" at truecenter with dissolve
    hide expression "bg_1/bg_3.png"
    nvl clear
    #店内图
    stop music fadeout 1.0
    play music "audio/night.wav" fadein 1.0 loop
    n "……"
    n "暖风机吹出的风，让人忘却自己身处寒冬。"
    n "在靠窗边的椅子坐下，搓了搓手，刚刚的燥热早已不复存在，取而代之的是一股从心底生出的暖流。"
    n "身子终于是暖和了起来，内心的空虚也像是被这股暖流填满，惬意得想让人就趴在这里浅浅地睡上一会。"
    show sbxsmile at lcg with dissolve
    gn "\n「给，不知道你喜欢喝什么，但应该不会讨厌甜的饮料吧。」\n"

    n "顾韦递过来一瓶阿萨拉奶茶，我顺手接下。"
    n "奶茶刚在暖柜里加热过，拧开盖子喝上一口，丝丝甜腻滑入喉咙，温暖着肚子。"
    n "说起来，也快要到吃饭的时间了。"

    bn "\n「甜的东西确实会让人忘记烦恼呢，我不讨厌。」\n"
    nvl clear
    gn "「那你是有什么烦恼吗，心不在焉的，连招牌掉下来了都没注意。」\n"
    hide sbxsmile
    show sbxworried at lcg 
    n "诶？他是怎么知道的，我表现得有那么明显吗？"

    bn "\n「我在找人，找一个可能不存在的人。」\n"
    hide sbxworried
    show sbxmianq at lcg 
    n "我低下头，手指不自觉地摩挲着瓶盖上的纹路。"

    gn "\n「都下定决心要去找了，为什么要在乎那个人存不存在呢。」\n"

    n "他笑了笑，坐在我对面的椅子上，"

    gn "\n「顺带一提，我也在找人。」\n"

    nvl clear

    show sbxworried at lcg with dissolve

    bn "「谁？」\n"

    n "几乎是脱口而出，下一瞬才发觉，自己这样直白是不是有些太过冒昧。"

    gn "\n「一个朋友，」\n"

    n "他指了指自己的右眼角，"

    gn "\n「他的右眼其实也有一颗泪痣，而且瞳孔的颜色和你的左眼很像。」\n"
    hide sbxworried
    show sbx at lcg with dissolve
    nvl clear
    n "和我很像的一个人。"
    n "我看着坐在对面的那人。虽说长相十分俊秀，但总有种说不出的感觉，"
    n "就像是倘若把他放进人群中，下一秒就会忘记他的样子，直至他的身影彻底被人潮淹没。"

    gn "\n「说真的，刚才你来买热贴的时候，我真的还以为是我的那个朋友呢，」"

    gn "「一样的白发，一样的泪痣，唯独就是眼睛颜色不一样。」\n"

    n "我跟他，没见过吧，记忆里确实没有顾韦的影子，难道是忘记了吗？"
    n "毕竟这样大众的长相，忘了也很正常吧。可对他无缘无故的信任感是怎么回事？"
    n "我真的，不认识他吗？"
    hide sbx
    #zc
    nvl clear
    show expression "bg_1/bg_5.png" at truecenter with dissolve
    hide sbxmianq 
    
    n "\n\n\n\n\n\n\n"
    n "窗玻璃突然被蒙上了白内障般的翳，天际线被灰黑色的云层遮盖，"#诡异的居中方法
    n "老旧的招牌被风吹得吱呀作响，人们裹紧衣服，不自觉地加快了回家的脚步。"
    nvl clear
    hide expression "bg_1/bg_5.png" with dissolve
    

    gn  "「要下雪了，江城已经很久没下过雪了。」\n"

    n "顾韦放好最后一件商品，"

    gn  "\n「还不回去吗，快要到吃年夜饭的时间了。」\n"
    show sbxworried at lcg 
    bn  "「那你呢，你为什么不回去？」\n"

    gn  "「不要用问题来回答问题啊！」\n"

    n "顾韦又坐了回来，看向窗外。"
    nvl clear

    gn  "「我家里又没人，父母都在国外。回去了也是无所事事，还不如在这里多待一会，」"

    gn  "「要是不多待一会，说不定你就被那个招牌砸到了呢。」"

    gn  "「而且，我对这条街有种莫名的亲切感，就好像在这里发生过什么一样，包括来这里打工，也是这个原因。」\n"

    n "说着，顾韦站起身，脱下了身上的工作服，往休息间走去。"

    gn  "\n「我准备换班了，等会要去前面坐公交，顺路吗，要不一起走吧。」\n"

    bn  "「不顺路呢……我要去坐地铁。」\n"

    gn  "「好吧好吧，那你先出去，我关门。」\n"
    nvl clear
    hide sbxworried
    show expression "bg_1/bg_6.png" at truecenter with dissolve
    hide expression "bg_1/bg_4.png"
    #show sbxworried at lcg with dissolve
    n "走在长长的街道，望着顾韦远去的背影，疼痛和空虚再一次涌上心头。"
    n "我捂住胸口蹲了下去，可是那即将失去什么的预感却更加强烈。"

    gn  "\n「我会去找你，如果找不到，那就一直，一直，一直找下去，」"
    gn  "「我爱你，我想永远和你在一起，」\n"
    bn  "「可是，这一次，真的要说再见了。」\n"
    hide sbxworried
    #show sbxcry at lcg with dissolve
    n "心中的苦涩顺着眼角滑落，被冰封的河流又一次流动。\n我想起来了。"
    n "我站起身，向着顾韦离开的方向跑去。"
    nvl clear
    bn  "「无论你消失在人潮里多少次，无论忘记你多少次，无论你还会不会记得我，我都会找到你，因为，这是我们之间的约定。」\n"
    n "拐角，又一次看见那道身影。人潮依旧，但我还是一眼就认出了那道平凡的身影。"
    n "即使一切被遗忘，你也仍在我眼中闪耀。"
    nvl clear
    hide sbxcry
    #hide expression "bg_1/bg_3.png" 
    show expression "bg_1/bg_3.png" at truecenter with dissolve
    show sbxcry at lcg with dissolve
    hide expression "bg_1/bg_6.png" 
    bn  "「不要走！」\n"

    n "“我一把抓住顾韦的手，就同很久以前，他抓住我一样。”"

    gn  "\n「诶？你不是要坐地铁吗，怎么？」\n"

    bn  "「无论怎样都行，明天，至少明天一天，陪我。」\n"

    gn  "「我一直都在那个便利店啊，怎么搞得好像我会失踪一样。再说了，明天是大年初一，我是不用走亲戚，你……」\n"

    bn  "「我没有亲戚可以走，父母那边也无所谓，只要明天一天就好！」\n"

    n "顾韦挠了挠头，"

    gn  "\n「真是的，明明只认识了一会而已，为什么会有种……我们相识了好久的感觉。」\n"


    nvl clear
    hide sbxcry
    hide expression "bg_1/bg_3.png" with dissolve
    
    #n "\n\n\n\n\n\n\n\n\n\n             Chapter 1 End"
    stop music fadeout 1.0
    

    pause 2
    jump ch2
    #截止到demo结束
    return




#ch2:363-
label ch2:
    stop music
    show expression "bg_2/c02.png" at truecenter with dissolve
    pause 2
    hide expression "bg_2/c02.png" with fade
    
    play music "audio/memorys.wav" fadein 1.0 loop
    show expression "bg_2/bg_1.png" at truecenter with dissolve
    nvl clear
    n "如鲠在喉，夜不能寐，深夜中每一个声音都被无限放大。"
    n "每一次翻身，衣物与被褥摩擦发出“窸窸窣窣”的声音，让人心烦意乱。"
    n "轻薄的羽绒被盖在身上却仿佛千斤重，压得人喘不过气。"
    #
    #zc
    n "望向天花板，偌大的房间，只能听见自己的呼吸声。"
    n "我想要大喊几声，打破这样的寂静。"
    n "房间隔音非常好，就算我现在大吼大叫，爸爸妈妈也不会听见。"
    n "又一次翻身，望向窗外的夜色，"
    n "霓虹灯早已熄灭，只有几盏路灯依旧在为回家的人们指引方向。"
    n "算了，不睡了。"
    nvl clear
    #zc
    show expression "bg_2/bg_2.png" at truecenter with dissolve
    hide expression "bg_2/bg_1.png" 
    n "翻身下床，地板上的热量传导到脚底，我这才惊觉，躺了这么久的被窝居然还没有地板温暖。"
    n "打开电脑，RGB灯光照亮了桌面，风扇转动发出的嗡鸣反而让我觉得有些安心。"
    n "平时在安静的环境里很快就能入睡，可是为什么脑袋里的那部分空白填补上过后，反而睡不着了呢？"
    n "是遗憾，是害怕，害怕遗忘，害怕失去。"
    n "「当太阳西升东落，降水倒流源头，雨滴重归于天，时针向后倒转的时候。」"
    n "梦野瞳是这样跟我说的。"
    n "可是就在不经意间，我回忆起来了失去的那段记忆，没有任何代价。"
    
    n "但我知道，凡事皆有代价。至于代价是什么，我无所谓，我只是害怕再次失去他，我不愿再次失去他。"
    nvl clear
    #show expression "bg_2/bg_3.png" at truecenter with dissolve
    hide expression "bg_2/bg_2.png"
    stop music fadeout 1.0
    #play music "<from 84 to 234>audio/dpx4.wav"  fadein 1.0 volume 0.3 
    
    show dpxmovie at center_zoom075 with dissolve
    show expression "bg_2/bgnvl.png" at topleft with dissolve
    n "「I loved you most...」"
    n "耳机里传来《极限竞速：地平线4》主题曲的旋律，我看向屏幕。"
    n "迈凯伦SENNA从阳光明媚的夏季缓缓驶入白雪皑皑的冬季，"
    n "从雨天走向晴天，从黄昏线迈向晨昏线，又再一次回到了那个明媚晃眼的夏日。"
    n "照这么说，我们已经经历过时光倒流了啊。她的话，真的能全信吗？"
    nvl clear
    #show expression "bg_2/bg_3.png" at truecenter with dissolve
    n "「I loved you most, I love you more now。」"
    n "按下手柄上的按钮，回到熟悉的山野小屋，眼前的景色让我倍感亲切。"
    n "在美国的生活算不上有趣，语言不通，文化不同，每天重复着两点一线的生活，枯燥，乏味。"
    n "唯一能称得上“慰籍”的就是学校放学还算早，在家能多玩一会电脑。但是在外国跟国内的队友打游戏，延迟简直惨不忍睹。"
    n "但是在外国跟国内的队友打游戏，延迟简直惨不忍睹。"
    n "在这种情况下，我喜欢上了单机游戏，不自觉地沉浸在第九艺术的世界中。"
    nvl clear
    #show expression "bg_2/bg_4.png" at truecenter with dissolve
    n "手指按下扳机，阿波罗IE的声浪将我的思绪拉回。"
    n "这台搭载了V12发动机的性能怪兽咆哮着，带着一往无前的勇气，飞驰在大不列颠的道路上。"
    n "只要一直向前就好了吧。既然不缺乏向前的勇气，那我还有什么好怕的呢？"
    n "就算世界将我们分开无数次，我也会再次找到你。"
    n "这样想着，手指按在扳机上的力量不由得加重了些，仪表盘的数字飞快飙升。"
    n "就这样一直奔跑下去吧。"
    
    #zc
    nvl clear
    hide expression "bg_2/bgnvl.png" with dissolve
    hide dpxmovie with dissolve
    stop music
    hide expression "bg_2/bg_2.png"
    #stop music fadeout 1.0
    
    show expression "bg_2/bg_5.png" at truecenter with dissolve
    play music "audio/days.wav"  fadein 1.0
    nvl clear
    #show expression "bg_2/bg_2.png" at truecenter with dissolve
    n "天刚微微亮，街道两侧的早餐店就已经忙碌了起来，"
    n "蒸腾的热气四处飘散，努力地让这座沉睡的城市从睡梦中苏醒。"
    n "时间还早，我伸了个懒腰，走向卫生间。"
    n "看着镜子中的自己，没有一丝熬夜过后的疲惫，反而像刚睡了个好觉一样。"
    nvl clear
    n "洗漱完，走进衣帽间挑选衣服，眼角余光落在衣柜角落的一件风衣上。"
    n "说起来，这还是上次回国跟陈默姐一起逛商场的时候买的。"
    n "「感觉会很适合你呢，一直都走的是可爱风，要不试试换个风格？帅气的半夏，我很期待哦。」"
    n "然后没几天就飞回美国去了，衣服就一直放在柜子里面。"
    n "既然看到了，那索性就试试吧。"
    show sbxsmile at lcg with dissolve
    n "这样想着，稍微搭配了一下，又从鞋柜里找到了一双骑士靴穿上。此时的镜子里，出现了一个与平时截然不同的自己。"
    n "这样来看，确实很有冰山美人的气质呢。"
    nvl clear
    n "在镜子前又转了两圈，越看越喜欢这套搭配。"
    bn "「苏半夏呀苏半夏，你怎么穿什么衣服都合适啊，你为什么长得这么好看呢。」"
    bn "「哼哼，那当然，谁叫我天生丽质呢。」"
    n "肚子不合时宜地发出抗议，将近12个小时没有吃东西，胃里的食物早就消化完了。"
    n "算了算了，不看了，先去过早，有什么事情先把肚子填饱了再说。"
    nvl clear
    hide sbxsmile fadeout 0.5
    hide expression "bg_2/bg_5.png" 
    show expression "bg_2/bg6.png" at truecenter with dissolve
    
    hide sbxsmile
    
    hide expression "bg_2/bg6.png" with dissolve
    show expression "bg_2/bg7.png" at truecenter with dissolve
    show expression "bg_2/bg_7.png" at truecenter 

    
    n "想念了许久的热干面，只有在进到肚子的那一刻才会感到满足。"
    n "顺滑的面条连同浓稠的芝麻酱被大口吸入嘴中，仓促咀嚼然后吞下，"
    n "再喝上一口热豆浆，整个身体都仿佛被这一口食物所滋润。"
    n "摊子上的人都被苏半夏这样豪迈的吃法所震惊，大爷大妈笑着看她这样大口吃面，直夸这姑娘伢好胃口。"
    n "我倒是不在乎这些，迅速扒完一碗后又要了一碗。"
    n "在美国吃的早饭连完全无法与热干面相提并论，害自己体重掉了快十多斤，我要把在美国没吃到的狠狠补回来。"
    nvl clear
    #hide expression "bg_2/bg6.png" 
    hide expression "bg_2/bg_7.png" with dissolve
    
    show expression "bg_2/bg_8.png" at truecenter with dissolve
    n "吃饱喝足，看了眼手机，时间还早。但不知怎的，突然想要坐公交去那里。这样一来，时间就刚刚好。"
    n "坐上公交，冬日的暖阳透过车窗洒在身上，看着窗外的风景慢慢掠过，总有些不一样的感觉。"
    n "平时坐地铁，大部分时间是手机不离手。虽然很快就会到目的地，但并没有什么真情实感，到地方了也就到了。"
    n "现在这样慢下来，在我作为半夏的人生中还是第一次。不用为了某些事情着急的感觉，真好。"
    n "公交车转了一个弯，窗外的高楼逐渐远离。冬日的江岸，总是缺了一点什么。"
    n "记忆中翠绿的芦苇荡，一直在脑海里挥之不去，"
    n "或者说，挥之不去的是那个夏天，是与他的回忆。"
    nvl clear
    n "但一切付出都是值得的。"
    n "世界如常运转。"
    n "颠簸的车厢，不由得让我产生了一丝困意，多想就这样伴随着冬日的阳光睡去。"
    n "嗯，就睡一小会，一小会就好。"
    hide expression "bg_2/bg7.png"
    window hide
    hide expression "bg_2/bg_8.png" with dissolve
    show expression "bg_2/bg_8.png" at truecenter with dissolve 
    hide expression "bg_2/bg_8.png" with dissolve 
    show expression "bg_2/bg_8.png" at truecenter with dissolve 
    hide expression "bg_2/bg_8.png" with dissolve 
    pause 3
    nvl clear
    show expression "bg_2/bg_8.png" with dissolve
    n "……"
    n "……"
    n "「喂，喂，小姑娘，醒一醒，到终点站了，该下车了。」"
    bn "「嗯，啊？我坐过站了吗？」"
    n "听到到了终点站，心中一惊，瞬间从睡梦中惊醒。"
    n "「嗯，到了，你怕不是睡过头了哦。」"
    n "看了一眼站点，突然松了一口气——还好要去的地方离终点站不是很远，只不过时间就不算充裕了……"
    bn "「师傅，这趟车一般是多久发一趟啊？」"
    n "「十分钟左右吧，哦，那边就有一辆，你去吧，下次在车上睡觉要注意着点。」"
    bn "「好的，谢谢师傅。」"
    nvl clear
    show expression "bg_2/bg_9.png" at truecenter with dissolve
    n "到目的地后，远远地就看见一个身影在四处张望。我一路小跑过去，抓住他的手腕。"
    bn "「不好意思，在路上睡着了。」"
    gn "「哇，吓我一跳！今天怎么换了一个穿衣风格，第一时间还没认出你。」"
    bn "「啊，嗯，朋友推荐的风格。」"
    n "我用手把被风吹散的头发捋到耳后。"
    gn "「可以，有那种冷酷黑道大小姐的感觉，很帅。」"
    bn "「咳咳，谢谢夸奖。」"
    gn "「那大小姐，今天准备去哪？」"
    hide expression "bg_2/bg_8.png"
    hide expression "bg_2/bg_9.png" with dissolve
    pause 1
    #jump ch3
    return

label ch3:
    nvl clear
    show expression "bg_3/bg_1n.png" at truecenter with dissolve
    show expression "bg_3/bg_1.png" at truecenter 
    n "印象里冬日的江城，总是被浓云裹得严实，远处的天际线也仿佛被压低了几分。"
    n "灰暗的天空，似是压抑着什么，让人喘不过气。"
    n "望着远处清晰的天际线失神，难得睡了个好觉，"
    n "今天也出乎意料的是个好天气，阳光照在身上暖洋洋的。心中的阴霾也随着昨天与苏半夏的相遇消散了几分。"
    bn "“不要走。”"
    n "听到少女的声音，我转过头去，撞入她的眼眸中。"
    
    n "那是多么美丽的一双眼睛啊，纯净得如同世界上最美好的珍宝。"
    n "眼底的那一丝悲伤烟消云散，取而代之的是即将喷薄而出的勇气与决心，无与伦比的坚定。"
    nvl clear
    n "为什么你的手这样温暖，为什么我舍不得放开呢。"
    n "如果能一直这样握住你的手，该有多好啊。"
    n "熟悉的感觉涌上心头，我能清晰地感受到胸膛中那颗心脏在疯狂地鼓动。"
    n "重逢的喜悦，寻回遗失珍宝的惊喜，心跳比记忆更先认出你来。"
    n "她就是夏天。"

    n "消失的那半个夏天回来了，可是我为什么还会有怅然若失的感觉呢，我应该高兴才对啊。"
    n "我，还忘了什么？"

    nvl clear
    show expression "bg_3/bg_2.png" at truecenter with dissolve
    show sbxsmile at lcg(1520) with dissolve
    n "只一眼，就注意到从人群中一闪而过的银白色头发的身影，"
    n "这才惊觉，已经到了约定的时间，我向着那道身影迎了上去。"
    bn "“不好意思，在路上睡着了。”"
    n "看着与昨日完全不同的装束，我打趣道：“感觉变了一个人，完全没认出你来。”"
    n "她把被风吹散的碎发往耳后捋了捋，“朋友推荐的风格。”然后目光才对向我，"
    bn "“今天，我们先去中山公园吧，听说那边的桃花开了，想去看看。”"
    n "她就这样说着，然后自顾自地向前走去。"
    hide sbxsmile
    nvl clear
    show expression "bg_3/bg_3.png" at truecenter with dissolve
    #树下图
    
    n "冬日的阳光把她的影子拉得很长，道路两旁的枯树更为身前的人影添上几分寂寥。"
    n "道路上的人们成双成对，穿着喜庆的衣服，说笑着庆祝着新年的到来。"
    n "街道上挂着火红色的灯笼，店铺大都贴上了春联，身穿着棕灰色大衣的她倒是显得与这喜庆的节日格格不入。"
    n "她走在我前面，冬日的寒风扯散她的长发。"
    n "我居然没理由地想起那年夏天，小沙坑里被拉拉扯扯的瘦弱身影。"
    n "心中的那股苦涩蔓延全身，脑海深处的声音催促着我，又要让她孤身一人吗？"
    n "去吧，上前去吧，这一次，一定要陪在她的身旁。"
    n "身体又一次抢在理性前做出行动，反应过来时苏半夏已经在我身侧。"
    nvl clear
    #展示一张半夏害羞图
    n "她侧过头，有些诧异地看向我。"
    bn "“诶，你怎么？”"
    n "我有些害羞地捂住脸，"
    gn "“看你一个人走怪孤单的，就想着，一起走……”"
    n "话音未落，温暖的触感攀上手掌，我明显感觉到了少女的身体在微微发抖，"
    n "看向她的时候她已经把头侧到另一侧。"
    gn "“怎么就突然牵上手了。”"
    n "少女没有回话，但一抹嫣红悄然爬上了她的侧脸，紧握住的手掌也更加用力。"
    n "就这样牵着她的手，两个人都很默契地没有再交流，沉默地走着这段路程。"
    show expression "bg_3/bg_4.png" at truecenter with dissolve
    nvl clear
    #湖边树林
    n "兴许是春节，往日热闹的公园突然冷清下来，路上看不见行人。"
    n "只剩几片枯叶挂在树枝上，随着寒风摇曳。"
    n "湖面上嬉闹的水鸟也不见了踪影，水面光滑得如同镜子一般，倒映着失去生机的公园。"
    gn "“感觉是被我们给包场了呢。”"
    n "苏半夏放开我的手，向前走了一步，转过身来看着我，笑着打趣道。"
    gn "“嗯，先不急着去看花吧，我还有一些地方想去。”"
    bn "“那走吧。”"
    nvl clear
    #长椅
    n "冬日的公园，真的很难让人有逛下去的欲望,凋敝的景色总会让人感受到无尽凄凉。"
    n "但苏半夏貌似很享受，看见某一条长椅，很自然地就坐了上去，十分放松地靠在椅背上。"
    n "伸出手，又突然收了回去，顺势拍了拍一旁的空位，示意我坐下。"
    n "我顺着她的想法坐下，坐在上面并没有什么特别的感觉，就是非常普通的公园椅。"
    gn "“顾韦，你有想起点什么吗？”"
    n "想起……什么？这是我，第一次来中山公园吧。"
    n "虽然在记忆里小时候父母带我来过，但也是很久以前的事情了。"
    nvl clear
    n "强烈的违和感，嗓子像是被鱼刺卡住一样，痛得我发不出声音，"
    n "后半句话被卡死在嗓子里，怎样都说不出口。"
    n "我来过这里，潜意识不断地暗示我，我跟很重要的人来过这里。"
    n "可是重要的人不就在眼前吗？"
    gn "“这样啊。”"
    n "苏半夏站起身，嘴唇微抿，眼底闪过一丝不易察觉的失落，但又很快恢复如初，"
    n "拍了拍身上的灰尘，“没事，去下一个地方吧。”"
    #喷泉
    nvl clear
    n "音乐喷泉，中山公园最著名的景点，平时这个时间，喷泉前应该会围满观景的人潮，"
    n "伴随着绚烂的灯光，十几米高的水柱喷涌而出，人群发出阵阵惊呼。"
    n "现在只能看到裸露在外的灰色水管和黑色射灯，往日盛景不再。"
    bn "“据说，在水柱喷射到最高的时候许愿，那个愿望就一定会实现。”"
    n "苏半夏的声音从身后传来，“你有许过什么愿望吗？”"
    gn "“没有，没许过，我甚至不知道有这一回事。”"
    n "我摇了摇头。"
    bn "“那，要不要现在许一个愿望。”"
    n "苏半夏像是想到了什么，"
    n "她突然兴奋起来，猛地靠近，眼里闪烁着激动的光芒，然后抓起我的手。"
    nvl clear
    bn "“可是，现在没有喷泉吧。”"
    gn "“哎呀，这有什么，试试嘛，说不定就实现了。”"
    n "身体完全无法抗拒，就如同本能一样，被苏半夏拉拽着，走到喷泉面前，然后模仿她闭上眼睛，双手合十。"
    nvl clear
    show expression "blank.png" at truecenter with dissolve
    
    n "不知道灵不灵验，但只要能够陪伴在半夏身边就好，再也不要分开了。"
    n "经历了多少苦难，只为寻回最初的她。"
    n "倘若世上真的有神明，就请实现我这样一个小小的愿望吧。"
    hide expression "blank.png" with dissolve
    n "睁开眼睛，苏半夏背着手站在面前，微笑着看着我。"
    nvl clear
    gn "“你……”"
    n "刚想开口，她伸出食指，抵上嘴唇，"
    gn "“嘘……”"
    n "她然后放下手指，牵住我的手，"
    gn "“说出来就不灵了。”"
    n "在这萧瑟的季节，万物凋敝，可她却在我的心底埋下一粒种子。"
    n "少女散发的光芒是如此温暖，在这座冰冷的城市中，无声地伴我同行。"
    n "我翻转手心，与她十指相扣，"
    gn "“没事的，神明大人会实现我这微不足道的愿望的。”"
    bn "“嗯，我们的愿望一定会实现的。”"
    n "她微微颔首，"
    bn "“那走吧，去最后一个地方。”"
    nvl clear
    #破旧红砖
    n "藏在公园角落的墙早已被时光侵蚀得破败不堪，大块红砖裸露在外，"
    n "湿滑的青苔在其上疯狂蔓延，蚕食着破碎的砖缝，只能从几近脱落的小块墙皮辨认出它曾经的色彩。"
    n "她牵着我的手走进半膝高的杂草丛，一深一浅地踩着脚下的土地。"
    n "望着近处破败不堪的砖墙，我不禁怀疑，这里真的会有盛开的桃花吗？"
    n "剥开杂乱的枯枝，走近墙内的世界。"
    n "没有想象中的花团锦簇，整个世界只剩下一片荒芜。"
    n "我看向苏半夏，她倒是没什么反应，"
    n "小心翼翼地走过去，生怕踩到了脚下枯萎的花丛。"
    nvl clear
    n "她伸出手，指尖摩挲着含苞待放的花骨朵，"
    n "低头像是在思考些什么，银色的发丝顺着她的额头垂下。"
    gn "“走吧，看起来还没有到开花的时候。”"
    n "她抬头伸手，遮住冬日的阳光，仿佛要把它抓入手中。"
    n "金色的发饰在阳光下闪烁着耀眼的光芒，嘴角带起浅浅的弧度，又很快抚平，"
    n "喉间滚动着像是要说些什么，未成型的话语却随着一声叹息，"
    n "化作白雾消散在风中，那些苦涩也被生生咽下。"
    nvl clear
    n "苏半夏的眼睛失去了往日的活力，变得浑浊不堪，像一具行尸走肉朝着来时的小径走去，"
    n "突然一脚踩空，身体向一侧倒去。我快步上前，将少女搂入怀中。"
    gn "“顾韦……我稍微有点累了，可以在你身上躺一会吗？”"
    n "她的话语带着哭腔，惹人怜爱。心脏仿佛被铁锤重击，敲得人生疼。"
    bn "“好。”"
    n "我背着她走到一条废弃的长椅边，身后传来熟悉的感觉，"
    n "很好闻的味道。很清新的薄荷香水，是苏半夏常用的，我记得这个气味。"
    n "夏日的味道。"
    nvl clear
    n "最后留在记忆深处的总是些虚无缥缈的东西，"
    n "就像你记住一个人往往不是因为她的美，很久之后你连她的样子都忘记了，"
    n "可偶然在人流如织的街头闻到她惯用的香水味，你在惊悚中下意识地回过头去，"
    n "却只看见万千记忆的泡影。"
    n "曾经，她也像这样躺在我的腿上。"
    n "层层叠叠的蓝粉色花瓣交织出绚烂的海，"
    n "那一抹浅白好似浪花打在礁石上的泡沫，又好似晚霞坠落人间。"
    n "我们曾在无尽夏海中入眠。"
    nvl clear
    #无尽夏花
    gn "‘顾韦，你知道吗，无尽夏的花语是即使短暂分别，我们终将会重逢。’"
    n "她抢走我手中的汽水，猛吸一大口。"
    gn "‘不要，还是你的那一杯好喝。’"
    n "燥热的夏，只要一杯柠檬汽水就可以缓解。"
    n "但炽烈的情感呢？"
    gn "‘记好了哦，我最喜欢这种香水了。不仅好闻，而且，只需要一瞬间，就能让人记住这个味道。’"
    gn "‘嘻嘻，下次你给我买哦。’"
    n "那就取一株薄荷，将它泡进夏天。"
    n "又像这样泪湿眼眶，追随着你“晚安”的序言。"
    nvl clear
    bn "‘如果，有一天，我不在了，你会怎么样？’"
    bn "‘我知道你不是我想象出来的。’"
    bn "‘是真实存在的。’"
    bn "‘是真实存在的，喜欢着我的人。’"
    bn "‘爱，只要一瞬就够了。’"
    gn "‘我爱你，我想和你永远在一起。’"
    gn "‘在满天星斗下，我们许下这样的愿望。’"
    bn "‘这一次，真的再见了。’"
    nvl clear
    n "为什么，在放手的时刻，眼泪会掉落呢。"
    n "记忆碎片在我眼前划过，一幕一幕闪着刺痛我。"
    n "欢笑与无言，如此回望平淡的时间。"
    n "剩下的那一半夏，是我与苏半夏的回忆，仅仅是苏半夏，不是夏天。"
    n "一滴泪水划过脸庞，我想起来了，那个不存在的夏天。"
    n "那一段不存在的回忆。"
    nvl clear
    bn "“顾韦，你哭了？”"
    n "苏半夏伸出手，替我擦拭着脸上的泪水。"
    gn "“半夏……”"
    bn "“嗯？我在。”"
    gn "“无论顺境还是逆境，无论贫穷还是富贵，无论健康还是疾病，”"
    gn "“我都会与你分担寒潮、风雷、霹雳，也会与你分享雾霭、流岚、虹霓。”"
    gn "“我以我的生命发誓，苏半夏将会是我生命里永远的主角。”"
    gn "“直至死亡，将你我分开。你，愿意吗？””"
    bn "“什么啊，你都在说些什么啊……”"
    n "苏半夏挣扎着坐了起来，双手托住我的脸，"
    nvl clear
    bn "“你知道你在说什么吗？”"
    gn "“我知道。”"
    bn "“我们才认识第二天吧，你就说这样的话。”"
    gn "“哪怕这个世界走向终结，你也是我无法忘却的人。”"
    n "我轻轻地抱住半夏，我能感受到她胸膛中的炽热，能感受到她的彷徨。"
    gn "“所以，你愿意吗。”"
    nvl clear
    n "她的双手无力地垂落下去，而后又猛地发力用力的挣脱出我的怀抱。"
    bn "“不行的……”"
    n "她晃着自己的脑袋，银白色的发丝随着寒风越飘越远。"
    n "我只是一个……不值得被爱的怪物”"
    n "我把那一缕发丝捧入手心，再次将半夏搂入怀中，像是握住了上天赐予我的稀世珍宝。"
    n "将这一缕银丝捋进发梢，我缓缓的抚摸着她的背。"
    gn "“可是我只有这一个夏天，往后的夏天就不会存在了。”"
    n "我停顿了一下，身体微微前倾，像是要倒在半夏的怀里一样。"
    n "我抓起她垂落的手，贴在胸膛上，心脏正在疯狂的鼓动。"
    nvl clear
    gn "“但是呢，你要是想要我的夏天的话，我便赠予你罢，”"
    gn "“往后余生，我的生命里，只会剩下春秋冬……”"
    nvl clear
    bn "“我不要，我不要……呜呜呜，我不要!”"
    n "半夏抽泣着，双手不停的捶打着我的胸口，像是孩童赌气一般。"
    bn "“我才不要你的夏天，呜……我只要你，咳咳……我只要你就够了。”"
    n "我慢慢凑近半夏的脸，看清她泛着水光的红眼眶，"
    n "一阵酸涩从胸口蔓延到手掌，迫使我收紧手臂和她贴得更密。"
    n "然后抵住熟悉的柔软的嘴唇，小心翼翼撬开。"
    nvl clear
    n "半夏的热情出乎我意料，我还只是轻轻舔了舔，她居然主动用舌尖来勾。"
    n "女孩不稳的喘息混着啧啧水声萦绕在耳畔，我可能也没多淡定，一味地配合着她加深，纠缠。"
    n "直到两瓣嘴唇都变得湿漉漉，我想应该停下了。"
    n "她却两手搂上我的脖子把我按住，仿佛要把自己整个献出来，"
    n "明明气息抖得越来越厉害了。想要失去掌控自己的能力，想要窒息吗？"
    n "无力的我别无办法宽慰她，只能如她所愿。"
    n "直到半夏连手上的力气都没有了，慢慢放松，我们的唇瓣才分开。"
    n "她两颊憋得通红，但还是轻轻的捧起我的脸，凑近我耳边呢喃，"
    bn "“我愿意。”"
    


    






    


    