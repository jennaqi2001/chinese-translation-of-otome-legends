
default channel = 0
default finalchannel = renpy.random.randint(333,666)
default tvch = 0
default tv_on = True
default tv_state = True

image tvchoff = "images/bg blank.png"
image tvch1 = Movie(size = (1250, 720), channel = "movie", play = "images/static.ogv", loop = True)
image tvch2 = Movie(size = (1250, 720), channel = "movie", play = "images/loading.ogv", loop = True)
image tvch3 = Movie(size = (1250, 720), channel = "movie", play = "images/senpaidrawings_video.ogv", loop = True)
image tvch4 = Movie(size = (1250, 720), channel = "movie", play = "images/racestart.ogv", loop = True)
image tvch5 = Movie(size = (1250, 720), channel = "movie", play = "images/race.ogv", loop = True)

screen terebi():
    add "tvch1"
    $ tvch = channel
    $ tv_state = tv_on
    if tv_state:
        if tvch in [1,2,3,4,5]:
            add "tvch[tvch]"
        elif tvch == finalchannel:
            add "tvchoff"
            imagebutton auto "images/skip button_%s.png" xpos 600 ypos 403 focus_mask True action Jump("ch1") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
        else:
            add "tvch1"
    else:
        add "tvchoff"
    add "images/tvscreen.png"
    text "[finalchannel]" size 40
    text "{color=#f00}[channel]{/color}" size 40 xpos 920 ypos 155
    imagebutton auto "images/tv_ue_%s.png" xpos 918 ypos 403 focus_mask True action SetVariable("channel", (channel + 1)%667) activate_sound "audio/choice_click.wav"
    imagebutton auto "images/tv_shita_%s.png" xpos 918 ypos 501 focus_mask True action SetVariable("channel", (channel - 1)%667) activate_sound "audio/choice_click.wav"
    if tv_state:
        imagebutton auto "images/tv_switchon_%s.png" xpos 900 ypos 255 focus_mask True action SetVariable("tv_on", not tv_on) activate_sound "audio/choice_click.wav"
    else:
        imagebutton auto "images/tv_switchoff_%s.png" xpos 900 ypos 255 focus_mask True action SetVariable("tv_on", not tv_on) activate_sound "audio/choice_click.wav"
