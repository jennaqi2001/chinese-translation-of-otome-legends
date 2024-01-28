# TODO: Translation updated at 2023-12-30 11:34
screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton _("English") action Language(None)
                    textbutton _("{font=xiaolai.ttf}中文{/font}") action Language("chinese")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

translate chinese strings:

    # game/screens.rpy:268
    old "History"
    new "历史记录"

    # game/screens.rpy:269
    old "Skip"
    new "跳过"

    # game/screens.rpy:270
    old "Auto"
    new "自动"

    # game/screens.rpy:271
    old "Save"
    new "保存"

    # game/screens.rpy:272
    old "Load"
    new "读取游戏"

    # game/screens.rpy:313
    old "Start"
    new "开始游戏"

    # game/screens.rpy:323
    old "Preferences"
    new "设置"

    # game/screens.rpy:327
    old "End Replay"
    new "结束回放"

    # game/screens.rpy:331
    old "Main Menu"
    new "标题菜单"

    # game/screens.rpy:333
    old "About"
    new "关于"

    # game/screens.rpy:338
    old "Help"
    new "帮助"

    # game/screens.rpy:344
    old "Quit"
    new "退出"

    # game/screens.rpy:579
    old "Reset All Data"
    new "初始化所有数据"

    # game/screens.rpy:583
    old "Return"
    new "返回"

    # game/screens.rpy:667
    old "Version [config.version!t]\n"
    new "版本 [config.version!t]\n"

    # game/screens.rpy:673
    old "Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]"
    new ""

    # game/screens.rpy:709
    old "Page {}"
    new "第{}页"

    # game/screens.rpy:709
    old "Automatic saves"
    new "自动存档"

    # game/screens.rpy:709
    old "Quick saves"
    new "快速存档"

    # game/screens.rpy:751
    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%Y-%m-%d %H:%M"

    # game/screens.rpy:751
    old "empty slot"
    new "空白档位"

    # game/screens.rpy:768
    old "<"
    new "<"

    # game/screens.rpy:771
    old "{#auto_page}A"
    new "{#auto_page}A"

    # game/screens.rpy:774
    old "{#quick_page}Q"
    new "{#quick_page}Q"

    # game/screens.rpy:780
    old ">"
    new ">"

    # game/screens.rpy:837
    old "Display"
    new "显示"

    # game/screens.rpy:838
    old "Window"
    new "窗口"

    # game/screens.rpy:839
    old "Fullscreen"
    new "全屏"

    # game/screens.rpy:843
    old "Rollback Side"
    new "回滚"

    # game/screens.rpy:844
    old "Disable"
    new "禁用"

    # game/screens.rpy:845
    old "Left"
    new "左边"

    # game/screens.rpy:846
    old "Right"
    new "右边"

    # game/screens.rpy:851
    old "Unseen Text"
    new "未读文本"

    # game/screens.rpy:852
    old "After Choices"
    new "选项后继续"

    # game/screens.rpy:853
    old "Transitions"
    new "忽略转场"

    # game/screens.rpy:866
    old "Text Speed"
    new "文本速度"

    # game/screens.rpy:870
    old "Auto-Forward Time"
    new "自动播放时间"

    # game/screens.rpy:877
    old "Music Volume"
    new "音乐音量"

    # game/screens.rpy:884
    old "Sound Volume"
    new "音效音量"

    # game/screens.rpy:890
    old "Test"
    new "测试"

    # game/screens.rpy:894
    old "Voice Volume"
    new "语音音量"

    # game/screens.rpy:905
    old "Mute All"
    new "全部静音"

    # game/screens.rpy:1024
    old "The dialogue history is empty."
    new "当前无对话记录"

    # game/screens.rpy:1094
    old "Keyboard"
    new "键盘"

    # game/screens.rpy:1095
    old "Mouse"
    new "鼠标"

    # game/screens.rpy:1098
    old "Gamepad"
    new "手柄"

    # game/screens.rpy:1111
    old "Enter"
    new "回车"

    # game/screens.rpy:1112
    old "Advances dialogue and activates the interface."
    new "推进对话并激活界面。"

    # game/screens.rpy:1115
    old "Space"
    new "空格"

    # game/screens.rpy:1116
    old "Advances dialogue without selecting choices."
    new "在没有选择的情况下推进对话。"

    # game/screens.rpy:1119
    old "Arrow Keys"
    new "方向键"

    # game/screens.rpy:1120
    old "Navigate the interface."
    new "导航界面。"

    # game/screens.rpy:1123
    old "Escape"
    new "Esc"

    # game/screens.rpy:1124
    old "Accesses the game menu."
    new "访问游戏菜单。"

    # game/screens.rpy:1127
    old "Ctrl"
    new "Ctrl"

    # game/screens.rpy:1128
    old "Skips dialogue while held down."
    new "按住时快进对话。"

    # game/screens.rpy:1131
    old "Tab"
    new "Tab"

    # game/screens.rpy:1132
    old "Toggles dialogue skipping."
    new "切换对话快进。"

    # game/screens.rpy:1135
    old "Page Up"
    new "上一页"

    # game/screens.rpy:1136
    old "Rolls back to earlier dialogue."
    new "回退至先前的对话。"

    # game/screens.rpy:1139
    old "Page Down"
    new "下一页"

    # game/screens.rpy:1140
    old "Rolls forward to later dialogue."
    new "向前至后来的对话。"

    # game/screens.rpy:1144
    old "Hides the user interface."
    new "隐藏用户界面。"

    # game/screens.rpy:1148
    old "Takes a screenshot."
    new "截图。"

    # game/screens.rpy:1152
    old "Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}."
    new "切换辅助{a=https://www.renpy.cn/doc/self_voicing.html}机器朗读{/a}"

    # game/screens.rpy:1156
    old "Opens the accessibility menu."
    new "打开无障碍菜单。"

    # game/screens.rpy:1158
    old "You can't ask for help now."
    new "现在你不能寻求帮助了"

    # game/screens.rpy:1164
    old "Left Click"
    new "左键点击"

    # game/screens.rpy:1168
    old "Middle Click"
    new "中键点击"

    # game/screens.rpy:1172
    old "Right Click"
    new "右键点击"

    # game/screens.rpy:1176
    old "Mouse Wheel Up\nClick Rollback Side"
    new "鼠标滚轮上\n点击回退操作区"

    # game/screens.rpy:1180
    old "Mouse Wheel Down"
    new "鼠标滚轮下"

    # game/screens.rpy:1188
    old "Right Trigger\nA/Bottom Button"
    new "右扳机键\nA/底键"

    # game/screens.rpy:1192
    old "Left Trigger\nLeft Shoulder"
    new "左扳机键\n左肩键"

    # game/screens.rpy:1196
    old "Right Shoulder"
    new "Right Shoulder"

    # game/screens.rpy:1201
    old "D-Pad, Sticks"
    new "D-Pad, Sticks"

    # game/screens.rpy:1205
    old "Start, Guide"
    new "Start, Guide"

    # game/screens.rpy:1209
    old "Y/Top Button"
    new "Y/Top Button"

    # game/screens.rpy:1212
    old "Calibrate"
    new "Calibrate"

    # game/screens.rpy:1285
    #old "Yes"
    #new "确定"

    # game/screens.rpy:1286
    #old "No"
    #new "取消"

    # game/screens.rpy:1326
    old "Skipping"
    new "正在跳过"

    # game/screens.rpy:1549
    old "Menu"
    new "主菜单"

