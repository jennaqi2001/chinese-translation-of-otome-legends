image hr1_sticker:
    "images/hr1_sticker1.png"
    .45
    "images/hr1_sticker2.png"
    .45
    repeat

image hnxt_background:
    "images/hnxt_background1.png"
    .45
    "images/hnxt_background2.png"
    .45
    repeat
    
screen hr1_minigame():
    add "images/hr1_background.png"
    add "hr1_sticker"
    imagebutton auto "images/hr1_item1_%s.png" xpos 400 ypos 500 action Jump("hr1_item1") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr1_item2_%s.png" xpos 722 ypos 581 action Jump("hr1_item2") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr1_item3_%s.png" xpos 240 ypos 540 action Jump("hr1_item3") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr1_item4_%s.png" xpos 634 ypos 124 action Jump("hnxt1") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr1_item5_%s.png" xpos 445 ypos 200 action Jump("hr1_item5") activate_sound "audio/choice_click.wav"

screen hr1_minigame_rope():
    add "images/hr1_background.png"
    add "hr1_sticker"
    imagebutton auto "images/hr1_item1_%s.png" xpos 400 ypos 500 action Jump("hr1_item1") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr1_item3_%s.png" xpos 240 ypos 540 action Jump("hr1_item3") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr1_item4_%s.png" xpos 634 ypos 124 action Jump("hnxt1") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr1_item5_%s.png" xpos 445 ypos 200 action Jump("hr1_item5") activate_sound "audio/choice_click.wav"

screen hr2_minigame():
    add "images/hr2_background.png"
    imagebutton auto "images/hr2_item1_%s.png" xpos 110 ypos 277 action Jump("hr2a") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr2_item2_%s.png" xpos 540 ypos 280 action Jump("hr2b") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr2_item3_%s.png" xpos 837 ypos 290 action Jump("hr3") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hreturn_%s.png" xpos 1045 ypos 45 action Jump("hr1") activate_sound "audio/choice_click.wav"

screen hr2a_minigame():
    add "images/hr2a_background.png"
    imagebutton auto "images/hr2a_item1_%s.png" xpos 920 ypos 300 action Jump("hr2a_item1") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr2a_item2_%s.png" xpos 1035 ypos 360 action Jump("hr2a_item2") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr2a_item3_%s.png" xpos 0 ypos 295 action Jump("hr2a_item3") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hr2a_item4_%s.png" xpos 647 ypos 434 action Jump("hr2a_item4") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hreturn_%s.png" xpos 1080 ypos 27 action Jump("hr2") activate_sound "audio/choice_click.wav"

screen hr2b_minigame():
    add "images/hr2b_background.png"
    imagebutton auto "images/hr2b_item1_%s.png" xpos 108 ypos 320 action Jump("hr2b_item1") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hreturn_%s.png" xpos 1090 ypos 27 action Jump("hr2") activate_sound "audio/choice_click.wav"

screen hnxt1_minigame():
    add "hnxt_background"
    imagebutton auto "images/hnxt_item1_%s.png" xpos 488 ypos 265 action Jump("hr2") activate_sound "audio/choice_click.wav"

screen hr3_minigame():
    add "images/hr3_background.png"
    imagebutton auto "images/hr3_item1_%s.png" xpos 544 ypos 184 action Jump("hr3_item1") activate_sound "audio/choice_click.wav"
    imagebutton auto "images/hreturn_%s.png" xpos 1045 ypos 45 action Jump("hr1") activate_sound "audio/choice_click.wav"
