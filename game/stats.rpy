screen stats:
    text "Player HP: [player_max_hp]" xpos 0 ypos 0
    text "Boss HP: [boss_max_hp]" xpos 0 ypos 30
    hbox:
        xalign 0.5
        yalign 0.95
        frame:
            xpadding 20
            ypadding 20
            xsize 200
            ysize 220
            xalign 0.5
            yalign 0.95

            hbox:
                spacing 10
                xsize 100
                ysize 100
                xanchor 0
                vbox:
                    spacing 25
                    textbutton _("Rock") focus_mask True action Jump("rock") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/unlock.wav"
                    textbutton _("Paper") focus_mask True action Jump("paper") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/unlock.wav"
                    textbutton _("Scissors") focus_mask True action Jump("scissors") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/unlock.wav"
                vbox:
                    spacing 25
                    text "{size=13}DMG ???{/size}"
                    text "{size=13}DMG ???{/size}"
                    text "{size=13}DMG ???{/size}"

        frame:
            xpadding 30
            ypadding 20
            xsize 500
            ysize 220
            xalign 0.5
            yalign 0.95
            vbox:
                spacing 20
                text "{size=18}Rock: beats scissors but loses against paper.{/size}"
                text "{size=18}Paper: beats rock but loses against scissors.{/size}"
                text "{size=18}Scissors: beats paper but loses against rock.{/size}"
