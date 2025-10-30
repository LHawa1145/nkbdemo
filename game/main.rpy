screen main_menu():
    $ renpy.start_predict_screen("gallery")
    tag menu
    
    add "gui/main_menu.png"  

    #save
    imagebutton:
        idle "images/mainmenu/start_btn_idle.png"   
        hover "images/mainmenu/start_btn_hover.png" 
        
        xpos 0.8
        ypos 0.4
        anchor (0.5, 0.5)
        action [Stop("music", fadeout=1.0), Start()]  # 进入游戏
        hover_sound "audio/hover.wav"

    #load
    imagebutton:
        idle "images/mainmenu/load_btn_idle.png"
        hover "images/mainmenu/load_btn_hover.png"
        
        xpos 0.8
        ypos 0.5
        anchor (0.5, 0.5)
        action ShowMenu('load')
        hover_sound "audio/hover.wav"

    #画廊
    imagebutton:
        idle "images/mainmenu/extra_idle.png"
        hover "images/mainmenu/extra_hover.png"

        xpos 0.8
        ypos 0.6
        anchor(0.5,0.5)
        action ShowMenu('gallery')
        hover_sound "audio/hover.wav"

    #章节
    # imagebutton:
    #     idle "images/mainmenu/chapter_btn_idle.png"
    #     hover "images/mainmenu/chapter_btn_hover.png"
    #     xpos 0.8
    #     ypos 0.5
    #     anchor(0.5,0.5)
    #     action ShowMenu('my_chapter')
    #     hover_sound "audio/hover.wav"
    #已废弃，凉鸢说没必要弄这个，好吧，亏我还写出来了

    #设置
    imagebutton:
        idle "images/mainmenu/pre_btn_idle.png"
        hover "images/mainmenu/pre_btn_hover.png"
        
        xpos 0.8
        ypos 0.7
        anchor(0.5,0.5)
        action ShowMenu('my_sound')
        hover_sound "audio/hover.wav"

    #退出
    imagebutton:
        idle "images/mainmenu/exit_btn_idle.png"
        hover "images/mainmenu/exit_btn_hover.png"

        pos(0.8,0.8)
        anchor(0.5,0.5)
        action ShowMenu("quitscreen")
        hover_sound "audio/hover.wav"
    textbutton("制作者的话及感谢名单（暂定界面）"):
        pos(0.8,0.88)
        anchor(0.5,0.5)
        action ShowMenu("lhandlysay")

screen lhandlysay():
    add "images/blank.png"
    tag menu
    text "哈喽各位玩家，首先我LH代表本《恋爱绮谭》二创制作组对于所有参与测试debug的玩家表示由衷的感谢！\n在此特别感谢：浅色回忆，恋爱绮谭系列的剧本主编；\n南城凉鸢，本二创剧情负责人；\n小萌新，夜莺小姐，冥王星植树僧人，Feif等群友，提供了许多精神和物质上的帮助;\n黑凤梨老师，章鱼老师，烈林凤老师，浅唱老师，龙叔老师，老马老师等各位renpy前辈，为我的代码部分提供了很大的帮助；\n雪枫，arior（ac），参与了第一规模demo测试，提出了许多宝贵的建议；\n以及所有热爱恋爱绮谭的玩家们。":
        xpos 0.5
        ypos 0.5
        anchor (0.5,0.5)
    

    imagebutton:
        idle "images/mainmenu/return_idle.png"
        hover "images/mainmenu/return_hover.png"
        xpos 0.85
        ypos 0.85
        anchor(0.5,0.5)
        action ShowMenu("main_menu")







screen my_sound():#音量设置和文本设置，也是进设置的默认界面
    add "gui/main_menu.png"
    tag menu
    add "gui/pref_bg.png"
    vbox:
        xpos 0.25
        ypos 0.3
        anchor(0.5,0)
        spacing 100
        imagebutton:
            idle "images/mainmenu/sound_hover.png"
            hover "images/mainmenu/sound_hover.png"
        
            anchor(0.5,0.5)
            
        imagebutton:
            idle "images/mainmenu/text_idle.png"
            hover "images/mainmenu/text_hover.png"
        
            anchor(0.5,0.5)
            action ShowMenu("my_say")
    vbox:
        xpos 0.45
        ypos 0.25
        anchor (0.5, 0.)
        spacing 30
        
        label "{font=wryh.ttf}音量设置{/font}" 
        hbox:
            text "{font=wryh.ttf}音乐音量{/font}" 
            bar value Preference("music volume") xsize 400 ysize 38
        hbox:
            text "{font=wryh.ttf}音效音量{/font}" 
            bar value Preference("sfx volume") xsize 400 ysize 38
        hbox:
            text "{font=wryh.ttf}语音音量{/font}" 
            bar value Preference("voice volume") xsize 400 ysize 38
        text ""
        label "{font=wryh.ttf}文本设置{/font}" 
        hbox:
            text "{font=wryh.ttf}文字速度{/font}" 
            bar value Preference("text speed") xsize 400 ysize 38
        hbox:
            text "{font=wryh.ttf}自动播放速度{/font}" 
            bar value Preference("auto-forward time") xsize 400 ysize 38
    textbutton "gongxi" action Preference("display",0.5):
        xpos 0.625
        ypos 0.55
        anchor(0.5,0.5)
    imagebutton:
        idle "images/mainmenu/return_idle.png"
        hover "images/mainmenu/return_hover.png"
        xpos 0.85
        ypos 0.85
        anchor(0.5,0.5)
        action ShowMenu("main_menu")


screen my_say():#快进界面，一个子界面
    add "gui/main_menu.png"
    tag menu
    add "gui/pref_bg.png"
    vbox:
        xpos 0.25
        ypos 0.3
        anchor(0.5,0)
        spacing 100
        imagebutton:
            idle "images/mainmenu/sound_idle.png"
            hover "images/mainmenu/sound_hover.png"
        
            anchor(0.5,0.5)
            action ShowMenu("my_sound")
        imagebutton:
            idle "images/mainmenu/text_hover.png"
            hover "images/mainmenu/text_hover.png"
        
            anchor(0.5,0.5)
            
    vbox:
        xpos 0.434
        ypos 0.4
        anchor (0.5, 0.5)
        spacing 30

        vbox:
            # style_prefix "check"
            label _("{font=wryh.ttf}快进{/font}")
            
            text "{font=wryh.ttf}未读文本（建议第一次游玩时关闭）{/font}"
            
            text "{font=wryh.ttf}选项后继续{/font}"
            
            text "{font=wryh.ttf}忽略转场（建议关闭）{/font}"
    imagebutton:
        idle "images/mainmenu/k_idle.png" 
        hover "images/mainmenu/k_idlel.png" 
        selected_idle "images/mainmenu/k_hover.png"
        selected_hover "images/mainmenu/k_hoverl.png"
        action Preference("skip", "toggle")
        pos(0.57,0.375)

    imagebutton:
        idle "images/mainmenu/k_idle.png" 
        hover "images/mainmenu/k_idlel.png" 
        selected_idle "images/mainmenu/k_hover.png"
        selected_hover "images/mainmenu/k_hoverl.png"
        action Preference("after choices", "toggle")
        pos(0.387,0.415)


    imagebutton:
        idle "images/mainmenu/k_idle.png" 
        hover "images/mainmenu/k_idlel.png" 
        selected_idle "images/mainmenu/k_hover.png"
        selected_hover "images/mainmenu/k_hoverl.png"   
        action InvertSelected(Preference("transitions", "toggle"))
        pos(0.468,0.457)
    #上面三个imagebutton依次对应未读，选项后继续和转场是否被选择

    imagebutton:
        idle "images/mainmenu/return_idle.png"
        hover "images/mainmenu/return_hover.png"
        xpos 0.85
        ypos 0.85
        anchor(0.5,0.5)
        action ShowMenu("main_menu")