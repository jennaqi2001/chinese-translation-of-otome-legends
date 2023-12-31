screen win_screen():
    add "senpaidrawings_video"
    add "images/youwin.png"
    imagebutton auto "images/gameretry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("doodlegame") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
    imagebutton auto "images/gamecontinue_%s.png" xpos 0 ypos 0 focus_mask True action Jump("backtoclass2") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen lose_screen():
    add "images/white.png"
    add "images/youlose.png"
    imagebutton auto "images/gameretry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("doodlegame") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen rwin_screen():
    add "threeleggedrace_video"
    add "images/youwin.png"
    imagebutton auto "images/gameretry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("race") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
    imagebutton auto "images/gamecontinue_%s.png" xpos 0 ypos 0 focus_mask True action Jump("backtoclass1") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen rlose_screen():
    add "threeleggedrace_video"
    add "images/youlose.png"
    imagebutton auto "images/gameretry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("race") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen breathe1():
    add "images/breathe.png"
    add "beating_heart"
    imagebutton auto "images/breathe_%s.png" xpos 0 ypos 0 focus_mask True action Jump("hallrun_continue_1a") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen breathe2():
    add "images/breathe.png"
    add "beating_heart"
    imagebutton auto "images/breathe_%s.png" xpos 0 ypos 0 focus_mask True action Jump("hallrun_continue_2a") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen hide1():
    add "images/breathe.png"
    add "beating_heart"
    imagebutton auto "images/breathe_%s.png" xpos 0 ypos 0 focus_mask True action Jump("haibiru_continue1") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen hide2():
    add "images/breathe.png"
    add "beating_heart"
    imagebutton auto "images/breathe_%s.png" xpos 0 ypos 0 focus_mask True action Jump("haibiru_continue2") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"


image beating_heart:
    "beating_heart1.png"
    .20
    "beating_heart2.png"
    .20
    "beating_heart3.png"
    .20
    "beating_heart2.png"
    .20
    repeat

image threeleggedrace_video = Movie(size = (1280,720), channel = "movie", play = "images/race.ogv", loop = True)
image senpaidrawings_video = Movie(size = (1280, 720), channel = "movie", play = "images/senpaidrawings_video.ogv", loop = True)

default points=50
default plus=5
default max_point=1000
default clicked = True

init:
    image draw1 = "doodle1.png"
    image draw2 = "doodle2.png"
    image draw3 = "doodle3.png"
    image draw4 = "doodle4.png"
    image write:
        "images/hand1.png"
        .45
        "images/hand2.png"
        .45
        repeat

screen clicker():
    modal True
    timer .5 repeat True action [If(points <= 0, true=Jump("lost"), false = SetVariable("points", points - 3))]
    add "images/notebook.png"
    add "write"
    button:
        text "[points] / [max_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("clicked", True), If(points >= max_point, true=Jump("win"), false=SetVariable("points", points + plus)), Play("sound", "audio/write.wav")] #add click.ogg file to 'game' folder
        vbar value StaticValue(points, max_point) xalign 1.0 yalign 1.0
    if points>=900:
        add "draw4" xalign 0 yalign 0
    elif points>=700:
        add "draw3" xalign 0 yalign 0
    elif points>=600:
        add "draw2" xalign 0 yalign 0
    elif points >=400:
        add "draw1" xalign 0 yalign 0
    if persistent.clicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("backtoclass2") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"



default rpoints=50
default rplus=4
default rmax_point=800
default rclicked = True

init:
    image race1:
        "images/track_minigame1A.png"
        .45
        "images/track_minigame2A.png"
        .45
        repeat
    image race2:
        "images/track_minigame1B.png"
        .45
        "images/track_minigame2B.png"
        .45
        repeat
    image race3:
        "images/track_minigame1C.png"
        .45
        "images/track_minigame2C.png"
        .45
        repeat
    image race4:
        "images/track_minigame1D.png"
        .45
        "images/track_minigame2D.png"
        .45
        repeat

screen rclicker():
    modal True
    timer .5 repeat True action [If(rpoints <= 0, true=Jump("rlost"), false = SetVariable("rpoints", rpoints - 2))]
    add "images/bg track_minigame.png"
    button:
        text "[rpoints] / [rmax_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("rclicked", True), If(rpoints >= rmax_point, true=Jump("rwin"), false=SetVariable("rpoints", rpoints + rplus)), Play("sound", "audio/write.wav")] #add click.ogg file to 'game' folder
        vbar value StaticValue(rpoints, rmax_point) xalign 1.0 yalign 1.0
    if rpoints>=500:
        add "race3" xalign 0 yalign 0
    elif rpoints>=300:
        add "race2" xalign 0 yalign 0
    else:
        add "race1" xalign 0 yalign 0
    if persistent.rclicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("backtoclass1") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

default h1points=50
default h1plus=4
default h1max_point=200
default h1clicked = True

init:
    image hallbg:
        "images/hallway_bg1.png"
        .05
        "images/hallway_bg2.png"
        .05
        "images/hallway_bg3.png"
        .05
        "images/hallway_bg4.png"
        .05
        "images/hallway_bg5.png"
        .05
        "images/hallway_bg6.png"
        .05
        "images/hallway_bg7.png"
        .05
        "images/hallway_bg8.png"
        .05
        "images/hallway_bg9.png"
        .05
        "images/hallway_bg10.png"
        .05
        "images/hallway_bg11.png"
        .05
        "images/hallway_bg12.png"
        .05
        "images/hallway_bg13.png"
        .05
        "images/hallway_bg14.png"
        .05
        repeat

    image hallrun:
        "images/hallway_run1.png"
        .12
        "images/hallway_run2.png"
        .08
        "images/hallway_run3.png"
        .08
        "images/hallway_run4.png"
        .08
        "images/hallway_run5.png"
        .12
        "images/hallway_run4.png"
        .08
        "images/hallway_run3.png"
        .08
        "images/hallway_run2.png"
        .08
        repeat

    image haibiru_bg:
        "images/haibiru_bg1.png"
        .05
        "images/haibiru_bg2.png"
        .05
        "images/haibiru_bg3.png"
        .05
        "images/haibiru_bg4.png"
        .05
        "images/haibiru_bg5.png"
        .05
        "images/haibiru_bg6.png"
        .05
        "images/haibiru_bg7.png"
        .05
        "images/haibiru_bg8.png"
        .05
        "images/haibiru_bg9.png"
        .05
        "images/haibiru_bg10.png"
        .05
        "images/haibiru_bg11.png"
        .05
        "images/haibiru_bg12.png"
        .05
        "images/haibiru_bg13.png"
        .05
        repeat

    image haibiru_run:
        "images/haibiru_run1.png"
        .12
        "images/haibiru_run2.png"
        .08
        "images/haibiru_run3.png"
        .08
        "images/haibiru_run4.png"
        .08
        "images/haibiru_run5.png"
        .12
        "images/haibiru_run4.png"
        .08
        "images/haibiru_run3.png"
        .08
        "images/haibiru_run2.png"
        .08
        repeat


screen h1clicker():
    modal True
    timer .5 repeat True action [If(h1points <= 0, true=Jump("h1lost"), false = SetVariable("h1points", h1points - 4))]
    add "hallbg"
    add "hallrun"
    add "images/round1.png"
    button:
        text "[h1points] / [h1max_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("h1clicked", True), If(h1points >= h1max_point, true=Jump("h1win"), false=SetVariable("h1points", h1points + h1plus)), Play("sound", "audio/menu_pop.mp3")] #add click.ogg file to 'game' folder
        vbar value StaticValue(h1points, h1max_point) xalign 1.0 yalign 1.0
    if persistent.hclicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("hallrun_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

default h2points=50
default h2plus=8
default h2max_point=300
default h2clicked = True

screen h2clicker():
    modal True
    timer .5 repeat True action [If(h2points <= 0, true=Jump("h1lost"), false = SetVariable("h2points", h2points - 12))]
    add "hallbg"
    add "hallrun"
    add "images/round2.png"
    button:
        text "[h2points] / [h2max_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("h2clicked", True), If(h2points >= h2max_point, true=Jump("h2win"), false=SetVariable("h2points", h2points + h2plus)), Play("sound", "audio/menu_pop.mp3")] #add click.ogg file to 'game' folder
        vbar value StaticValue(h2points, h2max_point) xalign 1.0 yalign 1.0
    if persistent.hclicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("hallrun_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

default h3points=50
default h3plus=10
default h3max_point=450
default h3clicked = True

screen h3clicker():
    modal True
    timer .5 repeat True action [If(h3points <= 0, true=Jump("h1lost"), false = SetVariable("h3points", h3points - 14))]
    add "hallbg"
    add "hallrun"
    add "images/round3.png"
    button:
        text "[h3points] / [h3max_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("h3clicked", True), If(h3points >= h3max_point, true=Jump("h3win"), false=SetVariable("h3points", h3points + h3plus)), Play("sound", "audio/menu_pop.mp3")] #add click.ogg file to 'game' folder
        vbar value StaticValue(h3points, h3max_point) xalign 1.0 yalign 1.0
    if persistent.hclicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("hallrun_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

default hb1points=50
default hb1plus=4
default hb1max_point=200
default hb1clicked = True

screen hb1clicker():
    modal True
    timer .5 repeat True action [If(hb1points <= 0, true=Jump("hb1lost"), false = SetVariable("hb1points", hb1points - 4))]
    add "haibiru_bg"
    add "images/haibiru_fire.png"
    add "haibiru_run"
    add "images/round1.png"
    button:
        text "[hb1points] / [hb1max_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("hb1clicked", True), If(hb1points >= hb1max_point, true=Jump("hb1win"), false=SetVariable("hb1points", hb1points + hb1plus)), Play("sound", "audio/menu_pop.mp3")] #add click.ogg file to 'game' folder
        vbar value StaticValue(hb1points, hb1max_point) xalign 1.0 yalign 1.0
    if persistent.hbclicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("haibiru_run_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

default hb2points=150
default hb2plus=8
default hb2max_point=300
default hb2clicked = True

screen hb2clicker():
    modal True
    timer .5 repeat True action [If(hb2points <= 0, true=Jump("hb1lost"), false = SetVariable("hb2points", hb2points - 12))]
    add "haibiru_bg"
    add "images/haibiru_fire.png"
    add "haibiru_run"
    add "images/round2.png"
    button:
        text "[hb2points] / [hb2max_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("hb2clicked", True), If(hb2points >= hb2max_point, true=Jump("hb2win"), false=SetVariable("hb2points", hb2points + hb2plus)), Play("sound", "audio/menu_pop.mp3")] #add click.ogg file to 'game' folder
        vbar value StaticValue(hb2points, hb2max_point) xalign 1.0 yalign 1.0
    if persistent.hbclicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("haibiru_run_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

default hb3points=250
default hb3plus=10
default hb3max_point=450
default hb3clicked = True

screen hb3clicker():
    modal True
    timer .5 repeat True action [If(hb3points <= 0, true=Jump("hb1lost"), false = SetVariable("hb3points", hb3points - 14))]
    add "haibiru_bg"
    add "images/haibiru_fire.png"
    add "haibiru_run"
    add "images/round3.png"
    button:
        text "[hb3points] / [hb3max_point]" size 40
        ##background "#000"
        ##xpos .5
        ##ypos .5
        xysize(1280, 720)
        action [SetVariable("hb3clicked", True), If(hb3points >= hb3max_point, true=Jump("hb3win"), false=SetVariable("hb3points", hb3points + hb3plus)), Play("sound", "audio/menu_pop.mp3")] #add click.ogg file to 'game' folder
        vbar value StaticValue(hb3points, hb3max_point) xalign 1.0 yalign 1.0
    if persistent.hbclicker:
        imagebutton auto "images/skip button_%s.png" xpos 18 ypos 592 focus_mask True action Jump("haibiru_run_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
