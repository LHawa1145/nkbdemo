screen help():
    use history
                
                    
#default history_bar_pos = renpy.display.behavior.Adjustment()
screen history():
    tag menu
    predict False
    add "gui/history_bg.png"
    frame:
        style "history_frame_style"
        frame:
            style "history_window_frame_style"

            vpgrid id "history_list":
                cols 1
                yinitial 1.0
                mousewheel True
                draggable True
                pagekeys True
                yadjustment history_bar_pos


                side_xfill True
                for h in _history_list:
                
                    window:
                        background None
                        ysize 100
                        if h.who:
                            label h.who:
                                xoffset 100
                                substitute False

                            
                                if "color" in h.who_args:
                                    text_color h.who_args["color"]
                        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                        text what:
                            color "#000000"
                            substitute False
        #这里照抄源代码，没啥参考价值倒是
                    
    vbox:
        
        align (0.95,0.5)
        vbar:
            # xsize 17
            # ysize 543
            # base_bar "gui/history_bar.png" 
            
            # thumb "gui/thumb.png" 
            # thumb_offset 20
        
            value YScrollValue("history_list")


            align (0.5, 0.5)
            xysize (17, 630)
            #value Preference("music volume")
            left_bar Fixed(Frame("gui/thumbk.png", ysize=630, align=(0.5, 0.5)))
            right_bar Fixed(Frame("gui/thumbk.png", ysize=630, align=(0.5, 0.5)))    
            thumb Fixed(Frame("gui/thumbk.png", xysize=(40,40), align=(0.5, 0.5)))
            thumb_offset 1000
            #这里本来想做进度条，但是thumb似乎出问题了，好吧



    imagebutton:
        idle "images/mainmenu/return_idle.png"
        hover "images/mainmenu/return_hover.png"
        xpos 0.9
        ypos 0.85
        anchor(0.5,0.5)
        action Return()
style history_frame_style:
    left_padding 200
    right_padding 0
style history_window_frame_style:
    top_padding 185
    bottom_padding 185
    xfill True

#重做的历史界面，现在正在思考如何以一种舒服的方式引入进去，而且还有句子太长出框的bug，拖动条本身想做也给删了（有bug），哎没救了这人








