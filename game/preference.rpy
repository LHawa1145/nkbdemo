init python:
    #config.font_replacement_map["SourceHanSansSC-Regular-2.otf", False, True] = ("SourceHanSansSC-Regular-2.otf", False, False)
    style.say_dialogue.color = "#000000"
    style.say_dialogue.outlines = [(1, "#ffffff", 0, 0)]
    #一个可能不怎么好看的文字外框？

init python:
    style.say_dialogue.font = "wryh.ttf"
    style.nvl_dialogue.font = "wryh.ttf"
    style.nvl_dialogue.size = 32
    #调节字体文件和字体大小

screen quitscreen():
    zorder 200
    modal True
    add Solid("#000") at fade_to_quit
    timer 1.0 action Quit(confirm=False)
transform fade_to_quit:
    alpha 0.0
    linear 1.0 alpha 1.0
#退出时渐黑退出


init python:
    config.keymap['game_menu'] = ['K_ESCAPE' ]
    
    config.rollback_enabled = False
    #拒绝了右键调用菜单和滚轮回滚

    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['debug_voicing'] = []

    #一些奇怪的机器朗读禁用



    #下面这里我用了一种取巧方法，把help界面改成跳转进history
    config.keymap['help'] = ["mousedown_4"]
    
    
    config.keymap['hide_windows'] = [ 'mouseup_3' ]
    
    if 'K_h' in config.keymap['hide_windows']:
        config.keymap['hide_windows'].remove('K_h')
    #加入了右键隐藏文本

init python:
    config.keymap['dismiss'] = [ 'mouseup_1', 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'joy_dismiss', 'joy_fire1', 'repeat_mouseup_1', 'mousedown_5' ]
    #表面很长但实际上只加入了滚轮过剧情


init python:
    #config.keymap['history'] = [ 'mousedown_4' ]
    config.keymap['rollback'] = []
    #拒绝回滚


init:
    # 设置文本框隐藏和显示的渐变动画
    define config.window_hide_transition = dissolve
    define config.window_show_transition = dissolve

init:
    transform scale05:
        zoom 0.5
        #大小0.5倍

    transform truecenter:
        xalign 0.5
        yalign 0.5
        #居中
    
    
init python:
    #人+说话
    def swv(who, what, voice_file):
        renpy.sound.play(voice_file)
        renpy.say(who, what)
    #这个好像用不上了



init:
    transform topleft:
        xalign 0.0
        yalign 0.0
    
    transform lcg(x=1520):
        align(0.5,0.5)
        zoom 0.4
        pos(x,700)
    #这个是显示角色图用，缩放0.4倍，xpos为1520刚好能比较舒服的显示人物图



init:
    transform center_zoom075:
        xalign 0.5
        yalign 0.5
        zoom 0.75
        #疑似也废弃了