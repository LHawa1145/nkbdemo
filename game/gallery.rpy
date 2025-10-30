image cg_1_1 = "cg/CG1 1.png"
image cg_2_1 = "cg/CG2 1.png"
image cg_3_1 = "cg/CG3 1.png"
image cg_4_1 = "cg/CG4 1.png"
image cg_5_1 = "cg/CG5 1.png"
image cg_6_1 = "cg/CG6 1.png"
init python:
    cg_list = ["cg_1", "cg_2", "cg_3", "cg_4", "cg_5", "cg_6"]
screen gallery():
    predict True
    tag menu
    add "gui/gallery/bg.png"
    imagebutton:
        pos(1800,880)
        auto "images/mainmenu/return_%s.png"
        action Return()
    frame:
        background None
        align(0.5,0.5)
        xysize(400,237)
        has grid 3 2
        spacing 20
        align(0.5,0.5)
        for i in range(6):
            $ thumb_name = cg_list[i] + "_1"
            imagebutton:
                idle Transform(thumb_name,zoom = 0.15)
                hover Transform(thumb_name,zoom = 0.17)
                xalign 0.5
                yalign 0.5
                action Show("cg_viewer", cg_index=i)
screen cg_viewer(cg_index):
    modal True
    zorder 100
    key "mouseup_1" action Hide("cg_viewer")
    # if cg_index < len(cg_list) - 1:
        #key "mouseup_1" action [Hide("cg_viewer"), Show("cg_viewer", cg_index=cg_index+1)]
    # else:
        # 如果是最后一张，左键关闭
    
    add cg_list[cg_index] + "_1" zoom 0.5 align(0.5,0.5) 
    
