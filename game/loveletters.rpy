screen loveletters:
    add "images/bg dashutsu.png"
    add "images/kaorus drawer.png"
    imagebutton:
        xpos 260
        ypos 125
        idle "kaoru_closedletter1.png"
        action Jump("kaoru_letter1")
        focus_mask True
    imagebutton:
        xpos 160
        ypos 310
        idle "kaoru_crumpledpaper.png"
        action Jump("kaoru_letter5")
        focus_mask True
    imagebutton:
        xpos 220
        ypos 250
        idle "kaoru_closedletter2.png"
        action Jump("kaoru_letter2")
        focus_mask True
    imagebutton:
        xpos 540
        ypos 235
        idle "kaoru_crumpledpaper.png"
        action Jump("kaoru_letter6")
        focus_mask True
    imagebutton:
        xpos 650
        ypos 100
        idle "kaoru_closedletter3.png"
        action Jump("kaoru_letter3")
        focus_mask True
    imagebutton:
        xpos 880
        ypos 425
        idle "kaoru_crumpledpaper.png"
        action Jump("kaoru_letter7")
        focus_mask True
    imagebutton:
        xpos 450
        ypos 300
        idle "kaoru_closedletter4.png"
        action Jump("kaoru_letter4")
        focus_mask True
    imagebutton:
        xpos 910
        ypos 25
        idle "kaoru_crumpledpaper.png"
        action Jump("kaoru_letter8")
        focus_mask True
    imagebutton:
        xpos 410
        ypos 20
        idle "kaoru_crumpledpaper.png"
        action Jump("kaoru_letter9")
        focus_mask True
    imagebutton:
        xpos 830
        ypos 10
        idle "kaoru_crumpledpaper.png"
        action Jump("kaoru_letter0")
        focus_mask True
    imagebutton:
        xpos 210
        ypos 60
        idle "kaoru_crumpledpaper.png"
        action Jump("kaorus_note")
        focus_mask True

    imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom6") activate_sound "audio/choice_click.wav"
