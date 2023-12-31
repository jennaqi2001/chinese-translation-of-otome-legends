
image heart:
    "images/heart1.png"
    .45
    "images/heart2.png"
    .45
    repeat

screen gameOver_screen0():
    add "images/gameover0.png"
    add "heart"
    imagebutton auto "images/retry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("start") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen gameOver_screen1():
    add "images/gameover1.png"
    add "heart"
    imagebutton auto "images/retry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("start") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen gameOver_screen2():
    add "images/gameover1.png"
    add "heart"
    imagebutton auto "images/retry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("haibiru_minigame") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen gameOver_screen3():
    add "images/gameover1.png"
    add "heart"
    imagebutton auto "images/retry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("choices9") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen gameOver_screen4():
    add "images/gameover0.png"
    add "heart"
    imagebutton auto "images/retry_%s.png" xpos 0 ypos 0 focus_mask True action Jump("bossbattle") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
