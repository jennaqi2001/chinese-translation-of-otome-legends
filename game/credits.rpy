image credits = Movie(size = (1280,720), channel = "movie", play = "images/credits.ogv", loop = False)

screen credits_screen():
    add "credits"

screen yuusuke_retry():
    add "images/haru credits.png"
    imagebutton auto "images/retry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("no_yuusuke_route") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
    #imagebutton auto "images/continue_%s.png" xpos 0 ypos 0 focus_mask True action Jump("haibiru_minigame") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
