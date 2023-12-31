screen freehand_draw1():
    add "images/art poster.png"
    vbox:
        hbox:
            hbox:
                style "draw_ui"
                imagebutton idle "pencil_icon.png" hover pencil_hover_icon selected_idle pencil_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.PENCIL)
                imagebutton idle "line_icon.png" hover line_hover_icon selected_idle line_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.LINE)
                imagebutton idle "circle_icon.png" hover circle_hover_icon selected_idle circle_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE)
                imagebutton idle "circle_icon_fill.png" hover circle_fill_hover_icon selected_idle circle_fill_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE_FILL)

            frame:
                background "#FFF"
                padding (0, 0)
                xsize 0
                ysize 0

                add freehand_canvas

        vbox:
            style "draw_ui"
            for colour in colours:
                button:
                    xsize 32
                    ysize 32
                    background colour
                    action SetField(freehand_canvas, 'colour', colour)



        vbox:
            style "draw_ui"
            imagebutton idle "thickness.png" hover thickness_hover_icon selected_idle thickness_hover_icon action SetField(freehand_canvas, 'line_width', 1)
            imagebutton idle "thickness_2.png" hover thickness_2_hover_icon selected_idle thickness_2_hover_icon action SetField(freehand_canvas, 'line_width', 2)
            imagebutton idle "thickness_3.png" hover thickness_3_hover_icon selected_idle thickness_3_hover_icon action SetField(freehand_canvas, 'line_width', 4)
            imagebutton idle "thickness_4.png" hover thickness_4_hover_icon selected_idle thickness_4_hover_icon action SetField(freehand_canvas, 'line_width', 8)
            textbutton "Clear Canvas" action Function(freehand_canvas.clear)

    imagebutton auto "images/batsu_%s.png" xpos 1040 ypos 550 focus_mask True action [Function(freehand_canvas.clear), Jump("posterdraw_after")] hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"

screen freehand_draw2():
    add "images/hiros manga2.png"
    vbox:
        hbox:
            vbox:
                style "draw_ui"
                imagebutton idle "pencil_icon.png" hover pencil_hover_icon selected_idle pencil_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.PENCIL)
                imagebutton idle "line_icon.png" hover line_hover_icon selected_idle line_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.LINE)
                imagebutton idle "circle_icon.png" hover circle_hover_icon selected_idle circle_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE)
                imagebutton idle "circle_icon_fill.png" hover circle_fill_hover_icon selected_idle circle_fill_hover_icon action SetField(freehand_canvas, 'mode', FreehandCanvas.CIRCLE_FILL)

            frame:
                background "images/hiros manga_mini.png"
                padding (0, 0)
                xsize 320
                ysize 180

                add freehand_canvas

        hbox:
            style "draw_ui"
            for colour in colours:
                button:
                    xsize 32
                    ysize 32
                    background colour
                    action SetField(freehand_canvas, 'colour', colour)



        hbox:
            style "draw_ui"
            imagebutton idle "thickness.png" hover thickness_hover_icon selected_idle thickness_hover_icon action SetField(freehand_canvas, 'line_width', 1)
            imagebutton idle "thickness_2.png" hover thickness_2_hover_icon selected_idle thickness_2_hover_icon action SetField(freehand_canvas, 'line_width', 2)
            imagebutton idle "thickness_3.png" hover thickness_3_hover_icon selected_idle thickness_3_hover_icon action SetField(freehand_canvas, 'line_width', 4)
            imagebutton idle "thickness_4.png" hover thickness_4_hover_icon selected_idle thickness_4_hover_icon action SetField(freehand_canvas, 'line_width', 8)
            textbutton "Clear Canvas" action Function(freehand_canvas.clear)


    imagebutton auto "images/batsu_%s.png" xpos 1040 ypos 550 focus_mask True action [Function(freehand_canvas.clear), Jump("mangaredraw_after")] hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
