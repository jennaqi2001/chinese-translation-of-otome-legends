screen choose_route:
    add "images/bulletin.png"
    hbox:
        xalign 0.5
        yalign 0.5
        yoffset 0.5
        spacing 20
        if not persistent.naomi:
            imagebutton:
                auto "images/snapshot_male1_%s.png"
                action Jump("ishida_route")
                sensitive True
                hover_sound "audio/menu_pop.mp3"
                activate_sound "audio/menu_click.mp3"

            if not persistent.no_yuusuke and not persistent.yuusuke:
                imagebutton:
                    auto "images/snapshot_male2_%s.png"
                    action Jump("yuusuke_route")
                    sensitive persistent.ishida == True
                    hover_sound "audio/menu_pop.mp3"
                    activate_sound "audio/menu_click.mp3"

            if persistent.yuusuke and not persistent.no_yuusuke:
                imagebutton:
                    idle "snapshot_blank"
                    hover "snapshot_glitch"
                    action Jump("no_yuusuke_route")
                    sensitive persistent.yuusuke == True
                    hover_sound "audio/error.wav"
                    activate_sound "audio/menu_click.mp3"

            imagebutton:
                auto "images/snapshot_male3_%s.png"
                action Jump("hiro_route")
                sensitive persistent.no_yuusuke == True
                hover_sound "audio/menu_pop.mp3"
                activate_sound "audio/menu_click.mp3"

            imagebutton:
                auto "images/snapshot_male4_%s.png"
                action Jump("kaoru_route")
                sensitive persistent.hiro == True
                hover_sound "audio/menu_pop.mp3"
                activate_sound "audio/menu_click.mp3"
        else:

            imagebutton:
                idle "snapshot_blank"
                hover "snapshot_glitch"
                action Jump("restart1")
                hover_sound "audio/error.wav"
                activate_sound "audio/menu_click.mp3"

    if not persistent.naomi:
        add "images/route_selection.png"



image snapshot_blank:
    "images/snapshot_male5_idle.png"

image snapshot_glitch:
    At("images/snapshot_male5_idle.png", glitch)
    pause 0.2
    At("images/snapshot_male5_idle.png", chromatic_offset)
    pause 0.15
    "images/snapshot_male5_idle.png"
    pause 0.05
    At("images/snapshot_male5_idle.png", chromatic_offset)
    pause 0.1
    "images/snapshot_male5_idle.png"
    pause 1.1
    repeat
