# The script of the game goes in this file.
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default persistent.restartnum = 0
default persistent.first_gameovernum = 0

default cursorlist = [["images/flashlight.png", "default", (1280, 720)], ["images/no_flashlight.png", (50, 50, 50, 50), (0, 0)]]

#Your Name#
define player = Character("[playername]", color = "#525252")
#Main Game Characters#
define mc = Character("Chiharu", color = "#93c47d")
define mc2 = Character("{font=OtsutomeFont.ttf}千春{/font}", color = "#93c47d")
##Harumiya Chiharu (春宮千春)
define bff = Character("Naomi", color = "#CD757C")
define bff2 = Character("{font=OtsutomeFont.ttf}直美{/font}", color = "#CD757C")
define male0 = Character("Naoya", color = "#CD757C")
##Nakamura Naomi (中村直美)
define male1 = Character("Ishida", color = "#63aced")
##Ishida Yuu (石田優)
define male2 = Character("Yuusuke", color = "#f78e20")
##Amano Yuusuke (天野祐介)
define male3 = Character("Hiro", color = "#268B4A")
##Hasegawa Takahiro　(長谷川孝弘)
define male4 = Character("Kaoru", color = "#6B62C7")
##Akeyuki Kaoru (明雪薫)
define imt = Character("Akari", color ="#f78e20")
##Amano Akari (天野明莉)

#Otome Legends Characters#
define shoujo1 = Character("Moteko", color = "#ff6baa")
#Sugoi Bijin (須吾井美仁)
define shoujo2 = Character("Yumeko", color = "#ef0ad1")
#Yumeyume Yumeko(夢夢ゆめ子)
define senpai1 = Character("Mafura Senpai", color = "#4422FF")
#Tennen Cool(天念久瑠)
define senpai2 = Character("Matsuge Senpai", color = "#ff4c4c")
#Akai Bara(赤井場羅)
define senpai3 = Character("Kinpatsu Senpai", color = "#d7a200")
#Ore Sama(尾例紗魔)
define senpai4 = Character("Ikemen Senpai", color = "#934B41")
#Handsomu Macho(半寒間頂)
define girl1 = Character("Pony-Tailed Girl", color = "#9D9EA1")
define girl2 = Character("Blond Girl", color = "#f1c232")
define girl3 = Character("Green-haired Girl", color = "#506a45")

style draw_ui:
    spacing 2

init:
    $ style.default.font = "Chinese_Font.ttf"

init python:
    colours = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#00FFFF', '#FF00FF', '#FF7F7F', '#FBEFE3']
    default_colour = '#000'
    freehand_canvas = FreehandCanvas(default_colour, 1280, 720)

    # Quick and dirty hover icons
    pencil_hover_icon = Fixed(
        Image("pencil_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    line_hover_icon = Fixed(
        Image("line_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    circle_hover_icon = Fixed(
        Image("circle_icon.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    circle_fill_hover_icon = Fixed(
        Image("circle_icon_fill.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    thickness_hover_icon = Fixed(
        Image("thickness.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    thickness_2_hover_icon = Fixed(
        Image("thickness_2.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    thickness_3_hover_icon = Fixed(
        Image("thickness_4.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

    thickness_4_hover_icon = Fixed(
        Image("thickness_4.png"),
        Transform(Frame(Solid("#FFF"), 5, 5), alpha=0.5),
        xysize=(32, 32),
    )

image flashback1:
    "images/cg fdesk1.png" with fade
    1.0
    "images/cg fdesk2.png"
    1.0
    "images/cg bully_fb2.png"
    1.0
    "images/cg bully_fb1.png"
    1.0
    "images/cg bully_fb3.png"
    1.0
    "images/cg fdesk1.png"
    .45
    "images/cg fdesk2.png"
    .45
    "images/cg bully_fb2.png"
    .45
    "images/cg bully_fb1.png"
    .45
    "images/cg bully_fb3.png"
    .45
    "images/cg fdesk1.png"
    .30
    "images/cg fdesk2.png"
    .30
    "images/cg bully_fb2.png"
    .30
    "images/cg bully_fb1.png"
    .30
    "images/cg bully_fb3.png"
    .30
    "images/cg fdesk1.png"
    .15
    "images/cg fdesk2.png"
    .15
    "images/cg bully_fb2.png"
    .15
    "images/cg bully_fb1.png"
    .15
    "images/cg bully_fb3.png"
    .15
    "images/cg fdesk1.png"
    .10
    "images/cg fdesk2.png"
    .10
    "images/cg bully_fb2.png"
    .10
    "images/cg bully_fb1.png"
    .10
    "images/cg bully_fb3.png"
    .10
    "images/cg fdesk1.png"
    .05
    "images/cg fdesk2.png"
    .05
    "images/cg bully_fb2.png"
    .05
    "images/cg bully_fb1.png"
    .05
    "images/cg bully_fb3.png"
    .05
    "images/cg fdesk1.png"
    .05
    "images/cg fdesk2.png"
    .05
    "images/cg bully_fb2.png"
    .05
    "images/cg bully_fb1.png"
    .05
    "images/cg bully_fb3.png"
    .05
    "images/cg fdesk1.png"
    .05
    "images/cg fdesk2.png"
    .05
    "images/cg bully_fb2.png"
    .05
    "images/cg bully_fb1.png"
    .05
    "images/cg bully_fb3.png"
    .05
    "images/cg fdesk1.png"
    .05
    "images/cg fdesk2.png"
    .05
    "images/cg bully_fb2.png"
    .05
    "images/cg bully_fb1.png"
    .05
    "images/cg bully_fb3.png"
    .05
    "images/cg fdesk1.png"
    .05
    "images/cg fdesk2.png"
    .05
    "images/cg bully_fb2.png"
    .05
    "images/cg bully_fb1.png"
    .05
    "images/cg bully_fb3.png"
    .05
    "images/cg fdesk1.png"
    .05
    "images/cg fdesk2.png"
    .05
    "images/cg bully_fb2.png"
    .05
    "images/cg bully_fb1.png"
    .05
    "images/cg bully_fb3.png"
    .05
    "images/cg fdesk1.png"
    .05
    "images/cg fdesk2.png"
    .05
    "images/cg bully_fb2.png"
    .05
    "images/cg bully_fb1.png"
    .05
    "images/cg bully_fb3.png"
    .05

image bff blinking:
    "images/bff normal.png"
    6.45
    "images/bff blink.png"
    .02
    "images/bff glee.png"
    .05
    "images/bff blink.png"
    .03
    "images/bff normal.png"
    3.45
    "images/bff blink.png"
    .02
    "images/bff glee.png"
    .15
    "images/bff blink.png"
    .03
    "images/bff normal.png"
    4.45
    "images/bff blink.png"
    .02
    "images/bff glee.png"
    .05
    "images/bff blink.png"
    .03
    "images/bff normal.png"
    1.45
    "images/bff blink.png"
    0.1
    "images/bff glee.png"
    .15
    "images/bff blink.png"
    .01
    "images/bff normal.png"
    7.50
    "images/bff blink.png"
    .01
    "images/bff glee.png"
    .08
    "images/bff blink.png"
    .01
    "images/bff normal.png"
    3.15
    "images/bff blink.png"
    .01
    "images/bff glee.png"
    .15
    "images/bff blink.png"
    .03
    "images/bff normal.png"
    1.0
    "images/bff blink.png"
    .02
    "images/bff glee.png"
    .10
    "images/bff blink.png"
    .03
    "images/bff normal.png"
    2.45
    "images/bff blink.png"
    .02
    repeat

image bff evil_smile:
    "images/bff normal.png" with dissolve
    .5
    "images/bff yandere_smile1.png" with dissolve
    .75
    "images/bff yandere_smile2.png" with dissolve
    1.0
    "images/bff mischievous.png" with dissolve

image click:
    "images/click1.png"
    .25
    "images/click2.png"
    .25
    "images/click3.png"
    .25
    repeat

image hr_thoughts:
    "images/hr_thoughts1.png"
    .45
    "images/hr_thoughts2.png"
    .45
    repeat

image flash red:
    "images/white.png" with dissolve
    .15
    "images/bg blank.png" with dissolve
    .25
    "images/bg red.png" with dissolve
    .45
    "images/bg blank.png" with dissolve

image cg kidnapped:
    "images/cg kidnapped1.png"
    .45
    "images/cg kidnapped2.png"
    .45
    repeat

image cg ambushed_thugs:
    "images/cg ambushed2.png"
    0.45
    "images/cg ambushed3.png"
    0.45
    repeat

image awaken:
    "images/awaken1.png"
    3.0
    "images/awaken2.png"
    0.45
    "images/awaken1.png"
    0.45
    "images/awaken2.png"
    2.0
    "images/awaken3.png"
    5.0

image bsb_glitch:
    "images/bsb_blank.png"
    .15
    "images/bsb_cursed.png"
    .45
    "images/bsb_blue.png"
    .3
    "images/bsb_cursed.png"
    .3
    "images/stare_red.png"
    .3
    "images/stare_glitch.png"
    .3
    "images/bsb_blue.png"

image bsb_sticker:
    "images/bsb_sticker1.png"
    .45
    "images/bsb_sticker2.png"
    .45
    repeat

image bff glitch:
    At("images/bff normal.png", glitch)
    pause 0.2
    At("images/bff normal.png", chromatic_offset)
    pause 0.15
    At("images/bff mischievous.png", glitch)
    pause 0.05
    At("images/bff normal.png", chromatic_offset)
    pause 0.3
    At("images/bff yandere_smile1.png", glitch)
    pause 0.05
    At("images/bff normal.png", chromatic_offset)
    pause 0.2
    "images/bff normal.png"

image male0 glitching:
    At("images/male0 blush.png", glitch)
    pause 0.2
    At("images/male0 blush.png", chromatic_offset)
    pause 0.15
    At("images/male0 glee.png", glitch)
    pause 0.05
    At("images/male0 normal.png", chromatic_offset)
    pause 0.3
    At("images/male0 glitch.png", glitch)
    pause 0.05
    At("images/male0 maniac.png", chromatic_offset)
    pause 0.2
    "images/male0 blush.png"

image cg ishida_game glitch:
    At("images/cg ishida_game2.png", glitch)
    pause 0.2
    At("images/cg ishida_game2.png", chromatic_offset)
    pause 0.15
    At("images/cg ishida_game2.png", glitch)
    pause 0.45
    At("images/stare_red.png", chromatic_offset)
    pause 0.3
    At("images/stare_glitch.png", glitch)
    pause 0.05
    At("images/cg ishida_game2.png", chromatic_offset)
    pause 0.2
    "images/cg ishida_game2.png"
    repeat

image bg bedroom_glitch:
    At("images/bg bedroom_dark.png", glitch)
    pause 0.2
    At("images/bg bedroom.png", chromatic_offset)
    pause 0.15
    At("images/bg classroom.png", glitch)
    pause 0.25
    At("images/bg bedroom_dark.png", chromatic_offset)
    pause 0.3
    At("images/bg bedroom.png", glitch)
    pause 0.05
    At("images/bg bedroom.png", chromatic_offset)
    pause 0.2
    "images/bg bedroom_dark.png"

image bg cyberspace_glitch:
    At("images/bg cyberspace.png", glitch)
    pause 0.2
    At("images/bg past1.png", chromatic_offset)
    pause 0.15
    At("images/bg past1.png", glitch)
    pause 0.1
    At("images/bg cyberspace.png", chromatic_offset)
    pause 0.3
    At("images/bg cyberspace.png", glitch)
    pause 0.05
    At("images/bg past1.png", chromatic_offset)
    pause 0.2
    "images/bg cyberspace.png"

image bg classroom_glitch:
    At("images/bg classroom.png", glitch)
    pause 0.2
    At("images/bg classroom.png", chromatic_offset)
    pause 0.15
    "images/bg classroom.png"


image mg thinking:
    "images/mg dots1.png"
    0.5
    "images/mg dots2.png"
    0.5
    "images/mg dots3.png"
    0.5
    repeat

image laugh1:
    "images/laughter1.png"
    0.5
    "images/laughter2.png"
    0.5
    repeat

image laugh2:
    "images/laughter3.png"
    0.5
    "images/laughter4.png"
    0.5
    repeat

image laugh3:
    "images/laughter5.png"
    0.5
    "images/laughter6.png"
    0.5
    repeat

screen snow():
    add Snow("gui/snow1.png")
    add Snow("gui/snow2.png")

screen roses():
    add Snow("gui/rose1.png")
    add Snow("gui/rose2.png")
    add Snow("gui/rose3.png")

screen sunrays():
    add Snow("gui/sun1.png")
    add Snow("gui/sun2.png")

screen confetti():
    add Snow("gui/fool1.png")
    add Snow("gui/fool2.png")
    add Snow("gui/fool3.png")

image mafura sticker:
    "images/intro_mafura_sticker1.png"
    0.45
    "images/intro_mafura_sticker2.png"
    0.45
    repeat

image intro mafura:
    "mafura sticker" with dissolve
    0.15
    "images/white.png" with dissolve
    1.5
    "mafura sticker" with dissolve

image matsuge sticker:
    "images/intro_matsuge_sticker1.png"
    0.45
    "images/intro_matsuge_sticker2.png"
    0.45
    repeat

image intro matsuge:
    "matsuge sticker" with dissolve
    0.15
    "images/white.png" with dissolve
    1.5
    "matsuge sticker" with dissolve

image kinpatsu sticker:
    "images/intro_kinpatsu_sticker1.png"
    0.45
    "images/intro_kinpatsu_sticker2.png"
    0.45
    repeat

image intro kinpatsu:
    "kinpatsu sticker" with dissolve
    0.15
    "images/white.png" with dissolve
    1.5
    "kinpatsu sticker" with dissolve

image moteko sketch:
    "images/moteko1.png"
    0.45
    "images/moteko2.png"
    0.45
    At("images/moteko1.png", glitch)
    pause 0.2
    At("images/moteko2.png", chromatic_offset)
    pause 0.15
    "images/moteko1.png"
    0.45
    "images/moteko2.png"
    0.45
    repeat

image handrawn hello:
    "images/handrawn hello1.png"
    0.25
    "images/handrawn hello2.png"
    0.25
    "images/handrawn hello3.png"
    0.25
    "images/handrawn hello4.png"
    0.25
    repeat

image handrawn name:
    "images/handrawn name1.png"
    0.5
    "images/handrawn name2.png"
    0.5
    repeat

image heart_progress1:
    "images/progress0.png"
    0.25
    "images/progress1.png"
    0.25
    "images/progress0.png"
    0.25
    "images/progress1.png"
    0.25
    "images/progress0.png"
    0.25
    "images/progress1.png"
    0.25
    "images/progress0.png"
    0.25
    "images/progress1.png"
    0.25
    "images/progress0.png"
    1.0
    "images/progress1.png" with dissolve

image heart_progress2:
    "images/progress1.png"
    0.25
    "images/progress2.png"
    0.25
    "images/progress1.png"
    0.25
    "images/progress2.png"
    0.25
    "images/progress1.png"
    0.25
    "images/progress2.png"
    0.25
    "images/progress1.png"
    0.25
    "images/progress2.png"
    0.25
    "images/progress1.png"
    1.0
    "images/progress2.png" with dissolve

image heart_progress3:
    "images/progress2.png"
    0.25
    "images/progress3.png"
    0.25
    "images/progress2.png"
    0.25
    "images/progress3.png"
    0.25
    "images/progress2.png"
    0.25
    "images/progress3.png"
    0.25
    "images/progress2.png"
    0.25
    "images/progress3.png"
    0.25
    "images/progress2.png"
    1.0
    "images/progress3.png" with dissolve

image bg childhood:
    "images/bg childhood1.png" with dissolve
    1.25
    "images/bg childhood2.png" with dissolve
    1.25
    repeat

transform drifting:
    xalign 0.0
    linear 10.0 xalign 1.0
    repeat

image naoya glitching = Movie(size = (1280, 720), channel = "movie", play = "images/naoya_glitch.webm", loop = False)
image racestart_video = Movie(size = (1280, 720), channel = "movie", play = "images/racestart.ogv", loop = True)
image loading = Movie(size = (1280, 720), channel = "movie", play = "images/loading.ogv", loop = True)
image static = Movie(size = (1280, 720), channel = "movie", play = "images/static.ogv", loop = True)
image chikatetsu = Movie(size = (1280, 720), channel = "movie", play = "images/chikatetsu_door.ogv", loop = False)


# The game starts here.
label splashscreen:
    if persistent.no_yuusuke and not persistent.yuusuke:
        jump reset
    if persistent.wish:
        jump wishgranted
    if persistent.wishproposal:
        jump wishproposal
    if persistent.endgame:
        jump endgame_wish
    if persistent.moteko_defeat:
        jump lastscene
    if persistent.escape:
        jump escape
    if persistent.dashutsu_end:
        jump dashutsu_after
    if persistent.save:
        jump finalsave
    if not persistent.naoya:
        show bg blank
        scene warnscreen with fade
        play sound "audio/advisory1.mp3" volume 0.5
        pause
        scene seizure_warning with fade
        play sound "audio/advisory2.mp3" volume 0.5
        pause
        scene copyright with fade
        play sound "audio/advisory3.mp3" volume 0.5
        pause
        show bg blank with fade
        return
    else:
        jump restart3

screen snow():
    add Snow("gui/snow1.png")
    add Snow("gui/snow2.png")

screen roses():
    add Snow("gui/rose1.png")
    add Snow("gui/rose2.png")
    add Snow("gui/rose3.png")

screen sunrays():
    add Snow("gui/sun1.png")
    add Snow("gui/sun2.png")


label start:
    $ phone_too = "unknown"
    if persistent.naomi:
        play music "audio/warppedmenu.mp3"
    else:
        play music "audio/menutheme.mp3"
    call screen choose_route

    label ishida_route:
    stop music
    label bgm:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    play music "audio/ponder_ost.mp3" fadein 1.0 volume 1.0
    scene white with dissolve
    centered "{color=#000000}中文测试It was a long time ago when I played that game.{/color}"
    centered "{color=#000000}Back then, I was just an unpopular high school girl that only could dream of
    being the most popular beauty in school.{/color}"
    centered "{color=#000000}I wasn't good at sports.{/color}"
    centered "{color=#000000}I wasn't good at school.{/color}"
    centered "{color=#000000}As a matter of fact, I wasn't good at anything.{/color}"
    centered "{color=#000000}But that was okay.{/color}"
    centered "{color=#000000}Because at least, I had a friend who made life worth while along the way.{/color}"
    stop music
    centered "{color=#000000}{cps=5}Her name was . . .{/cps}{/color}{w=1.5}{nw}"
    scene bg blank
    bff "Chiharu Chan!"
    ##### Day One ------------------------------------------------------------##
    label ch1:
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    "A mysterious figure calls my name from behind me."
    mc "Oh, hi there."
    $ achievement.grant("amogus")
    $ achievement.sync()
    show bff closeup
    mc "AHH!"
    show bff glee
    mc "Oh, its you."
    centered "{nw}"
    scene intro naomi bg1 with dissolve
    play sound "audio/tape.wav"
    pause (0.5)
    scene intro naomi bg2 with wipeleft
    play sound "audio/flute.wav"
    scene white with dissolve
    pause (2.0)
    play sound "audio/glitter.wav"
    scene intro naomi bg3 with dissolve
    pause (4.0)
    "It's Naomi, my best friend from elementary school."
    "We've been friends for a very long time."
    scene bg classroom
    show bff worried
    with dissolve
    bff "Cmon, we've known each other for like 10 years and you still can't tell
    when I'm sneaking up on you?"
    mc "Sorry, I didn't notice you standing there."

    show bff glee
    bff "BTW, you've heard about the new game that everyone's talking
    about right?"
    mc "What game?"
    show bff excited
    bff "Otome Legends! Everyones playing it!"

    "My best friend, Naomi, has always been an otome otaku. She's always
    talking about how her dream is to marry a prince one day."
    "Of course, I believe it's pretty far-fetched and childish, but at this
    point it doesn't really surprise me. She's been like this for ages."

    mc "Oh cmon, yknow I'm not really into that stuff right!?"

label choices:

    show bff worried
    bff "Just try it for one day pretty pleasseeee!!! I'll lend you my handheld
    Nony BSB!"

menu:
    "Okay, fine! I'll try it for one day and if I don't like it I'm giving
    it straight back to you!":
        jump choices1_playgame
    "No.":
        jump choices1_rejectgame
label choices1_playgame:
    show bff glee
    bff "Hehehehehe!"
    jump choices1_common

label choices1_rejectgame:
    show bff worried
    bff "Awwwww!"
    stop music fadeout 1.0

    ##ts --------------------------------------------------------------------
    scene bg blank with fade
    centered "{size=35}After School{/size}"
    ##ts --------------------------------------------------------------------

    scene bg bedroom_yoru with fade
    $ persistent.first_gameovernum += 1
    if not persistent.first_gameovernum == 10:
        "When the day was over, I walked back home and went to sleep."
        "Still, I wish she would just stop nagging me about that sort of stuff
        though!"
        jump choices1_endgame
    else:
        $ achievement.grant("egg_achievement")
        $ achievement.sync()
        jump choices1_endgame


label choices1_common:

    ##ts --------------------------------------------------------------------
    scene bg blank with fade
    centered "{size=35}After School{/size}"
    ##ts --------------------------------------------------------------------

    scene bg bedroom_yoru with fade
    stop music fadeout 1.75


    "After that day, I went home and tried that new game that Naomi recommended
    me."
    "I could have said no, but I decided that it was not worth listening to
    her constant nagging if I had done so."

    mc "This better be good."
    show bsb_blank
    "I started up the device and made a new save file."
    scene bg bsb_blank
    pause (1.0)
    play sound "audio/unlock.wav" volume 0.5
    play music "audio/bsbtheme.mp3" fadein 1.0 volume 1.0
    scene bg bsb_on with dissolve
    "shoujo:" " OH NO! I'm late for school!"
    "A cute kawaii shoujo runs out of her house with an entire plate of curry in her mouth."
    "shoujo" " ACK!"
    "Cute shoujo girl bumps into a tall handsome senpai."
    scene bg bsb_on_mafuracurry with dissolve
    "Senpai:" " Hey!"
    "A mysterious figure appears in front of you."
    "Senpai:" "Watch where you're going! You got curry all over my face!"
    "shoujo" "I'm SOOOO sorry!"
    "The high school shoujo looks at the time."
    "shoujo" "AAAHHH! I'M LATE!"
    "She runs to school."
    scene bg bsb_on with fade
    "Surprisingly, you weren't late to school after all."
    "shoujo" " OH NO! I RAN INTO A SUPER CUTE HOTTIE AND I RUINED HIS FACE?! WHAT AM I GONNA DO?!"
    "Mysterious Figure:" " Moteko Chan!"
    "It's your best friend, Yumeko."
    shoujo2 "Why the long face?"
    shoujo1 "I got curry all over some hot senpai's chin."
    shoujo2 " Oh?"
    shoujo1 "Yea, it's been bumming me out all morning!"
    shoujo2 "Well, why not try to make up with him with a box of chocolates?"
    "That sounds like a stupid idea."
    shoujo1 "GREAT IDEA! I'll go buy them at the vending machine during lunch and go apologize!!"
    play sound "audio/schoolchime2.wav"
    "The bell rings, it's time for class to start."
    "..."
    "After a bunch of long boring lectures, it's finally time for lunch."
    shoujo1 "Finally! Time to go buy the chocolate!"
    "As you walk to the vending machine you spot a strange figure approaching you."
    show senpai matsuge with dissolve
    senpai2 "HOHOHOHOHOHOHO!"
    "He laughs in an absolutely ridiculous manner."
    senpai2 "Bonjour mademoiselle! You dropped your handkerchief!"
    "Why is he speaking French?"
    shoujo1 "(blushes) oh... thanks I guess."
    "The senpai looks at his watch."
    senpai2 "OHOHOHO! Look at the time! I have to go now! Nice meeting ya!"
    shoujo1 "Wait!"
    play sound "audio/schoolchime2.wav"
    "The bell rings."
    shoujo1 "Oh no! I ran out of time to buy the chocolate!"
    scene bg bsb_on with dissolve
    "It is now time for gym class."
    "..."
    "And all the guys are flexing."
    scene bg bsb_on_senpaitachi with dissolve
    senpai2 "Look at my muscles you peons!"
    senpai3 "No! Mine! Mine are bigger!"
    senpai1 "No! Mine are cool and mysterious! Better than yours!"
    shoujo1 "(Oh my! they're all so handsome!)"
    "You can't help but think to yourself that this game is absolute cringe."
    "However, despite this, you find the game pretty enjoyable."
    "But seriously though, what the heck is wrong with their chins?"
    stop music fadeout 1.0
    ##ts --------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts --------------------------------------------------------------------

    #### Day Two morning -----------------------------------------------------##

    scene bg classroom with fade
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    show bff glee
    show ct_overlay
    show ct_tues
    show ct_830
    with dissolve
    bff "Sooo?"
    "Naomi comes up to me eagerly ready to ask me about the game."
    mc "So what?"
    show bff normal
    bff "How was the game??"
    mc "(Sigh)"
    mc "It was actually not too bad."
    hide ct_830
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff blush
    bff "I told you so!!"
    mc "... yea"
    show bff mischievous
    "Naomi looks at me mischievously."
    bff "You played the game all night didn't you?"
    "Naomi can see right through me."
    mc "..."
    mc "FINE! It was actually really good! Okay!?"
    show bff glee
    bff "Hehehe! I told ya, I have good tastes for these sorta things yknow?"
    mc "Yea... I guess."
    show bff worried
    bff "Whats wrong Chiharu?"
    mc "It's just that, I wish I were popular with guys too."
    show bff mischievous
    bff "Oh...?"
    mc "I'm not as pretty and popular as the typical otome heroine! Yknow!
    guys would never fall for someone as plain and boring as me!"
    mc "I'm not as pretty as you Naomi."
    show bff blush
    bff "Well, who says you can't get popular with the guys?"
    mc "Excuse me?"
    show bff normal
    bff "Well, that guy over there seems like he'd be head over heels for anyone
    why not try asking him out?"
    mc "What?! Why would I do that? That's weird!"
    show bff glee
    bff "Cmon, I know you got it in you!!"
    "My best friend pushes me towards the guy."
    scene bg classroom
    show male1 normal with dissolve
    mc "(Oh no... What am I gonna do now?)"
    mc "uh.. hello?"
    "Otaku" "..."
    "He looks at me with an annoyed stare."
    mc "..."
    mc "(This guy looks like a major otaku.)"
    "Translation Notes: Otaku means nerd in Japanese."
    mc "(I should say something before things get awkward.)"
    mc "Uh... hi!"
    mc "(Oh my god, what was that? That sounded so awkward!)"
    show male1 worried with dissolve
    "Otaku" "(Sigh)"
    hide male1 with dissolve
    "The otaku gets up and walks away."
    "I walk back to my desk and can't shake the feeling of embarrassment."
    show bff glee with dissolve
    bff "So how did it go?"
    mc "Bad."
    show bff normal
    bff "Welp, better luck next time right?!"
    mc "Why did you have to make me do that?"
    show bff worried
    bff "It's for your own good!"
    play sound "audio/schoolchime1.wav"
    show ct_overlay
    show ct_tues
    show ct_845
    with dissolve
    "The bell rings, its time for class to start."
    stop music fadeout 1.0
    ## Day 2 Morning End -----------------------------------------------------##

    ##Day 2 Classtime--------------------
    scene bg classroom with fade
    play sound "audio/chalkboard.wav" fadein 1.0
    "Sensei" "..."
    "Sensei" "And that is why history repeats itself..."
    "Sensei" "Alright class.."
    "Sensei" "Here are the chapters and topics we will be going over today."
    stop sound fadeout 2.0
    "Sensei" "Everyone, open your books to page 417!"
    "I stare out the window wondering when class will be over."
    mc "(Sigh)"
    "I stare vacantly at the clock."
    show ct_overlay
    show ct_tues
    show ct_905
    with dissolve
    mc "(How much longer?)"
    "The clock doesn't seem to be moving at all."
    mc "..."
    mc "(Maybe I should take a bathroom break.)"
    scene bg school_hallway with fade
    "I got up from the chair and walk out of the classroom."
    mc "(Man, I really need a break right now.)"
    mc "(I actually don't really need to go to the bathroom. Perhaps I should walk around for a bit to wake myself up a little.)"
    mc "..."
    mc "(Maybe I should go to the vending machine.)"


    label choices2:
        "Go to the vending machine?"
    menu:
        "Go to the vending machine.":
            jump choices2_a
        "Continue walking.":
            jump choices2_b
    label choices2_a:
        "Its a melon bread!"
        "But I don't have enough coins to buy it..."
        jump choices2_common

    label choices2_b:
        "Maybe another time."
        jump choices2_common


    label choices2_common:
        stop music fadeout 1.0

    pause
    #play sound "audio/punch.wav"
    "..."
    "Theres a noise coming from the direction of the bathroom."
    mc "(What was that?)"
    play music "audio/sad_theme.mp3"
    "Crowd" "HAHAHAHAHAHAHA"
    "What's going on?"
    show generic_male normal with dissolve
    "Guy" "Yknow, I think that's a great look for ya!"
    "Guy" "Yea, nobody likes a creepy nerd with glasses!"
    "The situation looks intense."
    hide generic_male
    show male1 worried_noglasses with vpunch
    $ renpy.vibrate(.5)
    "Otaku" "Hey! Give those back!"
    hide male1
    show generic_male normal
    "Guy" "Ahh~! Waaah~! Gimme my glasses back~!"
    "Guy" "Hahaha, what a crybaby."
    "Crowd" "Crybaby! Crybaby! Crybaby!"
    "Guy" "Anyways, lets bounce. I think we've had enough for today."
    "Guy" "Smell ya later! Nerd!"
    "The crowd dispersed."
    stop music fadeout 1.0
    scene bg school_hallway with dissolve
    mc "(It's best not to get involved with that.)"
    "I ended up walking to the bathroom after all."
    pause
    scene bg school_bathroom with fade
    mc "Oh my god, what was that?"
    mc "I must have the worst timing on planet Earth!"
    mc "Out of all the times to go to the bathroom, I picked the absolute worst possible time."
    mc "But seriously, what was that though?"
    mc "Huh, what's this?"
    play sound "audio/coin_sound.wav" volume 1.0
    show coin
    "Its a coin."
    hide coin
    mc "Wow, nevermind. I guess its my lucky day after all."
    mc "..."
    mc "Well, guess its time to head back to class."
    ###play walking sfx
    scene bg school_hallway with fade
    pause


    label choices3:
        default melonbread = False
        "Go to the vending machine?"
    menu:
        "Go to the vending machine.":
            jump choices3_a
        "Continue walking.":
            jump choices3_b

    label choices3_a:
        "This time I have enough coins to buy the melon bread."
        play sound "audio/unlock.wav"
        $ melonbread = True
        mc "Got it!"
        jump choices3_common

    label choices3_b:
        mc "I wasn't that hungry anyway."
        jump choices3_common


    label choices3_common:
        pause
    mc "..."
    mc "Whats this?"
    play sound "audio/unlock.wav"
    "I spot a pair of glasses in the garbage can."
    mc "So cruel."
    ##play walking sfx
    pause
    scene bg classroom with fade
    show ct_overlay
    show ct_tues
    show ct_910
    with dissolve
    mc "Whew, I made it back to class in one piece."
    ##ts ------------------------------------------
    scene ts after_class with fade
    pause
    ##ts -----------------------------------------
    scene bg classroom with fade
    bff "Haru Chan!!!"
    show ct_overlay
    show ct_tues
    show ct_100
    with dissolve
    show bff glee with dissolve
    mc "What Naomi?"
    show bff normal
    bff "Yknow...?"
    mc "I know what?"
    bff "That guy over there..."
    mc "What?"
    hide ct_overlay
    hide ct_tues
    hide ct_100
    with dissolve
    show bff blush
    bff "Hehehehe."
    mc "Naomi, no."
    show bff glee
    bff "Tee hee."
    mc "You want me to go talk to him right?"
    show bff normal
    bff "Yes."
    mc "(Sigh) Fine."
    mc "Why do I give into your antics?"
    hide bff normal with dissolve
    "You decide to go have a friendly chat with the loner otaku."
    scene bg classroom
    show male1 normal_noglasses with dissolve
    "I approach the strange loner otaku awkwardly."
    mc "Hey."
    show male1 worried_noglasses
    "Otaku" "..."
    show male1 normal_noglasses
    "Otaku" "Hello..."
    mc "Wanna have lunch with me?"
    show male1 worried_noglasses
    "I look away, flustered."
    mc "(God, what am I doing?)"
    show male1 normal_noglasses
    "Otaku" "..."
    mc "I have something I want to show you."
    "Otaku" "Ok..."
    "I decide to take him somewhere to have a private talk"
    play music "audio/peaceful.mp3"
    scene bg school_okujou with fade
    show male1 normal_noglasses with dissolve
    "The both of us awkwardly sit in silence on the school rooftop"
    "..."
    "It's a very awkward situation."
    mc "Anyways, I found this and I thought it might be yours."
    show male1 worried_noglasses
    "Otaku" "..."
    show male1 normal_noglasses
    "I gave him the glasses."
    "He examines the glasses."
    show male1 happy_noglasses
    "He smiles."
    show male1 happy
    "He finally put on the glasses."
    "Famished, I take out my bento box."
    mc "Are you not eating?"
    show male1 worried
    "Otaku" "..."

    ##melon bread decision--------------
    if melonbread:
        mc "Here."
        "I hand him the melon bread."
        "Otaku" "..."
        show male1 happy
        "He smiles."
        male1 "Ishida."
        mc "What?"
        male1 "That's my name."
        centered "{nw}"
        scene intro ishida bg1 with dissolve
        play sound "audio/tape.wav"
        pause (0.5)
        scene intro ishida bg2 with wipeleft
        play sound "audio/flute.wav"
        scene white with dissolve
        pause (2.0)
        play sound "audio/glitter.wav"
        scene intro ishida bg3 with dissolve
        pause (4.0)
        mc "(So his name is Ishida, huh.)"
        mc "(What a nice name.)"
        scene bg school_okujou
        show male1 normal
        with dissolve
        "And so, the two of us enjoy our lunch together in peace."
    else:
        stop music fadeout 1.0
        mc "Hold on."
        "I get up and dust myself off."
        mc "I'll be back."
        scene bg school_hallway with fade
        "I arrive at the vending machine."
        play sound "audio/coin_sound.wav"
        show coin
        "Eager to get back to the school rooftop, I take out my coins."
        scene bg school_hallway
        "All the melon bread is gone."
        mc "Ahhh!"
        mc "This is the worst!"
        "I kick the vending machine."
        mc "AHHH!"
        "It topples over and smashes me to pieces."
        "Game Over"
        jump choices3_endgame
    ##Day 2 Lunch time end -------------------------

    ##ts ----------------------------------------------------
    stop music fadeout 1.0
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------

    ##Day 2 Houkago -------------------------------


    ##play afterschool bgm
    play music "audio/houkago.mp3"
    scene bg school_genkan with fade
    show ct_overlay
    show ct_tues
    show ct_345
    with dissolve
    "Well, looks like its already time to go home."
    "Can't wait to go home and play some more Otome Legends!"
    show bff blush with dissolve
    bff "Haru Chan!"
    mc "Oh! Hi Nao."
    hide ct_345
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff glee
    bff "How did it go??"
    mc "Oh cmon, could you stop bothering me about that guy for one second?"
    show bff mischievous
    bff "Ohh?"
    mc "..."
    mc "He gave me his name."
    show bff blush
    bff "I knew you had it in you."
    show bff excited
    bff "Oh! Look! He's over there! Go say hi!"
    mc "Nao!!"
    show bff glee
    bff "Just kidding!"
    show bff normal
    bff "Anyway, cya later Chiharu!"
    show bff blush
    bff "Or should I say, Ohime Sama?"
    "Translator Notes: Ohime Sama means princess."
    mc "Nao!"
    show bff glee
    bff "Hehehehe."
    hide bff with dissolve
    "My bestfriend, Naomi, disappears into the sunset as she walks home."
    mc "(I guess I should be heading out soon.)"
    stop music fadeout 1.0
    ##ts
    scene ts home with fade
    pause
    ##ts
    scene bg bedroom_yoru with fade
    mc "(I'm back at my bedroom.)"
    show bsb_blank
    mc "(Time to start from where I left off.)"
    scene bg bsb_blank with dissolve
    pause
    play sound "audio/unlock.wav"
    play music "audio/bsbtheme.mp3"
    scene bg bsb_on with dissolve
    "P.E. class had just begun."
    "Today, class is out in the fields."
    "Looks like boys track is first."
    scene bg bsb_on_senpaitachi with dissolve
    senpai2 "HOHOHOHO! You peasants think you can out run me?"
    senpai1 "Oh please! I could outrun you in my sleep!"
    senpai3 "I could out run you with broken legs and both of my eyes closed! Just wait and see you punk!"
    play sound "audio/bonebreak.wav"
    "You hear a cracking noise."
    "It seems as though the blond haired senpai karate chopped both his legs, breaking them both in the process."
    "He also closed his eyes."
    scene bg bsb_on with dissolve
    "Gym Teacher" "Get ready!"
    "The race is starting."
    "..."
    show senpai mafura with dissolve
    "Mafura Senpai takes the lead."
    "..."
    scene bg bsb_on with dissolve
    "His tight scarf chokes him and he passes out in the middle of the race."
    "..."
    show senpai matsuge with dissolve
    "Matsuge Senpai takes the lead."
    "..."
    scene bg bsb_on with dissolve
    "He broke his chin."
    show senpai kinpatsu with dissolve
    "Kinpatsu Senpai is now taking the lead."
    "..."
    "He's running with his arms and hands."
    "..."
    "I don't think this would be safe to test in real life."
    "Gym Teacher" "And we have a WINNER!"
    "..."
    "Gym Teacher" "KINPATSU!"
    "Well, I guess that kinpatsu guy ended up winning after all."
    "Translator notes: kinpatsu means blond."
    senpai3 "HAHA! I WON YOU PUNKS! NOW COME FIGHT ME!"
    mc "I commend the voice actor who was willing to voice this script."
    mc "It's just so bad; I want to punch myself."
    mc "I think I've had enough for today."
    stop music fadeout 1.0
    play music "audio/houkago.mp3"
    scene bg school_genkan with fade
    show ct_overlay
    show ct_wed
    show ct_830
    with dissolve
    "It's Wednesday."
    "..."
    "And I'm already tired of school."
    "I just want the weekend to myself."
    bff "Haru!!!"
    "It's her again."
    hide ct_830
    hide ct_wed
    hide ct_overlay
    with dissolve
    show bff blush with dissolve
    mc "What?"
    "What put her in a good mood today?"
    show bff blinking
    bff "Do you know what day it is today?"
    mc "What?"
    bff "It's ...!"
    mc "It's what?"
    hide bff blinking
    $ renpy.block_rollback()
    show bff glee
    bff "Wednesday!"
    mc "Well, whoopie doo Captain Obvious, who would have known?"
    show bff normal
    bff "And!"
    mc "And what?"
    show bff blush
    bff "Do you know what happens on Wednesday?"
    mc "Geez, what could it possibly be?"
    mc "Window cleaning day?"
    mc "Is this another one of those ridiculous holidays that you always come up with?"
    show bff worried
    bff "No."
    bff "And you couldn't be anymore wrong!"
    mc "Alright then, what is it?"
    show bff excited
    bff "It's two months away from the sports festival!"
    mc "Is that what you're excited about?"
    show bff normal
    bff "And!!"
    mc "And?"
    show bff glee
    bff "Today is the day we get to pick our assigned sports!"
    mc "..."
    show bff worried
    bff "What is it Haru Chan?"
    "Oh snap..."
    "I dread this time of year like the horrors of the bubonic plague."
    "I'm not good at sports."
    "I managed to chicken out last time by faking a cold, but then I got in trouble when my mom found out I wasn't really sick."
    "I don't think she'll buy it this time."
    mc "Ahahaha... is that so?"
    mc "Right, right."
    mc "How could I forget about the sports festival?"
    show bff worried
    bff "Cmon, the sports festival only happens once a year, yknow!"
    show bff excited
    bff "I'm definitely gonna win this time!"
    mc "Haha, yea. I'm sure you'll win this one."
    show bff normal
    bff "Well?"
    mc "Well, what?"
    show bff blush
    bff "Won't you be my partner for the three-legged race?"
    mc "NO NO NO NO NO NO NO NO!"
    show bff worried
    bff "???"
    "Naomi looks puzzled."
    mc "Oh, no! I mean ...!"
    mc "(Oh snap, how do I think my way out of this one?)"
    mc "(Every year before the sports festival, Nao makes me train like crazy everyday for weeks!)"
    mc "(I would say no but...)"
    mc "(She tends to get really scary when this time of year comes.)"
    mc "(QUICK! I gotta think my way out of this one!)"
    mc "(Oh!)"
    mc "(I got it!)"
    mc "(Ishida!)"
    mc "Hahaha... I'm sorry, I don't think I can be your partner this year."
    show bff sad
    bff "What? But we're partners every year!"
    bff "And you didn't even get to participate last year because you were sick, remember?"
    mc "Yea... I know. But I was thinking about asking Ishida to do the three-legged race with me."
    show bff evil_smile
    bff "Oh...?"
    show bff excited
    bff "Well why didn't you say so sooner?"
    show bff glee
    bff "Alright, I guess I'll see ya after class."
    show bff worried
    bff "But you have to promise me next year that we'll be partners, okay?"
    mc "Alright, alright."
    hide bff with dissolve
    mc "(Whew, I'm glad I made my way out of that one.)"
    mc "(The thing about Nao is that, despite the fact she is excellent at sports,
     almost no body wants to team up with her because of how intense she usually
      is during the sports festival.)"
    mc "(I dodged a bullet with that one.)"
    mc "(I just have to make sure that I get picked before everyone else does.)"
    mc "(I don't wanna be left alone with Nao...)"
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    "It's time for class."
    stop music fadeout 1.0
    ##Day 3 Class -------------------------------------------------
    play music "audio/classtime.mp3"
    scene bg classroom with fade
    show ct_overlay
    show ct_wed
    show ct_830
    with dissolve
    "Sensei" "Alright everyone! Today, we're going to be assigning everyone to a sport!"
    "Sensei" "Anyone want to go first?"
    play sound "audio/chalkboard.wav" fadein 1.0
    "Almost all the students raise their hands as quickly as they can."
    "They're all staring at Nao."
    "They're all quivering and shaking."
    "My best guess is that nobody wants to be her partner."
    "She's normally calm and collected, but it's as if the sports festival changes her into a completely different person."
    stop sound fadeout 1.0
    "I need to stay calm."
    mc "(Breathe)"
    "Sensei" "Harumiya!"
    mc "YES YES?! I'M HERE!"
    "Sensei completely catches me off guard."
    "Sensei" "Did you decide on what you wanted to do?"
    mc "Oh! Yes! Three-legged race!"
    "Sensei" "Alright, and anyone want to be her partn-{nw}"
    mc "ISHIDA!"
    show male1 worried with dissolve
    male1 "!"
    scene bg classroom with dissolve
    "Sensei" "Alright, three-legged race, Harumiya and Ishida it is then."
    "YES! FINALLY! A partner thats not Nao!"
    mc "(I'm sorry Nao! I love you and I cherish our friendship but anytime near or during sports festival
    is the last time I want to hang out with you!)"
    mc "(No hard feelings right?)"
    stop music fadeout 1.0
    ##Day 3 Class End -------------------------------------------------

    ##Day 3 Lunch -----------------------------------------------------------
    scene bg classroom with fade
    "Finally time for lunch."
    "Perhaps I should go buy some green tea and melon bread at the vending machine."
    scene bg school_hallway with fade
    pause
    show ct_overlay
    show ct_wed
    show ct_105
    with dissolve
    "I walk towards the vending machine."
    play sound "audio/coin_sound.wav"
    "I buy the melon bread."
    "..."
    "But unfortunately I don't have enough to buy a drink."
    "Guy" "OI!"
    "I hear some guy screaming across the hallway."
    hide ct_105
    hide ct_wed
    hide ct_overlay
    with dissolve
    if not persistent.yuusuke:
        show male3 angry with dissolve
        "Guy" "I said no running in the hallways!"
        hide male3 angry
        show male2 worried
        "Other guy" "Relax dude! I just wanted to go buy a soda."
        hide male2 worried
        show male3 annoyed
        "Guy" "I don't know why I put up with you. You always end up getting into all sorts
        of trouble and end up dragging me along with you!"
        hide male3 annoyed
        show male2 normal
        "Other Guy" "Well, maybe you should chillax and let me buy you a soda."
        "Other Guy" "It was your idea wasn't it?"
        "Other Guy" "After all, its not my fault you got rejected now is it?"
        hide male2 normal
        show male3 blush
        "Guy" "Sh- Shut your mouth!"
        hide male3 blush
        show male2 normal
        "Other Guy" "Relax, I'm on your side remember? We made a deal that if she rejected you I'd owe you a soda."
        show male2 worried
        "Other Guy" "I honestly thought you had a chance dude, I was rooting for ya."
        hide male2 worried
        show male3 worried
        "Guy" "I guess..."
        hide male3 worried
        show male2 happy
        "Other Guy" "Now, do you want cherry or grape?"
        hide male2 happy
    show male4 happy with vpunch
    $ renpy.vibrate(.5)
    "Some Weird Kid" "HIROHIRO HIRO!!"
    hide male4 happy
    show male3 blush
    "Guy" "AHHH! THATS NOT MY NAME!!"
    "Hiro" "IT'S HIRO! HIRO!!!"
    show male3 angry
    "Hiro" "Hasegawa Takahiro, you numbskull!"
    scene bg school_hallway with dissolve
    "I get the feeling that I'm intruding on a very personal conversation."
    "Perhaps I should go upstairs and eat my lunch alone on the rooftop."
    "Surely Nao is too busy obsessing over the sports festival so it would be best not to bother her right now."

    ##Ishida Okujou Scene##-----------------------------------------------
    scene bg school_okujou with fade
    play music "audio/peaceful.mp3"
    "I thought I'd be alone on the rooftop."
    "..."
    "But surprisingly Ishida is here."
    show male1 worried
    male1 "..."
    male1 "H-H-How did you know I was here?"
    mc "I didn't."
    male1 "Then... why are you-"
    show male1 normal
    male1 "..."
    mc "Relax, I just wanted a quiet place to eat."
    show male1 blush
    male1 "Oh. . . I-I see."
    show male1 normal
    mc "Mind if I sit next to ya?"
    show male1 worried
    male1 "..."
    show male1 normal
    male1 "No."
    "He looks flustered."
    male1 "..."
    male1 "By the way..."
    mc "Hm?"
    male1 "Here."
    "He hands you a can of green tea."
    show male1 worried
    male1 "I-I... I was planning on giving it to you earlier but-"
    male1 "but..."
    male1 "..."
    pause
    mc "But what?"
    show male1 normal
    male1 "I was too shy."
    show male1 blush
    male1 "Its! Its for yesterday!"
    male1 "Th-Thanks for the melon bread; I really appreciated it!"
    pause
    male1 "..."
    show male1 happy
    "He gives an awkward smile."
    pause
    show male1 normal
    mc "Oh... that? I just happened to have an extra one on hand!"
    mc "You really don't have to thank me, but thanks for the green tea! I really was craving for one!"
    "..."
    show male1 happy
    pause
    "I feel an awkward silence fill the air."
    show male1 normal
    male1 "By the way..."
    mc "?"
    male1 "Why did you pick me?"
    male1 "I mean, for the three-legged race?"
    mc "Oh, that?"
    "If I told him that it was because my best friend kept trying to pair me up with him I'd die of embarrassment."
    mc "My best friend, she kind of gets intense during sports festival season."
    mc "And its a REAL pain to deal with."
    mc "To be honest, I'm not really good at sports"
    show male1 happy
    "Ishida smiles."
    male1 "Me neither."
    male1 "..."
    pause
    mc "... hey."
    show male1 normal
    male1 "..."
    mc "I got this crazy idea."
    male1 "?"
    mc "Lets win."
    show male1 worried
    male1 "W-what?!"
    mc "Yknow, the other day, I saw a couple of guys pick on ya earlier."
    show male1 blush
    male1 "!?"
    mc "I just thought, maybe... yknow?"
    male1 "... k-k-know wha...?"
    mc "Maybe, just maybe, if we beat them in a race, we could show them who's boss!"
    show male1 normal
    male1 "..."
    mc "What do you say?"
    show male1 happy
    male1 "Sure."
    mc "Great! Give me your phone number and its settled!"
    show male1 worried
    male1 "M-m-my phone number?!"
    "I eagerly take his phone and add myself to his contacts."
    "I smiled."
    mc "Call me anytime you're free! We could practice running around the track after school sometime!"
    show male1 blush
    male1 "Hahaha..."
    show male1 happy
    male1 "Chiharu, huh?"
    mc "?"
    male1 "So thats your name?"
    mc "Yep, the one and only!"
    "..."
    "The two of us sit awkwardly in silence."
    stop music fadeout 1.0
    play sound "audio/schoolchime1.wav"
    show ct_overlay
    show ct_wed
    show ct_120
    with dissolve
    "The bell rings"
    "Time for class."
    mc "Ok, I'll guess I'll see ya later then!"
    ##ts---------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts----------------------------------------------------------
    play music "audio/houkago.mp3"
    scene bg school_genkan with fade
    show ct_overlay
    show ct_wed
    show ct_400
    with dissolve
    "After classes were over, I decided to head over to the shoe lockers."
    "..."
    "Ishida."
    "I wonder how he's doing right now."
    hide ct_400
    hide ct_wed
    hide ct_overlay
    with dissolve
    centered "{nw}"
    show sm with dissolve
    pause
    play sound "audio/unlock.wav"
    show sm_400 with dissolve
    centered ""
    "After I checked my contacts I silently smiled to myself."
    mc "Welp, its time for me to go home now."
    stop music fadeout 1.0
    ##ts -------------------------------------------------------
    scene bg blank with fade
    centered "{size=50}{cps=12} A week later{/cps}{/size}"
    ##ts -----------------------------------------------------
    play music "audio/classtime.mp3"
    scene bg classroom with fade
    "It's been a week since I agreed to partner with Ishida for the sports festival."
    "I wonder how he's doing now."
    bff "Haru!"
    "It's Nao."
    mc "Oh, hey Nao."
    show ct_overlay
    show ct_mon
    show ct_830
    with dissolve
    show bff glee with dissolve
    bff "Watcha doin'?"
    mc "Nothing much."
    show bff normal
    bff "How far did you get in the game?"
    mc "I haven't touched it since last week."
    show bff worried
    bff "Oh, cmon."
    bff "Yknow you have to give me my game back soon."
    hide ct_830
    hide ct_mon
    hide ct_overlay
    with dissolve
    mc "Ok, fine. I'll finish it this week."
    show bff blush
    bff "I'll give you two weeks."
    mc "Wait, why?"
    show bff glee
    bff "To give you time to go through all the routes."
    show bff normal
    bff "Yknow, you gotta go through the otaku route first to unlock all the other characters."
    mc "What?"
    show bff glee
    bff "Nothing."
    show bff normal
    "I don't remember there being an otaku character in the game though..."
    "What is she on about?"
    play sound "audio/schoolchime1.wav"
    "The bell rings"
    "It's time for class."
    show bff blush
    bff "Alrighty, cya after class, Haru chan!!!"
    ##ts --------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts --------------------------------------------------------
    scene bg classroom with fade
    show ct_overlay
    show ct_mon
    show ct_930
    with dissolve
    "I ended up sleeping throughout the entire lesson."
    mc "(Oh snap, I slept throughout the entire thing!)"
    mc "(I wonder if I could ask Nao if I could borrow her notes.)"
    mc "Nao!"
    hide ct_930
    hide ct_mon
    hide ct_overlay
    with dissolve
    show bff normal with dissolve
    bff "What is it Haru chan?"
    mc "You think I could borrow your notes?"
    show bff worried
    bff "..."
    show bff glee
    bff "No."
    show bff normal
    mc "Awww, why?"
    show bff worried
    bff "You always borrow my notes."
    bff "Why don't you get some proper sleep instead?"
    bff "You're always up until like 2am in the morning."
    mc "H-how do you know?"
    show bff normal
    bff "You always message me during that time."
    show bff glee
    bff "Whenever you need help with assignments usually."
    mc "Thats cause I usually get my work done at that time!"
    show bff normal
    bff "Why don't you just do your assignments in the day instead?"
    mc "I can't focus during the day..."
    show bff worried
    bff "Well then its not my fault you always sleep during class."
    show bff normal
    mc "Oh, cmon Nao!"
    mc "If you lend me your notes I'll buy you a melon bread!"
    show bff worried
    bff "I'm kind of tired of melon bread to be honest."
    mc "..."
    mc "A chocolate bread!"
    show bff mischievous
    bff "hmmmm?"
    mc "A STRAWBERRY! HOW ABOUT A STRAWBERRY ONE?!"
    show bff blush
    bff "Then we have a deal."
    show bff worried
    bff "But you gotta promise me, bring it back before school is over okay?"
    show bff glee
    bff "And tell me more about you and Ishida kun, hehehe!"
    hide bff with dissolve
    "..."
    "Oh yea."
    "Today I invited Ishida to run around the track with me."
    "Maybe I should hang out with him."
    "But then again, I gotta catch up on what I missed from class."
    "I guess I'm gonna spend all break copying from Nao's notes."
    "..."
    "She has a point though."
    "Maybe I rely too much on her."
    stop music fadeout 1.0
    ##ts ------------------------
    scene ts after_school with fade
    pause
    ##ts -----------------------------
    play music "audio/peaceful.mp3"
    scene bg track with fade
    show sm with dissolve
    pause
    play sound "audio/unlock.wav"
    hide sm
    show sm_400
    centered ""
    "I look at my phone to check the time."
    "I wonder where he is."
    male1 "I'm here!"
    centered "{nw}"
    hide sm_400 with dissolve
    show male1 gym_exhausted with dissolve
    "There he is!"
    "He looks exhausted."
    "Did he run all the way here?"
    show male1 gym_normal
    male1 "Sorry I'm late."
    mc "There ya are!"
    "I hand him a bottle of water."
    scene mc smile_track1 with dissolve
    pause
    mc "I thought you'd might need this!"
    mc "It's a bottle of water in case you get thirsty."
    mc "We're gonna be running all day so stay hydrated!"
    mc "Just refill it when you run out, there is a water fountain over there!"
    male1 "Th-Thanks I guess..."
    scene bg track with dissolve
    show male1 gym_blush
    male1 "..."
    show male1 gym_happy
    pause
    mc "Oh!"
    show male1 gym_worried
    male1 "!"
    mc "I got something!"
    "After rummaging through my bag, I take out a ribbon."
    mc "I think we should practice our coordination first."
    show male1 gym_normal
    male1 "Ah, right."
    mc "..."
    mc "That should do it!"
    "I tie my leg with Ishida's"
    mc "Alright!"
    mc "Ready! Set! Go!"
    male1 "!!!"
    scene bg blank with fade
    #play sound "audio/thump.mp3"
    pause(1.0)
    "The both of us fall over."
    scene bg track with fade
    show male1 gym_worried with dissolve
    male1 "Sorry."
    mc "Haha... Lets try again."
    mc "Ready! Set! Go!"
    stop music fadeout 1.0

label race:
    scene bg blank with fade
    play music "audio/ponder_ost.mp3" fadein 1.0
    show racestart_video with dissolve
    centered "{color=#101151}{size=+15}{b}{fast}Click to make progress on the track field!!{w=2.0}{/b}{/size}{/color}"
    hide racestart_video with dissolve
    show click with fade
    centered "{w=1.0}"
    scene bg blank
    call screen rclicker with dissolve

label rwin:
    $ renpy.pause(2, hard=True)
    $ rpoints = 50
    $ persistent.rclicker = True
    scene bg blank
    scene white with fade
    call screen rwin_screen with dissolve

label rlost:
    $ rpoints = 50
    scene bg blank
    scene white with fade
    call screen rlose_screen with dissolve

label backtoclass1:
    hide screen skip_button1
    hide screen rclicker with fade
    stop music fadeout 1.0
    ##Minigame sequence end --------------------------------------------------
    play music "audio/peaceful.mp3"
    scene bg track with fade
    show male1 gym_exhausted
    male1 "Haaah haah hah."
    mc "Man...."
    mc "You get exhausted real quick don't ya..."
    mc "Well, it's a good thing that speed isn't that important for a three-legged race."
    mc "Still, maybe next time we should practice running."
    mc "Maybe we should practice at least 3 times a week?"
    show male1 gym_normal
    male1 "!"
    mc "Well, its time to get going."
    mc "..."
    show male1 gym_happy
    male1 "That was fun."
    mc "..."
    mc "I had fun too."
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi ishida with dissolve
    show progress0 with dissolve
    pause 1.0
    show heart_progress1
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart from Ishida!{/size}"
    scene bg track with fade
    show male1 gym_happy with dissolve
    "..."
    pause
    show male1 gym_normal
    mc "Ahh! Look at the time!"
    mc "I gotta get home before it gets too late"
    mc "Cya next time!"
    mc "Bye!!"
    stop music fadeout 1.0
    ##ts--------------------------------------------------
    scene ts home with fade
    pause
    ##ts--------------------------------------------------
    scene bg bedroom_yoru with fade
    mc "..."
    mc "(I can't believe I said all of that.)"
    mc "..."
    mc "(Oh my god, what am I getting so nervous for?)"
    mc "(Its not like I actually intend on pairing up with him or anything.)"
    mc "(I should calm down.)"
    mc "..."
    mc "(He IS kind of cute.)"
    mc "(Just a little, I guess...)"
    mc "..."
    mc "(No, no, no, no, no!)"
    mc "(Absolutely not! Ishida is just a friend.)"
    mc "(JUST a friend.)"
    mc "(Theres NO WAY I would fall for an otaku.)"
    mc "(Absolutely no way!)"
    mc "..."
    mc "(I should play some games to get my mind off of it.)"
    mc "(Yea, that would probably be for the best.)"
    "I took up the handheld BSB that I borrowed from Naomi."
    show bsb_blank
    scene bg bsb_blank with dissolve
    play sound "audio/unlock.wav"
    scene bg bsb_on with dissolve
    play music "audio/bsbtheme.mp3"
    "(After gym class all the senpais except for Mafura Senpai had to go to the hospital for intensive care)"
    "(A week has passed since then)"
    "(You are at the school shoe lockers preparing to go home)"
    shoujo1 "Huh, whats this?"
    "(You received a note in your locker)"
    shoujo1 "It's a note to meet someone at the school rooftop?"
    shoujo1 "Oh my, is it my secret admirer?"
    shoujo1 "I HAVE TO GO MEET THEM!"
    "(You run up the stairs and rush to the school rooftop)"
    shoujo1 "!"
    show senpai mafura with dissolve
    senpai1 "Hey."
    senpai1 "Soko no shoujo yo!"
    shoujo1 "!!!"
    senpai1 "I have something to ask you."
    shoujo1 "(OMG! Is this a confession?)"
    shoujo1 "(This HAS to be a confession!)"
    senpai1 "I-"
    shoujo1 "!"
    senpai1 "I!!!"
    shoujo1 "!"
    senpai1 "I need your help."
    shoujo1 "(...)"
    "(The shoujo feels disappointed)"
    senpai1 "You see, my friend Matsuge Senpai... He doesn't take defeat very well."
    senpai1 "And... I know we got off on the wrong foot but-"
    senpai1 "But he hasn't come out of his room for weeks."
    senpai1 "I think he's depressed."
    senpai1 "Do you think, maybe you could convince him to come back to class?"
    "(Senpai looks at you in a pleading manner)"
    shoujo1 "Ok. I'll see what I can do."
    senpai1 "Thanks!"
    hide senpai mafura with dissolve
    scene bg bsb_on with fade
    "(You arrive at Matsuge Senpai's house)"
    shoujo1 "Matsuge Senpai!"
    senpai2 "..."
    show senpai matsuge with dissolve
    senpai2 "What are you doing here?"
    shoujo1 "..."
    shoujo1 "I got you some chocolates."
    shoujo1 "Everyone at school is worried about you and they're asking for you to come back."
    senpai2 "Why would you be concerned for a pathetic loser like me?"
    shoujo1 "You're not a pathetic loser."
    senpai2 "I am, I lost the race."
    shoujo1 "You tried your best."
    shoujo1 "Thats all that matters!"
    shoujo1 "They say that the only way to succeed is to know how to fail first."
    senpai2 "..."
    senpai2 "Yknow what! You're right!"
    senpai2 "No more hiding in the dark!"
    senpai2 "I'm coming back to school tomorrow!"
    senpai2 "OHOHOHO! And I'll make the greatest comeback ever just you wait!"
    senpai2 "Thanks Chiharu Chan!"
    shoujo1 "... who?"
    senpai2 "Oh! I mean you! Thank you!"
    senpai2 "I will see you tomorrow! HOHOHO!"
    scene bg bsb_on with dissolve
    mc "..."
    mc "He said my name."
    mc "That was weird..."
    mc "Maybe I was just imagining things?"
    mc "Oh well, I'm calling it a night."
    mc "I'll finish this game later."
    stop music fadeout 1.0

    ##ts --------------------------------------------------
    scene ts a_few_days_later with fade
    pause
    ##ts -----------------


    play music "audio/classtime.mp3"
    scene bg classroom with fade
    show ct_overlay
    show ct_thurs
    show ct_830
    with dissolve
    bff "Harurin!"
    show bff excited
    mc "What is it this time Nao?"
    show bff blush
    bff "I won!!"
    mc "You won what?"
    show bff excited
    bff "I won Ikemen Senpai from the daily Otome Legends gacha!"
    show bff glee
    bff "Its a super rare!"
    mc "gacha?"
    hide ct_830
    hide ct_thurs
    hide ct_overlay
    with dissolve
    show bff worried
    bff "Oh cmon, Haru Chan."
    bff "You don't know what a gacha is?"
    mc "No, not that."
    mc "I just didn't know they had a gacha."
    show bff excited
    bff "It's on their app!"
    mc "There's an app?"
    show bff worried
    bff "Geez, you don't know alot of things don't you Haru Chan?"
    mc "..."
    show bff glee
    bff "Anyways, how are things going with Ishida Kun?"
    mc "Great."
    mc "..."
    mc "I-I mean fine I guess."
    show bff mischievous
    bff "Oh, Haru Chan."
    show bff glee
    bff "You just can't be honest with yourself can you?"
    mc "..."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Well, it's time for class!"
    show bff blush
    bff "Cya at lunch!"
    bff "By the way, don't forget that you still have to buy me that strawberry bread!"
    hide bff normal with dissolve
    ## Week2 Day 2 Morning end ------------------------------------------------

    ## Week2 Class ------------------------------------------------------------
label doodlegame:
    scene bg blank with fade
    play music "audio/ponder_ost.mp3"
    ##show drawstart_video with dissolve
    centered "Click the screen to doodle during class{vspace=30}
    instead of doing your work like you should be doing!!" with dissolve
    ##hide drawstart_video with fade
    show click with fade
    pause
    hide click with fade
    scene bg blank
    call screen clicker with fade
label win:
    $ renpy.pause(2, hard=True)
    $ points = 300
    $ persistent.clicker = True
    scene bg blank
    scene white with fade
    call screen win_screen with dissolve

default lostcounts = 0

label lost:
    $ lostcounts += 1
    if lostcounts >= 11:
        jump win
    if lostcounts == 10:
        scene bg blank with fade
        centered ". . ."
        centered "At this point you're testing my patience."
        centered "Get out of here."
        $ achievement.grant("ten_achievement")
        $ achievement.sync()
        jump backtoclass2
    if lostcounts >= 5:
        scene bg blank with fade
        centered "Dude, you failed like 5 times already, I lost track."
        centered "At this point I just I feel bad for you."
        centered "You still failed even after I gave you a 300 point headstart."
        centered "So I'm just gonna like, let you win this one."
        jump win
    scene bg blank with fade
    centered "You lost."
    centered "You never got to finish your doodles by the end of class."
    centered "Shame on you."
    $ points = 300
    scene bg blank
    scene white with fade
    call screen lose_screen with dissolve

    ## Week2 Day 2 Lunch ------------------------------------------------------
label backtoclass2:
    stop music
    ##ts --------------------------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts --------------------------------------------------------------------

    play music "audio/classtime.mp3" fadein 1.0
    scene bg classroom with fade
    bff "Haruuuuu Tan!!"
    show ct_overlay
    show ct_thurs
    show ct_100
    with dissolve
    show bff blush with dissolve
    mc "?"
    bff "Have lunch with me today!"
    mc "... you're not going to bother me about Ishida today?"
    show bff normal
    bff "Nope!"
    "Yes!!!"
    "I'm finally free!"
    show bff glee
    bff "We're going to go bother Ishida kun instead!"
    mc "Wait, what do you mean by tha-{nw}"
    show bff blush
    bff "Ishida!"
    hide bff blush
    hide ct_100
    hide ct_thurs
    hide ct_overlay
    with dissolve
    show male1 worried with vpunch
    $ renpy.vibrate(.5)
    male1 "!!!"
    hide male1 worried
    show bff blush
    bff "Won't you come have lunch with us?!"
    hide bff blush
    mc "..."
    show male1 happy
    male1 "Sure."
    stop music fadeout 1.0

    ##ts --------------------------------------------------------------------
    scene bg blank with fade
    "And just like that Ishida started having lunch with the three of us."
    ##ts --------------------------------------------------------------------

    ##Okujou wk2d2 -----------------------------------------------------
    play music "audio/peaceful.mp3" fadein 1.0
    scene bg school_okujou with fade
    mc "(Oh god.)"
    mc "(What have I gotten myself into?)"
    show bff glee
    bff "Wow! The view is amazing up here!"
    bff "Don't you think it's romantic?"
    mc "!!!"
    hide bff glee
    show male1 worried
    male1 "!!!"
    hide male1 worried
    show bff blush
    bff "Hahaha! Just kidding!"
    show bff normal

    label choices4:
        bff "Anyways, what do you guys do up here?"
    menu:
        "Nothing much.":
            jump choices4_a
        "Vent about our problems.":
            jump choices4_b
        "We stare at the sun until we go blind.":
            jump choices4_c

    label choices4_a:
        show bff worried
        bff "Ehhh, thats so boooring."
        bff "Don't you guys do anything interesting?"
        show bff blush
        bff "Yknow, like flirting maybe?"
        male1 "..."
        mc "..."
        mc "No."
        show bff worried
        bff "Mood killer much?"
        "That should be my line."
        "(Sigh)"
        "Why does she have to embarrass me like this all the time?"

        jump choices4_common

    label choices4_b:
        show bff excited
        bff "Oh, that sounds deep!"
        show bff normal
        bff "So do you guys tell eachother secrets and stuff like that?"
        show bff glee
        bff "Or maybe fortune telling!"
        show bff worried
        bff "Or maybe you guys are like those edgy middle schoolers that ponder
        about the meaning of life and talk about pretentious things..."
        bff "... like how life has no meaning or how your inner spirit is a wolf."
        show bff excited
        bff "If I had an inner spirit! I would definately be a unicorn!"
        mc "Unicorns don't exist Nao."
        show bff worried
        bff "Really? Then prove it!"
        show bff glee
        bff "Just kidding, I know they don't exist."
        jump choices4_common

    label choices4_c:
        show bff worried
        bff "..."
        show bff normal
        bff "I'm not even gonna ask..."
        jump choices4_common


    label choices4_common:
        show bff worried
        bff "Anyway..."
        "We all spend the remaining time of lunch talking on the rooftop."

    stop music fadeout 1.0
    ##Week2 Day2 Lunch end --------------------------------------------------

    ##ts --------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts --------------------------------------------------------------------

    ##Week2 Day 2 Houkago end -----------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0
    scene bg school_genkan with fade
    show ct_overlay
    show ct_thurs
    show ct_400
    with dissolve
    show bff blush with dissolve
    bff "Harurinrin!!!"
    mc "Whats up Nao?"
    show bff normal
    bff "Wanna go to the baseball field today?"
    mc "Sure."
    bff "Great!"
    hide ct_400
    hide ct_thurs
    hide ct_overlay
    with dissolve
    show bff glee
    bff "Just let me invite someone real quick."
    show bff blush
    bff "Ishida!"
    hide bff blush
    show male1 worried
    male1 "!!!"
    hide male1 worried
    show bff glee
    bff "Why don't you hang out with us?"
    bff "Me and Haru are going to the baseball field!"
    mc "..."
    hide bff glee
    show male1 blush
    male1 "... ok, sure."
    hide male1 blush
    show bff normal
    bff "Then it's settled!"
    show bff blush
    bff "Cmon, lets go!"
    stop music fadeout 1.0
    scene bg blank with fade
    "And so we all played at the baseball field until sunset."
    "It was a very fun and eventful day"
    ##ts --------------------------------------------------------------------
    scene bg blank with fade
    centered "Another week later."
    ##ts --------------------------------------------------------------------
    scene bg classroom with fade
    show ct_overlay
    show ct_thurs
    show ct_830
    with dissolve
    bff "Haru Chan!!!"
    "It's Naomi."
    show bff normal with dissolve
    mc "?"
    show bff glee
    bff "How are things going with Ishida?"
    show bff normal
    mc "I'm not sure."
    mc "We've been practicing for a couple of days, but then suddenly he stopped showing up."
    hide ct_830
    hide ct_thurs
    hide ct_overlay
    with dissolve
    show bff worried
    bff "... Is he okay?"
    mc "I'm not sure he hasn't been responding to my messages."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "I'll talk to you later about it, okay?"
    hide bff with dissolve
    "Naomi sits back at her desk."
    "Ishida..."
    "I wonder if he's doing alright."
    ##Week4 Day1 Morning end --------------------------------------------------

    ##ts --------------------------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts --------------------------------------------------------------------

    ##1 Month later Day 1 After school -------------
    play music "audio/houkago.mp3"
    scene bg school_genkan with fade
    mc "Hey Nao!"
    show ct_overlay
    show ct_thurs
    show ct_400
    with dissolve
    show bff normal with dissolve
    bff "Yeah, Haru?"
    mc "Where do you think we should hang out today?"
    show bff blush
    bff "Hmmm, maybe go shopping?"
    mc "Nah, I'm broke and I don't have any money."
    show bff worried
    mc "..."
    mc "How about the baseball field?"
    show bff glee
    bff "Sounds like a plan, but shouldn't we go get something to eat first?"
    hide bff
    show bff blinking
    mc "You're right."
    mc "How about the burger joint from across the street?"
    hide ct_400
    hide ct_thurs
    hide ct_overlay
    with dissolve
    show bff excited
    $ renpy.block_rollback()
    bff "Oooooh! I haven't had one of those in a while!"
    show bff normal
    mc "Yea, me neither."
    mc "I don't really go that often, my mom always tells me to stay away from eating fast food."
    show bff sad
    bff "Your mom must really care about you, huh?"
    show bff depressed
    mc "..."
    mc "Sorry for bringing it up."
    show bff worried
    bff "Oh! Don't worry about it."
    show bff normal
    bff "That stuff happened ages ago when we were kids remember?"
    mc "Yeah, we were neighbors back then."
    mc "I used to visit your house all the time."
    mc "When your mom would always make sandwiches for us."
    show bff blush
    bff "Yea, my mom's cooking was some of the best food I'd ever have."
    show bff worried
    bff "She didn't like it whenever I ate junk food either."
    bff "..."
    show bff glee
    bff "Anyways we should get going now."
    "Nao and I decided to go get some burgers before playing at the baseball field."
    stop music fadeout 1.0
    ## 1 month later Day 1 houkago end ---------

    ##ts --------------------------------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts --------------------------------------------------------------------

    ## 1 month later Day 1 outside ----------------
    scene bg baseball with fade
    play music "audio/houkago.mp3"
    "It's time to go home."
    show bff blinking with dissolve
    bff "It's getting late."
    mc "Yea."
    bff "We should get going now."
    $ renpy.block_rollback()
    show bff worried
    bff "Yknow, before it gets too dark."
    show bff glee
    bff "I had alot of fun today."
    mc "Me too."
    show bff normal
    bff "..."
    show bff blush
    bff "Alrighty then, cya later, alligator!"
    hide bff blush with dissolve
    "Naomi heads off into the sunset."
    mc "(I should get going too)"
    scene bg shopping_district with fade
    pause
    mc "(Perhaps I should visit the shopping district before heading home.)"
    "I spot a familiar figure coming out of the internet cafe."
    stop music fadeout 1.0
    scene bg shopping_district with hpunch
    $ renpy.vibrate(.5)
    mc "!!!"
    mc "Ishida?!"
    show male1 ikemen_shocked with dissolve
    male1 "..."
    mc "Where have you been?! Everyone at school is worried about you!"
    mc "Where are your glasses?!"
    mc "Why are you dressed like that?!"
    male1 "..."
    mc "Why haven't you been responding to my messages?!"
    mc "Ishida! What happ-{nw}"
    show male1 ikemen_angry
    play music "audio/sad_theme.mp3" fadein 1.0
    male1 "Go away."
    male1 "I don't want to hear it."
    show male1 ikemen_annoyed
    male1 "You think I like tailing around you every second?!"
    male1 "Just leave me alone."
    mc "..."
    mc "Why didn't you come to school yesterday?"
    mc "Or even the day before that?!"
    mc "You've been missing all week!"
    mc "What's up with that?!"
    mc "This entire time you've been skipping school and playing video games at the internet cafe when everyone is worried about you?!"
    show male1 ikemen_angry
    male1 "And who's worried about me?"
    mc "I AM!"
    show male1 ikemen_shocked
    male1 "..."
    show male1 ikemen_annoyed
    male1 "... Yea right, don't make me laugh."
    mc "Excuse me?"
    male1 "The only reason you approached me in the first place was because you thought I was an easy target."
    male1 "Or maybe even worse, you felt sorry for me."
    show male1 ikemen_angry
    male1 "Well guess what! I'm not some broken plaything for you to fix!"
    show male1 ikemen_annoyed
    mc "You know what..."
    mc "You are absolutely correct."
    show male1 ikemen_annoyed
    mc "You are a sad pathetic loser."
    mc "And I DID only approach you because I felt sorry for you!"
    mc "BECAUSE WHO WOULD WANT TO BE FRIENDS WITH A CREEPY SWIRLY GLASSES OTAKU LIKE YOU?!"
    show male1 ikemen_angry
    mc "..."
    show male1 ikemen_angry
    male1 "I think we're done talking here."
    show male1 ikemen_annoyed
    male1 "Just, leave me alone okay?"
    hide male1 with dissolve
    "..."
    "Did I just say that?"
    "What have I done?"
    stop music fadeout 1.0
    pause
    ## 1 month later Day 1 outside end ----------------

    ## 1 month later Day 1 bedroom ----------------------------
    scene bg bedroom_yoru with fade
    "..."
    mc "I can't believe I said that."
    mc "Oh my god."
    mc "He must hate me now."
    "I sulked into my bed frustrated at myself and Ishida."
    mc "(Sigh)"
    mc "What am I gonna do?"
    ## 1 month later Day 1 bedroom end--------------------------------------

    ##ts --------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts --------------------------------------------------------------------

    scene bg classroom with fade
    play music "audio/classtime.mp3"
    "Before class"
    bff "Hey!" with vpunch
    $ renpy.vibrate(.5)
    mc "..."
    show ct_overlay
    show ct_fri
    show ct_830
    with dissolve
    show bff blush with dissolve
    bff "Good Morning my beloved Haru Chan!!!"
    mc "What is it Nao?"
    show bff worried
    bff "You could be a little more enthusiastic."
    show bff glee
    bff "Guess who won an exclusive copy of Otome Legends!"
    show bff blush
    bff "I won it in a raffle!"
    bff "Aren't I the luckiest girl on earth?"
    mc "I'm not in the mood Nao."
    hide ct_830
    hide ct_fri
    hide ct_overlay
    with dissolve
    show bff worried
    bff "... killjoy."
    mc "..."
    bff "..."
    show bff sad
    bff "Haru, whats wrong?"
    mc "I got into a fight with Ishida."
    show bff worried
    bff "..."
    bff "What happened?"
    mc "..."
    "I almost start to cry just thinking about the events that occured yesterday."
    mc "After we played at the baseball field..."
    mc "On my way home, I saw him."
    mc "... I saw him walk out of an internet cafe and..."
    mc "I was just so upset and angry! I ended up saying things I shouldn't have said."
    show bff blinking
    bff "I'm sure he'll be okay, Haru."
    bff "Maybe you should try apologizing."
    bff "I'm sure he'll appreciate it."
    show bff glee
    bff "I'm sure he didn't just skip school just for the sake of it."
    bff "Just like how you lashed out at him, I'm sure you didn't do it just because."
    bff "He must have his reasons, I'm sure you have yours."
    mc "..."
    play sound "audio/schoolchime1.wav"
    "(The bell rings)"
    show bff normal
    bff "Oh, looks like its time for class."
    show bff glee
    bff "Anyways, I hope things go well with you and Ishida!"
    show bff blush
    bff "Bye!!"
    stop music fadeout 1.0
    ## Week5 Day 1 Morning end --------------------------------------------

    ##ts -------------------------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts -------------------------------------------------------------------

    ## Week5 Day 1 lunch --------------------------------------------------
    scene bg school_okujou with fade
    show ct_overlay
    show ct_fri
    show ct_105
    with dissolve
    "(...)"
    "(It's lonely without Ishida.)"
    "(I wonder what he's doing.)"
    play sound "audio/vibrate.wav"
    $ renpy.vibrate(.5)
    "(!!!)"
    "(It's a notification!)"
    hide ct_105
    hide ct_fri
    hide ct_overlay
    with dissolve
    centered "{nw}"
    show sm with dissolve
    play sound "audio/unlock.wav"
    show sm_n with dissolve
    "!!!"
    centered "{nw}"
    show sm_sms with dissolve
    hide sm_n
    pause
    "(It's a message from Ishida!)"
    "\"Come meet me at the baseball field tonight at 7pm.\""
    mc "Strange, the baseball fields are closed by then."
    mc "Why so late?"
    bff "Hey."
    centered "{nw}"
    hide sm_sms with dissolve
    play music "audio/ponder_ost.mp3" fadein 1.0
    scene cg naoharu_rooftop with fade
    centered "{w=3}{nw}"
    bff "I thought you'd be here."
    mc "Oh, hey Nao."
    bff "Have you thought about what you were going to say to him?"
    mc "..."
    mc "Not yet."
    mc "But its strange, yknow."
    bff "Whats strange?"
    mc "I just got a text from him just now."
    bff "Hmmm?"
    bff "What does it say?"
    mc "He told me to meet up with him at the baseball field tonight after school."
    bff "I see..."
    bff "I wonder why he would message you out of the blue like that."
    mc "I wouldn't know either."
    bff "Maybe you should meet him."
    bff "Want me to come with you?"
    mc "..."
    bff "It's okay, if you don't want me to tag along just say so."
    bff "Aren't you going to eat your lunch?"
    mc "I'm not hungry."
    bff "You're going to get hungry later."
    mc "You're right..."
    mc "But I just can't bring myself to eat."
    bff "Still upset about that huh?"
    mc "Wow, how can you tell?"
    bff "Anyway..."
    bff "Lets change the topic to something less serious to take your mind off these things."
    "My best friend Naomi and I chatted on the rooftop until the end of lunch."
    "It cheered me up a little."
    stop music fadeout 1.0
    ## Week5 day 1 Lunch end -------------
    scene ts home with fade
    pause

    ## Week5 day 1 Houkago ---------------------------------------------------
    scene bg bedroom with fade
    "Welp, I have all day until I meet with Ishida."
    "In the meantime, I think I'll go play some games."
    show bsb_blank with dissolve
    scene bg bsb_blank with dissolve
    play sound "audio/unlock.wav"
    show bsb_blue with dissolve
    play music "audio/bsbtheme.mp3"
    "You are ambushed by a group of thugs."
    show bsb_yankitachi1 with dissolve
    "Thugs" "Hey!"
    shoujo1 "!!!"
    "Thugs" "Give us your money!"
    show bsb_yankitachi2 with dissolve
    "Leader" "Or else we'll beat you to the pulp!"
    shoujo1 "NOOOOOOO!!!"
    "Someguy" "OI!!"
    "You hear a couple of mysterious voices calling out to save you."
    scene bg bsb_on_senpaitachi with dissolve
    "Senpai tachi" "No need to fear! The Senpais are here."
    "Thugs"  "(The thugs seem visibly confused)"
    "Thugs" "What are you going to do?"
    "Senpais Altogether" "Defeat you."
    show bg bsb_on with dissolve
    show senpai mafura with dissolve
    senpai1 "(Mafura senpai runs but his scarf chokes him while he tries to fight)"
    hide senpai mafura with dissolve
    "Thugs" "(The thugs chuckled a bit)"
    show senpai matsuge with dissolve
    senpai2 "(Matsuge senpai trips and falls on his chin)"
    hide senpai matsuge with dissolve
    pause
    show senpai kinpatsu with dissolve
    senpai3 "I can beat you using only my chin!"
    "Kinpatsu breaks his arms and legs."
    "Thugs" "(The thugs are laughing on the floor)"
    scene bg bsb_on with dissolve
    "You seemed visibly confused but you will not your let senpais' effort go in vain, you call the ambulance."
    stop music fadeout 1.0
    mc "Oh.."
    mc "It's already time..."
    mc "I should get going now."
    ##Week5 Day 1 baseball field ------------

    ##ts ----------------------------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts ----------------------------------------------------------------

    scene bg field with fade
    mc "(Strange.)"
    mc "(He said he would be here.)"
    mc "(But where is he?)"
    "When I looked at my phone..."
    centered "{nw}"
    show sm_sms with dissolve
    pause (2.0)
    scene bg blank
    pause (3.0)
    centered "I felt as if there was someone behind me."
    mc "... Who are yo-{nw}"
    play sound "audio/impact.wav"
    scene bg blank with hpunch
    $ renpy.vibrate(.5)
    pause (6.0)
    play sound "audio/heartbeat.wav"
    scene cg ambushed1 with fade:
        truecenter zoom 2.5 rotate 0 subpixel True xoffset 500 yoffset 350
        ease 5.0 zoom 2.5 xoffset 0 yoffset 50
    pause (3.0)
    play sound "audio/heartbeat.wav"
    scene cg ambushed1 with fade
    pause (3.0)
    play sound "audio/heartbeat.wav"
    scene cg ambushed_thugs:
        truecenter zoom 2.0 rotate 0 subpixel True xoffset -325 yoffset -50
        ease 3.0 zoom 2.0 xoffset -325 yoffset 250
    pause (3.0)
    play sound "audio/heartbeat.wav"
    scene cg ambushed_thugs
    pause (3.0)
    scene bg blank with fade
    pause (3.0)
    play music "audio/run.mp3" fadein 1.0
    scene bg haibiru with fade
    show hr_thoughts with dissolve
    centered "I was suddenly pushed down to the ground..."
    centered "and ambushed by a group of thugs..."
    centered "They had Ishida's phone in their hand..."
    centered "I thought that I was a goner."
    centered "But then..."
    stop music fadeout 1.0
    hide hr_thoughts
    show bg blank
    male1 "STOP!!"
    scene bg field
    show cg ishida_rescue
    with dissolve
    "Guy" "Oh, well isn't it the nerd?"
    male1 "Let her go!"
    "Guy" "Or else what?"
    "Other guy" "Yea, what are YOU gonna do?"
    "I hear police sirens suddenly ring."
    "Guy" "What the heck?"
    "Guy" "You called the police?!"
    "Other guy" "Cmon! Lets get out of here!"
    "The crowd dispersed."
    scene bg field with dissolve
    show male1 ikemen_worried with fade
    male1 "Are you alright?"
    show male1 ikemen_shocked
    male1 "!!!"
    male1 "Your eye!"
    mc "..."
    label underwater:
    stop music fadeout 1.0
    male1 "Chiharu!! Hang in there!"
    scene bg blank with fade
    play sound "audio/thump.mp3"
    centered "{w=3}{nw}"
    scene bg blank with fade
    play sound "audio/waterbubble.wav" volume 0.5
    pause 3.0
    play music "audio/underwater.mp3" fadein 1.0 volume 0.5
    scene cg sinking with fade
    pause 5.0
    show shade with dissolve
    centered "I remember a long time ago, when I used to be a shy and timid girl.{p} I didn't want any toys, I didn't want any pretty dresses, or even a fancy castle, I just wanted friends.{p} One day I was playing in the grass picking flowers by myself.{p} I thought I was alone until I fell over and scraped my knee but somebody was there to help me up.{p} It was a short haired boy wearing a cap and hoodie.{p} \"Need some help?\" he extended his hand out.{p} All I could remember was that after he grabbed my hand and helped me up,{p} I gave him a flower to thank him.{p} \"Do you wanna be friends?\"{p} I asked him.{p} \"Sure.\"{p} What I didn't expect was that after that exchange, he kissed me on the cheek and took off.{p} But before he ran away he breifly told me his name.{p} {cps=12} his name was...{/cps}"
    stop music fadeout 1.0
    scene white with dissolve
    pause 2.0
    scene white with fade
    show awaken with dissolve
    pause (10.0)
    scene bg hospital_room2 with fade
    ##show blinking
    mc "Huh?"
    mc "Where am I?"
    "Before I knew it I woke up in the hospital room."
    play sound "audio/door.mp3"
    mc "!!!"
    "Someone opened the door."
    "It's Ishida!"
    play music "audio/memory.mp3" fadein 1.0 volume 0.5
    scene bg hospital_room1 with dissolve
    show male1 ikemen_worried with dissolve
    male1 "!"
    show male1 ikemen_normal
    male1 "Oh, you're finally awake."
    mc "Ishida!"
    mc "What happened last night?"
    mc "And why am I-{nw}"
    mc "How did you know I was...?"
    show male1 ikemen_normal
    male1 "You passed out so I took you to the nearest hospital."
    show male1 ikemen_happy
    male1 "I know you're very confused right now so if you have any questions I'll be happy to answer."
    show male1 ikemen_normal
    mc "Well..."
    scene bg hospital_room1 with dissolve

    label choices5:
    menu:
        "(Ask Ishida what happened)":
            jump choices5_a
        "(Ask why he hasn't been coming to school)":
            jump choices5_b
        "(Ask how did he find you)":
            jump choices5_c
        "(Ask why is he dressed like that)":
            jump choices5_d
        "I think I'm good.":
            jump choices5_e

    label choices5_a:
        show male1 ikemen_worried
        male1 "You were ambushed by a group of thugs so we called the police."
        male1 "... and then you passed out so we called the ambulance."
        male1 "So I went with them to check if you were fine."
        show male1 ikemen_normal
        male1 "Anything else?"

        jump choices5

    label choices5_b:
        show male1 ikemen_worried
        male1 "..."
        male1 "A couple of guys noticed that I was hanging out with you."
        show male1 ikemen_annoyed
        male1 "They told me to stop coming to school or else they were gonna mess with you."
        male1 "But, I guess they did regardless."
        show male1 ikemen_worried
        male1 "I'm so stupid for believing in them."
        male1 "I just didn't want you to get hurt."
        male1 "..."
        show male1 ikemen_normal
        male1 "Anything else?"

        jump choices5

    label choices5_c:
        show male1 ikemen_normal
        male1 "A little birdy told me that you got a message from me to meet at the baseball field."
        male1 "So we decided to go and check out the situation."
        male1 "Luckily we managed to get there in time..."
        male1 "..."
        show male1 ikemen_worried
        male1 "I'm sorry for what happened to your eye though."
        show male1 ikemen_annoyed
        male1 "I guess I was a bit late on that part."
        show male1 ikemen_normal
        male1 "Anything else?"

        jump choices5

    label choices5_d:
        show male1 ikemen_shocked
        male1 "!!!"
        show male1 ikemen_annoyed
        male1 "Ok, don't tell anyone but..."
        male1 "I like dressing like this but I'm too embarrassed to be seen like this by anybody at school."
        show male1 ikemen_happy
        male1 "Kinda makes me feel cool... Haha"
        show male1 ikemen_annoyed
        male1 "... I'm so lame aren't I?"
        show male1 ikemen_normal
        male1 "Anything else?"

        jump choices5
    label choices5_e:
        show male1 ikemen_normal
        "..."

        jump choices5_common

    label choices5_common:
    show male1 ikemen_normal
    male1 "Well, I hope you feel better soon."
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi ishida with dissolve
    show progress1 with dissolve
    pause 1.0
    show heart_progress2
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart from Ishida!{/size}"
    scene bg hospital_room1 with fade
    show male1 ikemen_happy with dissolve
    male1 "I'll guess I'll see you later!"
    stop music fadeout 1.0


    ##Epilogue ----------------------------------------------------------
    scene bg blank with fade
    "I spent the next two days in the hospital."
    "The doctor informed me that the reason I passed out wasn't because of my black eye but because of vitamin deficiency."
    "..."
    "After Ishida went missing I hadn't eaten anything for three days straight."
    "They said thats what contributed to me suddenly collapsing on the ground."
    "After all, I don't think being punched in the face alone would be enough to make you suddenly pass out..."
    "At least... I think so."
    "I'll have so much make-up work to do when I get back home from school today."
    "Gotta prepare for the sports festival with Ishida too."
    "We're gonna be so behind, I already feel overwhelmed."
    ##Week 5 Day 4 end ------------------------

    ##Week6 Day 1 Morning ----------------------
    scene bg classroom with fade
    play music "audio/classtime.mp3" fadein 1.0 volume 0.5
    bff "Haru tan!!!"
    show ct_overlay
    show ct_mon
    show ct_930
    with dissolve
    show bff glee with dissolve
    "As usual, Nao greets me as I arrive to class."
    mc "Are you ever gonna stop with those weird nicknames?"
    show bff worried
    bff "No!"
    show bff blush
    bff "Its how I express my affection!"
    mc "Riiiiight."
    hide ct_930
    hide ct_mon
    hide ct_overlay
    with dissolve
    show bff glee
    bff "..."
    show bff worried
    bff "By the way, what happened to your eye?"
    mc "Oh."
    mc "That."
    mc "You just noticed that now?"
    show bff normal
    bff "I'm not as perceptive as you, yknow?"
    mc "(Sigh)"
    mc "I got ambushed by a crowd of guys."
    show bff worried
    mc "And they punched my face so hard I passed out."
    mc "But luckily Ishida was there and..."
    "Wait..."
    "How did Ishida know where I was?"
    show bff normal
    bff "Oh, I already know that."
    mc "Wait what how?!"
    show bff glee
    bff "..."
    show bff worried
    bff "Ok, I might have snooped through your phone while you took a bathroom break."
    show bff glee
    bff "So I decided to snoop through your messages to see how much progress you made with Ishida. Hehehe."
    mc "... uhm, stalker much?"
    show bff worried
    bff "Hey! I saved your life didn't I?"
    bff "I saw a text that seemed kind of suspicious."
    show bff glee
    bff "So I went to the internet cafe you mentioned because I thought he might've been there."
    show bff normal
    bff "And I saw Ishida there!"
    bff "And I asked him why he asked to meet you at the baseball field."
    show bff blush
    bff "Who knows? Maybe it could've been a romantic confession!"
    show bff worried
    bff "Then he told me that that was impossible because his phone got stolen."
    show bff glee
    bff "I thought he was being a tsundere at first."
    show bff normal
    bff "It turns out that he was telling the truth so we both went to go out to find you."
    bff "On our way to the trackfield we saw a crowd of guys show up."
    bff "So we called the police because it looked suspicious."
    show bff worried
    bff "Ishida told me to stay put and make the call while he went to go buy some time."
    show bff sad
    bff "By the time the cops arrived, you were already passed out."
    show bff depressed
    bff "He stayed up all night looking after you at the hospital just to make sure you were okay."
    play sound "audio/schoolchime1.wav"
    show bff worried
    "..."
    "The break is over."
    "It's time for class to start."
    show bff sad
    bff "... We can continue this later."
    stop music fadeout 1.0
    ##Week6 Day 1 Morning end ------------------
    scene bg blank with fade
    pause
    scene ts theres_supposed_to_be_text_here
    pause
    scene ts smilely
    pause
    scene ts lol
    pause
    scene ts just_kidding
    pause
    scene ts after_class
    pause

    ##Week6 Day 1 Lunch ----------------------
    scene bg classroom with fade
    play music "audio/classtime.mp3" fadein 1.0
    show ct_overlay
    show ct_mon
    show ct_100
    with dissolve
    show bff blush with dissolve
    bff "Haru Hime!"
    "Translator Notes: Hime is a suffix for princess."
    "It is pronounced (hee-meh)."
    "Like how the é in café is pronounced and the ca part in cafe is pronounced \"kah\""
    "Translator notes brought to you by the creator of this game to prevent you from sounding like an alien."
    "Or worse, a weeb that can't pronounce Japanese."
    "..."
    "Just like somebody I know..."
    "Anyways, back to the game."
    hide ct_100
    hide ct_mon
    hide ct_overlay
    with dissolve
    show bff glee
    bff "Wanna have lunch together on the rooftop?"
    mc "Nah."
    mc "I'd rather stay in the classroom and eat so I can do my work at the same time."
    mc "Maybe another day when I'm not busy."
    show bff worried
    bff "I see."
    show bff normal
    bff "Well if you don't mind, I'm gonna steal Ishida from you for the rest of lunch!"
    mc "Lol, have fun then."
    show bff blush
    bff "ISHIDA!"
    hide bff with dissolve
    mc "I wonder what goes through that chaotic head of hers."
    mc "Anyways, I should focus on my work."
    stop music fadeout 1.0
    scene bg blank with fade
    ##Week6 Day1 Lunch end -------------------------------------------------
    centered "{size=50}Class{/size}"
    ##Wk6d1 class ---------------------------------------------------------
    scene bg classroom with fade
    "It's the last class of the day."
    "I stare at the clock in hopes that the time passes by faster."
    show ct_overlay
    show ct_mon
    show ct_320
    with dissolve
    mc "(Augh, can this clock be any slower?)"
    "I stare out the window."
    mc "(Huh?)"
    mc "(Whats going on outside?)"
    "You see a couple of guys fighting outside on the school track field."
    hide ct_320
    hide ct_mon
    hide ct_overlay
    with dissolve
    play music "audio/houkago.mp3" fadein 1.0
    scene bg track with fade
    show male3 blush
    "Green-haired guy" "AHHHH!!! GIVE THAT BACK!!"
    hide male3 blush
    if not persistent.yuusuke:
        show male2 happy
        "Blond guy" "Ooooh, whats this?"
        hide male2 happy
        show male4 normal
        "Snow-haired guy" "Oh my, I didn't know you were into these types of things Hiroro."
        hide male4 normal
        show male2 happy
        "Blond guy" "What is this? shoujo manga?"
        "Translation notes: shoujo manga is typically manga for girls."
        "Translation notes: manga is a comic."
        hide male2
        show male3 blush
        "Green-haired guy" "G-Give that back!"
        show male3 annoyed
        "Green-haired guy" "It's not for me its for my sister!"
        hide male3 angry
        show male4 excited
        "Snow-haired guy" "Oh my, oh my~ I didn't know my Hirohiro hiro was a Hirohiro heroine."
        show male4 glee
        "Snow-haired guy" "So you want to get popular with the girls huh?"
        show male4 blush
        "Snow-haired guy" "Honestly, why didn't ya tell me that you needed a mentor? I'm right here!"
        hide male4
        scene cg trio_trackfight with dissolve
        "Green-haired guy" "AHHH! GIVE THAT BACK!!"
        "Snow-haired guy" "Ahahahaha!"
    else:
        show male4 happy
        "Snow-haired guy" "Ooooh, whats this?"
        show male4 normal
        "Snow-haired guy" "Oh my, I didn't know you were into these types of things Hiroro."
        show male4 happy
        "Snow-haired guy" "What is this? shoujo manga?"
        "Translation notes: shoujo manga is typically manga for girls."
        hide male4
        show male3 blush
        "Green-haired guy" "G-Give that back!"
        show male3 annoyed
        "Green-haired guy" "It's not for me its for my sister!"
        hide male3
        show male4 excited
        "Snow-haired guy" "Oh my, oh my~ I didn't know my Hirohiro hiro was a Hirohiro heroine."
        show male4 glee
        "Snow-haired guy" "So you want to get popular with the girls huh?"
        show male4 blush
        "Snow-haired guy" "Honestly, why didn't ya tell me that you needed a mentor? I'm right here!"
        "Snow-haired guy" "Ahahahaha!"
        hide male4
        show male3 angry
        "Green-haired guy" "AHHH! GIVE THAT BACK!!"
    stop music fadeout 1.0
    scene bg classroom with fade
    "..."
    mc "(I wonder what those guys are always up to?)"
    "I stare outside the window until the end of class."
    ##ts ----------------------------------------------
    scene ts after_class with fade
    pause
    ##ts ---------------------------------------------
    play music "audio/houkago.mp3"
    scene bg school_hallway with fade
    "I spot a familiar figure while walking on my way to the shoe lockers"
    "... It's Ishida."
    show ct_overlay
    show ct_mon
    show ct_345
    with dissolve
    show male1 worried_noglasses with dissolve
    male1 "!!!"
    mc "Ishida..."
    mc "Did you lose your glasses again?"
    show male1 blush_noglasses
    male1 "Hahahaha...."
    male1 "..."
    show male1 normal_noglasses
    male1 "... no"
    mc "Then...?"
    male1 "I-I-I..."
    male1 "I thought that maybe I would look better without glasses on cause..."
    hide ct_345
    hide ct_mon
    hide ct_overlay
    with dissolve
    show male1 normal_noglasses
    male1 "I don't know, I thought you said they were stupid..."
    male1 "But, I guess I look stupid either way."
    mc "... about that"
    mc "I'm sorry, I didn't actually mean anything I said to you last time."
    mc "I was just upset and angry, and I said things that I shouldn't have."
    show male1 worried_noglasses
    male1 "..."
    mc "And you don't have to worry about your glasses. You look just fine either with them on or off."
    show male1 blush_noglasses
    male1 "..."
    male1 "Hahaha, thanks..."
    show male1 blush
    "He put his glasses back on after all."
    show male1 happy
    mc "..."
    mc "Anyway! See ya at the tracks!"
    hide male1 happy with dissolve
    "I ran away as my face flushed completely red."
    stop music fadeout 1.0
    ##ts --------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------------
    scene bg track with fade
    play music "audio/peaceful.mp3" fadein 1.0
    show male1 gym_exhausted
    male1 "Haah, haah, hah."
    mc "Exhausted huh?"
    show male1 gym_normal
    male1 "... Yea."
    mc "We're gonna have to train extra hard because we're a few weeks behind on the training schedule."
    mc "To be honest I don't think at this point we're going to win."
    show male1 gym_worried
    male1 "... What?"
    mc "Oh, nothing."
    show male1 gym_normal
    mc "..."
    mc "By the way..."
    male1 "Hmm?"
    mc "What were you talking about with Nao on the rooftop?"
    show male1 gym_worried
    male1 "!!!"
    show male1 gym_blush
    male1 "Nothing..."
    show male1 gym_normal
    mc "Anyway..."
    "Ishida and I continued practicing everyday after school at the track fields."
    stop music fadeout 1.0
    ##ts --------------------------------------------------------------------
    scene ts one_week_until_the_sports_festival with fade
    pause
    ##ts --------------------------------------------------------------------
    scene bg classroom with fade
    mc "..."
    mc "Thats strange."
    mc "Where's Nao?"
    mc "!!!" with vpunch
    $ renpy.vibrate(.5)
    play sound "audio/horror_drum.wav"
    scene cg fdesk1
    pause
    scene bg blank with fade
    centered "(It's Ishida's desk...)"
    centered "{nw}"
    play music "audio/sad_theme.mp3" fadein 1.0
    scene cg fdesk2 with fade
    mc "..."
    scene cg bully_fb2 with fade
    pause
    scene cg bully_fb1 with dissolve
    "Group of Girls" "Oh, look at that. Your desk is dirty."
    "Green-haired girl" "I wonder who could've done that, looks so awful hahaha."
    "Ponytail girl" "Yeah I wonder. (snicker)"
    "Blonde girl" "I thought somebody might've had a funeral but it turns out it was just you."
    "Blonde girl" "Look, somebody already put flowers down for you. Hahaha."
    scene cg bully_fb3 with fade
    stop music fadeout 1.0
    pause
    play music "audio/heartbeat.wav"
    show flashback1
    $ renpy.pause(12.0, hard=True)
    centered "{w=3}{nw}"
    scene bg blank with fade
    stop music fadeout 1.0
    bff "Haru!"
    scene bg classroom with fade
    show bff worried with dissolve
    mc "Nao..."
    mc "What happened to Ishida?"
    show bff sad
    bff "..."
    hide bff sad with dissolve
    "She hands me a news paper and leaves the room."
    play sound "audio/paper.wav"
    show newspaper with dissolve
    mc "!!!"
    "No, I can't believe it..."
    "Ishida... he..."
    scene bg blank with fade

    play music "audio/sad_theme.mp3"
    $ persistent.ishida = True
    $ achievement.grant("yuusuke_achievement")
    $ achievement.sync()
    "Ishida route end 1/???"
    stop music fadeout 1.0
    scene bg blank with fade
    show sus naomi with dissolve
    pause
    "Naomi is sus!"
    return

    label yuusuke_route:
    stop music
    scene bg blank with fade
    "It's been a month since Ishida passed away."
    "I still can't believe it though..."
    "Just like that he..."
    "And so easily too."
    "They said that he jumped in front of the metrorail."
    "It's been all over the news lately."
    "Highschool student jumps in front of train on a Monday morning."
    "The thought of it has been haunting me every night for the past few weeks."
    "I can't help but think to myself..."
    "Was there something that I could have done?"
    "Where did it all go wrong?"
    "Why didn't he tell me? Why did he just disappear like that?"
    "Mom" "Chiharu!"
    scene bg bedroom_asa with fade
    mc "!!!"
    mc "Oh, thats right! I gotta get ready for school!"
    mc "Now where did I put my phone?"
    scene bg blank with fade
    pause (3.0)

    if persistent.yuusuke:
        jump no_yuusuke_route

    scene bg kinjo with fade
    mc "!!!" with vpunch
    mc "(It's the blond dude!)"
    mc "Are you okay?"
    mc "!!!" with vpunch
    $ renpy.vibrate(.5)
    mc "You're bleeding!"
    show male2 struggle with dissolve
    "Blondie" "Don't worry about it."
    mc "You go to my school right?"
    mc "Cmon, you're gonna be late!"
    mc "Lets get you to the clinic."
    scene bg school_clinic with fade
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    show ct_overlay
    show ct_mon
    show ct_845
    with dissolve
    mc "Hello?"
    mc "Is there anybody here?"
    mc "Nobody?"
    mc "(Sigh)"
    mc "Okay, where are the bandages?"
    hide ct_845
    hide ct_mon
    hide ct_overlay
    with dissolve
    show male2 worried with dissolve
    "Blondie" "Hey!"
    show male2 normal
    "Blondie" "I told you its fine, its not a big deal!"
    mc "Geez, why do you have to be so stubborn?"
    mc "You might get an infection if you leave wounds open without disinfecting them!"
    show male2 worried
    "Blondie" "..."
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi yuusuke with dissolve
    show progress0 with dissolve
    pause 1.0
    show heart_progress1
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart!{/size}"
    scene bg school_clinic with fade
    show male2 worried with dissolve
    "Blondie" "I guess..."
    hide male2 worried
    show male4 glee with dissolve
    "Some Guy" "YUUUUUUUUUSSSSSSSSSUUUUUUKEEEEEE!!!"
    "Some Guy" "YUU-YUU-YUU-YUU-YUUUUUSUKEE!"
    hide male4 glee
    show male2 surprised
    male2 "Do you have to scream my name like that every single time?"

    scene intro yuusuke bg1 with dissolve
    play sound "audio/tape.wav"
    pause (0.5)
    scene intro yuusuke bg2 with wipeleft
    play sound "audio/flute.wav"
    scene white with dissolve
    pause (2.0)
    play sound "audio/glitter.wav"
    scene intro yuusuke bg3 with dissolve
    pause (4.0)
    scene bg school_clinic
    show male2 struggle
    with dissolve
    male2 "You sound like a maniac."
    hide male2 struggle
    show male4 blush
    "Some Guy" "Do I need a reason to scream out my best friend's name?"
    show male4 worried
    "Some Guy" "We're practically brothers at this point don't you think?"
    show male4 normal
    "Some Guy" "Besides, its fun to say it like that."
    hide male4 normal
    show male2 struggle
    male2 "God, you're so cringe."
    hide male2 struggle
    show male4 normal
    "Some Guy" "And who is this?"
    show male4 happy
    "Some Guy" "Is it one of your lady friends?"
    hide male4 happy
    show male2 blush
    male2 "!!!"
    show male2 worried
    male2 "You need to stop with that."
    "..."
    "I have a feeling that these two are close friends."
    "These two remind me of whenever I'm with Naomi."
    "I can't help but chuckle to myself."
    hide male2 worried
    show male4 glee
    "Some Guy" "Anyway, what are you two hooligans doing in the clinic?"
    hide male4 glee
    show male2 normal
    male2 "Oh that?"
    male2 "I was walking by and..."
    mc "!!!"
    mc "Hey!"
    hide male2 normal
    show male4 nervous
    "Some Guy" "!"
    show male4 normal
    "Some Guy" "Yes?"
    mc "Do you know where the nurse is? We've been trying to find her."
    mc "We need antiseptics and some bandages, he got wounded on the way here."
    show male4 worried
    "Some Guy" "Oh my, did Yuusuke get into another fight again?"
    show male4 blush
    "Some Guy" "He's always like this, don't worry, I'll take care of it. You can go to class."
    show male4 worried
    "Some Guy" "Here's a note from me saying that you have an excused tardy."
    show male4 normal
    mc "Oh, ok thanks."
    mc "I guess I'll get going now."
    hide male4 normal with dissolve
    stop music fadeout 1.0
    scene bg blank with fade
    "I returned back to class with the excused note I got from the guy in the clinic."
    "The teacher looked slightly annoyed and disappointed at the same time reading it though."
    ##ts ---------------------------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts ---------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show ct_overlay
    show ct_mon
    show ct_930
    with dissolve
    show bff blush with dissolve
    bff "HARUURUU"
    show bff glee
    mc "?..."
    show bff normal
    bff "Haru..."
    bff "Lets say..."
    show bff glee
    bff "You're not in any clubs are you?"
    mc "No?"
    hide ct_930
    hide ct_mon
    hide ct_overlay
    with dissolve
    show bff normal
    bff "Hmmm"
    show bff excited
    bff "Then how about joining the art club?"
    show bff blush
    mc "I think I'll take a hard pass."
    show bff worried
    bff "Awe, why?"
    mc "Last time you made me join a club, it turned out to be full of cringe fan girls obsessed with boy idol groups."
    mc "You told me it was just a music club, and I was stupid for believing you."
    mc "And I know that the art club is filled with girls obsessed with dating sims just like you are."
    show bff glee
    bff "Oh cmon, that was middle school."
    show bff normal
    bff "I mean why not join?"
    show bff worried
    bff "Aren't you supposed to be really good at drawing?"
    mc "Nao, I'm just not really interested in joining any clubs."

    label choices6:
        default route2 = False
        show bff sad
        bff "Cmon, please!"
    menu:
        "(Say no)":
            jump choices6_a
        "(Say maybe)":
            jump choices6_b
        "(Say yes)":
            jump choices6_c

    label choices6_a:
        jump yuusuke_route1

    label choices6_b:
        $ route2 = True
        jump yuusuke_route2

    label choices6_c:
        jump yuusuke_route3


    label yuusuke_route1:
    mc "No means no Nao."
    show bff worried
    bff "Awww."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Anyways, I'll see ya after class."
    stop music fadeout 1.0
    ##ts ------------------------------------------------
    scene ts after_class
    pause
    ##ts -------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_hallway with fade
    show ct_overlay
    show ct_mon
    show ct_100
    with dissolve
    "Sensei told me to carry these papers to the teacher offices."
    "Still though, I wonder why she had to make me carry so many of these by myself."
    "It's towering over my face and its blocking my field of vision"
    "!!!" with hpunch
    $ renpy.vibrate(.5)
    "The Weird Kid" "Oh my gosh! I'm sorry!"
    "The Weird Kid" "Are you okay?"
    "The Weird Kid" "Here, let me carry these for you."
    hide ct_100
    hide ct_mon
    hide ct_overlay
    with dissolve
    scene bg school_hallway with fade
    show male4 worried
    "The Weird Kid" "Where are you taking these by the way?"
    mc "The teacher offices."
    show male4 normal
    "The Weird Kid" "I see."
    "The Weird Kid" "..."
    scene bg school_hallway with fade
    show male4 glee with dissolve
    "The Weird Kid" "Alright, thats that."
    show male4 happy
    "The Weird Kid" "..."
    show male4 normal
    "The Weird Kid" "Hey..."
    show male4 glee
    "The Weird Kid" "By any chance, do you think you could stop by the disciplinary room after school today?"
    mc "Uhm... why?"
    show male4 blush
    "The Weird Kid" "I kinda need a favor."
    mc "Uhm.. Okay, that's fine I guess."
    show male4 excited
    "The Weird Kid" "Alright! Great then!"
    show male4 glee
    "The Weird Kid" "Bye!"
    hide male4 with dissolve
    "The strange kid disappeared into the depths of the hallways as he waved to me goodbye."
    "What have I gotten myself into this time?"
    stop music fadeout 1.0

    ##ts ----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------------------------
    scene bg kaoru_office_door with fade
    "Is this the right room?"
    "(knocks)"
    "The Weird Kid" "Coming!"
    mc "..."
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg kaoru_office with fade
    show ct_overlay
    show ct_mon
    show ct_345
    with dissolve
    show male4 normal with dissolve
    mc "So what is it that you need help with?"
    "The Weird Kid" "So, I heard that you were good at drawing."
    mc "... Where did you hear that from?"
    show male4 scared
    "The Weird Kid" "..."
    show male4 nervous
    "The Weird Kid" "Naomi."
    show male4 worried
    "The Weird Kid" "I asked her if she was any good at drawing."
    show male4 blush
    "The Weird Kid" "She told me to ask you."
    mc "Wait, how do you know Naomi?"
    hide ct_mon
    hide ct_345
    hide ct_overlay
    with dissolve
    show male4 happy
    "The Weird Kid" "She's a good friend of mine."
    show male4 scared
    "The Weird Kid" "We often talk about... stuff.. together."
    show male4 normal
    "The Weird Kid" "Anyway! Lets get down to business!"
    hide male4 normal
    play sound "audio/door.mp3" volume 1.0
    "(The door opens)"
    show male2 normal
    male2 "Kaoru, do you think I can copy your homework for tomorrow?"
    hide male2 normal
    show male4 scared
    male4 "!!!"

    scene intro kaoru bg1 with dissolve
    play sound "audio/tape.wav"
    pause (0.5)
    scene intro kaoru bg2 with wipeleft
    play sound "audio/flute.wav"
    scene white with dissolve
    pause (2.0)
    play sound "audio/glitter.wav"
    scene intro kaoru bg3 with dissolve
    pause (4.0)
    scene bg kaoru_office
    show male4 normal
    with dissolve

    male4 "Oh, hi Yuusuke."
    show male4 happy
    male4 "I'm in a meeting right now with a fellow student."
    hide male4 happy
    show male2 surprised
    male2 "!!!"
    male2 "(It's the girl from earlier!)"
    show male2 normal
    male2 "Don't mind me I'm just going to copy down some..."
    male2 "notes..."
    hide male2 normal
    show male4 happy
    male4 "Yea, Go ahead, I left the homework on the desk over there. You can just copy down what I've already done."
    mc "Alright so, what is it that you need from me today?"
    show male4 scared
    male4 "So, I borrowed my friend's manga for a little bit."
    show male4 nervous
    male4 "And I accidentally spilled some tea on the pages as I was reading it..."
    male4 "And some of the pages got all blurry and messy..."
    show male4 scared
    male4 "And I tried cleaning it but"
    male4 "I messed up and ended up wiping the ink off the pages instead..."
    show male4 nervous
    male4 "So I took the cover of the manga and put it on a different manga and gave it back to him so he wouldn't notice."
    male4 "It's only a matter of time before he notices."
    show male4 blush
    male4 "Sooooo"
    male4 "I was wondering if you could help me redraw some of the pages."
    mc "Why don't you just print out the pages and stick them back into the book?"
    stop music fadeout 1.0
    show male4 scared
    play sound "audio/dooropen.wav"
    "The door opens"
    scene cg trio_antics2 with fade
    "I can't remember his name" "Kaoru!!!"
    "I can't remember his name" "Where is my manga?!"
    scene bg kaoru_office with fade
    show male4 scared with dissolve
    male4 "..."
    show male4 nervous
    male4 "Yuusuke has it!"
    hide male4 nervous with dissolve
    "He runs away."
    show male2 surprised
    male2 "!!!"
    "I can't remember his name" "YUUSUKEEE!!!"
    scene bg blank with fade
label hallrun_minigame1:
    $ renpy.block_rollback()
    play music "audio/chimetown.mp3" fadein 1.0 volume 1.0
    $ renpy.pause(2, hard=True)
    $ h1points = 50
    call screen h1clicker with fade
label h1win:
    $ renpy.block_rollback()
    $ renpy.pause(2, hard=True)
    $ h1points = 50
    scene cg hiro chase with fade
    mc "Is he gone yet?"
    male2 "No, I think he's coming closer."
    "I forgot his name" "I heard that!"
    male2 "Quick run!"
    scene bg blank with fade
    call screen breathe1 with fade

label hallrun_continue_1a:
    $ renpy.block_rollback()
    $ renpy.pause(2, hard=True)
    $ h2points = 50
    call screen h2clicker with fade
label h2win:
    $ renpy.block_rollback()
    $ renpy.pause(2, hard=True)
    $ h2points = 50
    scene cg hiro chase with fade
    mc "Do you think he'll find us here?"
    male2 "Shhhh!"
    male2 "Stay quiet!"
    "I forgot his name" "If I get my hands on you, you're dead meat!"
    male2 "He found us!"
    scene bg blank with fade
    call screen breathe2 with fade

label hallrun_continue_2a:
    $ renpy.block_rollback()
    $ renpy.pause(2, hard=True)
    $ h3points = 100
    call screen h3clicker with fade
label h3win:
    $ renpy.block_rollback()
    $ renpy.pause(2, hard=True)
    $ h3points = 100
    $ persistent.hclicker = True
    if route2:
        jump hallrun_after2
    else:
        jump hallrun_after

label h1lost:
    $ renpy.block_rollback()
    $ renpy.pause(2, hard=True)
    $ h1points = 50
    scene white with fade
    jump hallrun_minigame1

label hallrun_after:
    stop music fadeout 1.0
    scene bg track with fade
    show ct_overlay
    show ct_mon
    show ct_400
    with dissolve
    show male2 struggle with dissolve
    male2 "Haah, haah, hah."
    show male2 normal
    male2 "Okay I think he stopped following us."
    male2 "..."
    mc "Um... are you okay?"
    male2 "Oh?"
    male2 "Yea..."
    mc "No, I mean... your wound."
    show male2 surprised
    male2 "Oh! That!"
    show male2 happy
    male2 "Yea, its fine. Don't worry about it!"
    mc "So what happened?"
    show male2 normal
    male2 "Oh, you mean what happened earlier this morning?"
    male2 "I ran into trouble on the way to school, you could say."
    show male2 worried
    male2 "Anyways I gotta go."
    hide male2 worried with dissolve
    hide ct_400
    hide ct_mon
    hide ct_overlay
    with dissolve
    mc "..."
    mc "Maybe I should've joined a club after school after all."
    mc "I really don't have anything to do when school is done anyway."
    mc "I wonder if Nao is still busy with her club activities."
    mc "Maybe I should pay a visit."
    #play music "audio/remember.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    mc "!"
    mc "Nao!"
    show bff normal with dissolve
    bff "Oh! Hi Haruu!"
    mc "Why are you in the club room by yourself?"
    show bff worried
    bff "Oh... uhm"
    show bff sad
    bff "It's actually because I wanted to start a club by myself but I never got any members..."
    show bff normal
    bff "But thats okay, I'm working on the recruitment posters by myself."
    mc "..."
    mc "Do you want me to help you?"
    show bff excited
    bff "Would you?!"
    show bff blush
    bff "I mean, I would really appreciate it!"
    stop music fadeout 1.0
    scene bg blank with fade
    "And so, me and Nao spent the afternoon working on drawing and printing posters for the art club."
    stop music fadeout 1.0
    ##ts -------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts -------------------------------------------------------------------
    play music "audio/ponder_ost.mp3" fadein 1.0 volume 1.0
    scene bg grave with fade
    "Ishida's grave should be somewhere here."
    "I have to get home before it gets too late."
    "!!!"
    show male2 surprised with dissolve
    male2 "!"
    mc "What are you doing here?"
    show male2 worried
    male2 "That should be my line..."
    male2 "Relax, I'm not doing anything sketch. I'm just here to pay respects to an old friend of mine."
    show male2 normal
    mc "..."
    mc "Me too actually."
    "I take a glance at the grave."
    mc "Wait..."
    mc "Did you know Ishida by any chance?"
    show male2 worried
    male2 "(Sigh)"
    show male2 normal
    male2 "Well, whose else's grave would this be?"
    show male2 worried
    male2 "But yea, you could say that he used to be an old friend of mine."
    mc "So you knew him too huh?"
    male2 "... We used to be friends in middle school."
    show male2 struggle
    male2 "Still can't believe he did that though."
    mc "..."
    "I don't have anything to say."
    show male2 normal
    male2 "Anyways, it was nice seeing ya but I gotta head off now."
    hide male2 normal with dissolve
    "He disappears into the sunset."
    mc "(Ishida...)"
    mc "(I wish I could've gotten to spend more time with you.)"
    "After leaving flowers on his grave I head my way home."
    stop music fadeout 1.0
    ##ts ------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts ------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show ct_overlay
    show ct_tues
    show ct_930
    with dissolve
    show bff excited with dissolve
    bff "Harurunnn"
    mc "Yes?"
    show bff blush
    bff "Do you think you can go shopping with me after school?"
    mc "Hmm...."
    mc "I'm not sure if I have enough to buy anything."
    mc "Window shopping maybe."
    hide ct_930
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff worried
    bff "Don't worry, we're not going out to go shopping for clothes this time."
    show bff glee
    bff "It's my mom's birthday and I wanna go get something special."
    mc "Alright, I'll go then, I guess."
    show bff excited
    bff "Great! Meet me at the train station after school!"
    hide bff excited with dissolve
    play sound "audio/schoolchime1.wav"
    "The bell rings"
    "Just in time for class."
    stop music fadeout 1.0
    scene bg blank with fade
    "As usual, after school was over, I headed over to the school shoe lockers to meet up with Naomi."
    ##ts --------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts --------------------------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_genkan with fade
    show ct_overlay
    show ct_tues
    show ct_400
    with dissolve
    show bff worried
    bff "Haruuuu!"
    mc "Oh, hey."
    mc "You ready to go?"
    hide ct_400
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff excited
    bff "I'm ready when you are!"
    scene bg blank with fade
    "It's nice to hang out with Nao after school sometimes."
    "Though, I don't really like the train that much to be honest."
    "It's always crowded and full of creepy weirdos that like to harass women."
    "I heard about it on the news."
    "Stalking on the rise."
    "Women and children must be wary on trains."
    "Watch out for suspicious men who harass women."
    "Rush hour is the worst though."
    "Hundreds of people crammed into a small compact space just to make it to work on time."
    "I don't know how office workers do it."
    "If it were me bet I would suffocate on my way to work."
    bff "Haru!"
    scene bg station no_train with fade
    show bff glee with dissolve
    bff "We're here!"
    mc "..."
    mc "(We're here faster than I expected.)"
    mc "Oh."
    show bff normal
    bff "Our train will arrive in like 5 minutes."
    mc "I'll guess I'll just be on the look out until then."
    mc "... for the train I mean."
    scene bg blank with fade
    "I spend the next five minutes talking with Nao."
    "... listening to her talk about shoujo manga."
    "I hope she doesn't recommend me to read one as well."
    stop music fadeout 1.0
    scene bg station with fade
    show bff glee with dissolve
    bff "It's here!"
    mc "Alright."
    mc "!!!"

    scene bg blank
    pause 1.5
    show chikatetsu with fade
    pause 4.5
    scene bg blank
    play music "audio/heartbeat.wav" fadein 1.0 volume 1.0
    pause 5.0
    scene bg blank with fade
    centered "Huh?"
    centered "What is this feeling?"
    centered "I can't move..."
    centered "..."
    centered "It's okay, I just need to get on the train."
    centered "Yes, the train."
    centered "Theres nothing wrong with trains right?"
    centered "People ride them all the time."
    centered "..."
    centered "Ishida..."
    centered "Why..."
    jump yuusuke_route_common

    label yuusuke_route2:
    mc "I'll think about it."
    show bff glee
    bff "Alright, fair enough."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Anyways, I'll see ya after class."
    stop music fadeout 1.0
    ##ts ------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts -------------------------------------------------
    scene bg classroom with fade
    show ct_overlay
    show ct_mon
    show ct_105
    with dissolve
    mc "(Its lunch time.)"
    mc "..."
    mc "(But where is Nao?)"
    mc "(I'll guess I'll go to the vending machine.)"
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_hallway with fade
    "I make my way to the vending machine."
    "The Weird Kid" "Hey!"
    show male4 normal with dissolve
    mc "???"
    "The Weird Kid" "You're Haru right?"
    show male4 happy
    "The Weird Kid" "I heard about you from Naomi."
    mc "Naomi?"
    mc "(Sigh)"
    "I hope this isn't another one of her schemes to pair me up with another guy."
    mc "Yea, thats my name alright."
    mc "Anyway, do you need anything?"
    show male4 glee
    "The Weird Kid" "Actually, yes."
    show male4 blush
    "The Weird Kid" "I'm sorry, I forgot to introduce myself."
    show male4 happy
    male4 "I'm Kaoru, head of the disciplinary committee."

    scene intro kaoru bg1 with dissolve
    play sound "audio/tape.wav"
    pause (0.5)
    scene intro kaoru bg2 with wipeleft
    play sound "audio/flute.wav"
    scene white with dissolve
    pause (2.0)
    play sound "audio/glitter.wav"
    scene intro kaoru bg3 with dissolve
    pause (4.0)
    scene bg school_hallway
    show male4 normal
    with dissolve

    show male4 normal
    male4 "Theres actually a matter I would like to discuss with you in private."
    male4 "Do you think you can meet me in the disciplinary room after school?"
    mc "Okay, I guess."
    show male4 excited
    male4 "Alright, then its settled!"
    show male4 glee
    male4 "See ya after school!"
    hide male4 glee with dissolve
    "..."
    "Guess I'm occupied after school."
    stop music fadeout 1.0
    ##ts ----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------------------------
    scene bg kaoru_office_door with fade
    show ct_overlay
    show ct_mon
    show ct_400
    with dissolve
    "Is this the right room?"
    "(knocks)"
    male4 "Coming!"
    mc "..."
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg kaoru_office with fade
    show male4 normal with dissolve
    mc "So what is it that you need help with?"
    male4 "So, I heard that you were good at drawing."
    mc "... Where did you hear that from?"
    show male4 scared
    male4 "..."
    show male4 nervous
    male4 "Naomi."
    show male4 worried
    male4 "I asked her if she was any good at drawing."
    show male4 blush
    male4 "She told me to ask you."
    mc "Wait, how do you know Naomi?"
    show male4 happy
    male4 "She's a good friend of mine."
    show male4 scared
    male4 "We often talk about... stuff.. together."
    show male4 normal
    male4 "Anyway! Lets get down to business!"
    hide male4 normal
    play sound "audio/door.mp3" volume 1.0
    "(The door opens)"
    show male2 normal
    male2 "Kaoru, do you think I can copy your homework for tomorrow?"
    hide male2 normal
    show male4 scared
    male4 "!!!"
    show male4 normal
    male4 "Oh, hi Yuusuke."
    show male4 happy
    male4 "I'm in a meeting right now with a fellow student."
    hide male4 happy
    show male2 surprised
    male2 "!!!"
    male2 "(It's the girl from earlier!)"
    show male2 normal
    male2 "Don't mind me I'm just going to copy down some..."
    male2 "notes..."
    hide male2 normal
    show male4 happy
    male4 "Yea, Go ahead, I left the homework on the desk over there. You can just copy down what I've already done."
    mc "Alright so, what is it that you need from me today?"
    show male4 scared
    male4 "So, I borrowed my friend's manga for a little bit."
    show male4 nervous
    male4 "And I accidentally spilled some tea on the pages as I was reading it..."
    male4 "And some of the pages got all blurry and messy..."
    show male4 scared
    male4 "And I tried cleaning it but"
    male4 "I messed up and ended up wiping the ink off the pages instead..."
    show male4 nervous
    male4 "So I took the cover of the manga and put it on a different manga and gave it back to him so he wouldn't notice."
    male4 "It's only a matter of time before he notices."
    show male4 blush
    male4 "Sooooo"
    male4 "I was wondering if you could help me redraw some of the pages."
    mc "Sure... I guess"
    play music "audio/peaceful.mp3"
    scene bg blank with fade
    centered "Use the tools on the left side of the screen to draw!"
    centered "Click the x button to finish."
    centered "Press s to save a screenshot of your photo when you're done."
    centered "Careful though, your image doesn't save when you finish."
    call screen freehand_draw2 with fade

label mangaredraw_after:
    hide screen freehand_draw2
    stop music fadeout 1.0
    scene bg kaoru_office with fade
    show male4 normal
    male4 "Lets see."
    show male4 happy
    male4 "Ah.. It looks..."
    show male4 scared
    male4 "..."
    show male4 nervous
    male4 "Quite interesting I would say..."
    show male4 scared
    play sound "audio/dooropen.wav"
    "The door opens"
    scene cg trio_antics2 with fade
    "I can't remember his name" "Kaoru!!!"
    "I can't remember his name" "Where is my manga?!"
    scene bg kaoru_office with fade
    show male4 scared with dissolve
    male4 "..."
    show male4 nervous
    male4 "Yuusuke has it!"
    hide male4 nervous with dissolve
    "He runs away."
    show male2 surprised with dissolve
    male2 "!!!"
    "I can't remember his name" "YUUSUKEEE!!!"
    scene bg blank with fade
    jump hallrun_minigame1

label hallrun_after2:
    stop music fadeout 1.0
    scene bg track with fade
    show male2 struggle with dissolve
    male2 "Haah, haah, hah."
    show male2 normal
    male2 "Okay I think he stopped following us."
    male2 "..."
    mc "um... are you okay?"
    male2 "Oh?"
    male2 "Yea..."
    mc "No, I mean... your wound."
    show male2 surprised
    male2 "Oh! That!"
    show male2 happy
    male2 "Yea, its fine. Don't worry about it!"
    mc "So what happened?"
    show male2 normal
    male2 "Oh, you mean what happened earlier this morning?"
    male2 "I ran into trouble on the way to school you could say."
    show male2 worried
    male2 "Anyways I gotta go."
    hide male2 worried with dissolve
    mc "..."
    mc "Maybe I should head home too."

    ##ts ---------------------------------------------------------------------
    scene ts home with fade
    pause
    ##ts ---------------------------------------------------------------------
    scene bg bedroom with fade
    mc "..."
    mc "Now where was that device?"
    mc "Oh! Here it is!"
    show bsb_blank with dissolve
    pause
    scene bg bsb_blank with dissolve
    pause
    play sound "audio/unlock.wav"
    play music "audio/bsbtheme.mp3"
    scene bg bsb_on with dissolve
    "Its the next day."
    "You arrive at school just in time for class when you suddenly hear some random guy open the class door loudly."
    "Everyone notices him."
    show senpai matsuge with dissolve
    senpai2 "OH HOHOHOHOHOHO!"
    senpai2 "Moi? Perdre une course? Jamais de la vie !"
    senpai2 "..."
    senpai2 "Je n'y avais pas mis le cœur, autrement la victoire aurait été à moi, sans doute."
    senpai2 "Que je suis brillant, que je suis sportif ah la la..."
    senpai2 "Je n'ose plus jeter un seul coup d'œil à mon miroir, sous peine d'être ébloui par mon propre charme."
    senpai2 "Je ne perds uniquement que face à moi-même."
    senpai2 "Et même si j'avais joué contre moi, j'aurais gagné évidemment."
    "???"
    "What is he even saying?"
    "I checked the language options in the settings to make sure that I didn't accidentally set it to French."
    "... I don't think I changed it..."
    "Translation Notes: I'm sorry, I can't help you here. I don't speak French."
    shoujo1 "I'm glad Matsuge senpai finally mustered up the courage to come back!"
    shoujo2 "Yea, I was kind of worried about him."
    shoujo1 "Don't you think he sounds so romantic when he starts speaking in French though?"
    shoujo2 "Yea, I have absolutely no idea what he's saying but it sounds so dreamy!"
    stop music fadeout 1.0
    play sound "audio/unlock.wav"
    scene bg bsb_blank
    "..."
    "I don't think I can continue on with this game anymore."
    "..."
    "I think I'm gonna go to sleep."

    ##ts ----------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts ----------------------------------------------------------------------
    play music "audio/classtime.mp3"
    scene bg classroom with fade
    show ct_overlay
    show ct_tues
    show ct_930
    with dissolve
    show bff excited with dissolve
    bff "Harurunnn"
    mc "Yes?"
    hide ct_930
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff blush
    bff "Do you think you can go shopping with me after school?"
    mc "Hmm...."
    mc "I'm not sure if I have enough to buy anything."
    mc "Window shopping maybe."
    show bff worried
    bff "Don't worry, we're not going out to go shopping for clothes this time."
    show bff glee
    bff "It's my mom's birthday and I wanna go get something special."
    mc "Alright, I'll go then, I guess."
    show bff excited
    bff "Great! Meet me at the train station after school!"
    hide bff excited with dissolve
    play sound "audio/schoolchime1.wav"
    "The bell rings"
    "Just in time for class."
    stop music fadeout 1.0
    scene bg blank with fade
    "As usual, after school was over, I headed over to the school shoe lockers to meet up with Naomi."
    ##ts --------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts --------------------------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_genkan with fade
    show ct_overlay
    show ct_tues
    show ct_400
    with dissolve
    show bff worried
    bff "Haruuuu!"
    mc "Oh, hey."
    mc "You ready to go?"
    hide ct_400
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff excited
    bff "I'm ready when you are!"
    scene bg blank with fade
    "It's nice to hang out with Nao after school sometimes."
    "Though, I don't really like the train that much to be honest."
    "It's always crowded and full of creepy weirdos that like to harass women."
    "I heard about it on the news."
    "Stalking on the rise."
    "Women and children must be wary on trains."
    "Watch out for suspicious men who harass women."
    "Rush hour is the worst though."
    "Hundreds of people crammed into a small compact space just to make it to work on time."
    "I don't know how office workers do it."
    "If it were me bet I would suffocate on my way to work."
    bff "Haru!"
    scene bg station no_train with fade
    show bff glee with dissolve
    bff "We're here!"
    mc "..."
    mc "(We're here faster than I expected.)"
    mc "Oh."
    show bff normal
    bff "Our train will arrive in like 5 minutes."
    mc "I'll guess I'll just be on the look out until then."
    mc "... for the train I mean."
    scene bg blank with fade
    "I spend the next five minutes talking with Nao."
    "... listening to her talk about shoujo manga."
    "I hope she doesn't recommend me to read one as well."
    stop music fadeout 1.0
    scene bg station with fade
    show bff glee with dissolve
    bff "It's here!"
    mc "Alright."
    mc "!!!"

    scene bg blank
    pause 1.5
    show chikatetsu with fade
    pause 4.5
    scene bg blank
    play music "audio/heartbeat.wav" fadein 1.0 volume 1.0
    pause 5.0
    scene bg blank with fade
    centered "Huh?"
    centered "What is this feeling?"
    centered "I can't move..."
    centered "..."
    centered "It's okay, I just need to get on the train."
    centered "Yes, the train."
    centered "Theres nothing wrong with trains right?"
    centered "People ride them all the time."
    centered "..."
    centered "Ishida..."
    centered "Why..."
    jump yuusuke_route_common


    default yuusuke_choice_yes = False
    label yuusuke_route3:
    $ yuusuke_choice_yes = True
    mc "Alright, fine."
    show bff worried
    mc "I'll join."
    show bff blush
    bff "YAY!"
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Anyways, I'll talk to ya about it after class."
    ##ts ------------------------------------------------
    scene ts after_class
    pause
    ##ts -------------------------------------------------
    scene bg classroom with fade
    show ct_overlay
    show ct_mon
    show ct_100
    with dissolve
    show bff excited with dissolve
    bff "Harucchi"
    mc "Hmm?"
    show bff blush
    bff "Lets go eat lunch together on the-!"
    show bff worried
    bff "..."
    show bff glee
    bff "How about we both eat in the classroom?"
    show bff normal
    mc "..."
    mc "Don't we always usually eat in the classroom?"
    hide ct_100
    hide ct_mon
    hide ct_overlay
    with dissolve
    show bff worried
    bff "Uhm, forget I said anything."
    show bff normal
    bff "Anyway, I forgot my bento today."
    bff "Do you think you can go buy that strawberry bread for me today?"
    mc "Oh yea, I forgot about that."
    mc "Do you wanna come with or...?"
    "Sensei" "Nakamura san!"
    show bff worried with vpunch
    $ renpy.vibrate(.5)
    bff "!"
    bff "... I have to go now, Sensei is calling me for something."
    show bff glee
    bff "You can go get the strawberry bread without me, I'll be here when you come back."
    hide bff glee with dissolve

    #ts ------------------------------------------------------------------------
    scene bg blank with fade
    "The Hallway"
    #ts ------------------------------------------------------------------------
    scene bg school_hallway with fade
    "In the end they didn't have strawberry bread."
    "Only melon bread and chocolate cornets."
    "I hope Nao will accept this."
    "!!!" with hpunch
    $ renpy.vibrate(.5)
    show male2 normal with dissolve
    male2 "(I wonder why Hiro likes these so much.)"
    "It's that guy from earlier!"
    "He has a strawberry bread!"
    mc "Hey!"
    show male2 surprised
    male2 "!!!"
    mc "Do you think I can have that strawberry bread?"
    mc "I'll trade with you for my melon bread."
    show male2 normal
    male2 "Oh, its you."
    show male2 worried
    male2 "Sorry, but no can do. This bread is for a friend of mine."
    show male2 normal
    mc "Please!! I'll do anything!"
    mc "Yknow what, I'll buy it from you just let me check my wallet!"
    "..."
    "I checked my wallet..."
    "Unfortunately for me however, there is no cash."
    "Empty..."
    show male2 worried
    male2 "Look, I gotta go, okay?"
    hide male2 worried with dissolve
    "Yuusuke rushed quickly through the hallways."
    mc "..."
    mc "Man, I really do need a part-time job."
    scene bg classroom with fade
    show bff blush with dissolve
    bff "Haruu!!!"
    show bff excited
    bff "Did you get that strawberry bread I was asking for?"
    mc "..."
    mc "Here"
    show bff worried
    bff "Melon bread?"
    mc "I'm sorry, it was the only thing they had."
    show bff normal
    bff "Oh, is that so?"
    show bff glee
    bff "Well don't worry about it! Thanks for the melon bread! I have a strawberry milk to go with it so that makes it a strawberry bread right?"
    mc "I don't think thats how it works Nao."
    show bff worried
    bff "Well, thats how it works for me."
    show bff normal
    bff "Anyway, lets talk about our plans for the club."
    stop music fadeout 1.0
    ##ts ----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------------------------
    scene bg artroom with fade
    show ct_overlay
    show ct_mon
    show ct_400
    with dissolve
    show bff glee with dissolve
    bff "And we're here!"
    show bff normal
    mc "So, this is the club room right?"
    mc "Where are all the other members?"
    show bff worried
    bff "Oh... uhm"
    hide ct_400
    hide ct_mon
    hide ct_overlay
    with dissolve
    show bff sad
    bff "It's actually because I wanted to start a club by myself but I never got any members..."
    show bff normal
    bff "But thats okay, I'm working on the recruitment posters by myself."
    mc "..."
    mc "Do you want me to help you?"
    show bff excited
    bff "Ah thanks Haru!"
    show bff blush
    bff "I knew you were the best!!"
    scene bg blank with fade
    stop music fadeout 1.0
    play music "audio/peaceful.mp3" fadein 1.0
    scene bg blank with fade
    centered "Use the tools on the left side of the screen to draw!"
    centered "Click the x button to finish."
    centered "Press s to save a screenshot of your photo when you're done."
    centered "Careful though, your image doesn't save when you finish."
    call screen freehand_draw1 with fade

label posterdraw_after:
    hide screen freehand_draw1
    stop music fadeout 1.0
    scene bg artroom with fade
    show bff blush with dissolve
    bff "Lemme see! Lemme see!"
    show bff excited
    bff "Oh wow! You really must've out done yourself!"
    show bff normal
    bff "Anyway, I'll see you tomorrow I guess!"
    show bff glee
    bff "I can't wait to hang these up! I bet we're gonna get alot of members after we post these!"

    ##ts -------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts -------------------------------------------------------------------
    #play music "audio/mourning.mp3" fadein 1.0 volume 1.0
    scene bg grave with fade
    "Ishida's grave should be somewhere here."
    "I have to get home before it gets too late."
    "!!!"
    show male2 surprised with dissolve
    male2 "!"
    mc "What are you doing here?"
    show male2 worried
    male2 "That should be my line..."
    male2 "Relax, I'm not doing anything sketch. I'm just here to pay respects to an old friend of mine."

    label choices6_male2:
        show male2 normal
        male2 "Anyways, why are you here?"
    menu:
        "I actually knew Ishida too.":
            jump choices6_male2_a
        "I wanted to pay respects to a good friend of mine as well.":
            jump choices6_male2_b
        "...":
            jump choices6_male2_c

    label choices6_male2_a:
        mc "Ishida was also a good friend of mine."
        mc "Before the incident I mean."
        mc "I come here sometimes to check how he's doing."
        mc "Or at least, thats how I like to think about it."
        show male2 worried
        male2 "I feel ya."
        jump choices6_male2_common
    label choices6_male2_b:
        mc "... There was someone I wanted to see before I go back home."
        show male2 worried
        male2 "I see, so you're in the same boat as I am aren't ya?"
        jump choices6_male2_common

    label choices6_male2_c:
        mc "..."
        show male2 worried
        male2 "Speechless huh? Sometimes I get like that too when thinking about somebody close to me that has passed away."
        show male2 struggle
        male2 "I end up thinking to myself, was there more I could've done?"
        male2 "Why didn't he come to me?"
        jump choices6_male2_common

    label choices6_male2_common:

    show male2 normal
    male2 "Anyways, it was nice seeing ya but I gotta head off now."
    hide male2 normal with dissolve
    "He disappears into the sunset."
    mc "(Ishida...)"
    mc "(I wish I could've gotten to spend more time with you.)"
    "After leaving flowers on his grave I head my way home."
    stop music fadeout 1.0
    ##ts ------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts ------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show ct_overlay
    show ct_tues
    show ct_930
    with dissolve
    show bff excited with dissolve
    bff "Harurunnn"
    mc "Yes?"
    show bff blush
    bff "Do you think you can go shopping with me after school?"
    mc "Hmm...."
    mc "I'm not sure if I have enough to buy anything."
    mc "Window shopping maybe."
    show bff worried
    bff "Don't worry, we're not going out to go shopping for clothes this time."
    show bff glee
    bff "It's my mom's birthday and I wanna go get something special."
    mc "Alright, I'll go then, I guess."
    hide ct_930
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff excited
    bff "Great! Meet me at the train station after school!"
    hide bff excited with dissolve
    play sound "audio/schoolchime1.wav"
    "The bell rings"
    "Just in time for class."
    stop music fadeout 1.0
    scene bg blank with fade
    "As usual, after school was over, I headed over to the school shoe lockers to meet up with Naomi."
    ##ts --------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts --------------------------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0
    scene bg school_genkan with fade
    show ct_overlay
    show ct_tues
    show ct_400
    with dissolve
    show bff worried
    bff "Haruuuu!"
    mc "Oh, hey."
    mc "You ready to go?"
    hide ct_400
    hide ct_tues
    hide ct_overlay
    with dissolve
    show bff excited
    bff "I'm ready when you are!"
    scene bg blank with fade
    "It's nice to hang out with Nao after school sometimes."
    "Though, I don't really like the train that much to be honest."
    "It's always crowded and full of creepy weirdos that like to harass women."
    "I heard about it on the news."
    "Stalking on the rise."
    "Women and children must be wary on trains."
    "Watch out for suspicious men who harass women."
    "Rush hour is the worst though."
    "Hundreds of people crammed into a small compact space just to make it to work on time."
    "I don't know how office workers do it."
    "If it were me bet I would suffocate on my way to work."
    bff "Haru!"
    scene bg station no_train with fade
    show bff glee with dissolve
    bff "We're here!"
    mc "..."
    mc "(We're here faster than I expected.)"
    mc "Oh."
    show bff normal
    bff "Our train will arrive in like 5 minutes."
    mc "I'll guess I'll just be on the look out until then."
    mc "... for the train I mean."
    scene bg blank with fade
    "I spend the next five minutes talking with Nao."
    "... listening to her talk about shoujo manga."
    "I hope she doesn't recommend me to read one as well."
    stop music fadeout 1.0
    scene bg station with fade
    show bff glee with dissolve
    bff "It's here!"
    mc "Alright."
    mc "!!!"

    scene bg blank
    pause 1.5
    show chikatetsu with fade
    pause 4.5
    scene bg blank
    play music "audio/heartbeat.wav" fadein 1.0 volume 1.0
    pause 5.0
    scene bg blank with fade
    centered "Huh?"
    centered "What is this feeling?"
    centered "I can't move..."
    centered "..."
    centered "It's okay, I just need to get on the train."
    centered "Yes, the train."
    centered "Theres nothing wrong with trains right?"
    centered "People ride them all the time."
    centered "..."
    centered "Ishida..."
    centered "Why..."
    jump yuusuke_route_common

    label yuusuke_route_common:

    label choices7:
        "Get on the train?"
    menu:
        "Get on the train.":
            jump choices7_common1
        "Get on the train.":
            jump choices7_common1
        "Get on the train.":
            jump choices7_common1

    label choices7_common1:
            "Get on the train?"
    menu:
        "Get on the train.":
            jump choices7_common2
        "Get on the train.":
            jump choices7_common2
        "Get on the train.":
            jump choices7_common2

    label choices7_common2:
        stop music fadeout 1.0
        "{cps=8} Are you sure?{/cps}"
    menu:
        "Get on the train!":
            jump choices7_common3
        "Get on the train!":
            jump choices7_common3
        "Get on the train!":
            jump choices7_common3

label choices7_common3:
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump run



label run:
    play music "audio/run.mp3" fadein 1.0 volume 1.0
    scene bg run with fade
    show cg run_haru_run with dissolve

    label choices8:
        centered "{color=#f44336}{b}{size=+10}{fast}{font=DejaVuSans.ttf}Run{/font}{/size}{/b}{/color}" with dissolve
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common1
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common1
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common1

    label choices8_common1:
        centered "{color=#f44336}{b}{size=+10}{w=1.0}{fast}{font=DejaVuSans.ttf}Run{/font}{/size}{/b}{/color}" with dissolve
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common2
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common2
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common2

    label choices8_common2:
        centered "{color=#f44336}{b}{size=+10}{w=1.0}{fast}{font=DejaVuSans.ttf}Run{/font}{/size}{/b}{/color}" with dissolve
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common3
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common3
        "{font=DejaVuSans.ttf}Run{/font}":
            jump choices8_common3

label choices8_common3:
    stop music fadeout 1.0
    scene bg blank
    menu:
        "{color=#f44336}{b}{size=+10}{font=DejaVuSans.ttf}Die{/font}{/size}{/b}{/color}":
            jump yuusuke_route_common2



label yuusuke_route_common2:
    scene bg blank with fade
    male2 "Hey!" with hpunch
    $ renpy.vibrate(.5)
    "You ended up bumping into someone."
    "It's Yuusuke."
    scene bg kinjo with fade
    show male2 surprised with dissolve
    male2 "Hey!"
    male2 "Are you okay? You look like you've seen a ghost!"
    mc "..."
    show male2 worried
    male2 "You're shaking."
    show male2 surprised
    bff "Haru!!"
    hide male2
    show bff worried with dissolve
    "!"
    bff "Why did you run out like that?"
    show bff sad
    bff "I was worried about you!"
    show bff worried
    bff "...?"
    bff "Haru... who is this?"
    hide bff
    show male2 normal
    male2 "Oh, don't worry about me. She just happened to bump into me and I wanted to check if she was alright."
    male2 "Are you a friend of hers?"
    male2 "Anyway, what happened?"
    hide male2
    show bff worried
    bff "We were supposed to go shopping at the mall together this afternoon, but when the train arrived she suddenly ran away."
    hide bff
    show male2 normal
    male2 "The train huh?"
    show male2 worried
    male2 "Do you think she's going to be alright?"
    hide male2
    show bff sad
    bff "I'm not sure..."
    show bff worried
    bff "Cmon Haru, lets go home. We can go shopping another day."
    mc "..."
    mc "... o-okay..."
    show bff blush
    bff "Anyway! Thanks for looking after Haru for me!"
    hide bff
    show male2 blush
    male2 "!!!"
    show male2 normal
    male2 "..."
    show male2 happy
    male2 "Don't mention it."
    ##ts --------------------------------------------
    scene ts home with fade
    pause
    ##ts --------------------------------------------
    scene bg bedroom with fade
    mc "..."
    "Speechless, I fell asleep into my bed without a single thought in my mind."
    ##ts --------------------------------------------
    scene ts a_few_days_later with fade
    pause
    ##ts --------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    show ct_overlay
    show ct_thurs
    show ct_400
    with dissolve
    "Turns out I ended up joining the art club with Nao after all."
    show bff glee with dissolve
    bff "Chiharu Chan!"
    mc "So you finally call me by my name huh?"
    show bff worried
    bff "Oh, cmon, don't be like that."
    mc "Anyways..."
    mc "Do you think anyone is going to come to the club after they see the posters we put up?"
    mc "I mean, it's already been 3 days and so far no one has come."
    hide ct_400
    hide ct_thurs
    hide ct_overlay
    with dissolve
    show bff normal
    bff "Oh! Cmon Haru, try to be a little bit more optimistic!"
    show bff glee
    bff "People will come eventually, it's just a matter of time!"
    show bff normal
    "!!!"
    "The door suddenly opens."
    hide bff
    show male2 normal with dissolve
    male2 "Hey."
    mc "?"
    mc "Uhm, hi?"
    hide male2
    show bff excited
    bff "Haru, Haru!"
    bff "Look! We got a new member for the club!"
    show bff glee
    bff "See, I told ya that somebody would come after seeing our posters!"
    mc "..."
    "What is he doing here?"
    hide bff
    show male2 normal
    male2 "Uh, hey, do you think its okay that I join this club?"
    male2 "Theres also somebody else that I would like to have join too.."
    hide male2
    show bff excited
    bff "Sure sure sure!"
    show bff blush
    bff "And who is this other new member that will be joining us today?"
    show bff normal
    "Small voice" "Hello?"
    hide bff
    show imt exp1 with dissolve
    imt "..."
    hide imt
    show bff excited
    bff "Oh who is this?!"
    bff "She's sooo cute!"
    hide bff
    show male2 happy
    male2 "This is my little sister, Akari."
    male2 "She's shy so try to be gentle with her."
    male2 "Can she join too?"
    hide male2
    show bff excited with dissolve
    bff "Awww! Of course she can join! Let me get the supplies real quick! I'll be right back!"
    hide bff with dissolve
    mc "..."
    show male2 normal with dissolve
    male2 "..."
    mc "So..."
    mc "What brings you here?"
    male2 "Ah, that."
    male2 "So my mom asked me to look after my sister after she gets back from school."
    show male2 worried
    male2 "She's been causing alot of trouble lately."
    mc "What kind of trouble?"
    male2 "Lets just say we caught her doing something suspicious."
    imt "Hey!"
    imt "I'm here y,know!"
    hide male2
    show bff glee
    bff "I'm back!"
    show bff normal
    bff "Hmm.. so I think before we start we should all introduce ourselves."
    show bff excited
    bff "Haru? Why don't you start?"
    mc "???"
    mc "Me?"
    show bff glee
    bff "Yes, you."
    show bff normal
    bff "You need to be the example."
    mc "(sigh)"
    mc "Fine."
    mc "Hi, my name is Chiharu, but I normally go by Haru."
    mc "Not any of those weird nicknames that Naomi gives me."
    show bff worried
    bff "Hey!"
    bff "Its an expression of love!"
    mc "Whatever."
    show bff normal
    mc "My hobbies are drawing..."
    mc "Thats pretty much it."
    show bff glee
    bff "Ohhh! That was a good one!"
    bff "Okay, Akari is next!"
    hide bff
    show imt exp3
    imt "..."
    hide imt
    show male2 normal
    male2 "I'll go first."
    male2 "Hello guys, my name is Yuusuke."
    male2 "..."
    male2 "Thats pretty much it."
    hide male2
    show bff worried
    bff "Hey! That was barely an introduction!"
    hide bff
    show male2 worried
    male2 "It was good enough for me."
    hide male2
    show bff worried
    bff "..."
    bff "... Okay fine."
    show bff normal
    bff "I'll guess I'll go next then."
    show bff glee
    bff "Hello! My name is Naomi!"
    bff "My hobbies are drawing fan art, reading fanfics, playing video games, reading manga."
    show bff normal
    bff "You could say I like cooking, baking, sports, piano."
    show bff excited
    bff "And I recently got into a dating sim that I think you should really try! An AMAZING story! The characters are very interesting! The art is absolutely amazing and the music is breath-taking!"
    mc "Nao..."
    mc "We're not trying to be here all day yknow."
    show bff worried
    bff "Sorry."
    show bff normal
    bff "So that leaves Akari next huh?"
    show bff blush
    bff "Akari! Why don't you introduce yourself?"
    hide bff
    show imt exp3
    imt "..."
    imt "..."
    imt ". . ."
    imt "...hi."
    hide imt
    show bff normal
    bff "Shy, huh?"
    show bff glee
    bff "Well that's okay, you can introduce yourself later."
    show bff
    bff "Now lets move on to the club activity!"
    stop music fadeout 1.0
    scene bg blank with fade
    centered "And so, the 4 of us drew into sketchbooks until the day was over."
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_genkan with fade
    show bff glee with dissolve
    bff "Alright! I'm heading off for today! Lets meet again next week!"
    show bff blush
    bff "Bye!"
    hide bff with dissolve
    "Naomi heads off into the sunset."
    show male2 normal with dissolve
    male2 "..."
    male2 "Oh, yea, I forgot to give this to you."
    mc "!!!"
    mc "It's a strawberry bread!"
    show male2 happy
    male2 "Thanks for the other day."
    mc "?"
    mc "The other day?"
    show male2 normal
    male2 "Oh, the school nurses office incident and stuff."
    male2 "But, I think I'm gonna be needing another favor from you."
    male2 "I know its sudden, but, do you think you can look after my sister?"
    mc "Oh... ok I guess?"
    mc "Wait, how old is she anyway?"
    mc "She's wearing a middle school uniform and she probably doesn't attend this school."
    show male2 worried
    male2 "I know."
    male2 "..."
    show male2 normal
    male2 "Akari!"
    hide male2
    show imt exp1
    imt "?"
    hide imt
    show male2 normal
    male2 "Do you think you could get my notebook for me? I left it in the classroom."
    hide male2
    show imt exp1
    imt "Ok, sure."
    hide imt with dissolve
    "She walks away."
    stop music
    show male2 normal with dissolve
    male2 "So I probably don't have much time to say this but..."
    male2 "One day Akari came home with a bag full of money..."
    show male2 worried
    male2 "But... we don't know where she got it from."
    show male2 struggle
    male2 "So my mom's been asking me to look after her after school to make sure that she's not getting into any trouble."
    male2 "When we asked if she was getting involved with anyone suspicious she said..."
    hide male2
    show imt exp1
    imt "I'm back!"
    hide imt
    show male2 surprised
    male2 "... Akari!"
    show male2 worried
    male2 "..."
    show male2 happy
    male2 "I'll talk to you about it some other time."
    hide male2 with dissolve
    "Yuusuke disappears into the horizon with Akari."
    mc "..."
    mc "I should get going too."
    #ts -----------------------------------------------------------------------
    scene ts home with fade
    pause
    # ts ----------------------------------------------------------------------
    scene bg bedroom_yoru with fade
    mc "Yuusuke..."
    mc "I wonder what that was all about."
    play sound "audio/vibrate.wav"
    $ renpy.vibrate(.5)
    mc "Huh?"
    show sm_n with dissolve
    mc "It's a message from Naomi."
    mc "..."
    mc "\"Goodluck on expanding your harem... \""
    mc "(Sigh)"
    mc "Nao, why do you have to be so cringe?"
    hide sm_n with dissolve
    mc "..."
    mc "I have a feeling she's up to something and I don't like it."
    "After doing my homework, I watched some TV and then went to sleep."
    ##ts ------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts -------------------------------------------
    scene bg kinjo with fade
    show ct_overlay
    show ct_fri
    show ct_800
    with dissolve
    "On my way to school I spot a familiar figure in the distance."
    mc "!!!"
    "It's Yuusuke."
    hide ct_800
    hide ct_fri
    hide ct_overlay
    with dissolve
    show male2 struggle with dissolve
    male2 "Ugh"
    mc "???"
    mc "Are you okay?"
    male2 "..."
    "Something smells strange."
    mc "..."
    mc "Oh..."
    mc "Cmon, lets go wash it off at the gym storage house, I'm sure they have a hose."
    male2 "Uhm, no. You can leave."
    mc "???"
    male2 "No, really I'll handle it myself."
    mc "Oh c'mon. I'm not gonna leave you here."
    mc "Stop being stubborn and lets go."
    scene bg track with fade
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    show male2 normal with dissolve
    mc "Its a good thing I got gloves."
    mc "Let me see that."
    show male2 surprised
    male2 "WAIT! WAIT! WHAT?!"
    show male2 struggle
    male2 "Let me take care of it."
    male2 "You've done enough."
    male2 "Please just go. I got it!"
    mc "..."
    mc "If you say so."
    show male2 struggle
    "Yuusuke proceeds to scrub and wash the bottom of his shoe with soap and water."
    male2 "..."
    show male2 normal
    male2 "You don't have to follow me everywhere yknow..."
    mc "I know."
    mc "But I'm nosy so I don't care."
    show male2 worried
    male2 "(sigh)"
    show male2 normal
    male2 "Fine, lets go back before class starts."
    "Yuusuke checks his phone."
    show male2 struggle
    male2 "Oh snap not again!"
    male2 "It's already 8:44!"
    scene bg school_hallway with fade
    show male2 struggle with dissolve
    male2 "Haah, haah, haah."
    hide male2
    "Sensei" "You guys are late."
    "Sensei" "Chiharu, meet me in the office after schoo-"
    show male2 surprised
    male2 "Wait!"
    show male2 normal
    male2 "Shes late because of me."
    "Sensei" "What?"
    hide male2
    "Who is he again?" "Excuse me." with vpunch
    $ renpy.vibrate(.5)
    "Sensei" "?"
    show male3 normal with dissolve
    "Who is he again?" "Please don't mind these hooligans they're only late because they were helping me out with something this morning."
    "Sensei" "Oh, I see. Alright."
    "Sensei" "Chiharu, you're excused."
    mc "Ah, thanks."
    "I enter the classroom."
    show male3 normal with dissolve
    "Who is he again" "Yuusuke, isn't your class next door?"
    hide male3
    show male2 surprised
    male2 "Oh yea, that's right!"
    hide male2 with dissolve
    "Yuusuke rushes to his class immediately after noticing that he was at the wrong classroom."
    stop music fadeout 1.0
    ##ts -----------------------------------------
    scene ts after_class with fade
    pause
    ##ts ------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show ct_overlay
    show ct_fri
    show ct_100
    with dissolve
    show bff worried with dissolve
    bff "Haru chan."
    bff "Where were you this morning?"
    bff "You usually don't come late no matter how much you stay up."
    bff "Did your fatigue finally catch up to you?"
    mc "Uh... actually no."
    mc "I got caught up into something this morning actually."
    hide ct_100
    hide ct_fri
    hide ct_overlay
    with dissolve
    show bff mischievous
    bff "Oh really?"
    "Some Rando Dude" "Naomi!"
    "A strange figure calls Naomi's name from the classroom door."
    show bff excited
    bff "Oh my my, is that Kaorurun?"
    hide bff
    show male4 excited
    male4 "Yes it is my dear Naomimi"
    if yuusuke_choice_yes:
        scene intro kaoru bg1 with dissolve
        play sound "audio/tape.wav"
        pause (0.5)
        scene intro kaoru bg2 with wipeleft
        play sound "audio/flute.wav"
        scene white with dissolve
        pause (2.0)
        play sound "audio/glitter.wav"
        scene intro kaoru bg3 with dissolve
        pause (4.0)
        scene bg classroom
        show bff excited
        with dissolve
    hide male4
    show bff excited
    bff "Kaorururun!"
    hide bff
    show male4 excited
    male4 "Naomimimi"
    hide male4
    show bff excited
    bff "KAORURURUUUUN!"
    hide bff
    show male4 excited
    male4 "NAOMIMIMIIIII!"
    hide male4
    "..."
    "I have the feeling I have found Naomi's doppelganger."
    show bff blush
    bff "HARU! Have you met with Kaoru kun?"
    show bff glee
    bff "He's my friend from middle school."
    show bff normal
    bff "The last one I was at before I transferred."
    mc "Oh?"
    hide bff
    show male4 normal
    male4 "Hello there, I believe I've seen you before."
    show male4 happy
    male4 "Your name is Chiharu right? Naomi told me."
    show male4 blush
    male4 "I sincerely apologize for my friend Yuusuke's barbarian behavior."
    show male4 normal
    male4 "But you know when you tame a dog it starts to behave very well, teehee."
    show male4 nervous with vpunch
    $ renpy.vibrate(.5)
    "Ow!"
    hide male4
    show male2 normal with dissolve
    male2 "Kaoru, here's your homework from the other day."
    show male2 worried
    male2 "And stop flirting with the girls, hanging out with you is already embarrassing enough but you make me want to burn my eyes just watching you trying to be cool."
    hide male2
    show male4 scared
    male4 "Flirting?!"
    show male4 blush
    male4 "Oh cmon, you don't have to say that in front of the ladies."
    hide male4
    show male2 struggle
    male2 "Oh my god, you're so cringe."
    male2 "Just stop, please, stop."
    hide male2
    show bff worried
    bff "Uhm? Am I invisible to you or something?"
    hide bff
    show male2 surprised
    male2 "Oh! I'm sorry!"
    show male2 normal
    male2 "Am I interrupting something?"
    hide male2
    show bff glee
    bff "No, no, not at all!"
    show bff mischievous
    bff "I was talking to Kaoru kun."
    hide bff
    show male4 happy
    male4 "Oh, don't mind Yuusuke."
    show male4 glee
    male4 "He may look tough and scary but he's actually a softie!"
    hide male4
    show male2 blush
    male2 "Hey!"
    male2 "I AM NOT A SOFTIE!"
    mc "hehehe"
    show male2 surprised
    male2 "What are you laughing for?!"
    mc "Oh, its nothing, I just thought you guys were being funny."
    show male2 struggle
    male2 "..."
    hide male2
    show male4 normal
    male4 "Oh, relax Yuusuke, you know I'm just teasing you right?"
    show male4 excited
    male4 "You're just so adorable when you get flustered, I can't help it!"
    hide male4
    show male2 struggle
    male2 "Dude, just stop."
    hide male2
    show male4 normal
    male4 "Anyway, you called me here for something Naomi?"
    hide male4
    show bff blush
    bff "Oh, I was hoping that today we could eat in your office!"
    show bff glee
    bff "There's something I wanna show you."
    hide bff
    show male4 excited
    male4 "Well why didn't you say so sooner?!"
    male4 "Yuusuke, lets go! You need to make some more friends anyway!"
    hide male4
    show male2 blush
    male2 "Hey!"
    scene bg kaoru_office with fade
    show ct_overlay
    show ct_fri
    show ct_105
    with dissolve
    show male4 normal with dissolve
    male4 "Here we are!"
    hide male4
    show bff excited
    bff "Wow! You decorated this place by yourself?"
    hide bff
    show male4 happy
    male4 "Yes!"
    show male4 blush
    male4 "But sadly the other members are never here."
    hide male4
    show bff worried
    bff "Awe, thats a shame."
    show bff normal
    bff "..."
    hide ct_105
    hide ct_fri
    hide ct_overlay
    with dissolve
    show bff blush
    bff "I'm famished let's eat!"
    hide bff
    "Naomi eagerly opens her bento box."
    show male4 excited
    male4 "Oh my gosh is that chicken?!"
    male4 "Let me have a piece!"
    hide male4
    "And so Naomi and Kaoru talked nonstop leaving me and Yuusuke sitting awkwardly in silence to eat our lunch."
    stop music fadeout 1.0
    ##ts ----------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts ----------------------------------------------
    play music "audio/nowav.mp3" fadein 1.0 volume 1.0
    scene bg kaoru_office with fade
    show bff normal with dissolve
    bff "Kaoru kun."
    hide bff
    show male4 normal
    male4 "Yes, Naomi?"
    hide male4
    show bff glee
    bff "The thing."
    hide bff
    show male4 normal
    male4 "What thing?"
    male4 "..."
    show male4 scared
    male4 "Oh..."
    show male4 nervous
    male4 "THAT thing?"
    show male4 blush
    male4 "Ok guys, we'll be right back."
    hide male4 with dissolve
    "Kaoru and Naomi walked outside and left us alone by ourselves."
    show male2 normal with dissolve
    male2 "..."
    mc "..."
    mc "Those two are a handful aren't they?"
    show male2 worried
    male2 "Yea..."
    male2 "They sure are."
    show male2 normal
    male2 "They're practically twins."
    mc "..."
    male2 "..."
    show male2 worried
    male2 "So..."
    male2 "What happened to you at the train station the other day?"
    mc "!!!"
    stop music fadeout 1.0
    show male2 surprised
    male2 "!!!"
    male2 "Hey! Are you-"
    male2 "D-d-don't cry!"
    male2 "Are you alright?!"
    mc "..."
    mc "I..."
    mc "I-I-I don't know..."
    "Tears start uncontrollably streaming from my eyes."
    show male2 worried
    male2 "Hey."
    male2 "It's going to be okay."
    male2 "You don't have to say a word."
    male2 "I already know."
    play music "audio/memory.mp3" fadein 1.0 volume 1.0
    scene bg blank with fade
    "He embraces me into his arms without saying another word."
    "It feels warm."
    "Now that I think about it, Yuusuke might have actually seemed like an intimidating unapproachable guy at first."
    "But in actuality he's really sweet isn't he?"
    "No one's ever treated me so nicely before."
    "..."
    "Am I asking for too much?"
    "Am I really so useless?"
    "Do I always have to rely so much on others?"
    "Why am I so helpless?"
    "Do I even deserve so much kindness?"
    "After a while, people just end up getting sick and tired of being around me."
    "They say I'm boring."
    "That I'm too negative."
    "All I do is just bring down the mood."
    "..."
    "It took me a while to calm down."
    "Eventually, I stopped crying."
    scene bg kaoru_office with fade
    show male2 worried with dissolve
    male2 "You alright?"
    mc "Yea."
    mc "I think I've calmed down."
    show male2 normal
    male2 "Oh, by the way, here you go."
    hide male2
    scene bg kaoru_office
    play sound "audio/unlock.wav"
    show treat
    pause
    hide treat
    show male2 happy
    male2 "It's something my sister made for you the other day."
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi yuusuke with dissolve
    show progress1 with dissolve
    pause 1.0
    show heart_progress2
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart!{/size}"
    scene bg kaoru_office with fade
    show male2 happy with dissolve
    mc "Oh thanks."
    stop music
    play sound "audio/door.mp3"
    show male2 normal
    "The door opens."
    hide male2
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    show bff glee
    bff "We're back!"
    hide bff
    show male2 normal
    male2 "So what were you guys doing out there?"
    hide male2
    show bff glee
    bff "Oh, we were just talking about-"
    hide bff
    show male4 scared with vpunch
    $ renpy.vibrate(.5)
    male4 "Stuff!"
    show male4 nervous
    male4 "We were just talking about..."
    show male4 scared
    male4 "Stuff."
    hide male4
    show male2 normal
    male2 "Oookay, Mr. Suspicious."
    hide male2
    "Something falls onto the floor."
    show male4 scared
    male4 "!!!"
    hide male4
    show male2 normal
    male2 "..."
    show male2 happy
    male2 "Otome Legends?"
    male2 "I didn't know you were into romance visual novels for girls Kaoru."
    hide male2
    show bff worried
    bff "I wouldn't say that he's into it."
    bff "That's an understatement."
    show bff excited
    bff "HE'S WHAT WE LIKE TO CALL! THE OTOME MASTER!"
    hide bff
    show male4 blush
    male4 "You don't have to say that outloud Naomi!!!!"
    male4 "You're embarrassing me!!"
    hide male4
    show male2 worried
    male2 "Since when do you ever get embarrassed?"
    hide male2
    show male4 worried
    male4 "Anyways, I play them from time to time but it's just a small hobby of mine."
    hide male4
    play sound "audio/door.mp3"
    "The door suddenly opens."
    show male3 normal
    "I can't remember his name" "Kaoru, do you have any duct tape? I think I broke my..."
    show male3 blush
    "I can't remember his name" "N-N-NA-NAOMI?!"
    hide male3
    show bff glee
    bff "Oh hi, Hiro!"
    show bff normal
    bff "What's the matter? Do you need help fixing that brain of yours?"
    show bff glee
    bff "I'm sorry, but I don't think duct tape can fix it."
    bff "But you're probably not smart enough to figure that out are ya?"
    hide bff
    show male2 worried
    male2 "Geez Naomi, you don't have to be so mean. Hiro's a human being too, you know."
    hide male2
    show bff glee
    bff "Sorry, I was only stating facts."
    hide bff
    show male3 worried
    "Oh yea, it was Hiro" "..."
    male3 "Sorry, am I interrupting something?"
    hide male3
    show male4 happy
    male4 "No, no, no! Come in!"
    male4 "You said that you needed something Hiro?"
    hide male4
    show male3 normal
    male3 "Ah, yes."
    male3 "So, I was doing paperwork when suddenly the chair collapsed to the ground."
    male3 "I notified the head master and he told me that it would take a few days to find a replacement."
    show male3 worried
    male3 "So far I've been making do by finishing up the remaining copies of paperwork on the floor but my back is killing me."
    hide male3
    show male4 scared
    male4 "Wait."
    show male4 nervous
    male4 "So you need MY duct tape."
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 nervous
    male4 "So that you can fix your chair?"
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 nervous
    male4 "Because your back is hurting you..."
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 nervous
    male4 "From doing paper work on the floor?"
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 worried
    male4 "..."
    show male4 blush
    male4 "Why don't you just... do your paperwork in the classrooms?"
    hide male4
    show bff glee
    bff "Uhm, excuse me but I think I'm going to leave early."
    show bff normal
    bff "Thanks for inviting me."
    hide bff
    show male4 normal
    male4 "Oh, ok."
    show male4 happy
    male4 "Well, cya later then. I guess."
    hide male4
    mc "Bye Nao!!!"
    show bff glee
    bff "Oh, Haru! You're coming with me too!"
    mc "..."
    show bff normal
    bff "Bye guys!!!"
    hide bff
    play sound "audio/dooropen.wav"
    "Haru and Naomi both leave the room."
    show male2 normal
    male2 "..."
    show male2 worried
    male2 "You okay Hiro?"
    hide male2
    show male3 worried
    male3 "Yeah..."
    hide male3
    show male2 worried
    male2 "Cmon, cheer up."
    show male2 happy
    male2 "Anyway, guess what happened earlier. Did you know that Kaoru bought a copy of otome legends?"
    hide male2
    show male3 blush
    male3 "You mean that super cringe game with the guys and the long chins?!"
    hide male3
    show male4 blush
    male4 "Guys! Stop it! I'm right here!!"
    stop music fadeout 1.0
    scene bg school_hallway with fade
    show bff normal with dissolve
    bff "Glad we're out of that mess."
    mc "..."
    show bff worried
    bff "What's wrong Haru?"
    mc "Naomi, what's up with you today?"
    bff "?"
    bff "Oh, you mean Hiro?"
    show bff glee
    bff "I'll admit, I acted a bit out of character right there for a second."
    bff "You probably don't know him."
    show bff normal
    bff "He's what we like to call in the otome world, a tsundere."
    mc "What's a tsundere?"
    show bff worried
    bff "Oh, Haru. I knew you were clueless but I didn't know you were THAT clueless."
    show bff glee
    bff "A tsundere! A tsundere!"
    bff "A tsundere is absolutely no good!"
    show bff normal
    bff "Just know that there is no good tsundere."
    bff "They're all annoying."
    show bff worried
    bff "They all act like jerks, and act like they hate you, but in actuality they secretly have feelings for you."
    bff "They have no social skills and they don't know how to treat you right."
    show bff sad
    bff "All they do is treat you like trash then act surprised when you hate their guts!"
    mc "..."
    mc "That explanation sounds a bit biased don't you think?"
    show bff normal
    bff "Just know that a tsundere is absolutely no good."
    show bff glee
    bff "And I know I told you to go ahead and build your own harem, but if you get with a tsundere I might have to reconsider our friendship."
    "Translation notes: A tsundere is..."
    "I actually have no idea how to explain this."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show ct_overlay
    show ct_fri
    show ct_120
    with dissolve
    show bff normal
    bff "Oh, the bell has rung."
    bff "I guess it's time for class."
    show bff blush
    bff "We'll talk in the club room after school!"
    stop music fadeout 1.0
    ##ts -----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts -----------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    show ct_overlay
    show ct_fri
    show ct_400
    with dissolve
    "It's after school."
    "In the club room with Nao, Akari..."
    "But Yuusuke is nowhere to be found."
    mc "Where is Yuusuke?"
    hide ct_400
    hide ct_fri
    hide ct_overlay
    with dissolve
    show imt exp1 with dissolve
    imt "He said that he got a part-time job and he can't be late."
    hide imt
    show bff worried
    bff "Awe, really?"
    bff "Did he really just flake out on us?"
    show bff glee
    bff "Well, I guess it's a girls only club today!"
    hide bff
    "The door suddenly slides open."
    show male4 excited with dissolve
    male4 "Hellooo!!! My fellow classmates!"
    male4 "I'm here for the drawing competition! I hope that you don't mind that I brought a little friend of mine!"
    hide male4
    show male3 blush
    male3 "Why do you always have to be so dramatic and end up making a fool out of yourself?"
    show male3 annoyed
    male3 "And then you drag me along with you..."
    male3 "I'm only here because you promised me strawberry bread."
    hide male3
    mc "I don't recall any of us being classmates with you..."
    mc "And what do you mean by art competition? This is the first time I'm hearing about this."
    show bff normal
    bff "Oh! Hi Kaoru!"
    show bff worried
    bff "..."
    bff "and Hiro..."
    show bff glee
    bff "Anyways, what are you two doing here?"
    hide bff
    show male4 normal
    male4 "Oh, we just wanted to check up on you guys."
    hide male4
    show male3 normal
    male3 "Kaoru got bored with paperwork so he decided to bother you guys to kill time instead."
    hide male3
    show male4 worried with vpunch
    $ renpy.vibrate(.5)
    male4 "Hey!"
    show male4 blush
    male4 "You didn't have to phrase it like that okay!"
    hide male4
    show bff normal
    bff "Well, anyways, today we're drawing portraits."
    show bff glee
    bff "So everyone strike a pose and let me take a picture for each of you guys!"
    hide bff
    show male3 normal
    male3 "..."
    male3 "Don't we usually pose for the portrait while somebody else is drawing though?"
    hide male3
    show bff worried
    bff "Oh, cmon, do you really expect to just sit in the same spot for several hours when we have this thing called-"
    bff "Yknow..."
    bff "Technology?"
    hide bff
    show male3 worried
    male3 "I guess."
    hide male3
    show bff glee
    bff "Alrighty then!"
    bff "Lets get started!"
    stop music fadeout 1.0
    ##ts ------------------------
    scene ts some_time_later with fade
    pause
    ##ts -------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    show bff normal with dissolve
    bff "Alright everyone time is up, show me what you got!"
    bff "Kaoru, lemme see your portrait!"
    bff "Who did you draw?"
    hide bff
    show male4 scared
    male4 "Oh... we were drawing portraits?"
    hide male4
    show bff glee
    bff "Lemme see, lemme see!"
    scene bg artroom
    play sound "audio/paper.wav"
    show art_drawing1 with dissolve
    pause
    play sound "audio/paper.wav"
    hide art_drawing1 with dissolve
    show bff normal
    bff "..."
    show bff worried
    bff "Kaoru, this isn't even a portrait, you drew a doodle of Matsuge Senpai from Otome Legends."
    hide bff
    show male4 blush
    male4 "Sorry."
    hide male4
    show bff glee
    bff "Chiharu, you never disappoint me. What did you draw today?"
    scene bg artroom
    play sound "audio/paper.wav"
    show art_drawing2 with dissolve
    pause
    play sound "audio/paper.wav"
    hide art_drawing2 with dissolve
    show bff worried
    bff "..."
    bff "Haru, this is a portrait of yourself."
    mc "Hey, you never told us we couldn't draw ourselves."
    bff "..."
    bff "Fair point."
    bff "..."
    show bff excited
    bff "Akari! What did you draw today?"
    hide bff
    show imt exp3
    imt "..."
    hide imt
    show bff glee
    bff "Lets see!"
    scene bg artroom
    play sound "audio/paper.wav"
    show art_drawing3 with dissolve
    pause
    play sound "audio/paper.wav"
    hide art_drawing3 with dissolve
    show bff worried
    bff "..."
    bff ". . ."
    bff "Akari, you drew nothing."
    bff "This is a blank piece of paper."
    bff "Did you pay attention to anything I said today at all?"
    hide bff
    show imt exp2
    imt "Sorry..."
    hide imt
    show bff normal
    bff "Well, I guess thats it for today's activity."
    mc "Wait..."
    mc "Don't you think you're missing someone?"
    show bff glee
    bff "Oh, you mean Yuusuke?"
    bff "Akari already told you that he was out today."
    mc "No, I mean hir-"
    show bff blush
    bff "Okay! Thats it for today's club activity! I hope I see you all next week!"
    hide bff
    "Naomi rushes Hiro and Kaoru out of the room."
    scene bg artroom with fade
    show ct_overlay
    show ct_fri
    show ct_430
    with dissolve
    show bff normal with dissolve
    bff "Haru, I'm going to be heading out now."
    show bff glee
    bff "Have fun with Akari for me!"
    hide bff with dissolve
    "And just like that Naomi suddenly disappears."
    stop music fadeout 1.0
    hide ct_430
    hide ct_fri
    hide ct_overlay
    with dissolve
    show imt exp1
    imt "..."
    mc "..."
    mc "Uhm, hey..."
    mc "You doing alright?"
    "Oh dear."
    "I'm not exactly sure how to interact with a middle schooler."
    show imt exp4
    imt "I didn't do it."
    mc "?"
    imt "I swear I didn't do anything wrong."
    mc "..."
    mc "What are you talking about?"
    mc "You okay?"
    imt "..."
    show imt exp2
    imt "Whatever Yuusuke said, don't believe him."
    mc "What did Yuusuke say?"
    show imt exp3
    imt "That..."
    imt "I took money from suspicious people."
    mc "Oh?"
    mc "Do you want to talk about it?"
    show imt exp1
    imt "..."
    imt "My friend told me to do it."
    imt "She paid me to do her homework for her."
    show imt exp3
    imt "..."
    imt "I'm sorry."
    show imt exp2
    imt "I know I shouldn't have done that."
    mc "..."
    mc "I think you should tell your brother that."
    mc "He deserves to know, don't you think?"
    show imt exp4
    imt "Yea..."
    mc "Is that what's been bothering you today?"
    mc "Cmon, lets get you home. I can't leave you here at school by yourself."
    show imt exp1
    imt "Okay."

    label choices9:
        stop music
        scene bg school_genkan with fade
        show imt exp1 with dissolve
        "Akari seems a bit timid around other people."
        "It reminds me of the time when I was in middle school."
        "I wasn't so good at talking to people either."
        "It's easier to warm up to people if theres less people around."
        mc "..."
        mc "(I have a feeling Yuusuke is gonna take a while to finish work.)"
        default yuusuke_end1 = False
        default yuusuke_end2 = False
        default yuusuke_end3 = False
    menu:
        "Akari, do you wanna go to the baseball field today?":
            stop music fadeout 1.0
            jump choices9_a
        "Soo, is there any place you wanna go today?":
            stop music fadeout 1.0
            jump choices9_b
        "...":
            stop music fadeout 1.0
            jump choices9_c

    label choices9_a:
    mc "Akari, I think Yuusuke is gonna be a while."
    mc "So lets go hang at the baseball field today until he's done."
    show imt exp3
    imt "..."
    show imt exp1
    imt "Okay."
    mc "Great, text him and tell him to pick us up from there."
    jump choices9_common1
# ------------------------------------------------------------------------
    label choices9_b:
    mc "Anyway, where do you want me to drop you off?"
    show imt exp3
    imt "..."
    show imt exp1
    imt "The convienence store."
    imt "Thats where my brother works."
    mc "Alright."
    jump choices9_common2
# -------------------------------------------------------------------------
    label choices9_c:
    mc "..."
    show imt exp1
    imt "..."
    mc "Oh!"
    mc "I think I left something in the classroom."
    mc "Let me go get it."
    jump choices9_common3
# -------------------------------------------------------------------------
    label choices9_common1:
    scene bg blank with fade
    "And so me and Akari played baseball at the baseball field until Yuusuke arrived."
    ##ts ----------------------------------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts ----------------------------------------------------------------------
    scene bg bedroom_yoru with fade
    mc "Finally."
    mc "I can get some time to myself today."
    mc "..."
    mc "What should I do?"

    label choices9A:
    menu:
        "Play some more Otome Legends":
            jump choices9A_a
        "Go to sleep.":
            jump choices9A_a
    label choices9A_a:
        scene bg blank
        centered "{color=#f44336}{font=DejaVuSans.ttf}{cps=10}What made you think you actually had a choice?{/cps}{/font}{/color}"
        jump choices9A_common

    label choices9A_common:
        play sound "audio/glitch.wav"
        scene bg blank
        show bsb_glitch
        $ renpy.pause(4.0, hard=True)
        centered "{w=4.0}{nw}"
        scene bg blank
        play sound "audio/beep.wav"
        show bsb_cursed
        $ renpy.pause(7.0, hard=True)
        centered "{w=7.0}{nw}"
        play music "audio/static.wav"
        scene bg blank
        show static
        show bsb_transparent with dissolve
        centered "{w=7.0}{nw}"
        pause
        scene bg blank
        scene static
        show bg bsb_transparent
        stop music fadeout 1.0
        show bsb_sticker
        show bsb_msg1 with dissolve
        pause
        hide bsb_msg1 with dissolve
        show bsb_msg2 with dissolve
        pause
        hide bsb_msg2 with dissolve
        show bsb_msg3 with dissolve
        pause
        hide bsb_msg3 with dissolve
        show bsb_msg4 with dissolve
        pause
        hide bsb_msg4 with dissolve
        show bsb_msg5 with dissolve
        pause
        hide bsb_msg5 with dissolve
        show bsb_msg6 with dissolve
        scene bsb_cursed
        centered "{w=0.25}{nw}"
        play sound "audio/static.wav"
        scene bg blank
        show static
        centered "{w=3}{nw}"
        scene bg red
        centered "{w=1}{nw}"
        $ yuusuke_end2 = False
        $ yuusuke_end3 = False
        $ yuusuke_end1 = True
    jump choices9_common

    label choices9_common2:
    scene bg kinjo with fade
    mc "(It should be somewhere around here)"
    play sound "audio/vibrate.wav"
    $ renpy.vibrate(.5)
    mc "!!!"
    "It's a notification."
    show sm_n with dissolve
    "It's Naomi."
    "\"How are you doing?\""
    hide sm_n with hpunch
    $ renpy.vibrate(.5)
    "!!!"
    scene bg blank with fade
    "I end up accidentally dropping my phone onto the ground."
    "But as I frantically try to pick it up and check the screen for any cracks..."
    mc "Oh, thank goodness, it's safe."
    mc "..."
    mc "Akari?"
    "Akari was no where to be found..."
    "But then..."
    imt "GET OFF OF ME!"
    imt "LET ME GO!"
    "As soon as I heard her scream I turned around and..."
    play music "audio/run.mp3" fadein 1.0 volume 1.0
    scene cg akari_kidnap with fade
    "I saw her being dragged into a large white van..."
    mc "AKARI!!!"
    ##show hand with dissolve
    "I run and extend out my hand to Akari in a desparate attempt to save her."
    stop music
    play sound "audio/horror_drum.wav"
    scene flash red
    pause
    scene bg blank with fade
    "I woke up in a strange empty room."
    "I was left tied to a chair by some kidnappers..."
    "and it appears that the men that threw me in here left ages ago."
    "After some struggling I managed to get the blindfolds off..."
    centered "{nw}"
    play sound "audio/suspense.wav" volume 0.5
    $ renpy.pause(2, hard=True)
    scene cg kidnapped:
        truecenter zoom 2.5 rotate 0 subpixel True xoffset 0 yoffset 350
        pause (3.0)
        ease 8.0 zoom 1.0 rotate 0.0 xoffset 0 yoffset 0
    pause
    mc "..."
    mc "(Where am I?)"
    "Drip... drip... drip... drip... drip"
    "I hear the sound of water slightly beat against the ground."
    "As I avert my eyes away from the floor I find myself in a damp room with black puddles on the concrete scattered across the ground."
    play sound "audio/scream.wav" volume 0.3
    "Girl" "AAAAAAHHHHHHH!!"
    mc "(Who was that?)"
    mc "(Was that Akari?)"
    mc "(Oh my god...)"
    mc "(How could I forget? Akari! That van! She was being taken away!)"
    mc "(I have to go save her!)"
    mc "..."
    mc "(But how do I get these ropes off of me?)"
    play sound "audio/door.mp3"
    mc "!!!"
    scene bg haibiru with fade
    show male2 surprised with dissolve
    male2 "There you are!"
    show male2 struggle
    male2 "Cmon, lets get you out of there!"
    scene bg blank with fade
    "Yuusuke walks into the room with a broken glass bottle in his hand."
    play sound "audio/knife.wav"
    "Using the sharpened edge, he unfastened my restraints."
    scene bg haibiru with fade
    show male2 happy with dissolve
    male2 "There you go."
    mc "???"
    mc "Yuusuke?! How are you here?!"
    show male2 struggle
    male2 "Now is not the time to be thinking about this!"
    show male2 normal
    male2 "You can stand now right?"
    show male2 struggle
    male2 "We have to hurry."
    male2 "Akari must be here somewhere."

label haibiru_minigame:
    $ yuusuke1 = False
    $ yuusuke2 = False
    $ rope = False
    $ locked_door = False
    $ paperclips = False
    $ box_cutter = False
    $ flashlight = False

    default yuusuke1 = False
    default yuusuke2 = False
    default rope = False
    default locked_door = False
    default paperclips = False
    default box_cutter = False
    default flashlight = False
    scene bg blank with fade
    centered "Find a way out by clicking on items in the room."
    centered "Make sure to check in with Yuusuke from time to time."
    play music "audio/uncanny.mp3"
    scene bg haibiru
    label hr1:
        if rope:
            scene bg blank
            call screen hr1_minigame_rope with fade
        else:
            scene bg blank
            call screen hr1_minigame with fade
    label hr2:
        scene bg blank
        call screen hr2_minigame
    label hr2a:
        scene bg blank
        call screen hr2a_minigame
    label hr2b:
        scene bg blank
        if box_cutter:
            scene bg haibiru
            show hr_thoughts
            centered "I don't need to go in there anymore."
            jump hr2
        else:
            call screen hr2b_minigame
    label hr3:
        scene bg blank
        if flashlight:
            call screen hr3_minigame with fade
        else:
            scene bg blank
            centered "It's too dark to see."
            centered "I need to find a light somewhere."
            jump hr2
    label hnxt1:
        call screen hnxt1_minigame

label hr1_item1:
    scene bg haibiru
    show hr_thoughts
    centered "It's the chair I was tied to."
    scene bg blank
    jump hr1
label hr1_item2:
    scene bg haibiru
    show hr_thoughts
    if rope:
        centered "(You already have this item.)"
        scene bg blank
        jump hr1
    if yuusuke2:
        centered "It's a rope..."
        centered "Maybe I should bring it with me."
        $ rope = True
    else:
        centered "It's rope."
    scene bg blank
    jump hr1
label hr1_item3:
    scene bg haibiru
    show hr_thoughts
    centered "A cloth on the ground."
    scene bg blank
    jump hr1
label hr1_item5:
    scene bg haibiru with fade
    if yuusuke2:
        show male2 normal
        male2 "What are you waiting for?"
        male2 "Cmon, lets go!"
        scene bg blank
        jump hr1
    if paperclips:
        show male2 normal with dissolve
        male2 "You found some paper clips?"
        show male2 happy
        male2 "Great."
        male2 "Now we can lockpick the door."
        male2 "We're lucky I know how to pick locks with paper clips."
        show male2 normal
        male2 "Although, you might want to check if there is anything useful we could carry before we move on."
        male2 "Hurry up though, we don't know when they'll be back."
        hide male2 with dissolve
        $ yuusuke2 = True
        scene bg blank
        jump hr1
    if locked_door:
        show male2 normal with dissolve
        male2 "What?"
        male2 "..."
        show male2 surprised
        male2 "You found a door?"
        show male2 normal
        male2 "Oh, it's locked you say?"
        male2 "Try to see if you can find any keys laying around or something."
        show male2 worried
        male2 "Who am I kidding?"
        show male2 normal
        male2 "Who just leaves keys for doors lying around?"
        male2 "We'd have better luck if we found something to pick the lock or whatever."
        hide male2 with dissolve
        $ yuusuke1 = True
    else:
        show male2 struggle with dissolve
        male2 "So far I haven't been able to find a way out of here."
        show male2 normal
        male2 "Try to see if you can find anything useful."
        hide male2 with dissolve
    scene bg blank
    jump hr1

label hr2a_item1:
    scene bg haibiru
    show hr_thoughts
    centered "Table."
    scene bg blank
    jump hr2a
label hr2a_item2:
    scene bg haibiru
    show hr_thoughts
    if paperclips:
        centered "I don't think I need anymore."
        scene bg blank
        jump hr2a
    if yuusuke1:
        centered "(You collected some paper clips on the table.)"
        $ paperclips = True
    else:
        centered "Some paper clips."
    scene bg blank
    jump hr2a
label hr2a_item3:
    scene bg haibiru
    show hr_thoughts
    if flashlight:
        centered "I already looked through this mattress."
        scene bg blank
        jump hr2a
    if box_cutter:
        centered "(You ripped open the mattress with the box cutter)"
        centered "Huh? Whats this?"
        centered "Theres some old devices and other junk stuffed into the mattress."
        centered "... an old camera?"
        centered "Oh! It has batteries!"
        centered "I can use it for the flashlight!"
        $ flashlight = True
    else:
        centered "A mattress."
    scene bg blank
    jump hr2a
label hr2a_item4:
    scene bg haibiru
    show hr_thoughts
    centered "A bottle."
    scene bg blank
    jump hr2a

label hr2b_item1:
    scene bg haibiru
    show hr_thoughts
    centered "A box and a box cutter."
    centered "And theres a flashlight in the box."
    centered "..."
    centered "It doesn't seem to have batteries..."
    centered "I'll guess I take the box cutter for now."
    centered "..."
    centered "and the flashlight just incase."
    $ box_cutter = True
    scene bg blank
    jump hr2

label hr3_item1:
    if yuusuke2:
        scene bg blank
        jump haibiru_after
    else:
        scene bg haibiru
        show hr_thoughts
        centered "The door is locked."
        $ locked_door = True
    scene bg blank
    jump hr3

label haibiru_after:
    stop music
    scene bg blank with fade
    "Man 1" "HOW COULD YOU BE SO CARELESS?!"
    "Man 2" "I'm sorry."
    "Man 1" "We're supposed to sell the bodies."
    "Man 1" "Organs are worth a fortune nowadays."
    "Man 1" "And you had to mess it up because of your careless mistake!"
    "Man 1" "Organs don't just grow on trees you fool!"
    "Man 2" "..."
    "Man 1" "Get the lighter."
    "Man 1" "We have no choice."
    "Man 1" "Burn the building, tell everyone to evacuate the building in 5 minutes or else they're going down with the fire."
    "Man 2" "Wait? How am I going to get everyone?"
    "Man 2" "Theres like 40 of us and I don't even know where everyone is."
    "Man 2" "What happens if everyone doesn't get out in time?"
    "Man 1" "Heck if I care."
    "Man 1" "They can all burn in the fire for all I care."
    "Man 1" "I'm getting the gasoline."
    "Man 1" "We're burning the evidence, if anyone asks what happened just say one of our guys accidentally set the building on fire while lighting a cig."
    "Man 1" "The police will be here any minute now."

    scene bg haibiru with fade
    mc "Okay I think I got all the ropes off."
    mc "Akari can you stand?"
    show imt exp1 with dissolve
    imt "..."
    show imt exp2
    imt "What is this place?"
    mc "Now is not the time for questions, we gotta run!"
    hide imt
    show male2 struggle
    male2 "Ugh, What is that smell?"
    male2 "Is somebody smoking or..."
    show male2 surprised
    male2 "FIRE!"
    male2 "IT'S FIRE! WE GOTTA GET OUT OF HERE QUICK!"

    label haibiru_run_minigame:
        $ hb1points = 50
        $ renpy.block_rollback()
        scene bg blank
        play music "audio/chimetown.mp3" fadein 1.0 volume 1.0
        call screen hb1clicker with fade
    label hb1win:
        $ renpy.block_rollback()
        $ renpy.pause(2, hard=True)
        $ hb1points = 50
        scene cg haibiru_hide with fade
        male2 "SHHHHH!"
        "Yuusuke silently urges me and Akari to not walk any futher."
        male2 "..."
        "A group of hooded men run past the halls."
        male2 "Okay, I think it's safe now."
        scene bg blank with fade
        call screen hide1 with fade

    label haibiru_continue1:
        $ renpy.block_rollback()
        $ renpy.pause(2, hard=True)
        $ hb2points = 50
        call screen hb2clicker with fade
    label hb2win:
        $ renpy.block_rollback()
        $ renpy.pause(2, hard=True)
        $ hb2points = 50
        scene cg haibiru_hide with fade
        mc "..."
        male2 "..."
        "Yuusuke checks if there is anyone around the corner."
        male2 "The coast is clear."
        scene bg blank with fade
        call screen hide2 with fade

    label haibiru_continue2:
        $ renpy.block_rollback()
        $ renpy.pause(2, hard=True)
        $ hb3points = 150
        call screen hb3clicker with fade
    label hb3win:
        $ renpy.pause(2, hard=True)
        $ hb3points = 150
        $ persistent.hbclicker = True
        jump haibiru_run_after

    label hb1lost:
        $ renpy.block_rollback()
        $ renpy.pause(2, hard=True)
        $ hb1points = 50
        $ hb2points = 150
        $ hb3points = 250
        scene white with fade
        jump haibiru_run_minigame

    label haibiru_run_after:
    $ renpy.block_rollback()
    stop music fadeout 1.0
    scene bg haibiru with fade
    show hr_thoughts with dissolve
    centered "We ran."
    centered "We ran, we ran, we ran."
    centered "We ran as the building was being engulfed by the flames."
    centered "Eventually we were able to find the stairs."
    centered "Unfortunately, however, on our way down..."
    centered "a large portion of the stairs had already collapsed."
    if rope:
        centered "But luckily for us, I had brought some rope with me before we left."
        centered "We tied the rope to the stair railing."
        centered "After me and Akari climbed down it was finally Yuusuke's turn..."
        centered "But just as he was about to climb down..."
        centered "The railing broke off, along with the rope."
        centered "\"RUN!\" He said."
        centered "\"I'll find another exit!\" He said."
        centered "\"I'll catch up with you guys later! Just run and go find some help!\" He said."
        centered "We ran until we reached the outside."
        centered "And we waited..."
        centered "and waited..."
        centered "We waited and waited until the police arrived."
        centered "We waited and waited until the firemen arrived."
        centered "We waited and waited..."
        centered "But Yuusuke never showed up..."
    else:
        centered "We tried to climb back up to find another exit."
        centered "But it was too late."
        centered "The way in which we came was already engulfed by flames."
        centered "We were completely surrounded by the fire."
        centered "Soon enough the stairs became unable to support the weight of the three of us."
        centered "And all three of us ended up plummeting towards our inevitable death."
        play music("audio/sad_theme.mp3") fadein 1.0 volume 2.0
        scene bg blank
        jump choices9_endgame
    $ yuusuke_end1 = False
    $ yuusuke_end3 = False
    $ yuusuke_end2 = True
    jump choices9_common

    label choices9_common3:
    scene bg artroom with fade
    "It should be here somewhere"
    mc "!!!" with vpunch
    $ renpy.vibrate(.5)
    show male3 normal with dissolve
    mc "(It's!!!)"
    mc "(... Wait what was his name again?)"
    "I forgot his name again" "..."
    show male3 annoyed
    "I forgot his name again" "It's not what you think it is!"
    "I forgot his name again" "Naomi rushed everyone out the room before I had a chance to pick up my belongings."
    show male3 angry
    "I forgot his name again" "I wasn't waiting for anyone to come back here or anything like that!"
    mc "..."
    mc "Excuse me?"
    show male3 blush
    "I forgot his name again" "N-N-N-NOTHING!"
    show male3 normal
    "I forgot his name again" "..."
    "I forgot his name again" "So what brings you here?"
    mc "I left my drawing in the classroom..."
    mc "..."
    mc "I'm sorry to ask but what was your name again?"
    play sound "audio/vibrate.wav"
    $ renpy.vibrate(.5)
    mc "Huh?"
    "I got a notification from my phone."
    hide male3 with dissolve
    scene bg artroom with dissolve
    show sm_n with dissolve
    pause
    play sound "audio/unlock.wav"
    show sm_sms
    "\"I'm going to head home now, it was nice hanging out with you.\""
    "Akari..."
    "Is she gonna be alright walking home by herself?"
    "Oh well."
    "..."
    "Wait..."
    "Aren't I supposed to be looking after her?"
    "..."
    "Whatever, that's Yuusuke's job, not mine."
    ##ts --------------------------------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts --------------------------------------------------------------------
    scene bg blank with fade
    male2 "Mom, Akari, I'm home!"
    male2 "!!!" with hpunch
    $ renpy.vibrate(.5)
    play sound "audio/horror_drum.wav"
    scene cg dead_family
    pause
    scene cg yuusuke shock1 with fade
    play music "audio/run.mp3"
    male2 "WHAT THE HECK?!"
    male2 "NO, NO, NO, NO, NO!"
    male2 "WHAT HAPPENED?!"
    scene cg yuusuke shock2 with dissolve
    male2 "Mom?"
    male2 "Akari?"
    male2 "..."
    male2 "Oh my god..."
    stop music fadeout 1.0
    play sound "audio/stab.mp3" volume 0.5
    scene flash red
    centered "{w=3}{nw}"
    $ yuusuke_end1 = False
    $ yuusuke_end2 = False
    $ yuusuke_end3 = True
    jump choices9_common

    label choices9_common:
    play music "audio/uncanny.mp3" fadein 1.0 volume 1.0
    scene cg yuusuke hospital with fade
    pause
    if yuusuke_end1:
        "I regret letting Akari walk home by herself..."
        "After we played at the baseball field for a couple of hours, Yuusuke never showed up..."
        "She insisted on walking home by herself."
        "So I decided to call it a day and head home."
        "After I got home, however..."
        "Akari texted me that there was something wrong..."
        "She felt like someone was following her..."
        "She texted me if she could stay over at my house tonight..."
        "So I asked her to wait for me at the local conveinence store and call the police if she noticed anything suspicious."
        "After that she stopped responding to my texts..."
        "So I rushed out to go find her."
        "When I got there, the police were surrounding the convienence store..."
        "They asked if I knew Yuusuke..."
        "They asked if I knew Akari too..."
        "..."
        $ persistent.y_end1 = True
        "I didn't expect things to end up like this..."
        "Why?"
        "Why do the people I care about end up getting hurt?"
        "Yuusuke..."
        "Ishida..."
        "Why?"
        "Yuusuke Route: Ending 1/3"
        jump yuusuke_end_common
    if yuusuke_end2:
        "The police found him on the ground beside the burning building."
        "They said that they suspect he jumped out of a window in a desparate attempt to escape from the fire."
        "He hit the ground too hard."
        "Now he's unconscious."
        $ persistent.y_end2 = True
        "I didn't expect things to end up like this..."
        "Why?"
        "Why do the people I care about end up getting hurt?"
        "Yuusuke..."
        "Ishida..."
        "Why?"
        "Yuusuke Route: Ending 2/3"
        jump yuusuke_end_common
    if yuusuke_end3:
        "I shouldn't have let Akari walk home by herself..."
        "Whats wrong with me?"
        "The police suspected it to be a home robbery..."
        "But the robber ended up breaking into the house while Akari and Yuusuke's mom was still there..."
        "When Yuusuke got home... all that was left were the dead bodies..."
        "It looked as though Yuusuke put up a fight but he ended up getting stabbed in the abdomen..."
        "That criminal stabbed him and ran."
        "It seems the only thing that saved Yuusuke was the fact that crook seemed like he was in a rush to run away from the police."
        "... and because of that Yuusuke was the only one left that survived..."
        "...survived... at the very least..."
        "That stab wound left him in a coma."
        "I hope he wakes up soon..."
        $ persistent.y_end3 = True
        "I didn't expect things to end up like this..."
        "Why?"
        "Why do the people I care about end up getting hurt?"
        "Yuusuke..."
        "Ishida..."
        "Why?"
        "Yuusuke Route: Ending 3/3"
        jump yuusuke_end_common

    label yuusuke_end_common:
    scene bg blank with fade

    if persistent.y_end1 and persistent.y_end2 and persistent.y_end3:
        jump after_yuusuke
    else:
        jump yuusukeroute_end
    return

    label after_yuusuke:
    stop music fadeout 1.0
    ##ts --------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts --------------------------------------------------------------------
    play music "audio/uncanny.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show bff worried with dissolve
    bff "Haru, are you okay?"
    bff "You don't look so well today."
    mc "..."
    bff "Did something happen yesterday?"
    bff "You didn't respond to my text..."
    mc "Yuusuke..."
    mc "I couldn't save him..."
    mc "Yesterday, I saw him at the hospital."
    mc "The doctors said he was comatose..."
    mc "They don't know when he's gonna wake up."
    show bff depressed
    bff "..."
    bff "I'm sorry..."
    stop music fadeout 1.0
    show bff worried
    bff "But do you mind if I ask you one thing real quick?"
    mc "..."
    mc "What?"
    bff "Who is Yuusuke?"
    if persistent.yuusuke:
        jump yuusuke_end

    play sound "audio/horror_drum.wav"
    scene bg blank
    centered "{w=1}{nw}"
    $ renpy.pause(3.0, hard=True)
    play sound "audio/static.wav"
    scene bg blank
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg school_genkan
    mc "Anyway, where do you want me to drop you off?"
    show imt exp3
    imt "..."
    show imt exp1
    imt "The convienence store."
    imt "Thats where my uncle works."
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg artroom
    show imt exp2
    imt "Whatever Naomi said, don't believe her."
    mc "What did Naomi say?"
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg artroom
    show imt exp4
    mc "Akari, you drew nothing."
    mc "This is a blank piece of paper."
    mc "Did you pay attention to anything I said today at all?"
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg artroom
    "It's after school."
    "In the club room with Akari and..."
    "Naomi is nowhere to be found."
    mc "Where is Naomi?"
    show imt exp1 with dissolve
    imt "She said that she had to help my uncle with work at his store so she had to leave early."
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg kaoru_office
    show bff normal
    mc "Geez Naomi, you don't have to be so mean. Hiro's a human being too, you know."
    show bff glee
    bff "Sorry, I was only stating facts."
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg school_hallway
    show male3 normal
    male3 "Please don't mind this hooligan, she's only late because she was helping me out with something this morning."
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg kaoru_office
    "Naomi eagerly opens her bento box."
    show male4 excited
    male4 "Oh my gosh is that chicken?!"
    male4 "Let me have a piece!"
    hide male4
    "And so Naomi and Kaoru talked nonstop leaving me alone to sit awkwardly in silence to eat my lunch."
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg kaoru_office
    show male4 scared with dissolve
    male4 "..."
    show male4 nervous
    male4 "She did it!"
    hide male4 with dissolve
    "He runs away."
    male3 "YOU!!!!"
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    scene bg school_clinic
    show male4 normal
    male4 "And who is this?"
    show male4 happy
    male4 "Is it one of your lady friends?"
    hide male4 happy
    show male3 blush
    male3 "!!!"
    show male3 angry
    male3 "You need to stop with that."
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    $ renpy.pause(3.0, hard=True)
    $ persistent.yuusuke = True
    $ achievement.grant("redacted_achievement")
    $ achievement.sync()
    stop music
    scene bg blank
    centered "Something doesn't seem quite right..."
    centered "Maybe you should try again?"
    call screen yuusuke_retry with dissolve
    return

    label no_yuusuke_route:
    stop music
    scene bg kinjo with fade
    mc "!!!" with hpunch
    $ renpy.vibrate(.5)
    mc "Ow..."
    "I ended up falling and scraping my knee."
    mc "Oh no..."
    mc "It's bleeding...?"
    mc "I should get this patched up at the clinic."
    mc "I should get going before I'm late!"
    scene bg school_clinic with fade
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    mc "Hello?"
    mc "Is there anybody here?"
    mc "Nobody?"
    mc "(sigh)"
    mc "Okay, where are the bandages?"
    show male3 normal with dissolve
    male3 "Uhm..."
    male3 "Can I help you?"
    male3 "..."
    "He looks down at my scraped knee."
    show male3 worried
    male3 "Did you fall or something?"
    male3 "Hold on, I think I can find you some bandages."
    mc "Oh, no thanks..."
    mc "It's actually not a big deal."
    mc "... I'll just come back later..."
    show male3 annoyed
    male3 "Geez, why do you have to be so stubborn?"
    male3 "Yknow, you might get an infection if you leave wounds open without disinfecting them!"
    mc "..."
    mc "I guess..."
    hide male3 worried
    "The door opens."
    show male4 glee with dissolve
    male4 "HIROHIROHIRO!!!"
    male4 "HIROHIRO HIROHIROOOOO!!!"
    hide male4 glee
    show male3 angry
    male3 "Do you have to scream my name like that every single time?"

    scene intro hiro bg1 with dissolve
    play sound "audio/tape.wav"
    pause (0.5)
    scene intro hiro bg2 with wipeleft
    play sound "audio/flute.wav"
    scene white with dissolve
    pause (2.0)
    play sound "audio/glitter.wav"
    scene intro hiro bg3 with dissolve
    pause (4.0)
    scene bg school_clinic
    show male3 annoyed
    with dissolve

    with dissolve
    male3 "You sound like a maniac."
    hide male3
    show male4 blush
    male4 "Do I need a reason to scream out my best friend's name?"
    show male4 worried
    male4 "We're practically brothers at this point don't you think?"
    show male4 normal
    male4 "Besides, it's fun to say it like that."
    hide male4 normal
    show male3 annoyed
    male3 "God, you're so cringe."
    hide male3
    show male4 normal
    male4 "And who is this?"
    show male4 happy
    male4 "Is it one of your lady friends?"
    hide male4 happy
    show male3 blush
    male3 "!!!"
    show male3 angry
    male3 "You need to stop with that."
    "..."
    "I have a feeling that these two are close friends."
    "These two remind me of whenever I'm with Naomi."
    "I can't help but chuckle to myself."
    hide male3 worried
    show male4 glee
    male4 "Anyway, what are you two troublemakers doing in the clinic?"
    hide male4
    mc "Oh that?"
    mc "I was walking by and..."
    show male3 normal
    male3 "Hey!"
    hide male3
    show male4 nervous
    male4 "!"
    show male4 normal
    male4 "Yes?"
    hide male4
    show male3 normal
    male3 "Do you know where the nurse is? We've been trying to find her."
    male3 "We need antiseptics and some bandages."
    hide male3
    show male4 worried
    male4 "Oh my, did you get into another fight again?"
    show male4 blush
    male4 "He's always like this, don't worry, I'll take care of it. You can go to class."
    show male4 worried
    male4 "Here's a note from me saying that you have an excused tardy."
    hide male4
    show male3 normal
    male3 "Wait, hold on Kaoru!"
    hide male3
    show male4 blush
    male4 "Hiroro, shush! You're going to scare her away!"
    show male4 normal
    male4 "Nevermind him, you can get going now."
    mc "Oh, ok thanks."
    mc "I guess I'll get going now."
    "I exit the clinic and make my way towards the classroom."
    hide male4 normal
    show male3 normal
    male3 "Kaoru, you sure you can just give out excused tardy notes like that?"
    show male3 worried
    male3 "I think the teachers are annoyed that you keep passing those out to students so easily..."
    hide male3
    show male4 normal
    male4 "Oh, Hiro."
    male4 "We all know the only person that has to worry about what the teachers' think is me."
    show male4 glee
    male4 "Now, stop being nosy and mind your own business."
    stop music fadeout 1.0
    scene bg blank with fade
    "I returned back to class with the excused note I got from the guy in the clinic."
    "The teacher looked slightly annoyed and disappointed at the same time reading it though."
    ##ts ---------------------------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts ---------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show bff blush with dissolve
    bff "HARUURUU"
    show bff glee
    mc "?..."
    show bff normal
    bff "Haru..."
    bff "Lets say..."
    show bff glee
    bff "You're not in any clubs are you?"
    mc "No?"
    show bff normal
    bff "Hmmm"
    show bff excited
    bff "Then how about joining the art club?"
    show bff blush
    mc "I think I'll take a hard pass."
    show bff worried
    bff "Awe, why?"
    mc "Last time you made me join a club, it turned out to be full of cringe fan girls obsessed with boy idol groups."
    mc "You told me it was just a music club, and I was stupid for believing you."
    mc "And I know that the art club is filled with girls obsessed with dating sims just like you are."
    show bff glee
    bff "Oh cmon, that was middle school."
    show bff normal
    bff "I mean why not join?"
    show bff worried
    bff "Aren't you supposed to be really good at drawing?"
    mc "Nao, I'm just not really interested in joining any clubs."

    label no_choices6:
        show bff sad
        bff "Cmon, please!"
    menu:
        "(Say no)":
            jump no_choices6_a
        "(Say maybe)":
            jump no_choices6_b
        "(Say yes)":
            jump no_choices6_c

    label no_choices6_a:
        jump no_yuusuke_route1

    label no_choices6_b:
        jump no_yuusuke_route2

    label no_choices6_c:
        jump no_yuusuke_route3


    label no_yuusuke_route1:
    mc "No means no Nao."
    show bff worried
    bff "Awww"
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Anyways, I'll see ya after class."
    stop music fadeout 1.0
    ##ts ------------------------------------------------
    scene ts after_class
    pause
    ##ts -------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_hallway with fade
    "Sensei told me to carry these papers to the teacher's office."
    "Still though, I wonder why she had to make me carry so many of these by myself."
    "It's towering over my face and its blocking my field of vision"
    "!!!" with hpunch
    $ renpy.vibrate(.5)
    male4 "Oh my gosh! I'm sorry!"
    male4 "Are you okay?"
    male4 "Here, let me carry these for you."
    scene bg school_hallway with fade
    show male4 worried
    male4 "Where are you taking these by the way?"
    mc "The teacher offices."
    show male4 normal
    male4 "I see."
    male4 "..."
    scene bg school_hallway with fade
    show male4 glee with dissolve
    male4 "Alright, that's that."
    show male4 happy
    male4 "..."
    show male4 normal
    male4 "Hey..."
    show male4 glee
    male4 "By any chance, do you think you could stop by the disciplinary room after school today?"
    mc "Uhm... why?"
    show male4 blush
    male4 "I kinda need a favor."
    mc "Uhm.. Okay, that's fine I guess."
    show male4 excited
    male4 "Alright! Great then!"
    show male4 glee
    male4 "Bye!"
    hide male4 with dissolve
    "The strange kid disappeared into the depths of the hallways as he waved to me goodbye."
    "What have I gotten myself into this time?"
    stop music fadeout 1.0

    ##ts ----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------------------------
    scene bg kaoru_office_door with fade
    "Is this the right room?"
    "(knocks)"
    male4 "Coming!"
    mc "..."
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg kaoru_office with fade
    show male4 normal with dissolve
    mc "So what is it that you need help with?"
    male4 "So, I heard that you were good at drawing."
    mc "... Where did you hear that from?"
    show male4 scared
    male4 "..."
    show male4 nervous
    male4 "Naomi."
    show male4 worried
    male4 "I asked her if she was any good at drawing."
    show male4 blush
    male4 "She told me to ask you."
    mc "Wait, how do you know Naomi?"
    show male4 happy
    male4 "She's a good friend of mine."
    show male4 scared
    male4 "We often talk about... stuff.. together."
    show male4 normal
    male4 "Anyway! Let's get down to business!"
    show male4 happy
    mc "Alright so, what is it that you need from me today?"
    show male4 scared
    male4 "So, I borrowed my friend's manga for a little bit."
    show male4 nervous
    male4 "And I accidentally spilled some tea on the pages as I was reading it..."
    male4 "And some of the pages got all blurry and messy..."
    show male4 scared
    male4 "And I tried cleaning it but"
    male4 "I messed up and ended up wiping the ink off the pages instead..."
    show male4 nervous
    male4 "So I took the cover of the manga and put it on a different manga and gave it back to him so he wouldn't notice."
    male4 "It's only a matter of time before he notices."
    show male4 blush
    male4 "Sooooo"
    male4 "I was wondering if you could help me redraw some of the pages."
    mc "Why don't you just print out the pages and stick them back into the book?"
    stop music fadeout 1.0
    show male4 scared
    play sound "audio/dooropen.wav"
    "The door opens"
    scene cg trio_antics2 with fade
    male3 "Kaoru!!!"
    male3 "Where is my manga?!"
    scene bg kaoru_office with fade
    show male4 scared with dissolve
    male4 "..."
    show male4 nervous
    male4 "She did it!"
    hide male4 nervous with dissolve
    "He runs away."
    male3 "YOU!!!!"
    scene bg track with fade
    mc "Haah, haah, hah."
    mc "Okay I think he stopped following me."
    mc "..."
    mc "Maybe I should've joined a club after school after all."
    mc "I really don't have anything to do when school is done anyway."
    mc "I wonder if Nao is still busy with her club activities."
    mc "Maybe I should pay a visit."
    #play music "audio/remember.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    mc "!"
    mc "Nao!"
    show bff normal with dissolve
    bff "Oh! Hi Haruu!"
    mc "Why are you in the club room by yourself?"
    show bff worried
    bff "Oh... uhm"
    show bff sad
    bff "It's actually because I wanted to start a club by myself but I never got any members..."
    show bff normal
    bff "But that's okay, I'm working on the recruitment posters by myself."
    mc "..."
    mc "Do you want me to help you?"
    show bff excited
    bff "Would you?!"
    show bff blush
    bff "I mean, I would really appreciate it!"
    stop music fadeout 1.0
    scene bg blank with fade
    "And so, me and Nao spent the afternoon working on drawing and printing posters for the art club."
    stop music fadeout 1.0
    ##ts -------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts -------------------------------------------------------------------
    play music "audio/ponder_ost.mp3" fadein 1.0 volume 1.0
    scene bg grave with fade
    "Ishida's grave should be somewhere here."
    "I have to get home before it gets too late."
    "I take a glance at the grave."
    mc "(Ishida...)"
    mc "(I wish I could've gotten to spend more time with you.)"
    "After leaving flowers on his grave I head my way home."
    stop music fadeout 1.0
    ##ts ------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts ------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show bff excited with dissolve
    bff "Harurunnn"
    mc "Yes?"
    show bff blush
    bff "Do you think you can go shopping with me after school?"
    mc "Hmm...."
    mc "I'm not sure if I have enough to buy anything."
    mc "Window shopping maybe."
    show bff worried
    bff "Don't worry, we're not going out to go shopping for clothes this time."
    show bff glee
    bff "It's my mom's birthday and I wanna go get something special."
    mc "Alright, I'll go then, I guess."
    show bff excited
    bff "Great! Meet me at the train station after school!"
    hide bff excited with dissolve
    play sound "audio/schoolchime1.wav"
    "The bell rings"
    "Just in time for class."
    stop music fadeout 1.0
    scene bg blank with fade
    "As usual, after school was over, I headed over to the school shoe lockers to meet up with Naomi."
    ##ts --------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts --------------------------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_genkan with fade
    show bff worried
    bff "Haruuuu!"
    mc "Oh, hey."
    mc "You ready to go?"
    show bff excited
    bff "I'm ready when you are!"
    scene bg blank with fade
    "It's nice to hang out with Nao after school sometimes."
    "Though, I don't really like the train that much to be honest."
    "It's always crowded and full of creepy weirdos that like to harass women."
    "I heard about it on the news."
    "Stalking on the rise."
    "Women and children must be wary on trains."
    "Watch out for suspicious men who harass women."
    "Rush hour is the worst though."
    "Hundreds of people crammed into a small compact space just to make it to work on time."
    "I don't know how office workers do it."
    "If it were me, I bet I would suffocate on my way to work."
    bff "Haru!"
    scene bg station no_train with fade
    show bff glee with dissolve
    bff "We're here!"
    mc "..."
    mc "(We're here faster than I expected.)"
    mc "Oh."
    show bff normal
    bff "Our train will arrive in like 5 minutes."
    mc "I'll guess I'll just be on the lookout until then."
    mc "... for the train I mean."
    scene bg blank with fade
    "I spend the next five minutes talking with Nao."
    "... listening to her talk about shoujo manga."
    "I hope she doesn't recommend me to read one as well."
    stop music fadeout 1.0
    scene bg station with fade
    show bff glee with dissolve
    bff "It's here!"
    mc "Alright."
    mc "!!!"
    play music "audio/heartbeat.wav" fadein 1.0 volume 1.0
    scene bg blank with fade
    "Huh?"
    "What is this feeling?"
    "I can't move..."
    "..."
    "It's okay, I just need to get on the train."
    "Yes, the train."
    "There's nothing wrong with trains right?"
    "People ride them all the time."
    "..."
    "Ishida..."
    "Why..."
    jump no_yuusuke_route_common

    label no_yuusuke_route2:
    mc "I'll think about it."
    show bff glee
    bff "Alright, fair enough."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Anyways, I'll see ya after class."
    stop music fadeout 1.0
    ##ts ------------------------------------------------
    scene ts after_class with fade
    pause
    ##ts -------------------------------------------------
    scene bg classroom with fade
    mc "(Its lunch time.)"
    mc "..."
    mc "(But where is Nao?)"
    mc "(I'll guess I'll go to the vending machine.)"
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_hallway with fade
    "I make my way to the vending machine."
    male4 "Hey!"
    show male4 normal with dissolve
    mc "???"
    male4 "You're Haru right?"
    show male4 happy
    male4 "I heard about you from Naomi."
    mc "Naomi?"
    mc "(Sigh)"
    "I hope this isn't another one of her schemes to pair me up with another guy."
    mc "Yea, that's my name alright."
    mc "Anyway, do you need anything?"
    show male4 glee
    male4 "Actually, yes."
    show male4 blush
    male4 "I'm sorry, I forgot to introduce myself."
    show male4 happy
    male4 "I'm Kaoru, head of the disciplinary committee."
    show male4 normal
    male4 "There's actually a matter I would like to discuss with you in private."
    male4 "Do you think you can meet me in the disciplinary room after school?"
    mc "Okay, I guess."
    show male4 excited
    male4 "Alright, then it's settled!"
    show male4 glee
    male4 "See ya after school!"
    hide male4 glee with dissolve
    "..."
    "Guess I'm occupied after school."
    stop music fadeout 1.0
    ##ts ----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------------------------
    scene bg kaoru_office_door with fade
    "Is this the right room?"
    "(knocks)"
    male4 "Coming!"
    mc "..."
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg kaoru_office with fade
    show male4 normal with dissolve
    mc "So what is it that you need help with?"
    male4 "So, I heard that you were good at drawing."
    mc "... Where did you hear that from?"
    show male4 scared
    male4 "..."
    show male4 nervous
    male4 "Naomi."
    show male4 worried
    male4 "I asked her if she was any good at drawing."
    show male4 blush
    male4 "She told me to ask you."
    mc "Wait, how do you know Naomi?"
    show male4 happy
    male4 "She's a good friend of mine."
    show male4 scared
    male4 "We often talk about... stuff.. together."
    show male4 normal
    male4 "Anyway! Let's get down to business!"
    show male4 happy
    mc "Alright so, what is it that you need from me today?"
    show male4 scared
    male4 "So, I borrowed my friend's manga for a little bit."
    show male4 nervous
    male4 "And I accidentally spilled some tea on the pages as I was reading it..."
    male4 "And some of the pages got all blurry and messy..."
    show male4 scared
    male4 "And I tried cleaning it but"
    male4 "I messed up and ended up wiping the ink off the pages instead..."
    show male4 nervous
    male4 "So I took the cover of the manga and put it on a different manga and gave it back to him so he wouldn't notice."
    male4 "It's only a matter of time before he notices."
    show male4 blush
    male4 "Sooooo"
    male4 "I was wondering if you could help me redraw some of the pages."
    mc "Why don't you just print out the pages and stick them back into the book?"
    stop music fadeout 1.0
    show male4 scared
    play sound "audio/dooropen.wav"
    "The door opens"
    scene cg trio_antics2 with fade
    male3 "Kaoru!!!"
    male3 "Where is my manga?!"
    scene bg kaoru_office with fade
    show male4 scared with dissolve
    male4 "..."
    show male4 nervous
    male4 "She did it!"
    hide male4 nervous with dissolve
    "He runs away."
    male3 "YOU!!!!"
    scene bg track with fade
    mc "Haah, haah, hah."
    mc "Okay I think he stopped following me."
    mc "..."
    mc "Maybe I should head home too."
    ##ts ---------------------------------------------------------------------
    scene ts home with fade
    pause
    ##ts ---------------------------------------------------------------------
    scene bg bedroom_yoru with fade
    mc "..."
    mc "Now where was that device?"
    mc "Oh! Here it is!"
    show bsb_blank with dissolve
    pause
    scene bg bsb_blank with dissolve
    pause
    play sound "audio/unlock.wav"
    play music "audio/bsbtheme.mp3"
    scene bg bsb_on with dissolve
    "It's the next day."
    "You arrive at school just in time for class when you suddenly hear some random guy open the class door loudly."
    "Everyone notices him."
    show senpai matsuge with dissolve
    senpai2 "OH HOHOHOHOHOHO!"
    senpai2 "Moi? Perdre une course? Jamais de la vie !"
    senpai2 "..."
    senpai2 "Je n'y avais pas mis le cœur, autrement la victoire aurait été à moi, sans doute."
    senpai2 "Que je suis brillant, que je suis sportif ah la la..."
    senpai2 "Je n'ose plus jeter un seul coup d'œil à mon miroir, sous peine d'être ébloui par mon propre charme."
    senpai2 "Je ne perds uniquement que face à moi-même."
    senpai2 "Et même si j'avais joué contre moi, j'aurais gagné évidemment."
    "???"
    "What is he even saying?"
    "I checked the language options in the settings to make sure that I didn't accidentally set it to French."
    "... I don't think I changed it..."
    "Translation Notes: I'm sorry, I can't help you here. I don't speak French."
    shoujo1 "I'm glad Matsuge senpai finally mustered up the courage to come back!"
    shoujo2 "Yea, I was kind of worried about him."
    shoujo1 "Don't you think he sounds so romantic when he starts speaking in French though?"
    shoujo2 "Yea, I have absolutely no idea what he's saying but it sounds so dreamy!"
    stop music fadeout 1.0
    play sound "audio/unlock.wav"
    scene bg bsb_blank
    "..."
    "I don't think I can continue on with this game anymore."
    "..."
    "I think I'm gonna go to sleep."
    ##ts ----------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts ----------------------------------------------------------------------
    play music "audio/classtime.mp3"
    scene bg classroom with fade
    show bff excited with dissolve
    bff "Harurunnn"
    mc "Yes?"
    show bff blush
    bff "Do you think you can go shopping with me after school?"
    mc "Hmm...."
    mc "I'm not sure if I have enough to buy anything."
    mc "Window shopping maybe."
    show bff worried
    bff "Don't worry, we're not going out to go shopping for clothes this time."
    show bff glee
    bff "It's my mom's birthday and I wanna go get something special."
    mc "Alright, I'll go then, I guess."
    show bff excited
    bff "Great! Meet me at the train station after school!"
    hide bff excited with dissolve
    play sound "audio/schoolchime1.wav"
    "The bell rings"
    "Just in time for class."
    stop music fadeout 1.0
    scene bg blank with fade
    "As usual, after school was over, I headed over to the school shoe lockers to meet up with Naomi."
    ##ts --------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts --------------------------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_genkan with fade
    show bff worried
    bff "Haruuuu!"
    mc "Oh, hey."
    mc "You ready to go?"
    show bff excited
    bff "I'm ready when you are!"
    scene bg blank with fade
    "It's nice to hang out with Nao after school sometimes."
    "Though, I don't really like the train that much to be honest."
    "It's always crowded and full of creepy weirdos that like to harass women."
    "I heard about it on the news."
    "Stalking on the rise."
    "Women and children must be wary on trains."
    "Watch out for suspicious men who harass women."
    "Rush hour is the worst though."
    "Hundreds of people crammed into a small compact space just to make it to work on time."
    "I don't know how office workers do it."
    "If it were me bet I would suffocate on my way to work."
    bff "Haru!"
    scene bg station no_train with fade
    show bff glee with dissolve
    bff "We're here!"
    mc "..."
    mc "(We're here faster than I expected.)"
    mc "Oh."
    show bff normal
    bff "Our train will arrive in like 5 minutes."
    mc "I'll guess I'll just be on the look out until then."
    mc "... for the train I mean."
    scene bg blank with fade
    "I spend the next five minutes talking with Nao."
    "... listening to her talk about shoujo manga."
    "I hope she doesn't recommend me to read one as well."
    stop music fadeout 1.0
    scene bg station with fade
    show bff glee with dissolve
    bff "It's here!"
    mc "Alright."
    mc "!!!"
    scene bg blank with fade
    play music "audio/heartbeat.wav"
    "Huh?"
    "What is this feeling?"
    "I can't move..."
    "..."
    "It's okay, I just need to get on the train."
    "Yes, the train."
    "Theres nothing wrong with trains right?"
    "People ride them all the time."
    "..."
    "Ishida..."
    "Why..."
    jump no_yuusuke_route_common

    label no_yuusuke_route3:
    mc "Alright, fine."
    show bff worried
    mc "I'll join."
    show bff blush
    bff "YAY!"
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Anyways, I'll talk to ya about it after class."
    ##ts ------------------------------------------------
    scene ts after_class
    pause
    ##ts -------------------------------------------------
    scene bg classroom with fade
    show bff excited with dissolve
    bff "Harucchi"
    mc "Hmm?"
    show bff blush
    bff "Let's go eat lunch together on the-!{nw}"
    show bff worried
    bff "..."
    show bff glee
    bff "How about we both eat in the classroom?"
    show bff normal
    mc "..."
    mc "Don't we always usually eat in the classroom?"
    show bff worried
    bff "Uhm, forget I said anything."
    show bff normal
    bff "Anyway, I forgot my bento today."
    bff "Do you think you can go buy that strawberry bread for me today?"
    mc "Oh yea, I forgot about that."
    mc "Do you wanna come with or...?"
    "Sensei" "Nakamura san!"
    show bff worried with vpunch
    $ renpy.vibrate(.5)
    bff "!"
    bff "... I have to go now, Sensei is calling me for something."
    show bff glee
    bff "You can go get the strawberry bread without me, I'll be here when you come back."
    hide bff glee with dissolve

    #ts ------------------------------------------------------------------------
    scene bg blank with fade
    "The Hallway"
    #ts ------------------------------------------------------------------------
    scene bg school_hallway with fade
    "In the end they didn't have strawberry bread."
    "Only melon bread and chocolate kornets."
    "I hope Nao will accept this."
    "!!!" with hpunch
    $ renpy.vibrate(.5)
    show male4 worried with dissolve
    male4 "(I wonder why Hiro likes these so much.)"
    "It's that guy from earlier!"
    "He has a strawberry bread!"
    mc "Hey!"
    show male4 nervous
    male4 "!!!"
    mc "Do you think I can have that strawberry bread?"
    mc "I'll trade with you for my melon bread."
    show male4 normal
    male4 "Oh, it's you."
    male4 "Sorry, but no can do. This bread is for a friend of mine."
    mc "Please!! I'll do anything!"
    mc "Yknow what, I'll buy it from you just let me check my wallet!"
    "..."
    "I checked my wallet..."
    "Unfortunately for me however, there is no cash."
    "Empty..."
    show male4 blush
    male4 "I'm sorry but I gotta go, okay?"
    hide male4 with dissolve
    "Kaoru rushed quickly through the hallways."
    mc "..."
    mc "Man, I really do need a part-time job."
    scene bg classroom with fade
    show bff blush with dissolve
    bff "Haruu!!!"
    show bff excited
    bff "Did you get that strawberry bread I was asking for?"
    mc "..."
    mc "Here"
    show bff worried
    bff "Melon bread?"
    mc "I'm sorry, it was the only thing they had."
    show bff normal
    bff "Oh, is that so?"
    show bff glee
    bff "Well don't worry about it! Thanks for the melon bread! I have a strawberry milk to go with it so that makes it a strawberry bread right?"
    mc "I don't think thats how it works Nao."
    show bff worried
    bff "Well, thats how it works for me."
    show bff normal
    bff "Anyway, lets talk about our plans for the club."
    stop music fadeout 1.0

    ##ts ----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ----------------------------------------------------------------------

    scene bg artroom with fade
    show bff glee with dissolve
    bff "And we're here!"
    show bff normal
    mc "So, this is the club room right?"
    mc "Where are all the other members?"
    show bff worried
    bff "Oh... uhm"
    show bff sad
    bff "It's actually because I wanted to start a club by myself but I never got any members..."
    show bff normal
    bff "But thats okay, I'm working on the recruitment posters by myself."
    mc "..."
    mc "Do you want me to help you?"
    show bff excited
    bff "Ah thanks Haru!"
    show bff blush
    bff "I knew you were the best!!"
    show bff blush with fade
    bff "Lemme see! Lemme see!"
    show bff excited
    bff "Oh wow! You really must've out done yourself!"
    show bff normal
    bff "Anyway, I'll see you tomorrow I guess!"
    show bff glee
    bff "I can't wait to hang these up! I bet we're gonna get alot of members after we post these!"

    ##ts -------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts -------------------------------------------------------------------
    #play music "audio/mourning.mp3" fadein 1.0 volume 1.0
    scene bg grave with fade
    mc "(Ishida's grave should be somewhere here.)"
    mc "(I have to get home before it gets too late.)"
    "I placed flowers on top of his grave."
    mc "(Ishida...)"
    mc "(I wish I could've gotten to spend more time with you.)"
    "After leaving flowers on his grave I head my way home."
    stop music fadeout 1.0
    ##ts ------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts ------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show bff excited with dissolve
    bff "Harurunnn"
    mc "Yes?"
    show bff blush
    bff "Do you think you can go shopping with me after school?"
    mc "Hmm...."
    mc "I'm not sure if I have enough to buy anything."
    mc "Window shopping maybe."
    show bff worried
    bff "Don't worry, we're not going out to go shopping for clothes this time."
    show bff glee
    bff "It's my mom's birthday and I wanna go get something special."
    mc "Alright, I'll go then, I guess."
    show bff excited
    bff "Great! Meet me at the train station after school!"
    hide bff excited with dissolve
    play sound "audio/schoolchime1.wav"
    "The bell rings"
    "Just in time for class."
    stop music fadeout 1.0
    scene bg blank with fade
    "As usual, after school was over, I headed over to the school shoe lockers to meet up with Naomi."
    ##ts --------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts --------------------------------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0
    scene bg school_genkan with fade
    show bff worried
    bff "Haruuuu!"
    mc "Oh, hey."
    mc "You ready to go?"
    show bff excited
    bff "I'm ready when you are!"
    scene bg blank with fade
    "It's nice to hang out with Nao after school sometimes."
    "Though, I don't really like the train that much to be honest."
    "It's always crowded and full of creepy weirdos that like to harass women."
    "I heard about it on the news."
    "Stalking on the rise."
    "Women and children must be wary on trains."
    "Watch out for suspicious men who harass women."
    "Rush hour is the worst though."
    "Hundreds of people crammed into a small compact space just to make it to work on time."
    "I don't know how office workers do it."
    "If it were me bet I would suffocate on my way to work."
    bff "Haru!"
    scene bg station no_train with fade
    show bff glee with dissolve
    bff "We're here!"
    mc "..."
    mc "(We're here faster than I expected.)"
    mc "Oh."
    show bff normal
    bff "Our train will arrive in like 5 minutes."
    mc "I'll guess I'll just be on the look out until then."
    mc "... for the train I mean."
    scene bg blank with fade
    "I spend the next five minutes talking with Nao."
    "... listening to her talk about shoujo manga."
    "I hope she doesn't recommend me to read one as well."
    stop music fadeout 1.0
    scene bg station with fade
    show bff glee with dissolve
    bff "It's here!"
    mc "Alright."
    mc "!!!"
    play music "audio/heartbeat.wav" fadein 1.0
    scene bg blank with fade
    "Huh?"
    "What is this feeling?"
    "I can't move..."
    "..."
    "It's okay, I just need to get on the train."
    "Yes, the train."
    "Theres nothing wrong with trains right?"
    "People ride them all the time."
    "..."
    "Ishida..."
    "Why..."
    jump no_yuusuke_route_common

    label no_yuusuke_route_common:

    label no_choices7:
        "Get on the train?"
    menu:
        "Get on the train.":
            jump no_choices7_common1
        "Get on the train.":
            jump no_choices7_common1
        "Get on the train.":
            jump no_choices7_common1

    label no_choices7_common1:
        "Get on the train?"
    menu:
        "Get on the train.":
            jump no_choices7_common2
        "Get on the train.":
            jump no_choices7_common2
        "Get on the train.":
            jump no_choices7_common2

    label no_choices7_common2:
    stop music fadeout 1.0
    "{cps=8} Are you sure?{/cps}"
    menu:
        "Get on the train!":
            jump no_choices7_common3
        "Get on the train!":
            jump no_choices7_common3
        "Get on the train!":
            jump no_choices7_common3

    label no_choices7_common3:
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_run



label no_run:
    play music "audio/run.mp3" fadein 1.0 volume 1.0
    scene bg run with fade
    show cg run_haru_run with dissolve

    label no_choices8:
    centered "{color=#f44336}{b}{size=+10}{fast}{font=DejaVuSans.ttf}Run{/font}{/size}{/b}{/color}" with dissolve
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common1
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common1
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common1

    label no_choices8_common1:
    centered "{color=#f44336}{b}{size=+10}{w=1.0}{fast}{font=DejaVuSans.ttf}Run{/font}{/size}{/b}{/color}" with dissolve
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common2
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common2
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common2

    label no_choices8_common2:
    centered "{color=#f44336}{b}{size=+10}{w=1.0}{fast}{font=DejaVuSans.ttf}Run{/font}{/size}{/b}{/color}" with dissolve
    menu:
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common3
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common3
        "{font=DejaVuSans.ttf}Run{/font}":
            jump no_choices8_common3

    label no_choices8_common3:
    stop music fadeout 1.0
    scene bg blank
    menu:
        "{color=#f44336}{b}{size=+10}{font=DejaVuSans.ttf}Die{/font}{/size}{/b}{/color}":
            jump no_yuusuke_route_common2



    label no_yuusuke_route_common2:
    scene bg blank with fade
    "Stranger" "Hey!" with hpunch
    $ renpy.vibrate(.5)
    "You ended up bumping into someone."
    "It's a stranger."
    scene bg kinjo with fade
    "Stranger" "Hey!"
    "Stranger" "Are you okay? You look like you've seen a ghost!"
    mc "..."
    "Stranger" "You're shaking."
    bff "Haru!!"
    show bff worried with dissolve
    "!"
    bff "Why did you run out like that?"
    show bff sad
    bff "I was worried about you!"
    show bff worried
    bff "...?"
    bff "Haru... who is this?"
    "Stranger" "Oh, don't worry about me. She just happened to bump into me and I wanted to check if she was alright."
    "Stranger" "Are you a friend of hers?"
    "Stranger" "Anyway, what happened?"
    show bff worried
    bff "We were supposed to go shopping at the mall together this afternoon, but when the train arrived she suddenly ran away."
    "Stranger" "The train huh?"
    "Stranger" "Do you think she's going to be alright?"
    show bff sad
    bff "I'm not sure..."
    show bff worried
    bff "Cmon Haru, lets go home. We can go shopping another day."
    mc "..."
    mc "... o-okay..."
    show bff blush
    bff "Anyway! Thanks for looking after Haru for me!"
    "Stranger" "Don't mention it."

    ##ts --------------------------------------------
    scene ts home with fade
    pause
    ##ts --------------------------------------------
    scene bg bedroom with fade
    mc "..."
    "Speechless, I fell asleep into my bed without a single thought in my mind."
    ##ts --------------------------------------------
    scene ts a_few_days_later with fade
    pause
    ##ts --------------------------------------------

    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    "Turns out I ended up joining the art club with Nao after all."
    show bff glee with dissolve
    bff "Chiharu Chan!"
    mc "So you finally call me by my name huh?"
    show bff worried
    bff "Oh, cmon, don't be like that."
    mc "Anyways..."
    mc "Do you think anyone is going to come to the club after they see the posters we put up?"
    mc "I mean, it's already been 3 days and so far no one has come."
    show bff normal
    bff "Oh! Cmon Haru, try to be a little bit more optimistic!"
    show bff glee
    bff "People will come eventually, it's just a matter of time!"
    show bff normal
    bff "Speaking of which, I already got a new member for the club!"
    show bff excited
    bff "Akari! Come out!!"
    hide bff
    show imt exp1 with dissolve
    imt "..."
    imt "Hello..."
    hide imt
    show bff excited
    bff "Look, Look!!"
    bff "She's sooo cute!"
    bff "Don't you think so?!"
    mc "Who is this?"
    show bff blush
    bff "This is my little sister, Akari."
    show bff normal
    bff "Well, step-sister."
    show bff worried
    bff "She's shy so try to be gentle with her."
    show bff excited
    bff "Let me get the supplies real quick! I'll be right back!"
    hide bff with dissolve
    mc "..."
    scene bg artroom with fade
    show bff glee with dissolve
    "I'm back!"
    mc "... Hey, can I ask you a question?"
    show bff normal
    bff "Oh, what is it, Haru Chan?"
    mc "Do you mind if I ask what your sister is doing at our school? She looks like she's still in middle school."
    show bff glee
    bff "Oh, that."
    show bff normal
    bff "So my dad asked me to look after my sister after she gets back from school."
    show bff worried
    bff "She's been causing alot of trouble lately."
    mc "What kind of trouble?"
    bff "Lets just say we caught her doing something suspicious."
    imt "Hey!"
    imt "I'm here y,know!"
    hide male3
    show bff glee
    bff "Anyways,"
    show bff normal
    bff "Since we're preparing for new members I think we should practice introducing ourselves."
    show bff excited
    bff "Haru? Why don't you start?"
    mc "???"
    mc "Me?"
    show bff glee
    bff "Yes, you."
    show bff normal
    bff "You need to be the example."
    mc "(sigh)"
    mc "Fine."
    mc "Hi, my name is Chiharu, but I normally go by Haru."
    mc "Not any of those weird nicknames that Naomi gives me."
    show bff worried
    bff "Hey!"
    bff "It's an expression of love!"
    mc "Whatever."
    show bff normal
    mc "My hobbies are drawing, music, and cooking."
    show bff glee
    bff "Ohhh! That was a good one!"
    bff "Okay, Akari is next!"
    hide bff
    show imt exp3
    imt "..."
    hide imt
    show bff worried
    bff "Too shy huh?"
    show bff normal
    bff "I'll guess I'll go next then."
    show bff glee
    bff "Hello! My name is Naomi!"
    bff "My hobbies are drawing fan art, reading fanfics, playing video games, reading manga."
    show bff normal
    bff "You could say I like cooking, baking, sports, piano."
    show bff excited
    bff "And I recently got into a dating sim that I think you should really try! It has a nice story! The characters are very interesting! The art is absolutely amazing and the music is breath-taking!"
    mc "Nao..."
    mc "We're not trying to be here all day yknow."
    show bff worried
    bff "Sorry."
    bff "So that just leaves Akari, huh?"
    show bff blush
    bff "Akari! Why don't you try again?"
    hide bff
    show imt exp3
    imt "..."
    show imt exp2
    imt "...hi, my name is Akari."
    imt "..."
    imt "That's pretty much it."
    hide imt
    show bff worried
    bff "Hey! That was barely an introduction!"
    mc "It was good enough for me."
    show bff worried
    bff "..."
    bff "... Okay fine."
    show bff normal
    bff "Well that's okay, you can practice introducing yourself later."
    show bff
    bff "Now let's move on to the club activity!"
    stop music fadeout 1.0
    scene bg blank with fade
    centered "And so, the 4 of us drew into sketchbooks until the day was over."
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg school_genkan with fade
    show bff glee with dissolve
    bff "Alright! That's it for today!"
    show bff normal
    bff "..."
    bff "Oh, yea, I forgot to give this to you."
    mc "!!!"
    play sound "audio/unlock.wav"
    scene bg school_genkan
    show treat
    pause
    hide treat
    mc "Homemade cookies!!"
    show bff blush
    bff "Thanks for deciding to join the art club with me!"
    bff "Me and my sister made these last night and I saved some especially for you!"
    show bff normal
    bff "Oh yea, Haru, I think I'm gonna be needing another favor from you."
    show bff glee
    bff "I know it's sudden, but, do you think you can look after my sister?"
    mc "Oh... ok I guess?"
    mc "Wait, how old is she anyway?"
    mc "She's a middle schooler isn't she?"
    show bff worried
    bff "Yea, she is but..."
    bff "..."
    show bff normal
    bff "Akari!"
    hide bff
    show imt exp1
    imt "?"
    hide imt
    show bff normal
    bff "Do you think you could get my notebook for me? I left it in the classroom."
    hide bff
    show imt exp1
    imt "Ok, sure."
    hide imt with dissolve
    "She walks away."
    stop music
    show bff worried
    bff "So I probably don't have much time to say this but..."
    bff "One day Akari came home with a bag full of money..."
    show bff sad
    bff "But... we don't know where she got it from."
    show bff worried
    bff "So my dad's been asking me to look after her after school to make sure that she's not getting into any trouble."
    bff "When we asked if she was getting involved with anyone suspicious she said-"
    hide bff
    show imt exp1
    imt "I'm back!"
    hide imt
    show bff worried with vpunch
    $ renpy.vibrate(.5)
    bff "... Akari!"
    bff "..."
    bff "I'll talk to you about it some other time."
    hide bff with dissolve
    "Naomi disappears into the horizon with Akari."
    mc "..."
    mc "I should get going too."
    #ts -----------------------------------------------------------------------
    scene ts home with fade
    pause
    # ts ----------------------------------------------------------------------
    scene bg bedroom with fade
    mc "..."
    mc "I wonder what that was all about."
    play sound "audio/vibrate.wav"
    $ renpy.vibrate(.5)
    mc "Huh?"
    show sm_n with dissolve
    mc "It's a message from Naomi."
    mc "..."
    mc "\"Goodluck on expanding your harem... \""
    mc "(Sigh)"
    mc "Nao, why do you have to be so cringe?"
    hide sm_n with dissolve
    mc "..."
    mc "I have a feeling she's up to something and I don't like it."
    "After doing my homework, I watched some TV and then went to sleep."

    ##ts ------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts -------------------------------------------

    scene bg kinjo with fade
    "On my way to school I accidentally stepped into something mushy and sticky."
    mc "!!!"
    mc "..."
    mc "Ugh..."
    mc "Something smells strange."
    mc "..."
    mc "Oh..."
    mc "I should go wash it off at the gym storage house, I'm sure they have a hose."
    scene bg track with fade
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    mc "It's a good thing I got gloves."
    "I proceeded to scrub and wash the bottom of my shoe with soap and water."
    mc "That should do it."
    mc "I should probably go back before class starts."
    "After checking the time I realized that I was already almost late for class."
    mc "Oh snap not again!"
    mc "It's already 8:44!"
    scene bg school_hallway with fade
    mc "Haah, haah, haah."
    "Sensei" "You're late."
    "Sensei" "Chiharu, meet me in the office after schoo-"
    mc "Wait!"
    mc "I can explain!"
    "Sensei" "What?"
    male3 "Excuse me." with vpunch
    $ renpy.vibrate(.5)
    "Sensei" "?"
    show male3 normal with dissolve
    male3 "Please don't mind this hooligan, she's only late because she was helping me out with something this morning."
    "Sensei" "Oh, I see. Alright."
    "Sensei" "Chiharu, you're excused."
    mc "Ah, thanks."
    mc "By the way, isn't your class next door?"
    male3 "Yea, it is, but I'm doing hall patrol before class so..."
    male3 "Anyways, talk to you later, you should hurry before Sensei gets mad at you."
    hide male3 with dissolve
    "He walked away before I had the chance to say goodbye."
    stop music fadeout 1.0
    ##ts -----------------------------------------
    scene ts after_class with fade
    pause
    ##ts ------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg classroom with fade
    show bff worried with dissolve
    bff "Haru chan."
    bff "Where were you this morning?"
    bff "You usually don't come late no matter how much you stay up."
    bff "Did your fatigue finally catch up to you?"
    mc "Uh... actually no."
    mc "I got caught up into something this morning actually."
    show bff mischievous
    bff "Oh really?"
    male4 "Naomi!"
    "A strange figure calls Naomi's name from the classroom door."
    show bff excited
    bff "Oh my my, is that Kaorurun?"
    hide bff
    show male4 excited
    male4 "Yes it is my dear Naomimi"
    hide male4
    show bff excited
    bff "Kaorururun!"
    hide bff
    show male4 excited
    male4 "Naomimimi"
    hide male4
    show bff excited
    bff "KAORURURUUUUN!"
    hide bff
    show male4 excited
    male4 "NAOMIMIMIIIII!"
    hide male4
    "..."
    "I have the feeling I have found Naomi's doppelganger."
    show bff blush
    bff "HARU! Have you met with Kaoru kun?"
    show bff glee
    bff "He's my friend from middle school."
    show bff normal
    bff "The last one I was at before I transferred."
    mc "Oh?"
    hide bff
    show male4 normal
    male4 "Hello there, I believe I've seen you before."
    show male4 happy
    male4 "Your name is Chiharu right? Naomi told me."
    show male4 blush
    male4 "I sincerely apologize for my friend Hiroro's barbarian behavior."
    show male4 normal
    male4 "But you know when you tame a dog it starts to behave very well, teehee."
    show male4 nervous with vpunch
    $ renpy.vibrate(.5)
    male4 "Ow!"
    hide male4
    show male3 normal with dissolve
    male3 "Kaoru, here's your notes from the other day."
    show male3 annoyed
    male3 "And stop flirting with the girls, hanging out with you is already embarrassing enough but you make me want to burn my eyes just watching you trying to be cool."
    hide male3
    show male4 scared
    male4 "Flirting?!"
    show male4 blush
    male4 "Oh cmon, you don't have to say that in front of the ladies."
    hide male4
    show male3 angry
    male3 "Oh my god, you're so cringe."
    male3 "Just stop, please, stop."
    hide male3
    show bff worried
    bff "Uhm? Am I invisible to you or something?"
    hide bff
    show male3 blush
    male3 "N-Na-Naomi!"
    male3 "Oh! I'm sorry!"
    show male3 worried
    male3 "Am I interrupting something?"
    hide male3
    show bff glee
    bff "No, no, not at all!"
    show bff mischievous
    bff "I was talking to Kaoru kun."
    hide bff
    show male4 happy
    male4 "Oh, don't mind Hiro."
    show male4 glee
    male4 "He may look tough and scary but he's actually a softie!"
    hide male4
    show male3 blush
    male3 "Hey!"
    male3 "I AM NOT A SOFTIE!"
    mc "hehehe"
    show male3 angry
    male3 "What are you laughing for?!"
    mc "Oh, its nothing, I just thought you guys were being funny."
    male3 "..."
    hide male3
    show male4 normal
    male4 "Oh, relax Hiro, you know I'm just teasing you right?"
    show male4 excited
    male4 "You're just so adorable when you get flustered, I can't help it!"
    hide male4
    show male3 blush
    male3 "Dude, just stop."
    hide male3
    show male4 normal
    male4 "Anyway, you called me here for something Naomi?"
    hide male4
    show bff blush
    bff "Oh, I was hoping that today we could eat in your office!"
    show bff glee
    bff "There's something I wanna show you."
    hide bff
    show male4 excited
    male4 "Well why didn't you say so sooner?!"
    male4 "Hiro, lets go! You need to make some more friends anyway!"
    hide male4
    show male3 angry
    male3 "Hey!"
    male3 "I have plenty of friends mind you!"
    hide male3
    show male4 normal
    male4 "Oh yea, name one besides me then."
    hide male4
    show male3 blush
    male3 "..."
    male3 "Anyways, I'd rather be alone, I got stuff to do and I don't spend my time fooling around like you do."
    hide male3
    show male4 normal
    male4 "Alright bye, Hiro!"
    show male4 glee
    male4 "I guess that just leaves the three of us then."
    scene bg kaoru_office with fade
    show male4 normal with dissolve
    male4 "Here we are!"
    hide male4
    show bff excited
    bff "Wow! You decorated this place by yourself?"
    hide bff
    show male4 happy
    male4 "Yes!"
    show male4 blush
    male4 "But sadly the other members are never here."
    hide male4
    show bff worried
    bff "Awe, thats a shame."
    show bff normal
    bff "..."
    show bff blush
    bff "I'm famished let's eat!"
    hide bff
    "Naomi eagerly opens her bento box."
    show male4 excited
    male4 "Oh my gosh is that chicken?!"
    male4 "Let me have a piece!"
    hide male4
    "And so Naomi and Kaoru talked nonstop leaving me alone to sit awkwardly in silence to eat my lunch."
    stop music fadeout 1.0
    ##ts ----------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts ----------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg kaoru_office with fade
    show bff normal with dissolve
    bff "Kaoru kun."
    hide bff
    show male4 normal
    male4 "Yes, Naomi?"
    hide male4
    show bff glee
    bff "The thing."
    hide bff
    show male4 normal
    male4 "What thing?"
    male4 "..."
    show male4 scared
    male4 "Oh..."
    show male4 nervous
    male4 "THAT thing?"
    show male4 blush
    male4 "Ok Haru, we'll be right back."
    hide male4 with dissolve
    "Kaoru and Naomi walked outside and left me alone by myself."
    "..."
    "Those two are a handful."
    "They're practically twins."
    stop music fadeout 1.0
    scene bg blank with fade
    "..."
    "Ishida..."
    "Tears start uncontrollably streaming from my eyes."
    "To think that I thought he was just some lame nerd..."
    "But in actuality he was really sweet wasn't he?"
    "No one's ever treated me so nicely before."
    "..."
    "Am I asking for too much?"
    "Am I really so useless?"
    "Do I always have to rely so much on others?"
    "Why am I so helpless?"
    "Do I even deserve so much kindness?"
    "After a while, people just end up getting sick and tired of being around me."
    "They say I'm boring."
    "That I'm too negative."
    "All I do is just bring down the mood."
    "..."
    "It took me a while to calm down."
    "Eventually, I stopped crying."
    play music "audio/houkago.mp3" fadein 1.0 volume 1.0
    scene bg kaoru_office with fade
    "Ok."
    "I think I've calmed down."
    play sound "audio/door.mp3"
    "The door opens."
    show bff glee
    bff "We're back!"
    mc "So what were you guys doing out there?"
    show bff normal
    bff "Oh, we were just talking about-"
    hide bff
    show male4 scared with vpunch
    $ renpy.vibrate(.5)
    male4 "Stuff!"
    show male4 nervous
    male4 "We were just talking about..."
    show male4 scared
    male4 "Stuff."
    hide male4
    mc "Oookay, Mr. Suspicious."
    hide male3
    "Something falls onto the floor."
    show male4 scared
    male4 "!!!"
    mc "..."
    mc "Otome Legends?"
    mc "I didn't know you were into romance visual novels for girls Kaoru."
    hide male4
    show bff worried
    bff "I wouldn't say that he's into it."
    bff "That's an understatement."
    show bff excited
    bff "HE'S WHAT WE LIKE TO CALL! THE OTOME MASTER!"
    hide bff
    show male4 blush
    male4 "You don't have to say that outloud Naomi!!!!"
    male4 "You're embarrassing me!!"
    "After all the weird stuff he says he gets embarrassed over stuff like this?"
    show male4 worried
    male4 "Anyways, I play them from time to time but it's just a small hobby of mine."
    hide male4
    play sound "audio/door.mp3"
    "The door suddenly opens."
    show male3 normal
    male3 "Kaoru, do you have any duct tape? I think I broke my..."
    show male3 blush
    male3 "N-N-NA-NAOMI?!"
    hide male3
    show bff glee
    bff "Oh hi, Hiro!"
    show bff normal
    bff "What's the matter? Do you need help fixing that brain of yours?"
    show bff glee
    bff "I'm sorry, but I don't think duct tape can fix it."
    bff "But you're probably not smart enough to figure that out are ya?"
    hide bff
    mc "Geez Naomi, you don't have to be so mean. Hiro's a human being too, you know."
    show bff glee
    bff "Sorry, I was only stating facts."
    hide bff
    show male3 worried
    male3 "..."
    male3 "Sorry, am I interrupting something?"
    hide male3
    show male4 happy
    male4 "No, no, no! Come in!"
    male4 "You said that you needed something Hiro?"
    hide male4
    show male3 normal
    male3 "Ah, yes."
    male3 "So, I was doing paperwork when suddenly the chair collapsed to the ground."
    male3 "I notified the head master and he told me that it would take a few days to find a replacement."
    show male3 worried
    male3 "So far I've been making do by finishing up the remaining copies of paperwork on the floor but my back is killing me."
    hide male3
    show male4 scared
    male4 "Wait."
    show male4 nervous
    male4 "So you need MY duct tape."
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 nervous
    male4 "So that you can fix your chair?"
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 nervous
    male4 "Because your back is hurting you..."
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 nervous
    male4 "From doing paper work on the floor?"
    hide male4
    show male3 normal
    male3 "Yes."
    hide male3
    show male4 worried
    male4 "..."
    show male4 blush
    male4 "Why don't you just... do your paperwork in the classrooms?"
    hide male4
    show bff glee
    bff "Uhm, excuse me but I think I'm going to leave early."
    show bff normal
    bff "Thanks for inviting me."
    hide bff
    show male4 normal
    male4 "Oh, ok."
    show male4 happy
    male4 "Well, cya later then. I guess."
    hide male4
    mc "Bye Nao!!!"
    show bff glee
    bff "Oh, Haru! You're coming with me too!"
    mc "..."
    show bff normal
    bff "Bye guys!!!"
    hide bff
    play sound "audio/dooropen.wav"
    "Haru and Naomi both leave the room."
    show male4 worried
    male4 "..."
    male4 "You okay Hiro?"
    hide male4
    show male3 worried
    male3 "Yeah..."
    hide male3
    show male4 normal
    male4 "Cmon, cheer up."
    hide male4
    show male3 normal
    male3 "Anyways what's this on the ground?"
    show male3 blush
    male3 "WHAT THE?!"
    male3 "You have a copy of Otome Legends?"
    male3 "That super cringe game with the guys and the long chins?!"
    hide male3
    show male4 blush
    male4 "You don't have to embarrass me about it, yknow..!"
    stop music fadeout 1.0
    scene bg school_hallway with fade
    show bff normal with dissolve
    bff "Glad we're out of that mess."
    mc "..."
    show bff worried
    bff "What's wrong Haru?"
    mc "Naomi, what's up with you today?"
    bff "?"
    bff "Oh, you mean Hiro?"
    show bff glee
    bff "I'll admit, I acted a bit out of character right there for a second."
    bff "You probably don't know him."
    show bff normal
    bff "He's what we like to call in the otome world, a tsundere."
    mc "What's a tsundere?"
    show bff worried
    bff "Oh, Haru. I knew you were clueless but I didn't know you were THAT clueless."
    show bff glee
    bff "A tsundere! A tsundere!"
    bff "A tsundere is absolutely no good!"
    show bff normal
    bff "Just know that there is no good tsundere."
    bff "They're all annoying."
    show bff worried
    bff "They all act like jerks, and act like they hate you, but in actuality they secretly have feelings for you."
    bff "They have no social skills and they don't know how to treat you right."
    show bff sad
    bff "All they do is treat you like trash then act surprised when you hate their guts!"
    mc "..."
    mc "That explanation sounds a bit biased don't you think?"
    show bff normal
    bff "Just know that a tsundere is absolutely no good."
    show bff glee
    bff "And I know I told you to go ahead and build your own harem, but if you get with a tsundere I might have to reconsider our friendship."
    "Translation notes: A tsundere is..."
    "I actually have no idea how to explain this."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Oh, the bell has rung."
    bff "I guess it's time for class."
    show bff blush
    bff "We'll talk in the club room after school!"
    stop music fadeout 1.0
    ##ts -----------------------------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts -----------------------------------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    "It's after school."
    "In the club room with Akari and..."
    "Naomi is nowhere to be found."
    mc "Where is Naomi?"
    show imt exp1 with dissolve
    imt "She said that she had to help my uncle with work at his store so she had to leave early."
    mc "Awe, really?"
    mc "So she just left us here by ourselves?"
    "The door suddenly slides open."
    hide imt
    show male4 excited with dissolve
    male4 "Hellooo!!! My fellow classmates!"
    male4 "I'm here for the drawing competition! I hope that you don't mind that I brought a little friend of mine!"
    hide male4
    show male3 blush
    male3 "Why do you always have to be so dramatic and end up making a fool out of yourself?"
    show male3 annoyed
    male3 "And then you drag me along with you..."
    male3 "I'm only here because you promised me strawberry bread."
    hide male3
    mc "Oh! Hi Kaoru! Hi Hiro!"
    mc "Wait..."
    mc "I don't recall any of us being classmates"
    mc "And what do you mean by art competition? This is the first time I'm hearing about this."
    mc "Anyways, what are you two doing here?"
    show male4 normal
    male4 "Oh, we just wanted to check up on you guys."
    hide male4
    show male3 normal
    male3 "Kaoru got bored with paperwork so he decided to bother you guys to kill time instead."
    hide male3
    show male4 worried with vpunch
    $ renpy.vibrate(.5)
    male4 "Hey!"
    show male4 blush
    male4 "You didn't have to phrase it like that okay!"
    mc "Well, anyways, today we're drawing portraits."
    show male4 excited
    male4 "Portaits?! That sounds interesting! Let's all take selfies and use them as references!!"
    hide male4
    show male3 normal
    male3 "..."
    male3 "Don't we usually pose for the portrait while somebody else is drawing though?"
    hide male3
    show male4 worried
    male4 "Oh, cmon, do you really expect to just sit in the same spot for several hours when we have this thing called-"
    male4 "Yknow..."
    male4 "Technology?"
    hide male4
    show male3 worried
    male3 "I guess."
    hide male3
    show male4 glee
    male4 "Alrighty then!"
    male4 "Lets get started!"
    stop music fadeout 1.0
    ##ts ------------------------
    scene ts some_time_later with fade
    pause
    ##ts -------------
    play music "audio/classtime.mp3" fadein 1.0 volume 1.0
    scene bg artroom with fade
    mc "Alright everyone time is up..."
    mc "Kaoru, do you mind if I see your portrait?"
    show male4 scared
    male4 "Oh... we were drawing portraits?"
    hide male4
    scene bg artroom
    play sound "audio/paper.wav"
    show art_drawing1 with dissolve
    pause
    play sound "audio/paper.wav"
    hide art_drawing1 with dissolve
    mc "..."
    mc "Kaoru, this isn't even a portrait, you drew a doodle of Matsuge Senpai from Otome Legends."
    hide bff
    show male4 blush
    male4 "Sorry."
    hide male4
    show imt exp1
    mc "Akari! What did you draw today?"
    show imt exp3
    imt "..."
    hide imt
    scene bg artroom
    play sound "audio/paper.wav"
    show art_drawing3 with dissolve
    pause
    play sound "audio/paper.wav"
    hide art_drawing3 with dissolve
    mc "..."
    mc ". . ."
    mc "Akari, you drew nothing."
    mc "This is a blank piece of paper."
    mc "Did you pay attention to anything I said today at all?"
    show imt exp2
    imt "Sorry..."
    hide imt
    mc "Well, I guess that's it for today's activity."
    show imt exp1
    imt "Wait..."
    imt "Don't you think you're missing someone?"
    mc "Oh, you mean Naomi?"
    mc "You already told me that she was out today."
    show imt exp2
    imt "No, I mean hir-"
    show imt exp1
    mc "Okay! That's it for today's club activity. I hope I see you all next week."
    mc "..."
    mc "If you come next week, that is..."
    scene bg artroom with fade
    "As everyone leaves, I was left in the room alone with Akari."
    stop music fadeout 1.0
    show imt exp1
    imt "..."
    mc "..."
    mc "Uhm, hey..."
    mc "You doing alright?"
    "Oh dear."
    "I'm not exactly sure how to interact with a middle schooler."
    show imt exp4
    imt "I didn't do it."
    mc "?"
    imt "I swear I didn't do anything wrong."
    mc "..."
    mc "What are you talking about?"
    mc "You okay?"
    imt "..."
    show imt exp2
    imt "Whatever Naomi said, don't believe her."
    mc "What did Naomi say?"
    show imt exp3
    imt "That..."
    imt "I took money from suspicious people."
    mc "Oh?"
    mc "Do you want to talk about it?"
    show imt exp1
    imt "..."
    imt "My friend told me to do it."
    imt "She paid me to do her homework for her."
    show imt exp3
    imt "..."
    imt "I'm sorry."
    show imt exp2
    imt "I know I shouldn't have done that."
    mc "..."
    mc "I think you should tell Naomi that."
    mc "She deserves to know, don't you think?"
    show imt exp4
    imt "Yea..."
    mc "Is that what's been bothering you today?"
    mc "Cmon, let's get you home. I can't leave you here at school by yourself."
    show imt exp1
    imt "Okay."
    scene bg school_genkan with fade
    show imt exp1 with dissolve
    "Akari seems a bit timid around other people."
    "It reminds me of the time when I was in middle school."
    "I wasn't so good at talking to people either."
    "It's easier to warm up to people if there's less people around."
    mc "..."
    mc "(I have a feeling Naomi is gonna take a while to finish work.)"
    mc "Anyway, where do you want me to drop you off?"
    show imt exp3
    imt "..."
    show imt exp1
    imt "The convienence store."
    imt "Thats where my uncle works."
    stop music fadeout 1.0
    scene bg blank with fade
    "And so I dropped Akari by the convience store before going home."
    jump after_yuusuke

    label yuusuke_end:
    scene bg blank with fade
    $ persistent.no_yuusuke = True
    $ achievement.grant("hiro_achievement")
    $ achievement.sync()
    play sound "audio/horror_drum.wav"
    "To be continued..."
    return

    label hiro_route:
    stop music
    scene bg blank with fade
    pause(3.0)
    centered "A sudden chilling realization crossed my mind."
    show bg classroom with fade
    show bff worried with dissolve
    mc "What do you mean?!? You don't know who Yuusuke is?!"
    bff "..."
    mc "I could've sworn you were talking to him the other day!"
    mc "He left for his part time job remember?"
    mc "And he left Akari in the art room!"
    mc "And, and, and!"
    mc "She was kidnapped!"
    mc "And there was a murderer!"
    mc "There was a robbery at the convenience store!"
    mc "Organ traffickers kidnapped the both of us and the building burned down and...!"
    bff "..."
    bff "Haru..."
    bff "What are you talking about?"
    mc "What?!"
    show bff sad
    bff "Calm down!"
    show bff worried
    bff "Y,know..."
    bff "I think you've been watching too many horror movies lately."
    bff "It's not real Haru, serial killers don't come out of movie screens."
    bff "That movie we watched a few weeks ago about the convenience store serial killer that kills and kidnaps people for their organs so that he can stack them on his shelves isn't real Haru."
    mc "B-bu-but!!"
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    "It's time for class."
    show bff normal
    bff "Welp, it's time for class to start!"
    show bff glee
    bff "I'll talk to you about it at lunch."
    play music "audio/uncanny.mp3" fadein 1.0
    play sound "audio/chalkboard.wav" fadein 1.0
    scene bg blank with fade
    "..."
    stop sound fadeout 3.0
    "I spaced out staring into my notebook throughout the entirety of class without being able to focus on what the teacher was saying at all."
    "I just can't help but feel uneasy about what happened yesterday."
    "I don't understand what's going on..."
    "Why can't Naomi remember Yuusuke?"
    "She remembered him yesterday, what's going on?"
    #ts -----
    scene ts after_class with fade
    pause
    #ts -----
    scene bg classroom with fade
    show bff excited with dissolve
    bff "Haru! Lets go eat in the-{nw}"
    mc "No."
    mc "Not now, Nao."
    show bff worried
    bff "..."
    scene bg school_hallway with fade
    show male3 normal with dissolve
    male3 "...?"
    mc "Do you know Yuusuke?"
    male3 "Yuusuke? Who are you talking about?"
    mc "..."
    scene bg kaoru_office with fade
    show male4 normal with dissolve
    male4 "Yuusuke?"
    show male4 happy
    male4 "That doesn't seem to ring a bell..."
    show male4 excited
    male4 "OH! I got it now!"
    mc "!!!"
    show male4 glee
    male4 "You mean that voice actor that does Matsuge's voice in Otome Legends?"
    mc "NO!!"
    show male4 nervous
    male4 "..."
    male4 ". . ."
    show male4 scared
    male4 "O-o-okay..."
    scene bg school_hallway with fade
    stop music fadeout 1.0
    show bff worried with dissolve
    bff "Haru? You okay?"
    mc "..."
    "I avoided eye contact and clenched my hands to hide my frustration."
    mc "I'm fine..."
    bff "Oh..."
    show bff normal
    bff "Wait! I know what'll make you feel better!"
    show bff glee
    bff "Why don't we go over tips on how to expand your hare-{nw}"
    play music "audio/sad_theme.mp3" fadein 1.0
    mc "ENOUGH!"
    show bff worried
    mc "IS THAT ALL YOU CARE ABOUT?! THE STUPID HAREM?!"
    mc "WHO CARES ABOUT THE HAREM?! ISHIDA IS DEAD!"
    bff "..."
    mc "Why do you keep pushing me to do this stupid harem stuff?"
    mc "I know I said that I kinda wished that I had my own harem but..."
    mc "Don't you think you're pushing me too hard with this?"
    mc "Don't you think that this entire thing is ridiculous though?"
    mc "Do you really think I actually care about \"making my own harem.\""
    mc "Don't you realize how RIDICULOUS that sounds?!"
    mc "I just want to live a normal life!"
    mc "Do you actually think about how anyone feels?!"
    mc "Can you just stop bothering me with this stupid harem stuff FOR ONCE?!"
    show bff sad
    bff "..."
    bff "Haru..."
    bff "I'm sorry..."
    bff "I just wanted you to make friends..."
    bff "I thought joking about the harem thing would make you cheer up..."
    bff "Honestly, I don't know what's been going on."
    bff "You've been out of it since Ishida's death and for the last couple of weeks you've been staring into space and having conversations with yourself."
    bff "Y,know, I'm sad about Ishida's death too."
    bff "I've been trying to not think about it and act like everything has been fine."
    bff "Haru..."
    bff "I-I-I..."
    show bff depressed
    bff "I'm sorry..."
    bff "I'm a terrible friend!"
    mc "..."
    mc "Nao that's not what I-{nw}"
    hide bff with dissolve
    "She runs away."
    mc "Nao!"
    stop music fadeout 1.0
    ##ts -------
    scene ts some_time_later with fade
    pause
    ##ts ---------------
    scene bg school_okujou with fade
    show male4 worried with dissolve
    male4 "Naomi.."
    hide male4
    show bff sad
    bff "..."
    bff "What are you doing here?"
    hide bff
    show male4 worried
    male4 "I overheard what happened between you and Haru earlier."
    show male4 blush
    male4 "You could say I just happened to catch a glimpse of what happened."
    show male4 worried
    male4 "Are you okay?"
    hide male4
    show bff depressed
    bff "{cps=3}. . .{/cps}"
    bff "It happened just like this."
    bff "On the school rooftop..."
    scene bg blank with fade
    centered "{size=40}{cps=7}A few years ago...{/cps}{/size}"
    scene bg past1 with fade
    show girl1 with dissolve
    girl1 "Who does that girl think she is anyways?"
    hide girl1
    show girl2
    girl2 "\"Can I have lunch with you guys?\" Yeah, right!?"
    hide girl2
    show girl3
    girl3 "She's just so creepy, it's gross. All she does is stare at you like a ghost and doodles in her notebook all day."
    hide girl3
    show girl1
    girl1 "She probably has no friends. Poor thing. Maybe she'd have more of them if she wasn't such a soulless doll."
    girl1 "What do you think?"
    girl1 "Naomi?"
    hide girl1 with dissolve
    play music "audio/fuzzytube.mp3" fadein 1.0 volume 0.5
    show bff_p1 smirk with dissolve
    bff "Awe, don't you think you guys are being a little too harsh? It's not right to disrespect the deceased."
    bff "Oh wait, I forgot IT was still a living thing."
    bff "I still have a hard time believing she's not actually a ghost."
    show bff_p1 normal
    bff "Seriously though, she gives me the creeps."
    show bff_p1 nervous
    play sound "audio/vibrate.wav"
    $ renpy.vibrate(.5)
    bff "!!!"
    bff "Hold on, I think I got a text!"
    bff "!"
    bff "(It's Kaoru kun!)"
    bff "\"How is your new school?\""
    show bff_p1 normal
    bff "..."
    bff "(I wish you were here.)"
    hide bff_p1
    show girl1
    girl1 "Naomi, what are you grinning to yourself for? Did ya get a boyfriend?"
    hide girl1
    show girl2
    girl2 "Boyfriend?"
    girl2 "Why didn't she tell me about it?"
    hide girl2
    show bff_p1 nervous
    bff "Oh! Its nothing like that!"
    bff "It's just an old friend of mine!"
    hide bff_p1
    show girl3
    girl3 "That's what they ALL say!"
    girl3 "Anyway, could you get us some sodas from the vending machine?"
    hide girl3
    show girl2
    girl2 "Hey! I want a strawberry milk!"
    hide girl2
    show girl1
    girl1 "And make mine a green tea!"
    hide girl1
    show girl3
    girl3 "Green tea? But thats Sooo bitter!"
    hide girl3
    show girl1
    girl1 "Hey!"
    girl1 "I like what I like."
    hide girl1
    show bff_p1 normal
    bff "Alright, I'll be back in a few minutes."
    hide bff_p1 with dissolve
    "She walks out of the classroom."
    show girl1 with dissolve
    girl1 "She's convenient to have around isn't she?"
    hide girl1
    show girl3
    girl3 "Yea."
    girl3 "Free drinks are great, I was thirsty today."
    scene bg blank with fade
    bff "(I barely have enough for the drinks...)"
    bff "..."
    bff "(I'ma head to the bathroom real quick.)"
    bff "..."
    stop music fadeout 1.0
    scene cg bully_fb4 with fade
    play sound "audio/footsteps.wav"
    $ renpy.pause(15.0, hard=True)
    mc "{cps=2}. . .{/cps}"
    scene bg blank with fade
    play sound "audio/door.mp3"
    pause (2.0)
    bff "... What is that smell?"
    bff "Is somebody eating in the bathroom?"
    play sound "audio/knock.wav"
    pause (2.0)
    bff "!!!"
    bff "What are you doing eating in the bathroom?"
    bff "Y,know, you could get sick by doing that right?!"
    bff "Wait... I hear something."
    play sound "audio/suspense.wav"
    pause (3.0)
    bff "{cps=3}. . .{w=4}{nw}{/cps}"
    play sound "audio/dooropen.wav"
    pause (2.0)
    bff "!!!"
    girl1 "Hey!"
    play music "audio/fuzzytube.mp3" fadein 1.0 volume 0.5
    scene bg haibiru with fade
    show girl1 with dissolve
    girl1 "I didn't expect to find you here."
    hide girl1
    show bff_p1 normal
    bff "Oh, Hi."
    hide bff_p1
    show girl1
    girl1 "Who is this loser eating alone in the bathroom?"
    hide girl1
    show bff_p1 normal
    bff "..."
    show bff_p1 smirk
    bff "I don't know, but don't you think she looks pathetic?"
    bff "This little squirt here owes me a drink."
    hide bff_p1
    show girl1
    girl1 "Ah, is that so? Maybe if she has money to spare she should buy all of us some drinks."
    girl1 "Don't ya think so too?"
    girl1 "Chiharu Chan."
    mc "{cps=2}. . .{/cps}"
    stop music fadeout 1.0
    #ts -----------------------------------
    scene ts after_school with fade
    pause
    #ts -----------------------------------
    scene bg past1 with fade
    show girl3 with dissolve
    girl3 "Anyway, anyone up to go for some karaoke?"
    girl3 "Tonight they're doing a special discount I heard."
    hide girl3
    show girl1
    girl1 "Who cares about that, Naomi's gonna spot us anyway."
    girl1 "Right, Naomi?"
    hide girl1
    show bff_p1 nervous
    bff "..."
    bff "sure..."
    hide bff_p1
    show girl1
    girl1 "Ah, thanks! You're honestly the best!"
    hide girl1
    show girl2
    girl2 "Ah! Hold that thought."
    girl2 "I just got a text from my dad, he said I have tutoring tonight so I can't go."
    hide girl2
    show girl3
    girl3 "Awe, bummer."
    girl3 "Well, I guess we're not going today then."
    girl3 "Alright guys, I'ma bounce."
    hide girl3
    show girl1
    girl1 "Me too."
    hide girl1
    show girl2
    girl2 "Welp! I'm heading off! Cya later!"
    stop music fadeout 1.0
    #ts -----------------------------------------------------------------------
    scene ts the_next_day with fade
    pause
    #ts -----------------------------------------------------------------------
    scene bg past1 with fade
    bff "Hey, what are you gu-{nw}"
    play sound "audio/horror_drum.wav"
    scene cg fdesk2
    centered "{w=3}{nw}"
    scene cg bully_fb1 with fade
    pause (2.0)
    scene cg bully_fb1 with dissolve
    girl3 "Oh, look at that. Your desk is dirty."
    girl3 "I wonder who could've done that, looks so awful hahaha."
    girl1 "Yeah I wonder. (snicker)"
    girl2 "I thought somebody might've had a funeral but it turns out it was just you."
    girl2 "Look, somebody already put flowers down for you. Hahaha."
    scene cg bully_fb3 with fade
    mc "..."
    scene bg past1 with fade
    show bff_p1 normal with dissolve
    bff "..."
    show bff_p1 nervous
    bff "..."
    bff ". . ."
    bff "Guys, don't you think you're being a little bit too harsh?"
    bff "... I mean..."
    bff ". . ."
    play music "audio/disorganized.mp3" fadein 7.0 volume 0.5
    show bff_p1 smirk
    bff "It's not like I really care or anything."
    bff "But don't you think we might get in trouble for doing this out in the open?"
    bff "Why not pick a better place to do this?"
    bff "Somewhere nobody can bother us."
    hide bff_p1
    show girl1
    girl1 "Oh, Naomi, thats a great idea."
    girl1 "Y,know the other day this little squirt got me the wrong soda."
    girl1 "And I was just thinking..."
    girl1 "That she should pay me back somehow."
    girl1 "Y,know the other day I got in trouble for skipping class..."
    girl1 "So they assigned me to clean-up the pools after school for a week."
    girl1 "But really, I think she could do that for me instead."
    hide girl1
    show girl2
    girl2 "Ohhh! Thats actually really smart!"
    hide girl2
    show girl3
    girl3 "We got a favor-girl now?"
    girl3 "That sounds like fun!"
    girl3 "I wonder if she could do my homework for me too."
    hide girl3
    show girl1
    girl1 "Alright, you're cleaning the desk before the teacher comes back, and if you snitch on us you're gonna regret it."
    #ts ------------------------------------------------------------------------
    scene ts after_school with fade
    pause (1.0)
    #ts ------------------------------------------------------------------------
    scene bg haibiru with fade
    show girls with dissolve
    girl1 "Hehe, look at her."
    girl2 "I know, she's doing such a good job cleaning that pool isn't she?"
    girl3 "I think she can go faster."
    scene bg haibiru with fade
    show girl1 with dissolve
    girl1 "Hey Naomi."
    hide girl1
    show bff_p1 normal
    bff "Yes?"
    hide bff_p1
    show girl1
    girl1 "We'll be back real quick, theres something we left in the classrooms."
    girl1 "Do you think you can watch this nerd for us for a sec?"
    hide girl1
    show bff_p1 nervous
    bff "Oh..."
    show bff_p1 normal
    bff "Okay."
    stop music fadeout 1.0
    scene bg blank with fade
    centered "That day they left me to look after Chiharu Chan while they were gone."
    centered "They promised they would come back. . ."
    centered "But they never did."
    centered "We were there at the pool until sunset."
    centered "When it got dark I realized that they weren't coming back."
    centered "But despite all that, I still kept doing favors for them."
    centered "I just wanted them to like me."
    centered "So I thought that if I kept doing what they told me to do they would eventually let me into their group."
    centered "But one day, I realized that no matter how much I tried..."
    centered "They weren't going to like me anyways."
    centered "And one day, I found myself on the school rooftop."
    scene bg past3 with fade
    show bff_p1 normal with dissolve
    bff "..."
    bff "What are you doing here?"
    play music "audio/uncanny.mp3"
    show mc_p1 normal with dissolve
    mc "That should be my line..."
    show bff_p1 nervous
    bff ". . ."
    show mc_p1 normal
    mc "Probably the same reason why you're here."
    show mc_p1 normal
    scene bg haibiru with fade
    show hr_thoughts with dissolve
    centered "As I looked around I noticed that Chiharu was standing at the railing in her socks..."
    centered "..."
    centered "Her shoes were on the floor right beside her."
    scene bg past3 with fade
    show bff_p1 smirk with dissolve
    bff "So you finally came to your senses huh?"
    bff "You finally realized that you're a waste of space that doesn't deserve to live."
    show mc_p1 normal with dissolve
    mc "Naomi, drop the act."
    mc "I know those people aren't your real friends."
    mc "You're just acting like that to appease them but you finally realized that it's not working out."
    mc "Thats why you're up here, aren't you?"
    show mc_p1 normal with dissolve
    show bff_p1 normal
    bff "..."
    bff "Thats not any way to talk to an old friend is it?"
    show bff_p1 nervous
    bff "What would you know anyway?"
    bff "I already know I'm a horrible person so why should I even bother being nice to anyone?"
    show mc_p1 normal
    mc "..."
    mc "Do you honestly expect me to feel sorry for you after what you've done?"
    bff "..."
    show mc_p1 normal
    mc "Just go away and leave me alone."
    mc "..."
    show mc_p1 normal
    mc "And by the way..."
    mc "Thanks for helping me clean-up at the pools the other day."
    hide bff_p1 with dissolve
    pause (3.0)
    hide mc_p1 with dissolve
    stop music fadeout 3.0
    scene bg blank with fade
    "I turned around and I started to walk away."
    "But then I looked back, and when I saw her, she was standing over the railing..."
    bff "HEY! WAIT!"
    bff "DON'T JUMP!!!{w=0.5}{nw}"
    play sound "audio/horror_drum.wav"
    scene flash red
    pause(3.0)

    label darkroom:
    scene bg bedroom_dark with fade
    mc "..."
    mc "Was I just imagining things?"
    mc "Why doesn't anyone remember Yuusuke?"
    mc "..."
    mc "Am I going crazy???"
    mc "That can't be true right...?"
    mc "None of this makes any sense..."
    mc ". . ."
    mc "Anymore of this..."
    mc "And I'm gonna go insane."
    centered "{nw}"
    show bsb_blank with dissolve
    pause 5.0
    scene bg blank
    pause 2.0
    scene cg late_madness with fade
    pause 2.0
    play music "audio/heartbeat.wav"
    pause 5.0
    stop music

    label bsbgame1:
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    play music "audio/menutheme.mp3"
    scene otome title_screen1 with fade
    pause
    play music "audio/bsbtheme.mp3"
    scene bg bsb1 with pixellate
    "It's been a few months since the relay race."
    "Matsuge Senpai is back at school, Mafura Senpai seems like he is doing quite well, and Kinpatsu Senpai finally healed from all of his injuries."
    "Though..."
    "I still didn't get a chance to buy Mafura Senpai those chocolates though."
    shoujo1 "!!!" with vpunch
    "Oh no, I dropped my eraser on the floor!"
    "..."
    "Someone picked it up."
    senpai4 "I'm sorry, is this yours?"
    show senpai4 bsb with dissolve
    "A strong handsome boi has entered the battlefield."
    senpai4 "I saw you drop it on the floor."
    senpai2 "Hey!"
    scene cg senpai war with pixellate
    senpai2 "I see you!"
    senpai2 "You think you're so handsome!"
    senpai2 "Hitting on any girl you see!"
    senpai2 "But you know what!?"
    senpai2 "I'm the most handsome guy in school and everyone knows it!"
    senpai4 "Oh?"
    senpai4 "Is that so?"
    senpai4 "Well, why are you getting so hostile amigo?"
    senpai4 "I was just trying to help one of our fellow classmates."
    senpai4 "By the way, why are you holding a rose all the time?"
    senpai2 "Haha, you foolish peasant!"
    senpai2 "Roses only bloom for the beautiful!"
    senpai2 "God himself blessed me with roses because I am so fabulous OHOHOHOHOHOHOHOHO!"
    scene bg bsb1 with pixellate
    show senpai2 bsb with dissolve
    senpai2 "Excuse me, I heard that this peasant right here was trying to hand you an eraser from the filthy floor."
    senpai2 "I came here to hand you a fresh one..."
    senpai2 "Out of the box that is..."
    "Matsuge handed you an eraser..."
    "It's covered in blood."
    senpai2 "OHOHOHOHOHOHO! Look at the time! I must go now!"
    senpai2 "Adieu!!!"
    hide senpai2 bsb with dissolve
    shoujo1 "What was with that guy?"
    senpai3 "Hey there!"
    show senpai3 bsb with dissolve
    shoujo1 "..."
    senpai3 "Have you seen my tie?"
    senpai3 "I think I lost it."
    shoujo1 "(Oh my gosh.)"
    shoujo1 "(Is that Kinpatsu Senpai?)"
    shoujo1 "(I can't believe this.)"
    shoujo1 "(One of the hottest guys in school is right in front of me!)"
    shoujo1 "(And I'm a total sucker for blondies!)"
    shoujo1 "(Oh no! I should've put on makeup today!)"
    shoujo1 "(QUICK!! WHAT DO I SAY!?!?)"
    shoujo1 "...hi?"
    senpai3 "Uhm..."
    senpai3 "Did you see my tie?"
    shoujo1 "Oh yea, thats right!"
    shoujo1 "..."
    shoujo1 "Aren't you wearing it right now?"
    senpai3 "Oh, you're right."
    senpai3 "Thank you so much."
    hide senpai3 with dissolve
    shoujo1 "(Oh my god, I've been getting popular lately.)"
    stop music fadeout 1.0
    play sound "audio/schoolchime1.wav"
    "The school bell rings."
    "It's time for home economics class."
    shoujo1 "(OH! ITS HOME ECONOMICS CLASS!)"
    shoujo1 "(Maybe I can make the chocolates for Mafura senpai instead!)"
    play music "audio/bsbtheme.mp3" fadein 1.0 volume 0.5
    scene bg bsb2 with pixellate
    "You arrive at the home economics class."
    shoujo2 "{size=+3}Moteko! Have you seen the new guy in class?!{/size}"
    shoujo2 "He just transferred!"
    shoujo1 "YEA HE'S A TOTAL HOTTIE!"
    shoujo2 "SHHHHH!"
    shoujo2 "Don't say it so loud!"
    shoujo1 "Oops!"
    "Moteko and Yumeko continue talking amongst eachother about who is most attractive guy in school."
    show senpai2 bsb with dissolve
    senpai2 "Mafura! Kinpatsu we have an emergency!"
    hide senpai2
    show senpai1 bsb
    senpai1 "What is it?"
    hide senpai1
    show senpai2 bsb
    senpai2 "Haven't you noticed something?"
    senpai2 "Theres a new guy in class..."
    senpai2 "And he's getting the attention of all of the girls in school."
    senpai2 "This cannot happen!"
    senpai2 "The girls should all be looking at me; I am absolutely fabulous!"
    senpai2 "Quick! We have to devise a plan to get rid of him!"
    senpai2 "He threatens my very existence!"
    hide senpai2
    show senpai1 bsb
    senpai1 "I think you may be onto something Matsuge..."
    senpai1 "Ever since he got here, there hasn't been enough breeze to blow my scarf along with the wind."
    senpai1 "Y,know..."
    senpai1 "I'm just not feeling as COOL as I used to be."
    senpai1 "What do you think Kinpatsu?"
    hide senpai1
    show senpai3 bsb
    senpai3 "Huh, what?"
    senpai3 "Were you guys talking about something?"
    hide senpai3
    show senpai1 bsb
    senpai1 "..."
    senpai1 "Nevermind."
    hide senpai1
    show senpai3 bsb
    senpai3 "Oh!"
    senpai3 "By the way..."
    senpai3 "Have you seen my neck tie?"
    hide senpai3
    show senpai1 bsb
    senpai1 "..."
    senpai1 "Isn't it around your neck?"
    hide senpai1
    show senpai3 bsb
    senpai3 "Oh yeah, I forgot."
    hide senpai3
    show senpai2 bsb
    senpai2 "Guys, I got an idea!"
    senpai2 "Do you see those pretty ladies over there?"
    senpai2 "I bet if we impress them we can put that new guy back in his place!"
    hide senpai2
    show senpai1 bsb
    senpai1 "... uhm"
    senpai1 "Well, idk about tha-{nw}"
    hide senpai1
    show senpai2 bsb
    senpai2 "ALRIGHTY THEN! IT'S BEEN SETTLED!"
    senpai2 "WE'RE DOING A COOKING COMPETITION!"
    senpai2 "THE ONE WHO MAKES THE BEST DISH WILL WIN THE MAIDEN'S HEART!"
    senpai2 "Not that you baffoons stand a chance against me anyway."
    senpai2 "May the best chef win!"
    hide senpai2 with fade
    shoujo1 "Oh my god, is that the new mascara?"
    senpai2 "HEY YOU PEASANT OVER THERE!!!"
    shoujo1 "???"
    shoujo2 "???"
    show senpai4 bsb with dissolve
    senpai4 "¿¿¿?"
    hide senpai4
    show senpai2 bsb
    senpai2 "I CHALLENGE YOU TO A DUEL!"
    senpai2 "And who ever has the best cuisine may win!"
    stop music fadeout 1.0
    ##ts -----------------------------------------------
    scene bg blank with fade
    centered "{size=50}Some time later...{/size}"
    ##ts -----------------------------------------------
    play music "audio/bsbtheme.mp3" fadein 1.0 volume 0.5
    scene bg bsb2 with fade
    show senpai4 bsb with dissolve
    senpai4 "..."
    senpai4 "Seasoning, I need seasoning!!!"
    senpai4 "Oh, there it is!"
    senpai4 "Basil!"
    senpai4 "I wonder how Matsuge is doing..."
    senpai2 "HOHOHOHOHHO!"
    scene cg matsuge1 with pixellate
    pause
    senpai2 "Now just some salt and pepper and it will be perfectly seasoned!"
    senpai2 "There! It is done!"
    senpai2 "Bon Appétit."
    senpai2 "(sniff) (sniff)"
    senpai2 "... What is that smell?"
    scene cg matsuge2
    senpai2 "AAAAAAAHHHHHHHHHHHHHHH!!!!"
    senpai2 "MY HAIR IS ON FIREEEEE!!!"
    stop music fadeout 1.0
    ##ts -----------------------------------------------
    scene bg blank with fade
    centered "{size=50}Some time later...{/size}" with fade
    ##ts -----------------------------------------------
    play music "audio/bsbtheme.mp3" fadein 1.0 volume 0.5
    scene bg bsb1 with fade
    "It's Thursday..."
    "The disaster in the cooking room caused the principal to make a decision to cancel the class for the rest of the year."
    "It's a good thing for me though..."
    "I was failing that class anyway."
    senpai2 "I AM BAAACKKK!!!"
    show senpai2 bsb with pixellate
    senpai2 "I am here for ROUND TWO!!!"
    show senpai2 bsb_balding
    senpai2 "Hold on, I feel something strange..."
    senpai2 "It's almost as if something is falling off of my head..."
    show senpai2 bsb_scream
    senpai2 "AAAHHHHHHHHH!!!"
    senpai2 "MY BEAUTIFUL HAIRRR!"
    hide senpai2 with pixellate
    show senpai3 bsb with dissolve
    senpai3 "Hey Macho guy."
    senpai3 "Wanna do an arm wrestling match?"
    hide senpai3
    show senpai4 bsb
    senpai4 "Sure."
    scene cg kinpatsu1 with pixellate
    senpai3 "Okay!"
    senpai3 "Ready!"
    senpai3 "Set!!"
    senpai3 "Go!"
    senpai3 "Oh, wait... have you seen my tie?"
    scene cg kinpatsu2 with pixellate
    senpai4 "Ay, Dios Mio!!!"
    senpai4 "Sorry amigo..."
    senpai4 "I didn't mean to launch you that far, my bad."
    senpai3 "..."
    senpai3 "Are ya up for a round 2?"
    scene bg bsb1 with fade
    show senpai1 bsb with pixellate
    senpai1 "Uhm, guys..."
    senpai1 "I think we are approaching this the wrong way..."
    senpai1 "Hey, there new guy..."
    senpai1 "I think we should make a truce."
    senpai1 "Fighting isn't really my style anyway."
    senpai1 "What do you say?"
    hide senpai1
    show senpai4 bsb
    senpai4 "Sure!"
    scene cg ikemen1 with pixellate
    pause
    senpai4 "Glad to be friends with all of yall!"
    senpai4 "My name is Handsamu Macho, but my friends call me Ikemen!"
    senpai4 "Nice to meet you guys!"
    senpai3 "MY TIEE!!!!"
    stop music fadeout 1.0
    ##ts -----------------------------------------------
    scene bg blank with fade
    centered "{size=50}Some time later...{/size}"
    pause
    ##ts -----------------------------------------------
    play music "audio/bsbtheme.mp3" fadein 1.0 volume 0.5
    scene bg bsb1 with dissolve
    "It took a while but all the Senpai Tachis finally stopped fighting and made up."
    "Now they're practically best buddies."
    "..."
    "It's lunch time."
    "And Yumeko is busy."
    "I guess I'm alone for lunch now..."
    senpai4 "Hola Señorita!"
    shoujo1 "???"
    scene cg ikemen2 with pixellate
    senpai4 "I got you something."
    shoujo1 "!!!"
    "It's a box of chocolates!"
    senpai4 "I heard that you wanted to make some the other day but you didn't get a chance to."
    shoujo1 "Oh?"
    shoujo1 "Thank you!"
    stop music
    scene cg ikemen3
    pause (0.3)
    scene bg blank
    play sound "audio/static.wav"
    show static
    centered "{w=3}{nw}"
    play music "audio/menutheme.mp3" volume 0.5
    scene otome title_screen2 with fade
    pause
    show loading with fade
    centered "{w=3}{nw}"
    pause(0.5)
    stop music
    scene cg ikemen4
    senpai4 "Say ahh."
    scene bg blank with fade
    shoujo1 "Ahhh!"
    play sound "audio/alarm.wav"
    shoujo1 "AHHHHH!!!"
    shoujo1 "MY EARS!!!"
    shoujo1 "!!!"
    "(The alarm clock goes off and wakes you up)"
    shoujo1 "OH NO I'M GOING TO BE LATE FOR SCHOOL!"
    play music "audio/bsbtheme.mp3" fadein 1.0 volume 0.5
    scene bg bsb3 with fade
    "(You bump into a handsome senpai.)"
    shoujo1 "!!!" with vpunch
    show senpai1 real with dissolve
    senpai1 "Oi!"
    senpai1 "Soko no shoujo yo!"
    $ renpy.block_rollback()
    scene bg bsb3 with dissolve
    play sound "audio/flute.wav"
    show intro mafura with wipeleft
    pause(1.35)
    play audio "audio/thump.mp3"
    show overlay mafura with moveinleft
    show screen snow
    play audio "audio/glitter.wav"
    pause(6.0)
    hide screen snow with dissolve
    pause
    $ renpy.block_rollback()
    scene bg bsb3
    show senpai1 real
    with fade
    senpai1 "Watch where you're going!"
    shoujo1 "Oh my!"
    shoujo1 "I'm so sorry!"
    shoujo1 "AHHHHH!!!"
    shoujo1 "I GONNA BE LATE FOR SCHOOL!"
    scene bg bsb3 with fade
    shoujo1 "Haah, haah, haah."
    shoujo1 "Oh no..."
    shoujo1 "(I ended up running into Mafura Senpai again...)"
    shoujo1 "(Does that mean I owe him two chocolates this time?)"
    "Translation notes: Mafura means muffler."
    shoujo2 "MOTEKO!!!"
    "It's your best friend Yumeko."
    shoujo2 "Did you finally give Mafura his chocolates?"
    shoujo1 "... No"
    shoujo2 "Well, better luck next time. Am I right?"
    shoujo2 "By the way, I heard they were doing a chocolate sale at the department store,
    I think this might be the best time to take advantage!"
    shoujo2 "Don't forget to buy me some too!"
    shoujo1 "Yumeko..."
    shoujo1 "Aren't you sure you don't just want the chocolates for yourself?"
    shoujo2 "Teehee."
    senpai2 "Excusez moi, Mademoiselles!"
    $ renpy.block_rollback()
    scene bg bsb1 with dissolve
    play sound "audio/flute.wav"
    show intro matsuge with wipeleft
    pause(1.35)
    play audio "audio/thump.mp3"
    show overlay matsuge with moveinleft
    show screen roses
    play audio "audio/glitter.wav"
    pause(6.0)
    hide screen roses with dissolve
    pause
    scene bg bsb1
    show senpai2 real
    with fade
    $ renpy.block_rollback()
    senpai2 "Hello there ladies."
    senpai2 "I can't help but notice that you guys were talking about me."
    shoujo1 "But... no one was talking abou-{nw}"
    senpai2 "Shhhhh"
    senpai2 "I already know."
    senpai2 "Just know that..."
    senpai2 "I may look like quite the charmer but I'm actually single as of right now."
    senpai2 "And I haven't found the right match for me yet."
    senpai2 "But maybe..."
    senpai2 "You might have a chance."
    senpai2 "I'll be waiting for you after school under the sakura tree."
    "Translation note: Sakura means cherry blossom in Japanese."
    "These pink cherry trees are prevalent in romance anime, well... because romance."
    senpai3 "Matsuge!!!!"
    hide senpai2
    show senpai3 real with dissolve
    senpai3 "Matsuge, stop flirting with the girls!"
    "Translation notes: Matsuge means eyelashes in Japanese."
    hide senpai3
    $ renpy.block_rollback()
    scene bg bsb3 with dissolve
    play sound "audio/flute.wav"
    show intro kinpatsu with wipeleft
    pause(1.35)
    play audio "audio/thump.mp3"
    show overlay kinpatsu with moveinleft
    show screen sunrays
    play audio "audio/glitter.wav"
    pause(6.0)
    hide screen sunrays with dissolve
    pause
    $ renpy.block_rollback()
    scene bg bsb1
    show senpai2 real
    with fade
    senpai2 "Sacré bleu!"
    senpai2 "Kinpatsu you ruined the mood!"
    senpai2 "Anyways"
    senpai2 "I'll speak to you girls later, after school."
    senpai2 "À plus tard!"
    hide senpai2 with dissolve
    "He disappears into the..."
    "hall."
    show senpai3 real with dissolve
    senpai3 "Anyways, ladies, do one of you guys wanna see me lift some cars?"
    shoujo1 "..."
    shoujo2 "..."
    senpai4 "¡ESTOY AQUI!"
    "Translation notes: Sorry, I can't help you with spanish either."
    hide senpai3
    show senpai4 real with dissolve
    senpai4 "Buenos dias, amigos, amigas."
    senpai4 "What did you guys get on the math test last week?"
    hide senpai4
    show senpai3 real
    senpai3 "There was a test last week?"
    senpai3 "Oh, you mean the papers that sensei just handed out yesterday morning?"
    hide senpai3
    show senpai4 real
    senpai4 "Let me see that."
    senpai4 "..."
    senpai4 "¡AY, CARAMBA!"
    senpai4 "¡Ay Rubio que paso con este examen!"
    senpai4 "MIRA!"
    senpai4 "THESE GRADES ARE BASURA!"
    senpai4 "... I mean"
    senpai4 "It's okay, you just have to study more."
    senpai4 "Basura means okay."
    "Translation notes: No it doesn't."
    play sound "audio/schoolchime1.wav"
    "(The bell rings)"
    shoujo1 "Oh, its time for class now guys."
    shoujo1 "We gotta go, talk to you guys later."
    stop music fadeout 1.0
    ##ts -----------------------------------------------
    scene bg blank with fade
    centered "{size=50}After school...{/size}"
    ##ts -----------------------------------------------
    scene bg bsb1 with fade
    "It is now after school."
    "What should you do?"
    menu:
        "Get chocolates for Mafura":
            jump april_fools
        "Meet with Matsuge under the sakura tree":
            jump april_fools
        "Hang out with Kinpatsu":
            jump april_fools
        "Talk to Ikemen":
            jump april_fools

    label april_fools:
    stop music fadeout 1.0
    play sound "audio/beep.wav" volume 0.5
    scene bsb_cursed
    $ renpy.pause(8, hard=True)
    play music "audio/static.wav" volume 0.5
    scene static
    show bsb_transparent with dissolve
    $ renpy.pause(4, hard=True)
    stop music fadeout 1.0
    show bg bsb_transparent with dissolve
    pause (3.0)
    show bsb_sticker
    centered "{color=#ff0000}{b}{size=35}{font=DejaVuSans.ttf}What made{p} you think...{/font}{/size}{/b}{/color}"
    centered "{color=#ff0000}{b}{size=35}{font=DejaVuSans.ttf}That you actually{p} had a choice?{/font}{/size}{/b}{/color}"
    play sound "audio/static.wav"
    scene static
    pause (3.0)
    play music "audio/uncanny.mp3" fadein 1.0
    scene bg blank with fade
    play sound "audio/knock.wav"
    "Mom" "Haru!!"
    "Mom" "Haru!!!"
    "Mom" "Naomi came over."
    "Mom" "She wants to come and talk to you."
    mc "..."
    mc "Leave me alone."
    "I don't want to go outside..."
    "Why can't I just disappear?"
    ##ts --------------------------
    scene ts some_time_later with fade
    pause
    #ts ---------------------------
    scene bg bedroom with fade
    mc "..."
    mc "Are they finally gone?"
    mc "I thought they would never leave..."
    mc "..."
    mc "I'm just gonna go play some more games."
    mc "I don't wanna think about it anymore."
    show bsb_blank with dissolve
    pause (1.0)
    stop music
    scene bg blank
    pause (3.0)
    label bsbagain:
    play music "audio/bsbtheme.mp3" volume 0.5
    scene bg bsb1 with fade
    if choice_senpairedo == True:
        scene bg bsb1
        shoujo2 "Moteko, how are you doing?"
        shoujo1 "Terrible."
        shoujo2 "Well, when I'm in a bad mood I like to eat chocolate."
        shoujo2 "Maybe you should go buy some to cheer yourself up."
        shoujo2 "And some for me too."
        shoujo1 "Is that all you ever think about?"
        play sound "audio/schoolchime1.wav"
        shoujo2 "Anyway, its time for lunch."
        shoujo2 "I'll see you after school, I gotta do something."
        scene bg bsb1 with fade
        "Its time for lunch."
        "Who do you wanna hangout with today?"
    default choice_senpairedo = False
    default choice_senpai1 = False
    default choice_senpai2 = False
    default choice_senpai3 = False
    default choice_senpai4 = False
    default choice_senpainum = 0
    if choice_senpai1 and choice_senpai2 and choice_senpai3 and choice_senpai4:
        jump afterbsb
    else:
        menu:
            "Get chocolates for Mafura" if choice_senpai1 == False:
                jump choices_mafura
            "Meet with Matsuge under the sakura tree" if choice_senpai2 == False:
                jump choices_matsuge
            "Hang out with Kinpatsu" if choice_senpai3 == False:
                jump choices_kinpatsu
            "Talk to Ikemen" if choice_senpai4 == False:
                jump choices_ikemen

    label choices_mafura:
    $ choice_senpairedo = True
    scene bg bsb3 with pixellate
    "You arrive at the line of the department store Yumeko mentioned."
    shoujo1 "Wow, the line is very long..."
    shoujo1 "I wonder if I can make it back before lunch is over..."
    senpai1 "Oi!"
    "You hear a familiar voice creep up behind you."
    show senpai1 real with dissolve
    senpai1 "Soko no shoujo yo!"
    "Its just the muffler guy."
    senpai1 "What are you doing here in this line?"
    shoujo1 "Oh! Mafura Senpai!"
    shoujo1 "I was just..."
    shoujo1 "Wait, what are you doing here?"
    senpai1 "I'm just here because I owe Ikemen a favor for helping me lift some equipment for the drama club."
    senpai1 "He asked me if I could buy something at the store for him."
    shoujo1 "What did he ask you to buy?"
    senpai1 "Idk, but he said that he likes coco."
    senpai1 "Someone recommended this store to me, so I thought maybe I should get him some chocolate to thank him since he likes coco so much."
    shoujo1 "Are you gonna go get any for yourself?"
    senpai1 "No, I hate chocolate."
    shoujo1 "Oh..."
    senpai1 "Is there something wrong?"
    shoujo1 "No..."
    shoujo1 "..."
    shoujo1 "I actually need to get going now, thanks for the chat."
    senpai1 "Oookay? Bye...?"
    shoujo1 "Bye!"
    senpai1 "..." with fade
    senpai1 "I wonder what that was all about."
    scene bg bsb1 with pixellate
    shoujo1 "(Whew, that was embarrassing! I'm so glad I got out of that one!)"
    shoujo1 "(So he doesn't even like chocolate, huh?)"
    shoujo1 "(Ugh, why did I have to listen to Yumeko?)"
    shoujo2 "Moteko!!"
    shoujo1 "?"
    shoujo2 "Did you get the chocolates?"
    shoujo1 "No."
    shoujo2 "Aweee, I really wanted some."
    shoujo1 "And he doesn't even like chocolate!"
    shoujo1 "I don't know why I listen to you!"
    shoujo1 "What am I gonna do now?"
    shoujo2 "Relax, maybe theres something else he likes, just be patient."
    shoujo2 "You'll figure it out soon."
    shoujo1 "Yea, I guess..."
    play sound "audio/schoolchime1.wav"
    shoujo2 "I'll guess we can continue talking after class."
    $ choice_senpainum += 1
    $ choice_senpai1 = True
    if choice_senpainum == 2:
        jump shutin_act1
    elif choice_senpainum == 3:
        jump shutin_act2
    else:
        jump bsbagain

    label choices_matsuge:
    $ choice_senpairedo = True
    scene bg bsb3 with pixellate
    show senpai2 real with dissolve
    senpai2 "Hello there, beautiful maiden."
    senpai2 "May I ask for your name?"
    shoujo1 "..."
    shoujo1 "Moteko...?"
    senpai2 "Moteko choupinette."
    senpai2 "I know that you're probably wondering..."
    senpai2 "\"WOW! what is the most handsome guy in school doing talking to me right now?!\""
    senpai2 "I already know."
    senpai2 "You're probably nervous and your knees are shaking as we speak."
    senpai2 "Why is this charming man calling you over today, you may ask?"
    senpai2 "I just wanted to say..."
    senpai2 "You caught my attention."
    senpai2 "I think you deserve an award for your boldness!"
    shoujo1 "..."
    shoujo1 "Matsuge, why are you talking to yourself in a mirror?"
    senpai2 "Oh... that?"
    senpai2 "I was just admiring myself for a bit."
    senpai2 "Don't worry, I was talking to you."
    shoujo1 "Riiight."
    shoujo1 "(He's not even looking at me, he's looking at his mirror.)"
    shoujo1 "(I don't think he would notice if I left either.)"
    $ choice_senpainum += 1
    $ choice_senpai2 = True
    if choice_senpainum == 2:
        jump shutin_act1
    elif choice_senpainum == 3:
        jump shutin_act2
    else:
        jump bsbagain

    label choices_kinpatsu:
    $ choice_senpairedo = True
    scene bg bsb3 with pixellate
    show senpai3 real with dissolve
    "You decided to go with kinpatsu senpai to watch him lift some cars."
    "But there are no cars to be found."
    "Afterall, why would there be cars in the drama room?"
    senpai3 "Anyway, I think the cars are here."
    senpai3 "!!!" with vpunch
    play sound "audio/slide.mp3"
    "Somebody opens the door."
    hide senpai3
    show senpai1 real
    senpai1 "Kinpatsu did you get the thing I asked you to go get?"
    hide senpai1
    show senpai3 real
    senpai3 "The cars?"
    senpai3 "Yea, I think Ikemen helped me carry them in here."
    hide senpai3
    show senpai1 real
    senpai1 "Kinpatsu, for the last time they're carts, not cars."
    hide senpai1
    show senpai3 real
    senpai3 "Oh yea, then tell me why it has 4 wheels!"
    hide senpai3
    show senpai1 real
    senpai1 "..."
    senpai1 "You're really making me lose my cool man."
    senpai1 "(sigh)"
    senpai1 "Do you have the carts ready or not?"
    hide senpai1
    show senpai3 real
    senpai3 "Yea, I do! And I invited a friend to watch me lift them!"
    hide senpai3
    show senpai1 real
    senpai1 "And why would you do that?"
    hide senpai1
    show senpai3 real
    senpai3 "To show them that I'm not a punk to be messed with!"
    hide senpai3
    show senpai1 real
    senpai1 "Riiight."
    senpai1 "Well, you can tell Moteko chan to leave now because you \"lifted\" them in here already..."
    hide senpai1
    show senpai3 real
    senpai3 "Aww man."
    senpai3 "Sorry man."
    senpai3 "Maybe you could watch me lift cars another day!"
    shoujo1 "..."
    shoujo1 "Okay, bye I guess..."
    $ choice_senpainum += 1
    $ choice_senpai3 = True
    if choice_senpainum == 2:
        jump shutin_act1
    elif choice_senpainum == 3:
        jump shutin_act2
    else:
        jump bsbagain

    label choices_ikemen:
    $ choice_senpairedo = True
    scene bg bsb3 with pixellate
    "You arrive at the ice cream store with Ikemen Senpai."
    shoujo1 "Senpai, why are we at the ice cream store?"
    show senpai4 real with dissolve
    senpai4 "Because I really like azucar."
    senpai4 "And the ice cream machine at the WackieDDs was broken."
    shoujo1 "...ok?"
    shoujo1 "(What the heck is azucar?)"
    shoujo1 "So, whats your favorite ice cream flavor?"
    senpai4 "Fresa!"
    shoujo1 "I see..."
    shoujo1 "How about your 2nd favorite ice cream flavor?"
    senpai4 "Dulce de leche!"
    shoujo1 "..."
    shoujo1 "(Googole Translate please help me out!)"
    "Translation notes: As I said, I'm sorry I can't help you out. I don't speak Spanish."
    shoujo1 "Oh look, we're at the front of the line!"
    "cashier" "Hello, may I take your order."
    senpai4 "Hi, do you guys have Guayaba flavored ice cream?"
    "cashier" "... Come again?"
    senpai4 "Guayaba Ice cream, do you have?"
    "cashier" "Let me check."
    "The cashier pulls out his phone."
    "To search something on Googole Translate I presume."
    "..."
    "cashier" "I'm sorry sir I do not believe we have Guava flavored ice cream."
    senpai4 "Awe man."
    senpai4 "What about coco?"
    "cashier" "Alright, is that all sir?"
    senpai4 "And what would you like amiga?"
    shoujo1 "Do you have strawberry?"
    "cashier" "No."
    shoujo1 "Vanilla?"
    "cashier" "No."
    shoujo1 "... Birthday cake?"
    "cashier" "No."
    shoujo1 "What?!"
    shoujo1 "What flavors do you guys even have then?!?"
    "cashier" "Our popular flavors today are, squid ink, wasabi, and nattou flavored."
    "cashier" "I would personally recommend the soy sauce flavored one though."
    shoujo1 "..."
    shoujo1 "I'll just have what he's having."
    ##ts ----------------
    scene ts some_time_later with fade
    pause
    ##ts ----------------
    scene bg bsb3 with pixellate
    show senpai4 real with dissolve
    "cashier" "Here you guys are."
    "cashier" "Two chocolate ice creams."
    senpai4 "..."
    senpai4 "But I wanted coco icecream."
    "cashier" "But that is cocoa ice cream."
    senpai4 "No, I meant the coco thats brown on the outside and white on the-{nw}"
    senpai4 "..."
    senpai4 "Actually, nevermind..."
    senpai4 "This is fine."
    $ choice_senpainum += 1
    $ choice_senpai4 = True
    if choice_senpainum == 2:
        jump shutin_act1
    elif choice_senpainum == 3:
        jump shutin_act2
    else:
        jump bsbagain

    label shutin_act1:
    stop music
    play sound "audio/static.wav"
    scene bg blank
    show static
    pause (3.0)
    scene bg blank
    "Mom" "Haru!"
    "Mom" "Its time for school!"
    "Mom" "Naomi called."
    "Mom" "She's been asking about you!"
    "Mom" "Here, she came over the other day to drop off some snacks and medicine."
    "Mom" "I told her that you were sick."
    "Mom" "So you don't have to be ashamed, just come out."
    "Mom" "The teachers at school have been calling me asking me how you were doing."
    "Mom" "I went to the school and I got your homework for you."
    "Mom" "Please come out..."
    "Mom" "You've been hiding in your room for a week now."
    play sound "audio/static.wav"
    scene bg blank
    show static
    pause (3.0)
    scene bg blank
    jump bsbagain

    label shutin_act2:
    stop music
    play sound "audio/static.wav"
    scene bg blank
    show static
    pause (3.0)
    scene bg blank
    "Mom" "Haru!"
    "Mom" "Dinner is ready!"
    "Mom" "It's going to get cold if you don't eat it!"
    "Mom" "..."
    "Mom" "I'll leave it by the door."
    "Mom" "Love you sweetie."
    play sound "audio/static.wav"
    scene bg blank
    show static
    pause (3.0)
    scene bg blank
    jump bsbagain

    label afterbsb:
    stop music
    play sound "audio/static.wav"
    scene bg blank
    show static
    pause (3.0)
    scene bg blank
    play music "audio/uncanny.mp3" fadein 1.0 volume 0.5
    bff "Haru!!"
    play sound "audio/knock.wav"
    bff "I got you something!"
    bff "Are you okay?"
    "The knocking on the door mocks me."
    bff "Haru!?"
    play sound "audio/knock.wav"
    bff "... please could you come out?"
    "I just want people to leave me alone."
    bff "..."
    bff "I got you a melon bread and some green tea."
    bff "I know you love those."
    bff "..."
    bff "You still have to give me my game back."
    mc "..."
    mc "Fine, Nao."
    mc "I'll open the door."
    scene bg bedroom with fade
    show bff depressed with dissolve
    bff "Haru, you haven't come to school for 3 weeks, whats going on with you?"
    mc "..."
    show bff sigh
    bff "Anyway, I'm here to drop off your homework."
    show bff worried
    bff "But I doubt you can do all of these assignments by yourself."
    bff "Do you need any help?"
    mc "..."
    mc "I'm sorry."
    show bff sad
    bff "...?"
    bff "What?"
    mc "I'm a terrible friend."
    mc "Why do you always have to be so nice to me all the time?"
    mc "Even after what I said to you?"
    mc "After everything I say..."
    mc "You still stick around..."
    mc "When I'm such an awful person..."
    bff "Haru..."
    stop music fadeout 1.0
    show bff sigh
    bff "What are you talking about? You're one of the nicest people I've ever met."
    bff "You think I would be hanging out with you if you were an awful person?"
    show bff sad
    bff "..."
    bff "Please come back to school, Haru."
    bff "We all miss you..."
    mc "..."
    mc "Okay, fine."
    show bff glee
    bff "Great, now lets catch up on all that homework you missed."
    bff "I doubt you can do it all in one day but we'll do as much as possible."
    ##ts --------
    scene ts a_few_weeks_later with fade
    pause
    ##ts --------
    stop music
    scene bg blank with fade
    "Ever since that day, Nao has been coming over everyday to help me with my homework."
    "Eventually, I decided to come back to school."
    play music "audio/classtime.mp3" fadein 1.0
    scene bg classroom with fade
    bff "Haruu!!"
    mc "What is it now, Nao?"
    show bff closeup with vpunch
    mc "AAAAAAHHHHH!"
    show bff glee
    bff "Hi!"
    mc "Will you stop doing that? One day you're gonna give me a heart attack."
    show bff worried
    bff "Oh, cmon! I was just messing around!"
    bff "Anyway.."
    show bff normal
    bff "Have you ever thought about making your own visual novel?"
    mc "I can't say that I have."
    show bff worried
    bff "Oh, cmon!"
    show bff excited
    bff "Just think about it!"
    bff "Making your own video game! About being with the guys of your dreams! And even more! You get to pick all of them and live your fantasy with them!"
    bff "Just imagine! Having your own harem!"
    show bff blush
    bff "When I make my first visual novel game I'm gonna write a fanfiction about my own game!"
    mc "..."
    mc "Nao, I don't think you can write a fanfiction about your own game..."
    show bff excited
    bff "Maybe I'll make my own head cannons as well!"
    mc "..."
    "She's utterly beyond any single trace of hope."
    "Sometimes I wonder if those otome games and shoujo manga are bad for her mental health."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    show bff normal
    bff "Welp, cya after class, Haru!"
    show bff mischievous
    bff "And cya in the art club after school, make sure to bring your homework too."
    hide bff with dissolve
    "..."
    "She scares me sometimes."
    stop music fadeout 1.0
    ##ts -------------------------------------
    scene ts after_school with fade
    pause
    ##ts -------------------------------------
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg artroom with fade
    show bff normal with dissolve
    bff "Alright, Haru. All you have to do for this one is divide both sides by three and then combine like terms."
    play sound "audio/doorslide.wav"
    pause(0.5)
    show bff worried
    male3 "You two hooligans right there!" with vpunch
    hide bff
    show male3 normal
    male3 "Sorry to burst your bubble but you guys need to head out."
    male3 "The school is officially closed, and right now it is only opened to clubs."
    hide male3
    show bff worried
    bff "Uhm... excuse me; we ARE a club."
    show bff sigh
    bff "Are you sure you're not just singling us out?"
    bff "You've had no issues joining us last time; whats the big deal?"
    show bff worried
    bff "You don't have to be so petty just because I rejected you, y,know?"
    hide bff
    show male3 blush
    male3 "You can't just go around telling people that!"
    male3 "And its nothing like that at all! You got it all wrong!"
    show male3 annoyed
    male3 "The head master is getting more strict with the rules nowadays."
    show male3 normal
    male3 "He said clubs with less than 4 members cannot be deemed as official clubs and are to be disbanded immediately."
    male3 "So far your club only has 2 students."
    male3 "There was a problem with inactive clubs not participating in the culture festival last year."
    male3 "And since its coming up again, the head master is not willing to take anymore risks."
    hide male3
    show bff worried
    bff "And...?"
    bff "I'm sorry, I'm missing the part where thats my problem."
    bff "I don't care what the head master says, just leave us alone."
    hide bff
    show male3 worried
    male3 "I can't just let this slide Naomi."
    show male3 normal
    male3 "It's either I shut down this club or somebody else will."
    mc "Well Hiro, are you sure you can't make any exceptions?"
    male3 "What do you mean?"
    mc "Well, I'm sure you can convince the head master to give us a pass somehow."
    show male3 annoyed
    male3 "..."
    male3 "I'm not sure where you're going with this but I already don't like it."
    mc "I mean, after all, you're his son aren't you?"
    show male3 blush
    male3 "!!!"
    mc "You should be able to convince him somehow, can't you?"
    male3 "HOW DID YOU KNOW?!" with hpunch
    male3 "And-and-and!!"
    show male3 angry
    male3 "Even if THAT was true! What makes YOU think that I would be doing favours for YOU!"
    hide male3
    show bff glee
    bff "Oh, calm down Hiro, you don't have to boss everyone around just because you're student council president."
    show bff mischievous
    bff "I never knew you were a daddies boy, no wonder you never get in trouble, he must spoil you rotten!"
    show bff glee
    bff "Hiro, lets make a deal shall we?"
    bff "I beat you in a baseball match, and we get to keep the club."
    hide bff
    show male3 angry
    male3 "YOU!?"
    male3 "Thats hardly even fair!"
    male3 "You're an absolute demon when it comes to sports! You'd know I'd lose, and theres no way I would agree to that!"
    hide male3
    show bff worried
    bff "Fiiiine."
    show bff glee
    bff "Ok, how about this instead?"
    show bff normal
    bff "Haru beats you in a baseball match, we get to keep this club. We lose, we disband it just like you want us to."
    hide bff
    show male3 normal
    male3 "And what makes you think I'd agree to that?"
    hide male3
    show bff mischievous
    bff "We could tell the entire school that you didn't win your election fair and square and tell everyone its because your daddy loves and supports you. Awweeee!"
    show bff excited
    bff "Or we can tell everyone you read shoujo manga."
    hide bff
    show male3 worried
    male3 "Somehow you always get me involved into your reckless antics, Naomi."
    show male3 normal
    male3 "Fine, its a deal, but its not like I have any other choice at this point."
    male3 "I'm very busy this week, so next weekend we can settle this."
    show male3 angry
    male3 "And if I beat you guys {b}which I will{/b}, you're going to shut down this club once and for all!"
    show male3 annoyed
    male3 "Just do whatever you got to do for today and leave."
    hide male3 with dissolve
    mc "..."
    mc "(I wonder what's up with him.)"
    show bff sigh with dissolve
    bff "Haru, don't mind Hiro, he's just a jerk sometimes."
    show bff normal
    bff "Anyway..."
    "Nao continued helping me with my homework until it was time to go home."
    stop music fadeout 1.0
    ##ts ------------
    scene ts home with fade
    pause
    ##ts -------------
    scene bg bedroom with fade
    "..."
    "(I wonder what's with that guy.)"
    "(Hiro...)"
    "(Do you have a reason to be bothering us?)"
    "(Or is it just me?)"
    stop music fadeout 1.0
    ##ts ------------------
    scene ts the_next_day with fade
    pause
    ##ts -------------------
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    scene bg school_hallway with fade
    show ct_overlay
    show ct_wed
    show ct_345
    with dissolve
    "..."
    "(Where is Nao?)"
    "(I haven't seen her all day.)"
    "I spotted a familiar figure in the distance."
    "(It's Hiro!)"
    show male3 normal with dissolve
    male3 "(I knew they would be out of strawberry milk today, they don't restock until like next week...)"
    mc "Hiro!!!"
    show male3 blush
    male3 "AAAAAAHHHH!"
    male3 "Are you a MANIAC? You scared me!"
    mc "Do you know where Naomi is?"
    show male3 normal
    male3 "Naomi?"
    male3 "Why would I know?"
    male3 "She's always hanging out with Kaoru."
    show male3 worried
    male3 "Now that I think about it... I haven't seen Kaoru around for a while either..."
    show male3 normal
    male3 "Something gives me an idea."
    male3 "... come with me."
    scene bg kaoru_office_door with fade
    male3 "I think they might be in here."
    male3 "Huh? Thats strange; they left it ope-{nw}"
    male3 "!!!"
    scene cg kaoru_maid with fade
    male4 "!!!"
    male4 "Senpai!? I didn't expect you to be here so soon!"
    "It seems as if you're intruding on some questionable roleplay."
    male4 "What are you doing? I have to go back to work! I haven't finished making you that Omurice yet!"
    bff "(speaks in deep senpai voice) Hey, where are your manners?"
    bff "Shouldn't you be greeting your customers with some respect?"
    bff "You know what, I got an idea."
    bff "How about I feed you instead?"
    bff "Oh look, you got something in your mouth."
    male4 "Wait?! What are you doing?! Senpai! NOOOOO!"
    scene bg blank with fade
    "..."
    "I have no words for this."
    scene bg school_hallway with fade
    show male3 blush with dissolve
    male3 "My god... those two are embarrassing."
    male3 "It makes me wonder why am I even friends with them to begin with..."
    show male3 worried
    male3 "(sigh)"
    show male3 normal
    mc "..."
    mc "By the way Hiro..."
    male3 "...?"
    mc "Whats the deal between you and Naomi?"
    male3 "Oh."
    male3 "You could say that we used to get along... but not so much now."
    male3 "Anyway it doesn't matter. Whatever happened between me and Naomi is history."
    male3 "I think we should leave them alone to do whatever cringe trash they're doing and eat lunch in my office instead."
    stop music fadeout 1.0
    scene bg hiro_office with fade
    play music "audio/peaceful.mp3" fadein 1.0 volume 0.5
    show male3 normal with dissolve
    male3 "..."
    "An awkward silence fills the air for a brief moment"
    male3 "So... anyways..."
    male3 "Harumiya san..."
    male3 "Uhm. . ."
    male3 "How was your day?"
    mc "..."
    mc "Are you seriously going to ask me that?"
    male3 "..."
    show male3 worried
    male3 "Look."
    male3 "I'm sorry."
    male3 "But I gotta do what I gotta do."
    male3 ". . ."
    show male3 normal
    male3 "My father isn't exactly the easiest person in the world to please."
    male3 "I'm just following orders."
    mc "Oh really now?"
    show male3 angry
    male3 "Hey!"
    male3 "I'm doing what I can okay!"
    male3 "Besides, we still have the end of the week to decide!"
    male3 "Don't rush my decision making process!"
    male3 "A deal is a deal!"
    male3 "We'll settle it at the baseball field!"
    mc "..."
    mc "Fine."
    show male3 annoyed
    male3 "Hanging out with troublesome hooligans like yourself really makes my cortisol levels go through the roof!"
    male3 "I'm stressed out, okay?!"
    show male3 normal
    male3 "..."
    male3 "Let's eat our food."
    #ts -------------------------
    scene ts some_time_later with fade
    pause
    #ts -------------------------
    scene bg hiro_office with fade
    show male3 normal with dissolve
    male3 "Harumiya."
    mc "Yes, Hiro?"
    male3 "..."
    male3 "I know this is random but..."
    male3 "Do you wanna play 20 questions?"
    mc "Uhm..."
    mc "Sure?"
    show male3 angry
    male3 "Hey!"
    male3 "Don't look at me like that!!!"
    show male3 normal
    male3 "I'm just..."
    male3 "Not good at starting conversations."
    mc "..."
    mc "Alright."
    label trivia1:
    play music "audio/classic timer.wav" fadein 1.0 volume 0.5
    scene bg blank with fade
    centered "Type the letters that pop up on the screen before the timer runs out."
    scene white with fade
    centered "{color=#000}Alright, I'm going to give you a free hint.{/color}"
    centered "{color=#000}I'm thinking of something green.{/color}"
    scene mg trivia1 with fade
    show mg thinking with dissolve

    $ cont = 0 #continue variable
    $ arr_keys = ["z", "x", "c"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys

    call qte_setup1(0.75, 0.75, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup1
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    $ counter = 0 #counter variable
    while cont == 1 and counter < 10:
        call qte_setup1(0.75, 0.75, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup1_1
        $ counter = counter + 1 #increment/increase the counter each time. When it reaches 10, it will exit the loop
        # to repeat the qte events until it is missed

    if counter == 10: #if we reached 10 rounds without missing
        stop music
        play audio "audio/success.wav"
        scene mg trivia2
        mc "Is it a leaf?"
        jump trivia_end1
    else:
        stop music
        scene mg trivia2
        mc "Water!"
        scene mg trivia3
        play sound "audio/drop.mp3"
        male3 "In what world is water even green dum dum??!!"
        centered "{nw}"
        show mg_guu with dissolve
        pause (1.5)
        jump trivia1

label qte_setup1(time_start, time_max, interval, trigger_key, x_align, y_align):
    $ renpy.block_rollback()
    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple

    $ cont = _return
    play sound "audio/tiktak.wav" volume 0.5
    # 1 if key was hit in time, 0 if key not
    return

    label trivia_end1:
    stop music fadeout 1.0
    scene bg hiro_office with fade
    show male3 normal with dissolve
    male3 "Pretty close but thats not quite it."
    male3 "I was thinking of a bush."
    scene bg blank with fade
    "(I spent the remainder of lunch with Hiro.)"
    "(Though, its quite strange.)"
    "(I usually spend my lunches with Naomi.)"
    "(Maybe Hiro isn't such a bad apple after all...)"
    ##ts --------------------------------------------
    scene ts western_emoji with fade
    pause
    scene ts jp_emoji
    pause
    scene ts kaomoji1
    pause
    scene ts kaomoji2
    pause
    scene ts kaomoji3
    pause
    scene ts yey
    pause
    scene ts lol
    pause
    scene ts ok_enough
    pause
    scene ts a_few_days_later
    pause
    ##ts --------------------------------------------
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    scene bg baseball with fade
    show bff glee with dissolve
    bff "Okay, Hiro should be here any moment now."
    show bff excited
    bff "YOU BETTER SHOW HIM WHAT YOU GOT HARU!"
    bff "WE'RE GONNA SHOW THAT SCUMBAG JUST WHO'S BOSS!"
    show bff worried
    play sound "audio/bonebreak.wav"
    "(Thump)" with vpunch
    $ renpy.vibrate(.5)
    "You heard someone fall down."
    scene bg blank with fade
    mc "!!!"
    bff "!!!"
    male3 "Ow..."
    mc "Oh my god, Hiro! Are you okay?!"
    stop music fadeout 1.0
    ##ts ------------------------------
    scene ts a_few_days_later with fade
    pause
    ##ts ------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 0.5
    scene bg classroom with fade
    show ct_overlay
    show ct_mon
    show ct_830
    with dissolve
    "..."
    "It's been a few days since the incident."
    "When Hiro came to meet up with us at the baseball field, he fell down the steps and ended up breaking his arm so he couldn't play."
    "He automatically lost the bet."
    "I kind of feel bad..."
    "But Naomi insisted, a bet was a bet."
    "The art club didn't get shut down after all."
    "But in exchange, I have to help Hiro do his paper work after school since his arm is now broken."
    hide ct_overlay
    hide ct_mon
    hide ct_830
    with dissolve
    "..."
    "But its strange..."
    "Naomi is nowhere to be found."
    "She usually greets me in the mornings."
    male4 "Hey!!" with vpunch
    $ renpy.vibrate(.5)
    "!!!"
    "Kaoru?!"
    "What does he want?"
    scene bg school_hallway with fade
    show male4 normal with dissolve
    "..."
    "What does he want now?"
    male4 "Haru."
    male4 "Can I have a moment to speak with you?"
    mc "???"
    mc "Sure?"
    show male4 glee
    male4 "Okay!"
    show male4 scared with vpunch
    $ renpy.vibrate(.5)
    male4 "{size=16}Haru!!!{/size}"
    show male4 nervous
    male4 "{size=16}Whatever you saw me and Naomi doing... please act like you didn't see anything.{/size}"
    mc "What?!"
    show male4 scared with vpunch
    $ renpy.vibrate(.5)
    male4 "YOU SAW NOTHING!"
    mc "..."
    mc "O-O-Oookay?"
    show male4 nervous
    male4 "Hahahaha, good then."
    show male4 happy
    male4 "Nothing happened. Alright?"
    male3 "What happened?"
    hide male4 with dissolve
    show male3 cast_normal with dissolve
    male3 "What are you two trouble makers doing in the hallways?"
    male3 "It's almost time for class to start."
    hide male3
    show male4 scared
    male4 "HIRO!!!!???"
    male4 "SINCE WHEN DID YOU GET HERE?!"
    male4 "..."
    show male4 nervous
    male4 "NOTHING!"
    male4 "w-we-we were talking about..."
    male4 "NOTHING!"
    hide male4
    show male3 cast_normal
    male3 "Nothing huh?"
    male3 "That sounds really suspicious..."
    hide male3
    show male4 nervous
    male4 "Anyway! It's almost time for class! We can talk later!"
    hide male4 with dissolve
    "Kaoru disappeared into the hallway after waving goodbye."
    show male3 cast_normal with dissolve
    male3 "Don't mind Kaoru..."
    show male3 cast_happy
    male3 "Sometimes he's weird but he's actually a pretty cool guy sometimes."
    show male3 cast_angry
    male3 "If only he stopped annoying me almost EVERY SINGLE DAY!"
    show male3 cast_normal
    male3 "Anyways, I should get going too. Class is about to start."
    hide male3 with dissolve
    "Hiro slips away."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    "Its time for class to start."
    stop music fadeout 1.0
    ##ts ---------------------------
    scene ts some_time_later with fade
    pause
    ##ts ---------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 0.5
    scene bg classroom with fade
    "It's lunch time."
    "Naomi isn't here today."

    label choices11:
    "Where should I go?"
    menu:
        "Visit Hiro's office.":
            jump choices11_common
        "Visit Kaoru's office":
            jump choices11_common

    label choices11_common:
    "Maybe I should ask if Kaoru knows anything about Naomi's whereabouts."
    "I can catch up with Hiro after school."
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    scene bg kaoru_office with fade
    show ct_overlay
    show ct_mon
    show ct_105
    with dissolve
    mc "???"
    mc "..."
    mc "Hello?"
    mc "Is anybody here?"
    male4 "Boo."
    mc "!!!" with vpunch
    $ renpy.vibrate(.5)
    show male4 glee with dissolve
    male4 "Did I scare ya?"
    mc "Oh, hi Kaoru."
    male4 "Did you need something from me?"
    hide ct_105
    hide ct_mon
    hide ct_overlay
    with dissolve
    mc "..."

    label choices12:
    mc "Actually..."
    menu:
        "ask about Naomi":
            jump choices12_a
        "ask about Hiro":
            jump choices12_b
        "Nevermind":
            mc "actually nevermind."
            jump choices12_common

    label choices12_a:
        mc "I wanted to ask if you've seen Naomi recently."
        mc "I haven't seen her around lately."
        show male4 normal
        male4 "Naomi..."
        male4 "I don't think I've seen her around either."
        male4 "I've actually been looking for her myself but..."
        show male4 blush
        male4 "so far I've seen no sign of her."
        jump choices12_common


    label choices12_b:
        mc "I have a question I've been meaning to ask lately..."
        mc "How long have you and Hiro been friends?"
        show male4 happy
        male4 "Me and Hiro?"
        male4 "We've actually been friends for quite a while..."
        show male4 glee
        male4 "Since first year I believe."
        show male4 normal
        male4 "It sorta went something like this..."
        scene bg school_okujou with fade
        show male4 normal with dissolve
        male4 "So, what's your name?"
        hide male4
        show male3 normal
        male3 "Hasegawa Takahiro."
        male3 "Some call me Taka, some call me Hiro."
        male3 "But only my close friends and family call me that so everyone else just calls me Hasegawa if we're not on a first name basis yet..."
        male3 "Though some people get confused and say Hasehiro but its Hasegawa not Hirotaka or Hasetaka or Hirohiro."
        hide male3
        show male4 nervous
        male4 "..."
        show male4 scared
        male4 "Come again?"
        hide male4
        show male3 normal
        male3 "Hasehiro-"
        show male3 blush
        male3 "I MEAN!"
        male3 "HASEGAWA HASEGAWA!"
        show male3 worried
        male3 "Just call me Taka..."
        male3 "or Hiro..."
        show male3 normal
        male3 "Which ever one you prefer."
        hide male3
        show male4 normal
        male4 "Hasetaka Hasehiro?"
        hide male4
        show male3 normal
        male3 "No."
        hide male3
        show male4 happy
        male4 "Hasehiro Hirohawa!"
        hide male4
        show male3 annoyed
        male3 "No!"
        hide male3
        show male4 glee
        male4 "HIROHASE HIROTAKA"
        hide male4
        show male3 angry
        male3 "NOOOO!!!"
        hide male3
        show male4 excited
        male4 "HIROHIRO HIROHIRO!!!"
        hide male4
        show male3 blush
        male3 "AAHHHHHHH!!!"
        male3 "NO!! THATS NOT MY NAME!!"
        show male3 angry
        male3 "UGH! FORGET IT! JUST CALL ME HIRO?! OKAY?!"
        scene bg kaoru_office with fade
        show male4 excited with dissolve
        male4 "And, thats how I met Hiroro!"
        mc "Oookay?"
        jump choices12_common

    label choices12_common:
    stop music fadeout 1.0
    show male4 normal
    male4 "Anyways, Haru. What shampoo do you use?"
    mc "Huh?"
    show male4 happy
    male4 "Your hair looks dry..."
    mc "..."
    scene bg blank with fade
    "He comes closer."
    male4 "You look like you haven't been taking care of yourself lately, haven't you?"
    male4 "Look, you have split ends."
    mc "???"
    male4 "Here take a seat."
    play music "audio/ponder_ost.mp3" fadein 1.0 volume 0.5
    scene cg kaoru brush with fade
    pause
    male4 "Just let me fix you up a little bit."
    male4 "Y,know you should learn how to take care of yourself better."
    male4 "Naomi tells me all about you."
    male4 "She talks about you a lot."
    male4 "She tells me that when you get stressed you tend to look more disheveled than usual."
    male4 "And that often times you forget to take care of yourself, especially when you're overwhelmed."
    male4 "She cares about you alot."
    male4 "But girls like you look the most beautiful when you're being properly taken care of."
    mc "..."
    mc "Kaoru?"
    male4 "Yes, dear?"
    mc "Why are you doing my hair?"
    male4 "..."
    male4 "I'm sorry, do you not like it?"
    mc "..."
    mc "It's not that I don't like it."
    mc "Nevermind..."
    male4 "Alright then."
    male4 "You probably think it's strange for guys to be doing a girl's hair, that's probably what you're wondering right?"
    male4 "Well..."
    male4 "I happen to have many sisters."
    male4 "And my mother owns a beauty salon."
    male4 "I used to help her deal with clients."
    male4 "She taught me how to do their hair."
    male4 "..."
    male4 "That pretty much explains it."
    male4 "In school I used to get picked on for looking like a girl."
    male4 "Naomi was the first person who saw me as a guy."
    male4 "It's really funny though."
    male4 "At the time, I didn't even know she was a girl."
    male4 "We were practically polar opposites."
    "I felt as if Kaoru's gentle hands caressed each strand of my hair with care."
    "We bonded closer after exchanging stories with each other."
    stop music fadeout 1.0
    scene bg kaoru_office with fade
    show male4 happy with dissolve
    male4 "And we're done."
    stop music
    play sound "audio/dooropen.wav"
    show male4 nervous
    male4 "..."
    hide male4
    show male3 cast_normal with dissolve
    male3 "Kaoru."
    male3 "..."
    male3 "What are you two doing?"
    hide male3
    show male4 nervous
    male4 "N-N-NOTHING!"
    hide male4
    show male3 cast_normal
    male3 "..."
    male3 "Y,know what, I'm not even gonna ask."
    male3 "Haru, come with me."
    male3 "I need you to meet with me in my office real quick."
    hide male3
    show male4 worried
    male4 "Hey, she was talking with me."
    hide male4
    show male3 cast_normal
    male3 "So?"
    male3 "It's her fault my arm is broken so she owes me a favor."
    male3 "Now excuse us Kaoru."
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg hiro_office with fade
    "You arrive with Hiro at his office."
    show male3 cast_normal with dissolve
    male3 "Please excuse Kaoru."
    male3 "Sometimes he can get carried away..."
    show male3 cast_angry
    male3 "He likes to sweet talk women but apparently he's completely oblivious
    about what he actually says."
    male3 "He says tons of stuff without giving it second-thought."
    show male3 cast_normal
    male3 "I'm gonna warn you though, you shouldn't take what he says seriously."
    male3 "He's oblivious but he can be really inconsiderate sometimes."
    mc "... What do you mean?"
    show male3 cast_annoyed
    male3 "I mean he likes to mess with people's emotions too much."
    show male3 cast_normal
    male3 "Do you understand?"
    label choices13:
    mc "Uhm..."
    menu:
        "No, I don't.":
            jump choices13_common
        "I don't mind.":
            jump choices13_common
        "Really?":
            jump choices13_common

    label choices13_common:
    mc "..."
    mc "I actually don't know what to say."
    play sound "audio/schoolchime1.wav"
    "The bell rings."
    "It's time for class."
    male3 "It's time for class."
    show male3 cast_worried
    male3 "I'll see ya after school then, I guess."
    stop music fadeout 1.0
    ##ts ------------------------------------------------
    scene ts after_school with fade
    pause
    ##ts ------------------------------------------------
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg hiro_office with fade
    show ct_overlay
    show ct_mon
    show ct_430
    with dissolve
    show male3 cast_normal with dissolve
    male3 "Anyways..."
    male3 "The paperwork is over there."
    male3 "Do you think you can bring it over here for me?"
    male3 "..."
    male3 "And don't worry about my arm..."
    male3 "A deal's a deal."
    male3 "I'll talk to the head master about it sometime next week..."
    show male3 cast_worried
    male3 "I can't guarantee that he'll listen to me though."
    show male3 cast_normal
    mc "..."
    mc "Thanks."
    show male3 cast_blush
    male3 "W-Wh-What are you thanking me for!?!?"
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi hiro with dissolve
    show progress0 with dissolve
    pause 1.0
    show heart_progress1
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart from Hiro!{/size}"
    scene bg hiro_office with fade
    show male3 cast_blush with dissolve
    male3 "Just hurry up and go get the paperwork!!!"
    ##ts ----------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts ----------------------------------------------
    scene bg hiro_office with fade
    show male3 cast_normal with dissolve
    male3 "So, do you think you could help me sign and stamp here?"
    male3 "..."
    male3 "It needs my signiature..."
    show male3 cast_worried
    male3 "I'll guess I'll just make do with my left hand."
    show male3 cast_normal
    male3 "..."
    male3 "Harumiya..."
    male3 "What are you spacing out for?"
    mc "Oh!"
    mc "Sorry about that."
    male3 "Is there something on your mind?"
    mc "Uhm... no."
    mc "It's just..."
    male3 "It's just what?"
    mc "This is usually around the time Naomi helps me with my homework..."
    male3 "Oh."
    male3 "Is that so?"
    male3 "..."
    mc "..."
    male3 ". . ."
    male3 "Well..."
    male3 "Uhm. . ."
    male3 "How are your grades?"
    mc ". . ."
    male3 "We got our midterm results last week right?"
    male3 "What did you get?"
    mc "..."
    mc "What subject?"
    male3 "Uhhhh... I don't know."
    male3 "Math maybe?"
    mc "{size=16}34{/size}"
    male3 "..."
    male3 "Come again?"
    mc "..."
    mc ". . ."
    mc "I got a 34 in math okay?!"
    male3 "..."
    show male3 cast_blush
    male3 "YOU GOT A WHAT!?!?"
    show male3 cast_angry
    male3 "HOW DO YOU GET A 34 IN MATH?!"
    male3 "HOW ARE YOU GOING TO EXPLAIN THAT TO YOUR PARENTS?!"
    show male3 cast_blush
    male3 "I mean!!!"
    male3 "..."
    male3 "It's none of my business really!"
    male3 "..."
    show male3 cast_annoyed
    male3 "You better not be laughing at me!"
    mc "..."
    mc "Geez..."
    mc "Insecure much?"
    show male3 cast_normal
    male3 "Anyway..."
    male3 "..."
    male3 "I mean if you're grades are THAT bad I guess I could tutor you myself."
    mc "..."
    mc "Really?"
    show male3 cast_blush
    male3 "AAAAAAAAAHHHHHHHHHH!!!!"
    male3 "DON'T LOOK AT ME LIKE THAT!"
    show male3 cast_angry
    male3 "Look, I'm only doing this out of common courtesy!"
    show male3 cast_normal
    male3 "After all, its partially my fault that you don't have enough time to attend to your studies like you should be doing."
    male3 "You're spending your time helping me out after all."
    male3 "By extension that means I'm responsible for you..."
    male3 "For the time being..."
    male3 "..."
    show male3 cast_angry
    male3 "You better not get any weird ideas about it okay!"
    mc "... what are you talking about?"
    male3 "NOTHING!"
    play music "audio/classic timer.wav" fadein 1.0 volume 0.5
    scene bg blank with fade
    centered "Type the letters that pop up on the screen before the timer runs out."
    scene white with fade
    centered "{color=#000}Okay Haru, Lets start with simple warm ups!{/color}"
    centered "{color=#000}Whats 2 + 2 = ?{/color}"
    scene mg trivia1 with fade
    show mg thinking with dissolve

    $ cont = 0 #continue variable
    $ arr_keys = ["z", "x", "c"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys

    call qte_setup2(0.75, 0.75, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup2
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    $ counter = 0 #counter variable
    while cont == 1 and counter < 10:
        call qte_setup2(0.75, 0.75, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup2_1
        $ counter = counter + 1 #increment/increase the counter each time. When it reaches 10, it will exit the loop
        # to repeat the qte events until it is missed

    if counter == 10: #if we reached 10 rounds without missing
        stop music
        scene mg trivia2
        mc "3!"
        scene mg trivia4
        play sound "audio/drop.mp3"
        male3 "WRONG!"
        jump trivia_end2
    else:
        stop music
        scene mg trivia2
        mc "3!"
        scene mg trivia4
        play sound "audio/drop.mp3"
        male3 "WRONG!"
        centered "{nw}"
        show mg_guu with dissolve
        pause (1.5)
        jump trivia_end2

label qte_setup2(time_start, time_max, interval, trigger_key, x_align, y_align):
    $ renpy.block_rollback()
    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple

    $ cont = _return
    play sound "audio/tiktak.wav" volume 0.5
    # 1 if key was hit in time, 0 if key not
    return

    label trivia_end2:
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg hiro_office with fade
    show ct_overlay
    show ct_mon
    show ct_400
    with dissolve
    show male3 cast_annoyed with dissolve
    male3 "Jesus Christ! How did you even make it to highschool? You can't do math even if you're life depended on it!"
    male3 "Are you dumb? How could you not even solve a simple math equation?"
    show male3 cast_normal
    male3 "..."
    male3 "Let's just take a break from studying for now, you're raising my blood pressure just by me listening to your dumb answers."
    mc "..."
    mc "(Wow, Naomi is right, he is a jerk.)"
    "An awkward silence fills the air as Hiro and I continue filling out the paper work for the rest of the afternoon."
    stop music fadeout 1.0
    ##ts -----
    scene ts home with fade
    pause
    ##ts ---------
    scene bg bedroom with fade
    "Finally home."
    mc "..."
    show bsb_blank with dissolve
    mc "Wait..."
    mc "I just realized that..."
    mc "There's something off with this game..."
    mc "How come everything that happens in the game ends up happening in real life?"
    mc "Am I hallucinating again?"
    "Mom" "Chiharu!" with vpunch
    mc "!!!"
    hide bsb_blank with dissolve
    "Mom" "Dinner's ready!"
    mc "... I'll think about this some other time."
    ##ts -----
    scene bg blank with fade
    centered "{size=45}Two days later.{/size}"
    ##ts ---------
    play music "audio/classtime.mp3" fadein 1.0 volume 0.5
    scene bg classroom with fade
    show ct_overlay
    show ct_wed
    show ct_830
    with dissolve
    mc "..."
    mc "It's strange."
    mc "This is when Naomi usually greets me in the morning."
    mc "Where is she?"
    male4 "Haru!!!"
    mc "?"
    "Someone was calling me from the hallway."
    scene bg school_hallway with fade
    mc "..."
    mc "(Who was that?)"
    mc "!!!" with vpunch
    male4 "Guess who."
    mc "Kaoru! What are you doing?!"
    show male4 normal with dissolve
    male4 "You know, a girl like you shouldn't let your guard down so easily."
    male4 "After all, its really dangerous to go out there in the world by yourself when you can't sense danger."
    show male4 glee
    male4 "You should take more care of yourself."
    male4 "Who knows, you might die if you're not careful enough."
    mc "..."
    mc "What are you trying to say?"
    show male4 blush
    male4 "Nothing..."
    show male4 normal
    male4 "By the way..."
    mc "...?"
    male3 "Hold it right there!" with vpunch
    show male4 scared
    male4 "!!!"
    hide male4
    show male3 cast_normal
    male3 "She's coming with me."
    hide male3
    show male4 nervous
    male4 "Hiro, I was talking to her first. I kinda have something I want to talk to her about; do you think we can do this later?"
    hide male4
    show male3 cast_annoyed
    male3 "Excuse me?!"
    hide male3
    show male4 scared
    male4 "N-N-Nevermind!"
    show male4 nervous
    male4 "Sorry about that Haru, I guess I'll talk to you later about it okay!?"
    hide male4 with dissolve
    "He runs off into the distance."
    mc "..."
    mc "And there goes Kaoru..."
    show male3 cast_normal
    male3 "..."
    male3 "Harumiya san."
    male3 "I just wanted to let you know..."
    mc "..."
    male3 "Surprisingly, the club got approval."
    male3 "It was a hassle to explain but the head master approved of the club..."
    male3 "For now at least."
    male3 "You guys will need to be able to find one more member by the end of the month."
    mc "... one more?"
    mc "I thought we needed four in total."
    male3 "About that..."
    male3 "I somehow convinced him that Akari is a legitimate member."
    male3 "So she counts."
    show male3 cast_blush
    male3 "It was embarrassing! All right!?"
    male3 "He called the middle school and bribed them for permission!"
    show male3 cast_angry
    male3 "Just be happy that it wasn't your pride that had to be thrown under the bus for this!!"
    mc "..."
    mc "Thanks Hiro."
    mc "You really did keep your word."
    show male3 cast_normal
    male3 "..."
    show male3 cast_happy
    male3 "Don't mention it."
    male3 ". . ."
    show male3 cast_blush
    male3 "I-I-I MEAN!!!"
    male3 "AHHHHHHH!!! FORGET WHAT I JUST SAID!!! JUST-JUST-JUST...!"
    male3 "AHHHHHHHHHHHHHHH!!!!"
    hide male3 with dissolve
    "And just like that, Hiro disappeared into the halls."
    play sound "audio/schoolchime1.wav"
    "It's time for class to start."
    stop music fadeout 1.0
    ##ts -------------------------------------------------
    scene ts some_time_later with fade
    pause
    ##ts ------------------------------------------------
    scene bg classroom with fade
    show ct_overlay
    show ct_wed
    show ct_345
    with dissolve
    mc "Hmmmm..."
    mc "Where should I go today?"
    mc "Kaoru seemed like he wanted to talk to me about something..."
    mc "but I have obligations with Hiro after school..."
    mc ". . ."
    mc "I wonder who should I visit first?"
    label choices14:

    menu:
        "{s}Visit Kaoru's office.{/s}":
            jump choices14
        "Visit Hiro's office.":
            jump choices14_common

    label choices14_common:
        mc "I think I'll go visit Hiro today."
        mc "Whatever Kaoru wanted to tell me can't be that important right?"
    play music "audio/houkago.mp3" fadein 1.0 volume 0.5
    scene bg hiro_office with fade
    show male3 cast_normal with dissolve
    male3 "And here we are."
    male3 "The office."
    male3 "..."
    male3 "I think we should start working on the club applications next."
    stop music fadeout 1.0
    ##ts ---
    scene ts some_time_later with fade
    pause
    ##ts -----
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg hiro_office with fade
    show ct_overlay
    show ct_wed
    show ct_430
    with dissolve
    show male3 cast_angry with dissolve
    male3 "What is wrong with these people?!?"
    male3 "Seriously?!?"
    male3 "The friendless anti-social club?!"
    male3 "What kind of loser came up with this idea?!"
    show male3 cast_annoyed
    male3 "I swear people just write these club applications just to annoy me!"
    mc "..."
    show male3 cast_normal
    male3 "Whats wrong Harumiya?"
    hide ct_430
    hide ct_wed
    hide ct_overlay
    with dissolve
    mc "Hiro..."
    male3 "?"
    mc "I've been thinking about this for a while..."
    male3 "???"
    male3 "What?"
    mc "Shouldn't we be on a first name basis?"
    male3 "What do you mean?"
    mc "I mean, everybody calls you Hiro, I don't usually refer to you by your surname."
    mc "So why not try calling me Haru for a change? We're friends aren't we?"
    show male3 cast_blush
    male3 "W-WH-WHA-WHA-WHAAAAAT?!?"
    male3 "I CAN'T JUST CALL YOU BY YOUR FIRST NAME OUT OF THE BLUE LIKE THAT!!!"
    show male3 cast_angry
    male3 "Calling a girl by her first name?! Who do you think I am?!? Kaoru?!"
    mc "Well, you call Naomi by her first name."
    show male3 cast_blush
    male3 "THATS DIFFERENT!!!"
    show male3 cast_angry
    male3 "I can't just call you Haru out of the blue like that!"
    mc "... you kinda just did."
    show male3 cast_blush
    male3 "AAAHHHHH!!!!"
    male3 "T-TH-THAT DOESN'T COUNT!!!"
    "I chuckled to myself for a bit."
    "Hiro gets so flustered over the smallest things."
    show male3 cast_normal
    male3 "Anyway, I think we should call it a day on the paperwork."
    male3 "We can finish it up another time."
    male3 "Its almost 5pm right?"
    male3 "Before the day is over I think we should go over some equations."
    male3 "I can't have you flunking on me while you are helping me out, its going to reflect bad on me."
    male3 "As the student council president, I have the responsibility of looking after my fellow students."
    male3 "We've got 25 minutes."
    play music "audio/classic timer.wav" fadein 1.0 volume 0.5
    scene bg blank with fade
    centered "Type the letters that pop up on the screen before the timer runs out."
    scene white with fade
    centered "{color=#000}Alright, you've better have had studied this time!{/color}"
    centered "{color=#000}Do you remember what the pythagorean theorem is?{/color}"
    scene mg trivia1 with fade
    show mg thinking with dissolve
    $ cont = 0 #continue variable
    $ arr_keys = ["z", "x", "c"] #list of keyboard inputs to be selected from. See https://www.pygame.org/docs/ref/key.html for more keys

    call qte_setup3(0.75, 0.75, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup3
    # "Function Call" - see label qte_setup for detail on "function"
    # in the above, I randomly select a key from a previously defined set of keys (arr_keys), and randomise the location

    $ counter = 0 #counter variable
    while cont == 1 and counter < 10:
        call qte_setup3(0.75, 0.75, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1) from _call_qte_setup3_1
        $ counter = counter + 1 #increment/increase the counter each time. When it reaches 10, it will exit the loop
        # to repeat the qte events until it is missed

    if counter == 10: #if we reached 10 rounds without missing
        scene mg trivia2
        stop music
        play audio "audio/success.wav"
        mc "a^2 + b^2 = c^2!"
        scene bg hiro_office with fade
        show male3 cast_normal with dissolve
        male3 "..."
        show male3 cast_happy
        male3 "Wow, you actually remembered something for once."
        jump trivia_end3
    else:
        scene mg trivia2
        stop music
        mc "ax^2 + bx + c = 0!"
        scene mg trivia4
        stop music
        play sound "audio/drop.mp3"
        male3 "WRONG!"
        centered "{nw}"
        show mg_guu with dissolve
        pause (1.5)
        scene bg hiro_office with fade
        show male3 cast_angry with dissolve
        male3 "My god..."
        male3 "You really are hopeless, aren't you?"
        jump trivia_end3

label qte_setup3(time_start, time_max, interval, trigger_key, x_align, y_align):
    $ renpy.block_rollback()
    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple

    $ cont = _return
    play sound "audio/tiktak.wav" volume 0.5
    # 1 if key was hit in time, 0 if key not
    return

    label trivia_end3:
    scene bg hiro_office with fade
    show male3 cast_normal with dissolve
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    male3 "..."
    male3 "Okay, I think we're done for today."
    mc "..."
    mc "Hiro?"
    male3 "... yes?"
    mc "I know I kinda already asked this but..."
    mc "Why does Naomi hate you?"
    male3 "..."
    mc "I know it's not really my place to say this but..."
    mc "What happened between you two?"
    male3 "... That's a difficult question for me to answer."
    male3 "Let me think..."
    mc "Do you like her?"
    show male3 cast_blush
    male3 "!!!"
    male3 "D-d-did..."
    male3 "Did you really just ask that?!"
    mc "Yes."
    mc "Yes I did."
    male3 "..."
    show male3 cast_normal
    male3 "(clears throat)"
    male3 "Yes."
    male3 "Yes I do... but..."
    mc "But what?"
    male3 "Look."
    male3 "It happened a long time ago."
    #ts -----
    scene bg blank with fade
    centered "1 year ago."
    #ts ----
    scene bg hiro_office with fade
    show bff sigh with dissolve
    bff "(sigh)"
    show bff worried
    bff "So what is it that you needed to tell me Hasehaka kun?"
    bff "I mean, Hasehasa..."
    bff "Hasegawa kun."
    hide bff
    show male3 normal
    male3 "Hiro."
    male3 "Please call me Hiro."
    hide male3
    show bff worried
    bff "Oh right..."
    bff "It was Hiro."
    hide bff
    show male3 normal
    male3 "..."
    male3 "Ok..."
    male3 "Give me a moment..."
    male3 ". . ."
    hide male3
    show bff worried
    bff "... What is it Hiro?"
    hide bff
    show male3 normal
    male3 "..."
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    show male3 blush
    male3 "FINE!!"
    male3 "I LIKE YOU! OKAY?!"
    play sound "audio/slap.wav"
    show flash red with dissolve
    pause(3.0)
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    scene bg hiro_office with fade
    show male3 cast_normal with dissolve
    male3 "She slapped me in the face..."
    mc "..."
    mc "Pfffft."
    show male3 cast_blush
    male3 "HEY!"
    male3 "DON'T LAUGH!"
    mc "Sorry."
    mc "It's just really funny."
    show male3 cast_normal
    male3 "It's just..."
    show male3 cast_worried
    male3 "I thought that Naomi was the one for me."
    male3 "She's perfect."
    male3 "She cares about everyone, not just the people around her."
    mc "The {b}one{/b} for {b}you{/b}, huh?"
    mc "I'm sorry, but that sounds cringe."
    show male3 cast_angry
    male3 "HEY!"
    mc "lol."
    mc "Just kidding."
    mc "I'm sure you'll be able to find someone that will cherish and appreciate you one day."
    mc "You might come off as strict but you're actually very thoughtful."
    show male3 cast_blush
    male3 "..."
    show male3 cast_happy
    male3 "Thanks."
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi hiro with dissolve
    show progress1 with dissolve
    pause 1.0
    show heart_progress2
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart from Hiro!{/size}"
    #ts ------
    scene bg blank with fade
    centered "After hearing Hiro open up, he seemed a lot more relaxed than usual."
    centered "Maybe Naomi was wrong about him after all."
    stop music fadeout 1.0
    scene ts the_next_day with fade
    pause
    ##ts --------
    scene bg classroom with fade
    play sound "audio/schoolchime1.wav"
    "It's time for lunch."
    "And Naomi is nowhere to be found still."
    male4 "HARUHARU HARU!!!!!!"
    mc "???"
    play sound "audio/nowav.mp3" fadein 1.0 volume 0.5
    scene bg school_hallway with fade
    show male4 happy with dissolve
    male4 "Hey there, Haru!"
    mc "..."
    mc "What is it this time Kaoru?"
    show male4 normal
    male4 "Oh, right."
    male4 "I had something I wanted to tell you the other day."
    male3 "Stop right there!" with vpunch
    show male4 scared
    male4 "!!!"
    hide male4
    show male3 cast_annoyed
    male3 "Kaoru! What do you think you're doing?!"
    show male3 cast_angry
    male3 "You're crazy if you think I'd let you run off with a girl by yourself!"
    show male3 cast_blush
    male3 "I-I-I mean!"
    show male3 cast_normal
    male3 "So what?"
    male3 "She has an obligation with me after school!"
    male3 "If she hangs out with you she's going to end up flunking the whole semester, all you do is mess around all day!"
    hide male3
    show male4 worried
    male4 "Hiro, since when did you ever worry about others?"
    show male4 blush
    male4 "I promise I'm not doing anything sketch, I just need to borrow her for a moment."
    hide male4
    show male3 cast_angry
    male3 "Borrow her?!"
    male3 "She's not a toy you can play with!"
    male3 "She's coming with me and that's settled!"
    hide male3
    show male4 worried
    label choices16:
    male4 "Y,know what, why not ask her then?"
    stop music
    scene cg duo fight with fade
    menu:
        "Kaoru.":
            jump choices16_common1
        "Hiro.":
            jump choices16_common1

    label choices16_common1:
    menu:
        "Kaoru.":
            jump choices16_common2
        "Hiro.":
            jump choices16_common2

    label choices16_common2:
        play sound "audio/error.wav"
        scene cg duo fight
        scene cg duo fight at glitch
        pause 0.2
        scene cg duo fight
    menu:
        "Kaoru.":
            jump choices16_common3
        "Hiro.":
            jump choices16_common3

    label choices16_common3:
        scene cg duo fight
        play sound "audio/error.wav"
        scene cg duo fight at glitch
        pause 0.2
        scene cg duo fight at chromatic_offset
        pause 0.15
        play sound "audio/error.wav"
        scene cg duo fight at glitch
        pause 0.2
        scene cg duo fight
        menu:
            "Ishida.":
                jump choices16_common4
            "Ishida.":
                jump choices16_common4
            "Ishida.":
                jump choices16_common4
    label choices16_common4:
        scene cg duo fight
        play sound "audio/error.wav"
        scene cg duo fight at glitch
        pause 0.2
        scene cg duo fight at chromatic_offset
        pause 0.15
        play sound "audio/error.wav"
        scene cg duo fight at glitch
        pause 0.2
        scene cg duo fight
        play sound "audio/static.wav"
        scene bg blank
        show static
        pause (3.0)
        scene bg blank
    centered "It's been a few weeks since Hiro disappeared."
    centered "..."
    centered "There is only one week left before we can find a new member for the art club."
    centered "But I haven't seen Nao for weeks."
    centered "I got a note in my locker from Kaoru..."
    centered "It looks like he wants to meet me under the school sakura tree."
    $ persistent.hiro = True
    $ achievement.grant("kaoru_achievement")
    $ achievement.sync()
    centered "Hiro's route ???/???"
    return

    label kaoru_route:
    stop music
    scene cg confession1 with fade
    mc "Kaoru?"
    mc "What did you call me out here for?"
    scene cg confession2 with fade
    pause (2.0)
    male4 "Haru.."
    male4 "Do you like me?"
    mc "..."
    mc "Uhm..."
    mc "I'm not really sure..."
    mc "I mean..."
    mc "(Oh my god...)"
    mc "(What do I say? What do I say?!)"
    scene bg blank with fade
    mc "I mean... I guess"
    mc "But do you think you can do me a small favor?"
    male4 "?"
    ##ts -------------------------------
    scene ts after_school with fade
    pause
    ##ts -------------------------------
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg artroom with fade
    show ct_overlay
    show ct_mon
    show ct_400
    with dissolve
    show male4 smug with dissolve
    male4 "What is this?"
    mc "Oh this?"
    mc "Well, I was wondering..."
    mc "If maybe you could join the art club?"
    show male4 glee
    male4 "Oh, that was your favor?"
    mc "...yea"
    mc "I mean you come here often."
    mc "You might as well join."
    show male4 blush
    male4 "Sorry, no can do."
    mc "Wait? What?"
    mc "Why?!"
    show male4 worried
    male4 "It conflicts with my schedule."
    male4 "I'm already wrapped up in my work."
    male4 "Being a part of the disciplinary committee isn't exactly a walk in the park, yknow?"
    mc "..."
    mc "Can you please think about it for a second?"
    mc "This club needs 4 members by the end of this week or else it will get disbanded."
    mc "I promised Naomi that I would get more members..."
    mc "It's not exactly easy doing it by myself..."
    mc "She's been gone for a few weeks now and I just don't know what to do."
    mc "Please?"
    mc "Its the one thing that I could do for her."
    show male4 blush
    male4 "(sigh)"
    male4 "If its that important, I guess I could help out."
    show male4 worried
    male4 "But, don't expect too much from me, alright?!"
    male4 "Now, is that all you needed?"
    mc "Yes."
    show male4 worried
    male4 "Alright then."
    show male4 excited
    male4 "By the way..."
    mc "?"
    male4 "Are you going to give me an answer any time soon?"
    mc "..."
    mc "I don't know how I feel about you yet, Kaoru..."
    show male4 normal
    male4 "Oh really?"
    male4 "Fair enough, I guess."
    mc "..."
    mc "I mean..."
    mc "Its not that I don't like you, {size=12}I do... I just...{/size}"
    show male4 excited
    male4 "YOU DO?!"
    mc "...nevermind, I didn't say anything!"
    show male4 glee
    male4 "Awe, Haru! Hasn't anyone told you how adorable you are?"
    show male4 excited
    male4 "You know that you're terrible at lying but you try to hide how you feel anyways!"
    mc "!!!"
    "Its not like he's good at lying himself either..."
    imt "Hello?"
    show male4 nervous with vpunch
    mc "???"
    play sound "audio/slide.mp3" volume 0.5
    mc "!!!"
    mc "Akari?!"
    hide male4 with dissolve
    hide ct_400
    hide ct_mon
    hide ct_overlay
    with dissolve
    show imt exp1 with dissolve
    imt "Hi."
    mc "Akari, what are you doing here?"
    mc "...and where's Nao?"
    show imt exp3
    imt "..."
    show imt exp2
    imt "That's what I've been meaning to ask you..."
    mc "What?"
    imt "Naomi hasn't come home in a few days."
    imt "I'm not even sure where she is."
    imt "I asked my mom and my step-dad about her too..."
    imt "But for some reason they act like everything is fine and they keep avoiding my questions."
    mc "Why would they do that?"
    show imt exp4
    imt "I'm not sure..."
    imt "To be honest, my mom and Naomi don't get along."
    show imt exp1
    imt "It doesn't seem like they want to find her."
    imt "..."
    show imt exp2
    imt "I don't know what to do."
    "Akari looked serious."
    "At the time I had so many questions on my mind."
    "Did Naomi get into a fight or something with her family?"
    "Is she okay?"
    "Where did she go?"
    "At that moment I just remember feeling like I wasn't sure what to do..."
    "But I could never forget the look on her face."
    mc "Anyway... Akari, say hello to our new member today."
    show imt exp1
    imt "Kaoru?!"
    imt "You're gonna join the art club too?"
    hide imt
    show male4 happy
    male4 "Akari!!!!!"
    male4 "Did ya bake any cookies today?"
    hide male4
    show imt exp1
    imt ". . ."
    imt "No..."
    hide imt
    show male4 glee
    male4 "Next time bake cookies for me when you come!"
    show male4 blush
    male4 "Y,know I love those! Your cookies are the best!"
    show male4 happy
    male4 "{size=14}In exchange I'll tell you how to get to ikemen senpai's route.{/size}"
    mc "...?"
    show male4 scared
    male4 "Oh!"
    show male4 nervous
    male4 "Sorry, just ignore what I just said."
    show male4 normal
    male4 "Anyway, I'm here for the art competition."
    hide male4
    show imt exp2
    imt "Wait... we're having another competition again?"
    mc "Excuse me?"
    mc "I'm sorry but I'm with Akari on this one."
    mc "Who said we were having {b}ANOTHER{/b} art competition?"
    hide imt
    show male4 glee
    male4 "I did!"
    male4 "Okay guys! Get your pencils, pens, and brushes ready! Today's topic is fan art!!!"
    mc "..."
    show male4 happy
    male4 "Lets begin!"
    mc "Wait Kaoru..."
    mc "Fan art of what exactly?"
    show male4 excited
    male4 "OTOME LEGENDS of course!"
    show male4 blush
    male4 "No fan art is true fan art unless it is otome legends fan art."
    show male4 glee
    male4 "Cmon guys! Lets start!"
    stop music fadeout 1.0
    scene bg blank with fade
    centered "After some time..."
    play music "audio/nowav.mp3" volume 0.5 fadein 1.0
    scene bg artroom with fade
    show male4 excited with dissolve
    male4 "Alright guys! Show me what you got!"
    male4 "Haru! Show me yours first!!!"
    show male4 glee
    male4 "Lemme see! Lemme see!"
    hide male4 with dissolve
    scene bg artroom with dissolve
    show art_drawing0 with dissolve
    pause
    hide art_drawing0 with dissolve
    show male4 nervous with dissolve
    male4 "..."
    mc "..."
    male4 ". . ."
    male4 "Haru..."
    show male4 scared
    male4 "Why is your canvas completely blank still?"
    mc "..."
    mc "Yea, I know..."
    mc "Sorry, I couldn't think of anything to paint."
    show male4 blush
    male4 "Oh, its ok. Don't worry about it too much."
    show male4 happy
    male4 "Okay, now next is Akari."
    male4 "Akari, who did you draw?"
    hide male4 with dissolve
    scene bg artroom with dissolve
    show art_drawing4 with dissolve
    pause
    hide art_drawing4 with dissolve
    show male4 scared
    male4 "..."
    male4 "Akari..."
    show male4 nervous
    male4 "What is this?"
    hide male4
    show imt exp2
    imt "My drawing."
    hide imt
    show male4 nervous
    male4 "Right..."
    mc "Kaoru."
    show male4 normal
    male4 "Yes?"
    mc "Why don't you show us your art?"
    show male4 nervous
    male4 ". . ."
    male4 "Oh I didn't make anything."
    mc "But you were painting on a canvas the entire time..."
    show male4 scared
    male4 "Oh that?!"
    male4 ". . ."
    show male4 nervous
    male4 "I was just practicing my... uhh. . ."
    show male4 scared
    male4 "POSTURE!"
    male4 "It's nice to practice holding the brush!"
    mc ". . ."
    mc "But there was paint on the brus-{nw}"
    male4 "PAINT!?" with vpunch
    male4 "Oh?! That wasn't paint! I was just moving the brush so fast that you could see colors!"
    show male4 nervous
    male4 "It's an optical illusion!"
    hide male4
    show imt exp1
    imt "I love optical illusions."
    hide imt
    show male4 nervous
    male4 ". . .yea, sure."
    mc "It can't be that bad."
    show male4 scared
    male4 "No! Wait! Don't look!"
    hide male4 with dissolve
    scene bg artroom with dissolve
    show art_drawing5 with dissolve
    pause
    "Fanart by Nokodox!"
    centered ""
    hide art_drawing5 with dissolve
    show male4 blush with dissolve
    male4 ". . ."
    mc ". . ."
    male4 "You weren't supposed to see that."
    hide male4
    show imt exp2
    imt "Theres a 2nd one..."
    mc "A second one!?"
    mc "When did he have the time to paint anoth-{nw}"
    hide imt
    show male4 scared
    male4 "NO! STOP!!"
    male4 "ANYTHING BUT THAT!"
    hide male4 with dissolve
    scene bg artroom with dissolve
    show art_drawing6 with dissolve
    pause
    hide art_drawing6 with dissolve
    show male4 worried
    male4 ". . ."
    mc "..."
    mc "Kaoru, what is thi-{nw}"
    hide male4
    show imt exp1 with vpunch
    imt "I know!"
    imt "It's the Matsugelisa!"
    mc "..."
    "This is some new level of cringe I am observing."
    hide imt
    show male4 nervous
    male4 "Anyway..."
    stop music fadeout 1.0
    scene bg blank with fade
    ##ts —-----------------------
    scene ts some_time_later with fade
    pause
    ##ts —------------------------
    play music "audio/rainloop.wav" fadein 1.0 volume 0.5
    scene bg blank with fade
    "After hanging out in the artroom, it was time for us to head home."
    "Akari had already went ahead of us and walked home by herself."
    "All I remember is that it was a rainy afternoon."
    "I thought I was going home alone but then..."
    mc "(I could've sworn that I brought my umbrella with me today.)"
    male4 "Haruharu Haruuuuu!!!!"
    mc "???"
    scene bg rain
    show cg aiaigasa1
    with fade
    male4 "So how are you doing?"
    mc "..."
    show cg aiaigasa3 with dissolve
    male4 "Y,know, I'm really sorry about what happened earlier."
    male4 "You really shouldn't have seen that."
    show cg aiaigasa5
    male4 "No, really..."
    show cg aiaigasa4
    male4 "Hahaha..."
    mc "..."
    mc "Kaoru, you have the same umbrella as I do..."
    show cg aiaigasa5
    male4 "Oh really?"
    show cg aiaigasa2
    male4 "I guess great minds do think alike."
    show cg aiaigasa3
    male4 "Haha!"
    mc "I guess."
    scene bg rain with fade
    show cg aiaigasa7 with dissolve
    pause (4.0)
    mc "..."
    "Even though I was under an umbrella, my shoulder felt very wet."
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi kaoru with dissolve
    show progress0 with dissolve
    pause 1.0
    show heart_progress1
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart from Kaoru!{/size}"
    scene bg blank with fade
    centered "It's strange not having Naomi around."
    centered "She probably would've done the same thing."
    centered "I do have a habit of always losing my umbrella."
    centered "Though I was pretty sure that today I brought mine..."
    centered "There was a pretty rough storm today."
    centered "I couldn't see much in the rain."
    centered "There were rain puddles and tree branches everywhere."
    centered "Even amongst all the chaos, I feel reassured that Kaoru is here with me."
    centered "Or at least, I feel like thats how I'm supposed to feel..."
    male4 "!!!" with vpunch
    mc "What is it, Kaoru?"
    male4 "Oh! It's just..."
    male4 "Wait a sec, let me adjust the umbrella."
    male4 "The wind is a bit strong so I'm putting it away for a second."
    "Kaoru collapses the umbrella and puts it in his pocket."
    male4 "Its so hard to see."
    male4 ". . ."
    male4 "The puddles here are deep..."
    male4 "I think we should head in the other direction."
    male4 "Try not to get your shoes wet, okay?"
    mc "Okay?"
    stop music
    scene cg catastrophe1 with fade
    play sound "audio/horror_drum.wav"
    pause
    play sound "audio/zap.mp3" volume 0.5
    mc "Uhm... Kaoru, did you hear something just now?"
    male4 "No? I don't think so?"
    mc "..."
    mc "Nevermind."
    ##ts -------------------------------------------
    scene ts some_time_later with fade
    pause
    #ts --------------------------------------------
    play music "audio/rainloop.wav" fadein 1.0 volume 0.5
    scene bg rain with fade
    show cg aiaigasa2 with dissolve
    male4 "Anyway..."
    male4 "Theres been a lot of things going on lately."
    show cg aiaigasa3
    male4 "I mean, next year, we're all going to be seniors."
    male4 "Its almost time for final exams."
    show cg aiaigasa5
    male4 "I'm not sure if I'm prepared, I'm actually pretty nervous."
    male4 "I think next year I'm gonna take it easy and stop being president of the disciplinary committee."
    show cg aiaigasa2
    male4 "The first year wasn't so bad because my friends were willing to help out."
    show cg aiaigasa5
    male4 "But now it kinda feels like I'm the only one running stuff."
    show cg aiaigasa3
    male4 "It kind of gets exhausting after a while, y,know?"
    mc "..."
    mc "That sounds pretty rough."
    show cg aiaigasa5
    male4 "Yeah, no joke."
    male4 "I usually don't have any problems in school but lately its been stressful finishing my work and focusing on final exams at the same time."
    show cg aiaigasa2
    male4 "But can you believe its already been a year?!"
    male4 "I've been so hung up on work I haven't even figured out what I was going to do this spring break."
    show cg aiaigasa3
    male4 "Like.. theres just so many things that I want to do before I die."
    mc "What?"
    show cg aiaigasa5
    male4 "Oh! Nothing!"
    show cg aiaigasa3
    male4 "Do you got any plans?"
    mc "..."
    mc "Other than stay inside and watch webbflix all day, no."
    show cg aiaigasa4
    male4 "Haha, its ok."
    male4 "I haven't figured it out either."
    show cg aiaigasa6
    male4 "Oh!"
    show cg aiaigasa3
    male4 "Nevermind! We're already here!"
    scene bg konbini with fade
    show male4 normal with dissolve
    male4 "We're here at the convenience store."
    show male4 glee
    male4 "Go ahead, I'm sure they have umbrellas inside."
    #ts ------------------
    scene ts some_time_later with fade
    pause
    #ts ------------------
    scene bg konbini with fade
    show male4 happy with dissolve
    male4 "Oh? You already got your umbrella?"
    male4 "Do you mind if you let me look at it really quick?"
    show male4 glee
    male4 "Here, hold mine for a bit."
    show male4 normal
    male4 "..."
    show male4 happy
    male4 "Thanks for buying me an umbrella, I'll cya later."
    hide male4 with dissolve
    mc "..."
    mc "(Wait... this is my umbrella...)"
    mc ". . ."
    mc "(He just tricked me into buying him one didn't he?)"
    mc "..."
    mc "(What a jerk.)"
    stop music fadeout 1.0
    ##ts --------------------------------
    scene ts home with fade
    pause
    ##ts ---------------------------------
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg bedroom_yoru with fade
    mc "..."
    mc "I can't believe that guy!"
    mc "How come I didn't notice it earlier?!"
    mc "I knew that I didn't lose my umbrella!"
    mc "Why didn't I realize it sooner?!"
    mc "If only I wasn't so stupid..."
    mc "I wonder what goes on through his mind anyways."
    mc "Maybe some otome games will help me understand what goes on through a guys mind."
    mc "Nah."
    mc "That sounds cliche."
    mc "Its not like anything that happen in these dumb otome games happen in real life."
    mc "..."
    mc "But now that I think about it..."
    mc "Maybe it can...?"
    mc "Nevermind... what am I thinking?"
    mc "Thats a stupid idea."
    mc "As if Otomes ever reflect what happens in real life."
    mc "..."
    mc "Well, I'm bored anyways so I might as well."
    centered "{nw}"
    stop music fadeout 1.0
    show bsb_blank with dissolve
    pause (1.0)
    scene bg bsb_blank with dissolve
    pause
    play sound "audio/unlock.wav"
    scene bg bsb_on
    show senpai matsuge
    senpai2 "HOHOHOHOHO!"
    play music "audio/bsbtheme.mp3"
    scene cg matsuge horserider with fade
    senpai2 "What a beautiful day."
    senpai2 "It's the perfect day to ride my beautiful horse."
    senpai2 "LUCY! COME HERE!!"
    scene cg matsuge camel with fade
    senpai2 "There you are my beloved Lucy!"
    senpai2 "Here! Have a rose for your fabulous mouth!"
    "Matsuge senpai is having the time of his life with his so called \"horse\" ..."
    "But you're pretty sure that's a camel, not a horse..."
    stop music
    play sound "audio/unlock.wav"
    scene bg bsb_blank
    centered "{nw}"
    pause (3.0)
    mc "{cps=3}. . .{/cps}"
    mc "You know what, nevermind, I regret my life choices."
    stop music fadeout 1.0
    ##ts --------------------------------------------------------
    scene ts the_next_day with fade
    pause
    ##ts --------------------------------------------------------
    scene bg blank with fade
    centered "It took me a while to arrive, but I managed to barely make it to class on time."
    centered "Though..."
    centered "Something felt off..."
    centered "On my way to class I could've sworn that I caught a glimpse of a few people giggling and smiling at me."
    centered "But it didn't become to clear to me what was going on..."
    centered "That was, until I opened the classroom door."
    stop music
    play sound "audio/horror_drum.wav"
    scene bg blank
    show cg crowd1
    show laugh1 with dissolve
    pause (1.5)
    play sound "audio/horror_drum.wav"
    scene bg blank
    show cg crowd2
    show laugh2 with dissolve
    pause (1.5)
    scene bg blank
    pause (2.0)
    play sound "audio/tinnitus.mp3" fadein 3.0
    scene cg crowd3 with fade:
        truecenter zoom 1.0 rotate 0 subpixel True
        ease 8.0 zoom 2.5 rotate 0.0
    pause (10.0)
    scene white with fade
    pause (3.0)

    play sound "audio/paper.wav"
    show handrawn hello
    pause
    play sound "audio/paper.wav"
    show handrawn name
    pause
    play music "audio/ponder_ost.mp3" fadein 4.0 volume 0.5
    play sound "audio/paper.wav"
    scene handrawn1
    pause
    "As long as I could remember I was always a shy and timid person."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn2
    pause
    "Even when I was in elementary school I would always play by myself because I was too shy to talk to anyone."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn3
    pause
    "And sometimes it felt like I was never even there."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn4
    pause
    "I noticed that other kids were playing their toys in groups."
    "I thought that maybe the reason kids didn't wanna play with me was because they weren't interested in my toys."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn5
    pause
    "So I asked the other kids if I could play with them."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn6
    pause
    "Unfortunately for me though it didn't go too well."
    "And eventually, I stopped trying and thought it would've been best to stick by myself."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn7
    pause
    "In middle school though, things got worse."
    "I thought no one would bother me as long as I never talked to them."
    "But I guess people thought it would've been funny to pick on the quiet girl."
    "I just remember that it happened too many times."
    "Scratches and marks on my desk..."
    "Crumbled up paper thrown at my face..."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn8
    pause
    "There was even one time... where I walked into the art room and I got paint splattered all over my face."
    centered "{nw}"
    play sound "audio/paper.wav"
    scene handrawn9
    pause
    "To them it was all fun and games..."
    "But to me it wasn't very funny."
    play sound "audio/paper.wav"
    scene handrawn10
    pause
    "Even to this day I still have a hard time socializing with people."
    "I thought that I could leave middle school behind..."
    "But it feels as if my past is coming back to haunt me again."
    centered "{nw}"
    scene white with dissolve
    pause (2.0)
    centered "{color=#000000}Sometimes I wish that I didn't have to exist.{/color}"
    centered "{color=#000000}Why did I ever think that people would like me?{/color}"
    centered "{color=#000000}This is what I get for trying to make friends.{/color}"
    centered "{color=#000000}If only I kept to myself, I wouldn't have to get into any trouble.{/color}"
    centered "{color=#000000}I wouldn't have gotten anyone else in trouble either.{/color}"
    centered "{color=#000000}Afterall..."
    centered "{color=#000000}The world would be just fine without me."
    centered "{nw}"
    stop music
    pause (3.0)
    play sound "audio/doorslide.wav"
    scene bg blank
    pause (1.0)
    play music "audio/running1.wav"
    pause (4.0)

    stop music
    scene bg blank
    mc "!!!" with vpunch
    male4 "Hey."
    play music "audio/uncanny.mp3" fadein 1.0 volume 0.5
    mc "..."
    male4 "Whats wrong?"
    centered "{nw}"
    scene bg past2 with fade
    show male4 normal with dissolve
    male4 "Are you ok?"
    mc "Kaoru."
    show male4 glee
    male4 "Yes sweetheart?"
    mc "Can you stop with that?"
    male4 "With what?"
    mc "I want nothing to do with you!!"
    show male4 nervous
    male4 "???" with vpunch
    male4 "Come again?"
    mc "YOU'RE AN ABSOLUTE SCUMBAG!" with vpunch
    mc "Do you think I'm stupid?!"
    mc "IT WAS A STUPID PRANK WASN'T IT!?"
    mc "I don't know WHY I actually thought you were a decent guy!" with vpunch
    mc "What's wrong with you?!"
    mc "You embarrassed me in front of everyone!"
    show male4 scared
    male4 "Oh, cmon Haru! You know that was just a joke right?"
    male4 "Maybe have a sense of humor?"
    mc "HAVE A SENSE OF HUMOR?!?!" with vpunch
    show male4 nervous
    male4 "Sorry! That's not what I exactly meant!"
    mc "Leave me alone!"
    show male4 blush
    male4 "W-w-wait!"
    show male4 worried
    male4 "Haru, I can explain!"
    stop music fadeout 1.0
    scene bg blank with fade
    centered "{size=30}A few moments later{/size}"
    scene bg school_clinic with fade
    play sound "audio/schoolchime2.wav"
    pause (12.0)
    mc "{cps=3}. . .{/cps}"
    show ct_overlay
    show ct_tues
    show ct_845
    with dissolve
    "The school bell rang."
    mc "(Even after I got to school on time...)"
    mc "(Why do I even bother?)"
    mc "(It's not like I care about school anyway.)"
    play sound "audio/slide.mp3" volume 0.5
    mc "!!!"
    show male4 worried with dissolve
    male4 "Oh my gosh, there you are!"
    hide ct_overlay
    hide ct_tues
    hide ct_845
    with dissolve
    show male4 blush
    male4 "What are you doing in here?"
    male4 "The bell rang already silly, you're supposed to be in class."
    mc "..."
    show male4 worried
    male4 "Look."
    male4 "I'm sorry."
    male4 "I didn't know it would make you {b}that{/b} {size=15}upset.{/size}"
    show male4 blush
    male4 "But could you please explain to me what happened back there?"
    male4 "I'm a bit lost."
    mc "..."
    label choices17:
    menu:
        "It's nothing...":
            jump choices17_a
        "Since when did you care?":
            jump choices17_b
        "Do you really not know?":
            jump choices17_c

    label choices17_a:
        mc "It's nothing..."
        show male4 worried
        male4 "Oh, come on."
        show male4 blush
        male4 "You have to be upset about something, just tell me about it."
        mc "..."
        mc "Did you have anything to do with it?"
        show male4 worried
        male4 "With what?"
        mc "That so called \"prank\" you pulled on me yesterday."
        mc "Everyone was laughing at me."
        mc "Do you really think I'm that stupid?"
        mc "You set me up!"
        mc "The confession was fake!"
        show male4 nervous
        male4 "..."
        male4 "Wait, so you're not mad about the umbrella?"
        mc "NO!"
        male4 "... oh..."
        show male4 blush
        male4 "Then I'm glad."
        mc "WHAT!?!"
        show male4 scared
        male4 "Wait, wait, wait! No thats not what I meant!"
        show male4 worried
        male4 "I mean I'm sorry, just..."
        show male4 blush
        male4 "(sigh)"
        male4 "Was what they did that serious?"
        mc "What?!"
        show male4 blush
        male4 "They told me that all they were gonna do was joke about it a little."
        male4 "I didn't think they would go that far."
        mc ". . ."
        mc "Do you really expect me to forgive you that easily?"
        jump choices17_common

    label choices17_b:
        mc "Since when did you care?"
        show male4 worried
        male4 "..."
        male4 "What do you mean?"
        male4 "Of course I care about you."
        mc "Then why did you do that?"
        male4 "Do what?"
        mc "Set me up so that everyone could make fun of me!"
        mc "It was a prank!"
        mc "Do you think I like to be a laughing stalk?"
        show male4 nervous
        male4 "..."
        male4 "What?"
        mc "Don't play dumb!"
        show male4 blush
        male4 "Wait, wait, time out!"
        show male4 worried
        male4 "Are you talking about the umbrella?"
        male4 "I'm really sorry, I promise I'll pay you back!"
        mc "I WAS TALKING ABOUT THAT DUMB FAKE CONFESSION YOU IDIOT!"
        show male4 scared
        male4 "..."
        male4 "The confession!?!?"
        mc "What else would I be talking about?!"
        show male4 blush
        male4 "(sigh)"
        male4 "Look, I..."
        male4 "I didn't know that they were gonna make fun of you like that."
        mc "Do you really expect me to believe that?!"
        jump choices17_common

    label choices17_c:
        mc "Do you really not know?"
        show male4 worried
        male4 "Know what?"
        mc "That confession you did the other day."
        mc "It was a prank, wasn't it?"
        mc "You lied to me..."
        mc "You're such a jerk!"
        show male4 blush
        male4 "Haru..."
        male4 "Did it really mean that much to you?"
        mc "I don't want to talk about it anymore."
        mc "Because of you, I'm the laughing stalk of the whole class."
        mc "Whats wrong with you?"
        show male4 worried
        male4 "Wait..."
        male4 "Is that what happened?"
        male4 "They told me that it was just a harmless little joke."
        male4 "Those people weren't your friends?"
        mc "Are you stupid?"
        show male4 blush
        male4 "Yes."
        male4 "I'll have you know that I am very stupid."
        show male4 glee
        male4 "So you're not mad about the umbrella right?"
        mc "???"
        show male4 blush
        male4 "Okay, sorry, sorry!"
        jump choices17_common

    label choices17_common:
    show male4 worried
    male4 "..."
    male4 "No."
    mc "..."
    show male4 blush
    male4 "I'm sorry, I didn't mean to hurt you, I just..."
    male4 "Look."
    male4 "I'll make it up to you."
    mc "... How?"
    show male4 nervous
    male4 "..."
    show male4 scared
    male4 "I actually don't know."
    show male4 normal
    male4 "But I do have one thing in mind."
    mc "Like what?"
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    show male4 excited
    male4 "You can transfer classes with me!"
    mc "..."
    mc "And how is that going to make things any better?"
    show male4 happy
    male4 "Because next time they mess with you! I can write them up!"
    mc "..."
    mc "Kaoru..."
    male4 "Yes dear?"
    mc "Do you actually do your job?"
    show male4 scared
    male4 "..."
    male4 "I can if I feel like it..."
    mc "Pfft!"
    show male4 nervous
    male4 "What are you laughing for?"
    mc "Thats just funny, lol"
    mc "I mean, okay, sure."
    mc "Do you really think it will make things better though?"
    show male4 happy
    male4 "Of course."
    male4 "I'm sure it will!"
    show male4 glee
    male4 "And you better get back to class!"
    show male4 normal
    male4 "I wrote a hall pass for you just incase."
    scene bg blank with fade
    centered "Yeah, right..."
    centered "As if he could make it up to me."
    centered "Sometimes I wonder why Kaoru does the things he does."
    centered "Is he just pretending to be nice to me...?"
    centered "Why would he...?"
    centered "I don't understand."
    centered "Maybe Hiro was right, he's just messing with my feelings isn't he?"
    centered "What does he get out of it anyway?"
    centered "Am I over thinking things?"
    centered "Why do I have to be so confused."
    stop music fadeout 1.0
    #ts ------------------------------
    scene ts after_school with fade
    pause
    #ts ----------------------------------
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg artroom with fade
    mc "..."
    mc "(Kaoru sure is strange...)"
    mc "(Maybe he's not so bad afterall...)"
    show ct_overlay
    show ct_tues
    show ct_400
    with dissolve
    pause (2.0)
    play sound "audio/slide.mp3" volume 0.5
    mc "!!!" with vpunch
    male4 "Heya!"
    show male4 happy with dissolve
    male4 "Do you always hang out in here after school?"
    mc "... maybe?"
    show male4 normal
    male4 "Soooo."
    mc "So what?"
    male4 "I dunno."
    show male4 glee
    male4 "I've been tryna figure out a way to break the ice."
    mc "Riiiight."
    mc ". . ."
    mc "You've been hanging out here alot lately..."
    mc "Don't you have anything else better to do?"
    show male4 happy
    male4 "Woah, look who's fiesty."
    male4 "You're the one that asked me to join in the first place."
    mc "I guess..."
    show male4 glee
    male4 "But in a sense you are right."
    male4 "I usually spend my time bothering Hiro."
    male4 "But I'm not quite sure how he's been lately."
    show male4 worried
    male4 "It's weird, he kind of just disappeared."
    mc "I see."
    show male4 smug
    male4 "You're not much of a talker are you?"
    mc "I guess you could say that."
    mc "It's just..."
    mc "I feel like this have been going a bit too fast for me lately."
    mc "I'm no good at school."
    mc "My best friend is suddenly gone..."
    mc "And I thought I finally found another friend other than Naomi."
    mc "I thought everything was going well but... its all been too confusing."
    mc "But I feel like everyone around me in my life has been disappearing..."
    mc "And theres nothing I can do about it."
    show male4 blush
    male4 "That sounds pretty rough."
    male4 "But you do know, you have one thing going for you."
    mc "Like what?"
    stop music
    show male4 happy
    male4 "Well..."
    male4 "You have me."
    mc "{cps=3}. . .{/cps}{nw}"
    play sound "audio/vibrate.wav"
    show male4 nervous
    male4 "!!!"
    show male4 scared
    male4 "Thats a call from my mom I have to pick up!"
    male4 "Sorry! Gotta go!"
    hide male4 with dissolve
    mc "..."
    mc ". . ."
    mc "(What did he mean by that?)"
    stop music fadeout 1.0
    ##ts -----
    scene ts home with fade
    pause
    ##ts ------
    scene bg bedroom_yoru with fade
    mc "Back at home at last."
    mc "It's been a long day."
    mc "..."
    mc "Naomi hasn't answered her phone for weeks now..."
    mc "I still haven't returned her game back yet..."
    centered "{nw}"
    show bsb_blank with dissolve
    pause (2.0)
    mc "Huh...?"
    mc "That's strange..."
    mc "It won't turn on."
    mc "..."
    mc "Oh no..."
    mc "What am I gonna tell Nao?!"
    mc "..."
    mc "I'm just going to call it a day and go to sleep."
    mc "... wait"
    scene bg bsb_blank with dissolve
    pause (1.0)
    play sound "audio/unlock.wav"
    scene bg bsb_on
    pause (2.0)
    mc "Why did it turn on by itself?"
    pause (1.0)
    play music "audio/static.wav"
    scene bg blank
    scene static
    show bg bsb_transparent
    pause (4.0)
    stop music
    play sound "audio/glitch.wav"
    show bsb_glitch
    $ renpy.pause(4.0, hard=True)
    centered "{w=4.0}{nw}"
    play sound "audio/beep.wav"
    scene bsb_cursed
    $ renpy.pause(7.0, hard=True)
    centered "{w=7.0}{nw}"
    scene bg blank
    pause (2.0)
    play sound "audio/ehe.mp3" fadein 1.0 volume 0.5
    pause (1.0)
    scene bg blank
    show moteko sketch with fade
    shoujo1 "Hello there."
    shoujo1 "Long time no see."
    shoujo1 "I think its time for you to wake up now."
    shoujo1 "You know that you can't stay in this reality forever."
    shoujo1 "And from this point on..."
    $ renpy.block_rollback()
    shoujo1 "You can't turn back.."
    shoujo1 "After all..."
    shoujo1 "All good things must come to an end."
    shoujo1 "You should know that already, right?"
    shoujo1 "{color=f44336}Chiharu Chan.{/color}{nw}"
    stop sound
    play music "audio/static.wav"
    scene bg blank
    show static
    $ renpy.pause(4.0, hard=True)
    centered "{w=4.0}{nw}"
    stop music
    scene bg bedroom_asa
    mc "..."
    mc "I can't quite remember what happened last night."
    mc "What time is it?"
    mc "!!!" with vpunch
    mc "It's already this late?!"
    scene bg blank with fade
    centered "The next day I got a letter in my locker from Kaoru."
    centered "He wants me to meet him in the art room during lunch"
    centered "I think he knows something about Naomi.."
    centered "Maybe he knows something about that I don't..."
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg artroom with fade
    show ct_overlay
    show ct_wed
    show ct_105
    with dissolve
    show male4 normal with dissolve
    male4 "Hello Haru."
    mc "..."
    mc "What is it Kaoru?"
    male4 "Here, I wanted to give you this first."
    play sound "audio/unlock.wav"
    centered "{nw}"
    show ichigopan
    pause
    mc "!!!"
    mc "It's a strawberry bread!"
    hide ichigopan
    show male4 worried
    male4 "I'm... really sorry about the other day."
    mc "???"
    male4 "About embarrassing you and all."
    male4 "Lets just say a couple of kids asked me to do them a little \"favor.\""
    show male4 blush
    male4 "{size=18}They know my secret...{/size}"
    hide ct_overlay
    hide ct_wed
    hide ct_105
    with dissolve
    mc "..."
    mc "Fine."
    mc "I guess I can forgive you."
    mc "Anyway? Is that what you called me here for?"
    mc "What about Naomi?"
    show male4 nervous with vpunch
    male4 "Oh! T-t-th-that!"
    show male4 scared
    male4 "Naomi!"
    male4 "YES! How can I forget about Naomi?"
    show male4 worried
    male4 "Ok, Haru. Listen very closely."
    mc "?"
    play music "audio/run.mp3" fadein 1.0 volume 0.5
    show male4 scared:
        ease 1.5 zoom 1.5 xoffset -550 yoffset 350

    male4 "Look!"
    show bg blank behind male4 with dissolve
    male4 "There's something up with Naomi."
    male4 "I mean..."
    male4 "You know she blinks right?!?"
    show male4 scared:
        zoom 2.5 xalign 0.65 yalign 0.38
    male4 "YOU KNOW THAT SHE BLINKS RIGHT?!?"
    male4 "I mean, don't you think it's suspicious?!"
    male4 "Ishida suddenly disappeared."
    male4 "Hiro just suddenly vanished."
    male4 "Y,know the other day..."
    male4 "I went to Wacdonalds..."
    male4 "And the ice cream machine was actually working."
    male4 "It's all too suspicious."
    male4 "Please tell me it's not just me, right?!"
    male4 "It's not just me, right?!?"
    stop music
    play sound "audio/vibrate.wav"
    show male4 nervous
    male4 "!!!" with vpunch
    scene bg artroom
    show male4 nervous
    with fade
    male4 ". . ."
    male4 "I have to go..."
    show male4 normal
    male4 "Oh, by the way Haru."
    show male4 worried
    male4 "I wouldn't touch the bsb ever again if I were you."
    male4 "That thing's dangerous."
    hide male4 with dissolve
    "Kaoru disappears into the hallway."
    mc ". . ."
    mc "What was that all about?"
    ##ts ------------------------------
    scene bg blank with fade
    centered "{size=34}Class{/size}"
    ##ts -----------------------------
    play sound "audio/chalkboard.wav" fadein 1.0 volume 0.5
    scene bg classroom with fade
    "Sensei" "Alright class, today we'll be going over quadratic equations."
    "Sensei" "So are there any volunteers for the first question?"
    stop sound fadeout 1.0
    mc "(This class is so boring...)"
    mc "(I will rip my brain out if I have to listen to this teacher any longer.)"
    mc "(I'm just gonna draw and pretend to write notes instead.)"
    mc "(It's a good thing that this is the last class of the day.)"
    mc "(I can finally go home after this.)"
    "(The teacher continues to lecture the class while you open your notebook to draw)"
    label rollthedice:
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    scene bg blank with fade
    centered "{size=30}Hi{/size}"
    centered "{size=30}So uh...{/size}"
    centered "{size=30}Here is a minigame I had to come up with because we ran out of budget for the game.{/size}"
    centered "{size=30}...{/size}"
    centered "{size=30}So I'm thinking of a number between 1-6.{/size}"
    centered "{size=30}Do you think you could guess what it is?{/size}"
    default guess_num = None
    default dice_num = None
    $ guess_num = renpy.random.randint(1,6)
    menu:
        "Yes":
            centered "{size=30}Oh thats great then.{/size}"
            jump guessinggame
        "No":
            centered "{size=30}Oh...{/size}"
            centered "{size=30}Welp, I guess we're going back to the game then.{/size}"
            jump guessinggame_after

    label guessinggame:
    centered "{size=30}Okay so you're gonna roll the dice to get the number I'm thinking of.{/size}"
    screen rolling_dice:
        textbutton _("{size=50}ROLL THE DICE{/size}") xalign 0.5 yalign 0.5 focus_mask True action Jump("dice_guessing") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/menu_click.mp3"
    call screen rolling_dice

    label dice_guessing:
    $ die_num = renpy.random.randint(1,6)

    if die_num == 1:
        show die1 with dissolve
        pause
    if die_num == 2:
        show die2 with dissolve
        pause
    if die_num == 3:
        show die3 with dissolve
        pause
    if die_num == 4:
        show die4 with dissolve
        pause
    if die_num == 5:
        show die5 with dissolve
        pause
    if die_num == 6:
        show die6 with dissolve
        pause

    if die_num == guess_num:
        "YOU WIN!!!"
        "You rolled a [die_num]"
        "Which matches my guess, [guess_num]."
        "Hehe."
    else:
        "Sorry, you lose."
        "You rolled a [die_num]."
        "You were supposed to roll a [guess_num]"
    scene bg blank with fade
    centered "{size=30}Yay that was fun.{/size}"
    centered "{size=30}Okay, now its time to get back to the game.{/size}"

    label guessinggame_after:
    $ achievement.grant("budget_achievement")
    $ achievement.sync()
    stop music fadeout 1.0
    play sound "audio/schoolchime1.wav"
    scene bg classroom with fade
    show ct_overlay
    show ct_wed
    show ct_400
    with dissolve
    "Class is over."
    mc "(Finally, now I can relax.)"
    mc "(I'm gonna head to the art room before going home.)"
    mc "(I wonder if anyone's gonna visit today.)"
    hide ct_overlay
    hide ct_wed
    hide ct_400
    with dissolve
    stop sound fadeout 1.0
    ##ts --------------------------------------------
    scene ts after_school with fade
    pause
    #ts ---------------------------------------------
    play music "audio/houkago.mp3" fadein 1.0 volume 0.5
    scene bg artroom with fade
    play sound "audio/slide.mp3" volume 0.5
    mc "..."
    mc "Kaoru?"
    mc "What are you doing here?"
    show male4 normal with dissolve
    male4 "Oh hi there."
    male4 "I thought you'd be here."
    male4 "So I decided to pay a visit."
    mc "..."
    show male4 happy
    male4 "I also have to check the halls after school so I decided to drop by."
    mc "Is that so?"
    show male4 smug
    male4 "Not in a mood for talking?"
    mc "..."
    mc "It's not that."
    mc "I just have a lot on my mind."
    show male4 normal
    male4 "Final exams?"
    mc "Nah..."
    mc "It's just..."
    mc "How do you think Hiro is doing?"
    mc "I'm a bit worried..."
    mc "Naomi too."
    show male4 worried
    male4 "To be honest..."
    male4 "I'm not even sure what happened to the both of them."
    male4 "Hopefully they're not dead."
    mc "... excuse me?"
    show male4 scared
    male4 "Oh... I just mean that I hope they're safe and all."
    mc "Oh.. okay?"
    mc "Well, Naomi is my best friend and all."
    mc "Even though we argue alot, I would hate to lose her."
    show male4 blush
    male4 "I feel ya."
    male4 "I just hope Hiro is not getting himself into any trouble."
    mc "What do you mean?"
    show male4 worried
    male4 "Well, you've noticed it too right?"
    male4 "Hiro and Naomi don't particularly get along."
    male4 "Both are my friends, I know them very well."
    male4 "Actually, its strange..."
    male4 "A few weeks ago, I was talking to him about this."
    scene bg blank with fade
    centered "{size=45}A few weeks ago{/size}"
    scene bg hiro_office with fade
    show male4 worried with dissolve
    male4 "Hiro..."
    male4 "You gotta get over Naomi."
    hide male4
    show male3 worried
    male3 "I know..."
    male3 "But I just feel so conflicted."
    hide male3
    show male4 blush
    male4 "You like her don't you though?"
    male4 "Haru, I mean."
    hide male4
    show male3 normal
    male3 "I mean... I do it's just..."
    hide male3
    show male4 worried
    male4 "Then go for it!"
    male4 "You have to realize that Naomi is a lost cause!"
    male4 "You can't wait on her forever, you have to move on!"
    hide male4
    show male3 worried
    male3 "I know..."
    show male3 normal
    male3 "But wait a minute Kaoru..."
    male3 "Why are you rooting for me?"
    male3 "Don't you like her too."
    hide male3
    show male4 blush
    male4 "Don't drag me into this Hiro..."
    show male4 smug
    male4 "You should know that more than anyone I gave up on my love life a long time ago."
    male4 "Don't worry about me, I'll be fine."
    play sound "audio/dooropen.wav"
    show male4 nervous
    male4 "!!!"
    show male4 blush
    male4 "Oh, its just Haru."
    show male4 normal
    male4 "Anyway Hiro, I'll leave it to ya."
    show male4 happy
    male4 "Cya later!"
    scene bg artroom with fade
    show male4 excited with dissolve
    male4 "You see, Hiro had a crush on you but he was too afraid to admit it."
    show male4 glee
    male4 "For the longest time he was hung up on Naomi!"
    male4 "But ever since you came along, I think he's been starting to move on."
    show male4 happy
    male4 "if only he weren't such a stubborn piece of work"
    male4 "Ever since you came into the picture, he doesn't know what to do with himself anymore."
    show male4 normal
    male4 "But you know what?"
    mc ". . ."
    mc "What?"
    show male4 happy
    male4 "Well, I told him..."
    stop music
    male4 "If he won't take you, I'll gladly take you for myself."
    mc "!!!"
    scene bg blank with fade
    centered "All I remember was..."
    centered "At that moment..."
    centered "I did something that I shouldn't have..."
    centered "I pushed him away and ran."
    centered "If only..."
    centered "I knew what was going to happen next..."
    centered "I would have acted differently."
    centered "But then, as I got ready to walk home..."
    centered "I saw him there."
    centered "And thats when strange things started happening"
    centered "It was another rainy evening..."
    centered "And thats where it all began..."
    play music "audio/rainloop.wav" fadein 1.0 volume 0.5
    scene bg school_genkan with fade
    mc "(Was it raining this afternoon?)"
    mc "(There's gonna be puddles everywhere.)"
    mc "(Ugh, that means I'm going to have to clean my shoes when I get back...)"
    male4 "Heya, Ruha!"
    hide ct_overlay
    hide ct_wed
    hide ct_400
    with dissolve
    show male4 glee with dissolve
    male4 "Ruhachi Chan!"
    mc ". . ."
    mc "I'm not even gonna say anything."
    show male4 normal
    male4 "Y,know I was thinking..."
    male4 "Maybe we could walk home together again today."
    mc "You're not gonna trick me into buying you another umbrella today are you?"
    show male4 worried
    male4 "No, no, no."
    show male4 happy
    male4 "I just have a lot on my mind that I want to talk to you about today."
    mc "Sorry, I'm busy."
    show male4 worried
    male4 "Awe..."
    show male4 blush
    male4 "Well at least give me a call when you get home safe."
    mc "Are you my mom?"
    show male4 happy
    male4 "Haha, nah."
    male4 "But lets exchange numbers just incase."
    mc "???"
    mc "Sure, I guess?"
    mc "..."
    mc "Actually, I'm not in a rush to go home."
    mc "Are you doing anything today?"
    show male4 worried
    male4 "Me?"
    show male4 blush
    male4 "I was kinda in the middle of doing my paperwork but I got lazy and decided I wanted to put it off for tomorrow!"
    mc ". . ."
    mc "Do you need help?"
    show male4 nervous
    male4 "!!!" with vpunch
    show male4 scared
    male4 "Uhm, Haru, do you think we can stand over here?"
    mc "Oookay?"
    show male4 glee
    male4 "Okay, now, slightly to the left."
    mc "Here?"
    stop music
    scene bg blank
    play sound "audio/collapse.mp3"
    pause (2.0)
    stop sound fadeout 1.0
    mc "!!!" with vpunch
    mc "Oh my god!"
    mc "That was close!"
    scene cg catastrophe2 with fade
    male4 ". . ."
    male4 "Yea..."
    male4 "That was close."
    mc "..."
    male4 "..."
    male4 "Anyway..."
    male4 "I think we should get going."
    male4 "Lets get heading to my office, I guess."
    stop music fadeout 1.0
    ##ts --------------------------------
    scene ts some_time_later with fade
    pause
    ##ts --------------------------------
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    scene bg kaoru_office with fade
    show male4 blush
    male4 "This one is a pretty difficult case to crack."
    show male4 worried
    male4 "Haru, do you think this guy is guilty or not?"
    mc "I mean, I wouldn't know."
    show male4 blush
    male4 "Yeah, enforcing rules is pretty difficult."
    mc "Kaoru, may I ask you a question?"
    show male4 happy
    male4 "What is it, dearie?"
    mc "Do you have to call me that?"
    show male4 excited
    male4 "Harurinrin!"
    male4 "Harinrinrin!"
    mc "..."
    mc "Nevermind, you can stick with dearie..."
    show male4 glee
    male4 "Hahaha!"
    show male4 normal
    male4 "Was that your question?"
    mc "Wait? What? No!"
    mc "I mean..."
    mc "I actually wanted to ask about something else."
    mc "Why are you in the disciplinary committee in the first place?"
    mc "It seems like you're the only one here, and you practically never do your job."
    show male4 happy
    male4 "Oh, that."
    male4 "Funny story, actually."
    male4 "It kind of just happened."
    male4 "One of my friends thought it would've been fun to play school police and mess around in school."
    show male4 excited
    male4 "So I decided to join the disciplinary committee!"
    mc "..."
    mc "And how did that go?"
    show male4 glee
    male4 "Ahahaha!"
    show male4 scared
    male4 "Pretty bad..."
    mc "Oh..."
    show male4 happy
    male4 "My friends realized that it was actually too much work, so they bailed out on me and left me to do the rest of the work."
    male4 "When I first started, I was completely worthless when it came to the work."
    male4 "Instead of doing the paperwork to discipline people I'd just bail people out for the sake of it."
    male4 "A lot of people liked me because I kept letting people get away with everything!"
    show male4 worried
    male4 "But then I kept getting scolded by the headmaster for not doing my job properly."
    show male4 normal
    male4 "But then Hiro saw how useless I was at my job, so he decided to help me out with my work."
    male4 "He seems really strict but beneath that he's a great guy!"
    mc "..."
    mc "Why the disciplinary committee out of all things though?"
    show male4 smug
    male4 "Oh that?"
    male4 "Cause, I thought it would be fun being a hall monitor."
    show male4 excited
    male4 "You get unlimited bathroom breaks, and you can show up late to class and all you have to say is that you were handling some business."
    mc ". . ."
    mc "(Kaoru is really hopeless isn't he?)"
    show male4 normal
    male4 "I think the rain stopped."
    male4 "You should try heading home before it gets too late."
    male4 "Oh yea, heres my Liner."
    mc "?"
    mc "Oh, I forgot about that."
    male4 "Make sure the text me when you get back home okay?"
    play sound "audio/vibrate.wav"
    show male4 nervous with vpunch
    male4 "!!!"
    mc "I sent one to you just now."
    show male4 happy
    male4 "Oh? Thats great!"
    mc "Well, I'll get going now."
    mc "Bye!"
    show male4 glee
    male4 "Bye!"
    stop music fadeout 1.0
    ##ts --------------------------------
    scene ts home with fade
    pause
    ##ts --------------------------------
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    scene bg bedroom_yoru with fade
    mc "... I'm tired"
    mc "I think I'm gonna go to sleep and call it a day."
    mc "I can't be bothered to do my homework tonight."
    play sound "audio/vibrate.wav"
    mc "!!!" with vpunch
    mc "It's a message from Kaoru!"
    centered "{nw}"
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    call phone_start(0) from _call_phone_start
    play sound "audio/pop.mp3"
    call message_start("akeyuki_pf", "Kaoru", "Harupyun beware of the shadows. Remember you are Mortal.") from _call_message_start
    play sound "audio/pop.mp3"
    call message_reply("What is that even supposed to mean Kaoru?") from _call_message_reply
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I have no idea.") from _call_message
    play sound "audio/pop.mp3"
    call message_reply("???") from _call_message_reply_1
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Just remember that the grass is not always greener on the other side, and...idk") from _call_message_1
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Man I am sounding like those video games I play.") from _call_message_2
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Corny and cheesy.") from _call_message_3
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Wait, is cheesecorn a thing?") from _call_message_4
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Hey, Haru. Do you wanna go get some corn with cheese one of these days?") from _call_message_5
    play sound "audio/pop.mp3"
    call message_reply("I don't think that exists...") from _call_message_reply_2
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Uncultured swine...") from _call_message_6
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "em, you never had food from where Ikemen senpai hails.") from _call_message_7
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "BLASPHEMY! AND YOU call yourself an Otome Legends fan?") from _call_message_8
    play sound "audio/pop.mp3"
    call message_reply("I don't though.") from _call_message_reply_3
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "You disgrace the name of the Senpai-Tachi") from _call_message_9
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Haha...") from _call_message_10
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Oh yea, I had something else that was important I wanted to tell you.") from _call_message_11
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Don't touch that game anymore though, I'm serious.") from _call_message_12
    play sound "audio/pop.mp3"
    call message_reply("That last line is the only coherent sentence you said in the past 5 minutes.") from _call_message_reply_4
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Btw, do you think you could do me a favor Chiharurun?") from _call_message_13
    play sound "audio/pop.mp3"
    call message_reply("???") from _call_message_reply_5
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Do you think you could meet with me somewhere before school?") from _call_message_14
    play sound "audio/pop.mp3"
    call message_reply("So long it ain't shady. What's up?") from _call_message_reply_6
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Have you ever ate at the 35?") from _call_message_15
    play sound "audio/pop.mp3"
    call message_reply("uh did you finish your sentence... 35 what? Pizza? Fish?") from _call_message_reply_7
    play sound "audio/pop.mp3"
    call message_reply("And why am I going to eat thirty-five of something. What if I get a stomach-ache?") from _call_message_reply_8
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Lolol don't change Chiharu.") from _call_message_16
    play sound "audio/pop.mp3"
    call message_reply("But I am being serious.") from _call_message_reply_9
    play sound "audio/pop.mp3"
    call message_reply("Also, why can't we just go after school?") from _call_message_reply_10
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Because there is a 500 yen discount in the morning. Buy one get one free.") from _call_message_17
    play sound "audio/pop.mp3"
    call message_reply("But if we get one is it just one?") from _call_message_reply_11
    play sound "audio/pop.mp3"
    call message_reply("And how big is it? What actually is it anyway?") from _call_message_reply_12
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Ice cream. It is a convinence store with really good ice cream.") from _call_message_18
    play sound "audio/pop.mp3"
    call message_reply("Ice cream?? Then why is it called 35? Do I get something special when I am 35?") from _call_message_reply_13
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "??? HUH") from _call_message_19
    play sound "audio/pop.mp3"
    call message_reply("Oh wait, why for breakfast.") from _call_message_reply_14
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Haru, I don't think you know what breakfast is.") from _call_message_20
    play sound "audio/pop.mp3"
    call message_reply("And you do?!?!?") from _call_message_reply_15
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Ice Cream is a well balanced meal of the day to start you off.") from _call_message_21
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "You have milk, egg, salt, chocolate. You basically got your protein for the day and we are just breakfast also unlike toast it won't fall off your mouth.") from _call_message_22
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "So if anything, why not Ice cream?") from _call_message_23
    pause
    "Translation Notes: There is no validity in what he is saying. He just really wanted Ice cream."
    centered "{nw}"
    play sound "audio/pop.mp3"
    call message_reply("Ok deal, we will banana split it.") from _call_message_reply_16
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Omg, yas queen.") from _call_message_24
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Alright, cya tomorrow early in the morning!") from _call_message_25
    play sound "audio/pop.mp3"
    call message_reply("kk") from _call_message_reply_17
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide screen phone_message_image2
    with dissolve
    scene bg bedroom_yoru with dissolve
    call phone_end(0) from _call_phone_end
    mc "What have I've gotten myself into..."
    mc "Kaoru..."
    mc "I guess he's nice..."
    scene cg texting with fade
    male4 "Hehe.."
    male4 "Haru can be so cute sometimes."
    stop music fadeout 1.0
    ##ts -------------------------
    scene ts the_next_day with fade
    pause
    ##ts -------------------------
    play music "audio/nowav.mp3" fadein 1.0 volume 0.5
    scene bg blank with fade
    centered "When I showed up at the thirty-five, Kaoru wasn't there."
    centered "I waited for him for 30 minutes, and he didn't answer any of my messages."
    centered "When I looked at the time, I was already late for school."
    centered "By the time I got there, the gates had already closed on me."
    centered "So I decided to call it a day and started walking home."
    mc "(sigh)"
    mc "What am I gonna do now?"
    male4 "Hey there!"
    mc "???"
    scene bg kinjo with fade
    show male4 normal with dissolve
    male4 "Guess we're in the same boat, haha."
    mc "..."
    mc "What are you doing out here?"
    mc "Why aren't you in school?"
    show male4 glee
    male4 "Because they're big scary monsters in there, silly-billy!"
    mc "...you mean the teachers?"
    show male4 excited
    male4 "Yeah!"
    mc ". . ."
    show male4 happy
    male4 "So do you wanna go get that ice cream today?"
    mc "... Is that ice cream machine still working though?"
    show male4 nervous
    male4 "..."
    male4 "Let's get going then."
    scene white with dissolve
    centered "{color=#000000}Instead of going to school, I skipped class and went to the convinence store to get ice cream with Kaoru.{/color}"
    centered "{color=#000000}I'm not sure how my mom will feel about this though...{/color}"
    stop music fadeout 1.0
    ##ts ------
    scene ts home with fade
    pause
    ##ts ------
    scene bg bedroom_yoru with fade
    mc "..."
    mc "Strange things have been happening today..."
    play sound "audio/vibrate.wav"
    mc "!!!" with vpunch
    mc "It's Kaoru."
    mc "I wonder what's up with him."
    play music "audio/club.mp3" fadein 1.0 volume 0.5
    call phone_start(0) from _call_phone_start_1
    play sound "audio/pop.mp3"
    call message_start("akeyuki_pf", "Kaoru", "Heya, Harucchi.") from _call_message_start_1
    play sound "audio/pop.mp3"
    call message_reply("Is that a Naominmin?") from _call_message_reply_18
    play sound "audio/pop.mp3"
    call message_reply("Oh, wait it's you.") from _call_message_reply_19
    play sound "audio/pop.mp3"
    call message_reply("Will you stop with those nicknames, you're starting to sound like Naomi.") from _call_message_reply_20
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Lol, soz.") from _call_message_26
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Yea, Naomi calls you that sometimes.") from _call_message_27
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I just thought it would've been funny to copy her.") from _call_message_28
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Y,know the weird nickname thing? She gets it from me, lol.") from _call_message_29
    play sound "audio/pop.mp3"
    call message_reply("Wow, so now ik who to blame for it, huh?") from _call_message_reply_21
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Lol.") from _call_message_30
    play sound "audio/pop.mp3"
    call message_reply("Anyways, what's up?") from _call_message_reply_22
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "ygytfyrdtrser") from _call_message_31
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Oh sorry about that.") from _call_message_32
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Keyboard malfunction, lol.") from _call_message_33
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Anyway...") from _call_message_34
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I've been avoiding asking this for a while but...") from _call_message_35
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "How do you feel about dying?") from _call_message_36
    play sound "audio/pop.mp3"
    call message_reply("Oh no, please don't tell me") from _call_message_reply_23
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "What?") from _call_message_37
    play sound "audio/pop.mp3"
    call message_reply("We are in poorly made scripted teen drama.") from _call_message_reply_24
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "No, because at least we have personality.") from _call_message_38
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Anyway, we all die someday. I was just wondering, have you ever been afraid of dying?") from _call_message_39
    play sound "audio/pop.mp3"
    call message_reply("Idk man, life is like a gacha game. You never know what you're gonna get.") from _call_message_reply_25
    play sound "audio/pop.mp3"
    call message_reply("Or... uh... when you're gonna die, in that case, I guess...") from _call_message_reply_26
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Never truer words have been spoken.") from _call_message_40
    play sound "audio/pop.mp3"
    call message_reply("so why do you think you are going to pass gas") from _call_message_reply_27
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "WHAT!!?") from _call_message_41
    play sound "audio/pop.mp3"
    call message_reply("Autocorrect, SOZ! i meant to say pass away") from _call_message_reply_28
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Because I've been having a nasty cough from time to time and i think its a sign that its my time to go.") from _call_message_42
    play sound "audio/pop.mp3"
    call message_reply("I'm pretty sure that you just have allergies.") from _call_message_reply_29
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I took medication in the morning and I haven't felt any better if anything I get sleepy.") from _call_message_43
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "But you know what's strange?") from _call_message_44
    play sound "audio/pop.mp3"
    call message_reply("The ice cream machine at that one place is still working?") from _call_message_reply_30
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "You really put the Boba in Boba tea.") from _call_message_45
    pause
    "Translation notes: My smartphone translator app says that in Spanish Boba means stupid."
    centered "{nw}"
    play sound "audio/pop.mp3"
    call message_reply("Are you speaking ecquestrian?") from _call_message_reply_31
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Are you thinking about the language spoken in Ecuador because, A, that is Spanish, and B, idk man, did you parents drop you as a kid??") from _call_message_46
    play sound "audio/pop.mp3"
    call message_reply("I am craving arrow con Leche") from _call_message_reply_32
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Autocorrect again?") from _call_message_47
    play sound "audio/pop.mp3"
    call message_reply("No in spanish rice is arrow") from _call_message_reply_33
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "It is arroz") from _call_message_48
    play sound "audio/pop.mp3"
    call message_reply(". . . . .") from _call_message_reply_34
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Anyways Haruhuru, do you have a boyfriend") from _call_message_49
    play sound "audio/pop.mp3"
    call message_reply("Why? Aren't you my boy friend?") from _call_message_reply_35
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru","EHH?????") from _call_message_50
    play sound "audio/pop.mp3"
    call message_reply("Wut?!") from _call_message_reply_36
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Wait, do you think I mean that I am your friend that is a guy?") from _call_message_51
    play sound "audio/pop.mp3"
    call message_reply("Isn't that what you meant?") from _call_message_reply_37
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Ahhhh fwiwiwiwiwiwiiwiwiwwiwwww. You're lovely Haru. No wonder Naomi is so crazy about you.") from _call_message_52
    play sound "audio/pop.mp3"
    call message_reply("Anyway, I'm going to go to sleep tonight.") from _call_message_reply_38
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Alright, cya then.") from _call_message_53
    call phone_end(0) from _call_phone_end_1
    "Wait..."
    "Why would he ask me if I had a...?"
    ". . ."
    centered "{nw}"
    play sound "audio/rpsselect.wav"
    show chibi kaoru with dissolve
    show progress1 with dissolve
    pause 1.0
    show heart_progress2
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 0.5
    play sound "audio/rps.wav"
    pause 2.0
    play sound "audio/sparkle.wav"
    pause 4.0
    scene bg blank with fade
    pause 1.0
    play sound "audio/unlock.wav"
    centered "{size=50}You've earned a heart from Kaoru!{/size}"
    scene bg bedroom_yoru with fade
    "I must be imagining things." with dissolve
    stop music fadeout 1.0
    ##ts —----
    scene ts the_next_day with fade
    pause
    ##ts —---
    play music "audio/classtime.mp3" fadein 1.0 volume 0.5
    scene bg school_genkan with fade
    mc "I wonder why Kaoru suddenly invited me to the ice cream place with him."
    mc "It was really fun..."
    mc "..."
    mc "But I can't help but feel like there's always something on his mind..."
    male4 "Haru!!!"
    mc "(This maniac again...)"
    mc "Hi?"
    show male4 happy with dissolve
    male4 "Y,know..."
    male4 "The other day..."
    male4 "The stairs to the 2nd floor collapsed."
    show male4 glee
    male4 "So you'd have to take the long way to class instead."
    mc ". . ."
    show male4 normal
    male4 "What is it Harununu?"
    mc "What happened yesterday?"
    show male4 scared
    male4 "Oh!"
    male4 "Sorry, about that!"
    show male4 blush
    male4 "Last morning, the apartment stairs collapsed on me the other day."
    male4 "I'm sorry for being late..."
    mc "Oh..."
    "Man is everything collapsing nowadays?"
    show male4 happy
    male4 "Anyways lets take this to the halls."
    male4 "Theres something I wanna talk to you about."
    scene bg school_hallway with fade
    show ct_overlay
    show ct_thurs
    show ct_830
    with dissolve
    show male4 normal with dissolve
    mc "What was it that you wanted to tell me Kaoru?"
    show male4 happy
    male4 "Oh..."
    male4 "Well, how do I put this?"
    show male4 worried
    male4 "Ok, this is not gonna be easy to say but..."
    male4 "The art club is going to be disbanded."
    mc "What?! Why?!"
    show male4 worried
    male4 "You didn't know?"
    show male4 blush
    male4 "Naominmin got expelled."
    mc "Expelled?!?"
    mc "Since when?!?"
    mc "And, how do you know?!"
    show male4 worried
    male4 "Look, when students are disciplined it falls under my radar."
    male4 "Expulsion is just one of the things I handle."
    male4 "... the paperwork... that is."
    show male4 blush
    male4 "I usually have no control, I just carry out orders."
    show male4 worried
    male4 "It's one of my responsibilities as the head of the disciplinary committee."
    show male4 worried
    male4 "But it's strange..."
    hide ct_thurs
    hide ct_830
    hide ct_overlay
    with dissolve
    pause (1.0)
    male4 "I thought she would at least talk to you about it." with dissolve
    mc ". . ."
    show male4 blush
    male4 "I'm sorry."
    male4 "I know you guys put effort into keeping that club open..."
    male4 "I heard about it from Hiro..."
    show male4 worried
    male4 "Before he disappeared, that is."
    mc "..."
    mc "That's okay, I guess."
    mc "But there's something else I wanted to ask you."
    show male4 happy
    male4 "What is it dear?"
    mc "uhm..."
    mc "That confession under the sakura tree the other day."
    mc "Were you really messing with my feelings?"
    mc "or were you actually serious?"
    mc "I mean, you didn't sound like you were trying to mess with my head..."
    show male4 blush
    male4 "About that..."
    male4 "I'm really sorry about that, it's just..."
    male4 "I didn't mean to hurt your feelings, honestly!"
    show male4 worried
    male4 "I-I-I mean I!"
    play sound "audio/schoolchime1.wav"
    "It's time for class"
    show male4 blush
    male4 "We can talk about this another time, okay?"
    male4 "You can talk to me at lunch."
    hide male4 with dissolve
    "He disappeared into the halls."
    mc "..."
    mc "Strange."
    stop music fadeout 1.0
    ##ts ------------------------------------------
    scene ts after_class with fade
    pause
    ##ts -------------------------------------------
    play music "audio/classtime.mp3" fadein 1.0 volume 0.5
    play sound "audio/schoolchime1.wav"
    scene bg classroom with fade
    mc "(It's lunch time...)"
    mc "(But I'm not sure who I should eat lunch with...)"
    mc "(...)"
    mc "(Maybe I should sleep in class instead.)"
    mc "(I wish Nao were here...)"
    mc "(I wonder what she's up to.)"
    mc "(...)"
    mc "(. . .)"
    mc "(Maybe she was right...)"
    mc "(I should make more friends.)"
    mc "(Afterall, I relied too much on her.)"
    mc "(Yea, I should be able to make my own decisions now.)"
    "What should you do?"
    label choices15:
    menu:
        "Visit Kaoru.":
            pass
    stop music
    "It's not like you had any other choice anyway."
    play music "audio/club.mp3"
    scene bg blank with fade
    "I wandered around the hallways for a bit before stumbling across Kaoru's office."
    scene bg kaoru_office_door with fade
    mc "(...)"
    mc "(Maybe I should pay him a visit.)"
    scene bg kaoru_office with fade
    mc "Hello?"
    mc "Kaoru, are you there?"
    mc "(That's strange...)"
    mc "(He's usually here...)"
    mc "(...no)"
    mc "(Something's not right...)"
    mc "(Did he go missing too???)"
    male4 "Boo!"
    mc "!!!" with vpunch
    mc "Do you have to scare me like that??"
    show male4 happy with dissolve
    male4 "Sorry."
    male4 "Were you looking for me?"
    mc "...yes"
    show male4 excited
    male4 "Awwwe!"
    male4 "That's so adorable!"
    show male4 blush
    male4 "Anywho, I was on my way to the vending machine just now because I forgot my lunch today."
    mc "..."
    $ renpy.music.set_volume(0.00, delay=0, channel='music')
    mc "Then what is that bento doing in the garba-{nw}"
    show male4 scared with vpunch
    male4 "GARBAGE?!?"
    $ renpy.music.set_volume(1.00, delay=0, channel='music')
    show male4 nervous
    male4 "Excuse me what? I don't see anything in the garbage, cmon let's go!"
    scene bg school_hallway with fade
    show male4 normal with dissolve
    male4 "Anyway, here we are."
    male4 "Do you want anything? I'm getting melon bread with chocolate milk."
    show male4 scared
    male4 "Hold on!"
    "He knocked on the vending machine for a bit before slowly backing away."
    show male4 nervous
    male4 "Haru, you might want to step away from that thing."
    mc "Okay???"
    "I moved out of the way."
    mc "Kaoru, why are we standing he-{nw}"
    hide male4
    scene bg blank
    stop music
    play sound "audio/crash.mp3"
    pause (3.0)
    scene cg catastrophe3 with fade
    play sound "audio/zap.mp3"
    mc "!!!" with vpunch
    male4 "{cps=15}. . .{/cps}"
    male4 "Uhm..."
    male4 "Yea, maybe I don't need lunch today."
    male4 "Haru, do you mind if we talk for a bit in my office instead?"
    mc "...I guess not?"
    ##ts —-----------------
    scene ts some_time_later with fade
    pause
    ##ts —------------------------
    scene bg kaoru_office with fade
    show male4 normal with dissolve
    male4 "Soooo..."
    male4 "Do you have any plans after school?"
    mc "... no?"
    show male4 nervous
    male4 "Oh..."
    mc "Uhm, are you really not gonna eat anything?"
    show male4 glee
    male4 "No, no!"
    male4 "I'm fine ya see!"
    play sound "audio/hungry.mp3" volume 0.25
    show male4 scared
    male4 ". . ."
    mc "Here."
    centered "{nw}"
    play sound "audio/unlock.wav"
    show ichigopan
    pause
    hide ichigopan
    show male4 smug
    male4 "Oh?"
    male4 "This is the melon bread I gave you."
    show male4 worried
    male4 "I can't take this, it's a gift..."
    mc "We can split it."
    male4 "..."
    show male4 blush
    male4 "Okay..."
    "Kaoru reluctantly took a piece of my strawberry melon bread."
    show male4 glee
    male4 "Wow! This is so good!"
    male4 "I see why Hiro likes these so much!"
    show male4 worried
    male4 "If only he were here..."
    mc "What's wrong Kaoru?"
    show male4 blush
    male4 "Oh, it's nothing."
    show male4 normal
    male4 "It's just that, it feels kinda strange with Hiro gone and all."
    male4 "Naomi too."
    mc "Yea..."
    mc "I feel you."
    mc "Kaoru..."
    show male4 happy
    male4 "Hm?"
    mc "Do you think Hiro will come back?"
    show male4 nervous
    play sound "audio/vibrate.wav"
    male4 "..." with vpunch
    show male4 scared
    male4 "I gotta... go."
    hide male4 with dissolve
    mc "..."
    mc "I wonder whats up with him..."
    ##ts —-----------------
    scene ts home with fade
    pause
    ##ts —------------------------
    label last_message:
    scene bg bedroom with fade
    mc "Home at last!"
    mc "Can't wait to marathon that new webbflix show!"
    play sound "audio/vibrate.wav"
    mc "!!!" with vpunch
    mc "Kaoru, again?"
    mc "What does he want this time?"
    call phone_start(0) from _call_phone_start_2
    play sound "audio/pop.mp3"
    call message_start("akeyuki_pf", "Kaoru", "Haru.") from _call_message_start_2
    play sound "audio/pop.mp3"
    call message_reply("Waddup?") from _call_message_reply_39
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I have something serious to tell you.") from _call_message_54
    play sound "audio/pop.mp3"
    call message_reply("Wait, what?") from _call_message_reply_40
    play sound "audio/pop.mp3"
    call message_reply("What is it?") from _call_message_reply_41
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Look at the news.") from _call_message_55
    pause
    "?"
    call phone_end(0) from _call_phone_end_2
    stop music
    scene bg blank with fade
    show tvnews with dissolve
    pause (1.0)
    "News Broadcaster" "Reports of various mini earthquakes around the local city area have been increasing as of recently." with dissolve
    "News Broadcaster" "Strangely enough emergency alert services have failed to release public notifications during each of these incidental happenings."
    "News Broadcaster" "Regardless, we advise citizens to abide by regular precaution procedures and be wary of any future earthquake-like incidents."
    "News Broadcaster" "So far there have been no casualties, but there has been significant property damage."
    mc "???"
    scene bg blank with dissolve
    pause (3.0)
    play music "audio/uncanny.mp3" fadein 1.0 volume 0.5
    call phone_start(0) from _call_phone_start_3
    play sound "audio/pop.mp3"
    call message_reply("Kaoru, what is going on?!?!") from _call_message_reply_42
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I'm not sure...") from _call_message_56
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "But I do have a gut feeling on what is happening.") from _call_message_57
    play sound "audio/pop.mp3"
    call message_reply("What do you mean?") from _call_message_reply_43
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "You might think I'm crazy...") from _call_message_58
    play sound "audio/pop.mp3"
    call message_reply("JUST SPIT IT OUT!") from _call_message_reply_44
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Okay...") from _call_message_59
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Haru, you know...") from _call_message_60
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I'm next.") from _call_message_61
    play sound "audio/pop.mp3"
    call message_reply("What are you talking about?") from _call_message_reply_45
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I mean, I'm next.") from _call_message_62
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I'm going to die soon.") from _call_message_63
    play sound "audio/pop.mp3"
    call message_reply("WHAT ARE YOU TALKING ABOUT?!!?") from _call_message_reply_46
    play sound "audio/pop.mp3"
    call message_reply("KAORU! DON'T PLAY JOKES WITH ME LIKE THAT!!!") from _call_message_reply_47
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "I just want you to know...") from _call_message_64
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "If anything happens to me.") from _call_message_65
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Just know that I love you.") from _call_message_66
    play sound "audio/pop.mp3"
    call message("akeyuki_pf", "Kaoru", "Stay safe.") from _call_message_67
    play sound "audio/pop.mp3"
    call message_reply("Kaoru?!") from _call_message_reply_48
    play sound "audio/pop.mp3"
    call message_reply("KAORU?!") from _call_message_reply_49
    play sound "audio/pop.mp3"
    call message_reply("KAORU! ANSWER ME!") from _call_message_reply_50
    play sound "audio/pop.mp3"
    call message_reply("DON'T DO ANYTHING STUPID! ANSWER ME!!!") from _call_message_reply_51
    play sound "audio/pop.mp3"
    call message_reply("Kaoru? iF THIS IS A JOKE ITS NOT FUNNY!") from _call_message_reply_52
    play sound "audio/pop.mp3"
    call message_reply("Like sERIOUSly STOP!") from _call_message_reply_53
    play sound "audio/pop.mp3"
    call message_reply("IT'S NOT FUNNY!!!") from _call_message_reply_54
    play sound "audio/pop.mp3"
    call message_reply("KAORU!") from _call_message_reply_55
    play sound "audio/pop.mp3"
    call message_reply("KAORU!") from _call_message_reply_56
    play sound "audio/pop.mp3"
    call message_reply("KAORU!") from _call_message_reply_57
    play sound "audio/pop.mp3"
    call message_reply("KAORU!") from _call_message_reply_58
    play sound "audio/pop.mp3"
    call message_reply("KAORU!!!!!!") from _call_message_reply_59
    play sound "audio/pop.mp3"
    call message_reply("Please don't leave me...") from _call_message_reply_60
    play sound "audio/pop.mp3"
    call message_reply("Not you too...") from _call_message_reply_61
    play sound "audio/pop.mp3"
    call message_reply("Please answer me.") from _call_message_reply_62
    call phone_end(0) from _call_phone_end_3
    mc "..."
    mc "(I need to call emergency services!)"
    scene bg blank with fade
    centered ". . ."
    play sound "audio/phoneservice.wav"
    centered "I'm sorry, it appears the number you called is currenly out of service."
    scene bg bedroom_dark with fade
    mc "..."
    mc ". . ."
    mc "What?!?"
    play sound "audio/vibrate.wav"
    pause 3.0
    mc "!!!" with vpunch

    call phone_start(0) from _call_phone_start_4
    play sound "audio/pop.mp3"
    call message("unknown_pf", "Unknown", "If you want to see him, he's at the school.") from _call_message_68
    play sound "audio/pop.mp3"
    call phone_end(0) from _call_phone_end_4

    play sound "audio/error.wav"
    show bg bedroom_glitch
    pause (3.0)
    scene bg bedroom_dark
    mc "!!!" with vpunch
    scene esc room8 with fade
    mc "(Where is he?!)"
    "(Exhausted I ran all the way to the school.)"
    "(I wasted no time, not even changing into my shoes before I ran into the halls without a second thought.)"
    "(He should've picked up his phone though, I got a bad feeling about this.)"
    scene bg blank with fade
    play sound "audio/running2.wav"
    pause (4.0)
    mc "!!!"

    label stab:
    stop music
    play sound "audio/stab.mp3"
    show flash red
    pause (3.0)
    scene cg stab_white with fade
    scene cg stab_black with dissolve
    pause (2.0)
    scene bg blank with fade
    $ persistent.kaoru = True
    $ achievement.grant("unknown_achievement")
    $ achievement.sync()
    centered "Kaoru route, ending 0/0 ..."
    centered "Who am I kidding?"
    centered "You never had a choice anyway."

    label naomi_route:
    mc "{cps=12}. . .{/cps}"
    scene bg past1 with fade
    play music "audio/run.mp3"
    show bff normal with dissolve
    bff "Oh, hey Haru."
    show bff glee
    bff "You weren't supposed to see that."
    mc "..."
    bff "You're probably wondering right now..."
    bff "\"Naomi, why is Kaoru dead on the floor with a knife in his chest?\""
    show bff excited
    bff "Well, I have an explanation for all of that!"
    show bff glee
    bff "You see, Kaoru was getting a bit too friendly with you."
    show bff normal
    bff "So I tried to kill him several times, but all my attempts ended up failing."
    show bff sigh
    bff "He was just being so hard to kill."
    bff "He managed to escape from every {b}single{/b} one of my deathtraps I laid out for him."
    show bff depressed
    bff "The electric pole in the water puddle."
    bff "The falling ceiling."
    bff "And even the vending machine..."
    bff "So I resorted to direct underhanded methods, which is not usually my preference but..."
    show bff mischievous
    bff "I got him in the end didn't I?"
    show bff blinking
    bff "Now, you can be with me."
    mc "..."
    "As I slowly backed up to prepare to run..."
    "I noticed... that the door was locked behind me."
    show bff blush
    bff "Oh Haru! You know that I wouldn't have let you escape that easily!"
    show bff evil_smile
    bff "I locked this very room door from the inside out so that Kaoru wouldn't have an easy time to escape."
    mc "..."
    mc "Please let me go..."
    show bff worried
    bff "Awe, Haru, did I scare you?"
    bff "I'm sorry, I'll fix that up right now."
    show bff closeup
    bff "We can start this entire thing all over, and you can forget about all of this."
    bff "Yea."
    bff "I think that would be for the best."
    $ persistent.naomi = True
    $ renpy.quit(relaunch=True, status=0, save=True)

    label restart1:
    if persistent.restart2:
        jump restart2

    stop music
    play music "audio/classtime.mp3" fadein 1.0 volume 0.5
    scene bg classroom with fade
    $ achievement.grant("jpn_achievement")
    $ achievement.sync()
    "{font=OtsutomeFont.ttf}去年はまるでたった一瞬で過ぎた。{/font}"
    "{font=OtsutomeFont.ttf}昔、石田はいつもその無器用な姿で一人で昼飯を大人しく食べていた。{/font}"
    "{font=OtsutomeFont.ttf}けれども、今の石田くんはまるで別人のようだった。{/font}"
    "{font=OtsutomeFont.ttf}始まると同時に大変身した.{/font}"
    "{font=OtsutomeFont.ttf}石田はその短い数ヵ月の間でゼロから学校の一番人気者になった。{/font}"
    show bff blinking with dissolve
    bff2 "{font=OtsutomeFont.ttf}はるッチ!{/font}"
    "{font=OtsutomeFont.ttf}友人直美のいつも通りの挨拶だ。{/font}"
    mc2 "{font=OtsutomeFont.ttf}今度は何でしょう、なお?{/font}"
    show bff excited
    bff2 "{font=OtsutomeFont.ttf}ねえ、ねえ!{/font}"
    bff2 "{font=OtsutomeFont.ttf}この間ね、話題の映画が出たし!{/font}"
    bff2 "{font=OtsutomeFont.ttf}一緒に見に行かない?{/font}"
    show bff glee
    bff2 "{font=OtsutomeFont.ttf}超面白そうなのよ!{/font}"
    show bff blinking
    mc2 "{font=OtsutomeFont.ttf}映画か?{/font}"
    mc2 "{font=OtsutomeFont.ttf}っていうか、そもそも映画の内容とか、ジャンルとかまだ聞いてないし。{/font}"
    mc2 "{font=OtsutomeFont.ttf}なお! 人を映画に誘う前にちゃんとどんな映画を見るのかを説明してくれない?{/font}"
    mc2 "{font=OtsutomeFont.ttf}...{/font}"
    mc2 "{font=OtsutomeFont.ttf}ちょっと待って。{/font}"
    mc2 "{font=OtsutomeFont.ttf}まさか、瞬きしてんの?{/font}"
    mc2 "{font=OtsutomeFont.ttf}ええええぇぇぇ!!??{/font}"
    mc2 "{font=OtsutomeFont.ttf}おい! キモいよ!{/font}"
    mc2 "{font=OtsutomeFont.ttf}その瞬きやめてよ!{/font}"
    mc2 "{font=OtsutomeFont.ttf}マジでキモいからやめて!{/font}"
    mc2 "{font=OtsutomeFont.ttf}やめてば!{/font}"
    show bff glee
    bff2 "{font=OtsutomeFont.ttf}放課後は暇でしょう？{/font}"
    label choices18:
    menu:
        "{font=OtsutomeFont.ttf}見る。{/font}":
            pass
        "{font=OtsutomeFont.ttf}見ない。{/font}":
            pass
        "{font=OtsutomeFont.ttf}助けて。{/font}":
            pass

    label choices19:
    play sound "audio/error.wav"
    scene bg blank
    show bg classroom_glitch
    menu:
        "Translator notes.":
            pass

    "Translator notes: What do you want now?"
    "I need your help."
    "The game is entirely in Japanese."
    "Translator notes: So?"
    "Translator notes: The game takes place in Japan."
    "Translator notes: And why would you care? Who actually reads visual novels nowadays?"
    "Translator notes: I know you just skipped all the dialogue and just so u could look at the cgs."
    "Translator notes: I mean, thats what most people do anyways."
    "Yea, but I can't read Japanese."
    "Translator notes: Fiiiiine"
    "Translator notes: Do you want me to put the game back in English for you?"
    "Yes."
    "Translator notes: But in order to do that I need to restart the game."
    "Translator notes: Just give me a sec..."
    "Translator notes: By the way..."
    "Translator notes: I wouldn't trust that bsb game if I were you."
    $ persistent.restart2 = True
    $ renpy.quit(relaunch=True, status=0, save=True)

    label restart2:
    stop music
    play music "audio/classtime.mp3" fadein 1.0 volume 0.5
    scene bg classroom with fade
    show ct_overlay
    show ct_fri
    show ct_830
    with dissolve
    "Last year passed by in a mere blink of an eye. "
    "Back then, Ishida used to awkwardly eat alone by himself during lunch. "
    "But now things have taken a turn for the better."
    "It seems as if that clumsy swirly eyed nerdy boy had gotten a complete makeover. "
    "In just those short few months, he went from being a complete nobody to one of the most popular guys in school ."
    show bff blink with dissolve
    bff " Harucchi !!!! "
    "Oh, it's my best friend Naomi's pet name greetings as usual."
    play sound "audio/error.wav"
    show bff glitch
    mc "What is it now, Nao?"
    show bff blush
    bff "Hey, Haru !!!"
    bff "Did'ja hear bout that new movie that just came out?!"
    hide ct_overlay
    hide ct_fri
    hide ct_830
    with dissolve
    pause (0.5)
    show bff excited
    bff "Everybody's watching it! Lets go watch it sometime later!"
    show bff glee
    bff "I heard it was really good!"
    show bff blinking
    mc "A movie?"
    mc "Wait, hold on Nao! You're going too fast for me. What movie? Where? When?!?"
    mc "Aren't ya supposed to at least tell me what movie we're watching or what the movie is about before we go decide to go spend money on tickets?"
    mc "..."
    mc " ... I mean "
    mc "If you're paying I don't really have a problem but I'm kinda tight on allowance money right now."
    show bff worried
    bff "Haru Chan, sometimes you're such a cheapskate. Y'know that right?"
    show bff glee
    bff "You're in luck I got a coupon! How about we see the movie after school?"
    label choices20:

    menu:
        "I'm a bit busy ...":
            pass
        " I have other plans.":
            pass
        "I'd rather not?":
            pass
    stop music

    label choices21:
    menu:
        "Sure, I mean why not? I was bored anyway.":
            pass

    mc "Sure, I mean why not? I was bored anyway."
    show bff excited
    bff "Yay!"
    play sound "audio/schoolchime1.wav"
    "Its time for class."
    show bff glee
    bff "K bye then!  Cya after class!"
    ##ts ---------
    scene ts after_class with fade
    pause
    #ts -------
    scene bg classroom with fade
    "It's time for lunch."
    "I wonder where I should go."
    label choices22:
    menu:
        "Visit Naomi on the rooftop for lunch.":
            pass
        "Stay in class and do homework.":
            pass

    label choices23:
    menu:
        "Talk to Ishida.":
            pass
    play music "audio/memory.mp3" fadein 1.0 volume 0.5
    male1 "Hey."
    mc "???"
    show male1 ver2_normal with dissolve
    male1 "Long time no see, Haru Chan."
    mc "Ishida?"
    mc "Is that you?"
    show male1 ver2_glee
    male1 "Haha, yea you're probably not used to seeing me like this in school, huh?"
    mc "..."
    mc "I mean, you don't look bad..."
    male1 "Thanks Chiharu."
    mc "?!?!"
    mc "Wha, what did I do?"
    show male1 ver2_normal
    male1 "For helping me out at the sports festival."
    male1 "Because of you, I was able to find myself a group of friends."
    male1 "They thought I was cool, and it turns out I was worried for nothing at all."
    mc "Oh thats great!"
    mc "Wait, did you lose your glasses again?"
    show male1 ver2_glee
    male1 "Haha no, I got rid of those goofy looking goggles."
    mc "..."
    mc "{size=16}I thought they looked cute on you though...{/size}"
    show male1 ver2_normal
    male1 "What?"
    mc "..."
    mc "Nevermind."
    show male1 ver2_glee
    male1 "Anyway, I'm gonna go eat with my friends!"
    male1 "See you later!"
    hide male1 with dissolve
    mc "..."
    mc "(He has friends now, huh.)"
    scene bg blank with fade
    centered "It's been a while since I've seen Ishida."
    centered "I wonder how's he's been."
    centered "Now that we're seniors..."
    centered "Things are different now."
    centered "But sometimes I wonder..."
    centered "Does he still like me?"
    stop music fadeout 1.0
    scene bg classroom with fade
    play sound "audio/schoolchime1.wav"
    show ct_overlay
    show ct_mon
    show ct_345
    with dissolve
    "School is over."
    "Maybe I should meet with Nao at the shoe lockers as usual."
    "But then again, I haven't seen Ishida in a long time."
    "Maybe I should talk to him first?"
    label choices24:
    menu:
        "Go to the movies with Naomi.":
            jump choices24_a
        "Go talk to Ishida.":
            jump choices24_common

    label choices24_a:
    scene bg blank
    centered "You wanted to go and talk with Ishida, remember?"
    scene bg classroom
    jump choices24


    label choices24_common:
    play music "audio/memory.mp3" fadein 1.0 volume 0.5
    scene bg school_genkan with fade
    mc "..."
    mc "Strange."
    mc "Nao is usually here today."
    male1 "Hey."
    mc "!!!"
    show male1 ver2_normal with dissolve
    male1 "How are you doing?"
    mc "(Ishida!)"
    mc "Oh, hi there."
    show male1 ver2_glee
    male1 "Uhm..."
    male1 "I've been meaning to ask you..."
    mc "?"
    ##ts ------------
    scene ts some_time_later with fade
    pause
    ##ts -------------
    scene bg ishida_game
    show cg ishida_game1
    with fade
    mc "What did you want to show me at the internet cafe?"
    male1 "Oh, nothing."
    male1 "It's just this game I was trying out, I'd thought you'd like it."
    mc "A game?"
    male1 "Yea."
    male1 "..."
    male1 "I'm sorry, am I being weird?"
    mc "No! Not at all!"
    mc "Okay so what do I do now?"
    male1 "You just turn this on..."
    male1 "Let me open the game for you."
    pause (2.0)
    mc "..."
    mc "These controls are a bit difficult."
    male1 "Here, let me help you."
    male1 "Okay, so the goal is to..."
    mc ". . ."
    male1 "Whats wrong?"
    mc "Oh, nothing. Its just that I'm not used to this."
    male1 "..."
    male1 "Haru, do you think you could stand up for a bit? I wanna see something."
    mc "Oh, what is it?"
    stop music
    play sound "audio/kiss.wav"
    scene bg blank
    pause (4.0)
    mc "???"
    scene bg ishida_game
    show cg ishida_game2
    with fade
    pause (3.0)
    mc ". . ."
    mc "Ishida..."
    play sound "audio/glitch.wav"
    scene bg blank
    show cg ishida_game glitch
    pause (6.0)
    stop sound
    scene bg blank
    pause (5.0)
    play music "audio/static.wav"
    scene static
    show cg ishida_game3
    with dissolve
    pause
    stop music fadeout 1.0
    show bg blank behind cg with dissolve
    pause
    centered "{color=#d13028}{size=60}{font=DejaVuSans.ttf}{b}This is what you wanted.{/b}{/font}{/size}{/color}"
    centered "{color=#d13028}{size=60}{font=DejaVuSans.ttf}{b}Right?{/b}{/font}{/size}{/color}"
    scene bg blank
    pause (8.0)
    play sound "audio/run.mp3" fadein 1.0 volume 0.5
    scene bg past1 with fade
    show bff normal with dissolve
    bff "You wanted a happy ending with Ishida."
    show bff glee
    bff "As a matter of fact!!!"
    show bff normal
    bff "You wanted a happy ending with everyone except for me."
    show bff mischievous
    bff "But you know what Haru?"
    bff "I'm sick of being stuck as the best friend character."
    show bff blush
    bff "I love you just as much!"
    show bff worried
    bff "No!"
    show bff excited
    bff "I love you even more than any of those guys do!"
    show bff glee
    bff "Y,know..."
    bff "Ishida is a lying back stabber."
    show bff normal
    bff "If you stayed with him, he would've cheated on you."
    bff "And Hiro would've neglected you and treated you like trash."
    bff "Kaoru is dense and all he does with is toy with your emotions."
    show bff worried
    bff "Just like how he messes with every other girl..."
    show bff sad
    bff "To them you're not anything special."
    bff "None of them actually cared about your feelings."
    show bff mischievous
    bff "So I killed them all."
    bff "and if that so called Yuusuke guy ever existed I bet he would've ghosted you."
    bff "I would've killed him too."
    bff "Every single one of them."
    show bff worried
    bff "Oh... yea, spoilers."
    show bff sigh
    bff "Sorry I spoiled the whole game for you."
    mc "..."
    mc "Why..."
    show bff depressed
    bff "Oh Haru, please don't cry!"
    show bff sad
    bff "All of those guys were jerks."
    bff "They deserved it."
    mc "... Wha-What did you do to Ishida?!?"
    show bff normal
    bff "Oh, him?"
    bff "I pushed him off the platform."
    show bff blush
    bff "I called him out to meet me at the train station at night and I pushed him infront of the train."
    bff "Afterall, he deserved it."
    show bff normal
    bff "As for Hiro..."
    show bff glee
    bff "Lets just say I kept him somewhere in my basement."
    show bff normal
    bff "Don't worry, he's not alive."
    bff "He eventually died from thirst and starvation."
    bff "I fed him to my dogs."
    show bff worried
    bff "Which I poisoned because they were a pain to deal with."
    bff "It was a pain to explain though."
    bff "I told my dad that the dogs got food poisoning and died."
    show bff sigh
    bff "They yelled at me for being too careless and letting them get sick in the first place."
    show bff glee
    bff "And Kaoru..."
    show bff mischievous
    bff "That annoying piece of trash."
    bff "He just wouldn't die no matter what I threw at him."
    bff "I'm surprised he even survived for this long."
    show bff glee
    bff "So I decided to take matters into my own hands."
    show bff worried
    bff "I'm sorry about earlier though..."
    bff "You weren't supposed to see that."
    mc "..."
    show bff sad
    bff "Haru..."
    bff "Won't you still pick me?"
    label choices25:
    menu:
        "No.":
            pass
    show bff worried
    bff "Oh..."
    bff "I get it now..."
    bff "You only like guys, don't you?"
    bff "After all, this is an Otome game."
    show bff normal
    bff "Well, don't worry."
    show bff mischievous
    bff "I have just the solution for that."
    $ persistent.naoya = True
    $ renpy.quit(relaunch=True, status=0, save=True)

    label restart3:
    stop music
    scene bg past1 with fade
    show male0 normal with dissolve
    "???" "How do I look?"
    mc "..."
    show male0 blush
    "???" "Oh Haru, you don't have to say anything."
    show male0 disapproval
    "???" "Y,know..."
    "???" "Kaoru lied about me getting expelled..."
    "???" "He just didn't want you to try looking for me anymore."
    "???" "Isn't that cruel?"
    mc "Naomi...?"
    show male0 blush
    "???" "Oh please."
    play music "audio/run.mp3" fadein 1.0 volume 0.5
    show male0 normal
    male0 "Call me Naoya."
    show male0 blush
    male0 "Hehehe."
    "A chilling feeling surrounds the air."
    "The only way I can describe this feeling..."
    "Utter fear."
    male0 "Y,know... I read the game script."
    male0 "And they all led to unhappy endings."
    male0 "Can't you see Haru?"
    male0 "I was only trying to protect you."
    male0 "So I had to kill them all."
    show male0 maniac
    male0 "AND I WOULD DO IT AGAIN IF I HAD THE CHANCE!"
    male0 "HAHAHAAHAHAHAHAHAHA!!"
    show male0 normal
    male0 "I know what's best for you!"
    show male0 blush
    male0 "I know what's best for you!!"
    play sound "audio/error.wav"
    show male0 glitching
    pause (0.5)
    play sound "audio/error.wav"
    male0 "I know what's best for you!"
    show male0 maniac
    male0 "ONLY I KNOW!"
    show male0 disapproval
    male0 "Even if that means killing everyone."
    male0 "Killing every single person on this Earth."
    male0 "So why don't you love me?"
    mc "..."
    show male0 normal
    male0 "Hey, Haru Chan."
    male0 "You know that I love you right? I wouldn't let anyone hurt you."
    show male0 glee
    male0 "So why don't we get along? Just for old times sake?"
    male0 "Afterall, you trust me right?"
    show male0 normal
    male0 "Also, if you have a long day ahead of you I'd recommend that you quit the game now."
    $ persistent.save = True
    male0 "Don't worry, it will save."
    male0 "Final warning."

    label finalsave:
    stop music
    scene bg past1
    show male0 glee
    male0 "Ookay! Back to the game!"

    show male0 blush
    male0 "Haruuuu... You trust me right?"
    male0 "Of course you do, I'm your best friend, so why wouldn't you?"
    show male0 maniac
    male0 "You have to trust me."
    mc "..."
    mc "You're insane."
    mc "Why would you do this?!"
    show male0 shock
    male0 "Because I love you.{nw}"
    play sound "audio/glitch.wav"
    show naoya glitching
    pause (0.5)
    stop sound
    play sound "audio/error.wav"
    scene stare_red
    pause (0.2)
    scene stare_glitch
    pause (0.1)
    scene bg blank
    centered "Escape."
    centered "You must escape."
    $ persistent.escape = True
    $ renpy.quit(relaunch=True, status=0, save=True)
    $ persistent.restartnum = 0

    label eyes_poked:
    $ persistent.eyes_poked = True
    $ renpy.quit(relaunch=False, status=0, save=True)

    label escape:
    if persistent.eyes_poked:
        stop music
        scene bg dashutsu with fade
        show naoya upset with dissolve
        $ achievement.grant("eye_achievement")
        $ achievement.sync()
        male0 "Ow, you poked me in the eyes!"
        $ persistent.eyes_poked = False

    if persistent.restartnum == 0:
        stop music
        play music "audio/run.mp3" fadein 1.0 volume 0.5
        scene bg dashutsu with fade
        show naoya stare with dissolve
        male0 "What do you think of the nice set up I have here?"
        mc "..."
        male0 "What?"
        male0 "You want to escape?"
        male0 "Haha..."
        male0 "Don't make me laugh."
        male0  "You can't escape now..."
        male0 "Even if you try..."
        male0 "It's useless."
        male0 "Don't even try pressing alt+f4 or closing out the window."
        male0 "You're stuck here forever now."
        jump dashutsu

    if persistent.restartnum == 1:
        stop music
        play music "audio/run.mp3" fadein 1.0 volume 0.5
        scene bg dashutsu with fade
        show naoya stare with dissolve
        male0 "Oh, you tried escaping but you can't  close the window?"
        male0 "Hmmmm..."
        male0 "Maybe try pressing the windows key and going to your task manager?"
        male0 "You can try closing the window from there maybe..."
        male0 "Just press quit task."
        male0 "I'll be here waiting for you until you come back."
        jump dashutsu

    if persistent.restartnum == 2:
        if not persistent.secondtry:
            stop music
            play music "audio/run.mp3" fadein 1.0 volume 0.5
            scene bg dashutsu with fade
            show naoya stare with dissolve
            male0 "Haha, just kidding."
            male0 "I know that THAT won't even work."
            male0 "How about we play a game of 20 questions instead?"
            male0 "Or in this case, infinite questions!"
            male0 "We could get to know each other better."
            male0 "Let's start!"
            male0 "I'm thinking of something... something very weak and frail."

            menu:
                "Is it living?":
                    "Well, not anymore I guess."
                    pass
                "Is it small?":
                    "I guess you could say that."
                    pass

            menu:
                "Is it round?":
                    "I don't think so..."
                    pass
                "Is it flat?":
                    "Nah."
                    pass

            menu:
                "Is it something important?":
                    "Definately not."
                    pass
                "Does it have legs?":
                    "Yea, it has legs."
                    pass

            menu:
                "Is it an animal?":
                    "It might as well be."
                    pass
                "Is it a person?":
                    "I guess you could say that."
                    pass

            menu:
                "Is it a student?":
                    "Used to be"
                    pass
                "Is it an adult?":
                    "No?"
                    pass

            menu:
                "Yuusuke?":
                    "Who?"
                    pass
                "Hiro":
                    "As much as I hate that thing I'm afraid to say that that was not who was on my mind."
                    "Good guess though."
                    pass

            menu:
                "Kaoru?":
                    "Nope."
                    "It was Ishida."
                    "I know you still have 14 questions left, but I'm kinda getting bored of this game."
                    pass
                "Ishida?":
                    "Haha, how could you have guessed?"
                    "In only 6 guesses too, Impressive"
                    pass



            $ persistent.secondtry = True
        jump dashutsu

    if persistent.restartnum == 10:
        stop music
        play music "audio/run.mp3" fadein 1.0 volume 0.5
        scene bg dashutsu with fade
        show naoya stare with dissolve
        male0 "Don't you get tired of doing that?"
        male0 "Just quit it."
        male0 "You're not escaping anyways."
        jump dashutsu

    if persistent.restartnum == 15:
        stop music
        play music "audio/run.mp3" fadein 1.0 volume 0.5
        scene bg dashutsu with fade
        show naoya stare with dissolve
        male0 "..."
        male0 "I think you should've realized by now that the game can't close no matter what you do."
        male0 "Why don't you try talking to me instead?"
        jump dashutsu

    if persistent.restartnum >= 100:
        stop music
        scene bg blank with fade
        centered "Okay, at this point I just feel really bad for you."
        centered "So I'm just gonna let you escape now."
        $ achievement.grant("hundred_achievement")
        $ achievement.sync()
        jump dashutsu_after

    stop music
    play music "audio/run.mp3" fadein 1.0 volume 0.5
    scene bg dashutsu with fade
    show naoya stare with dissolve
    male0 "Hello there."

    default dashutsu_end = False
    default status = "alert"
    default escpoints = 3
    $ escpoints = 3
    jump dashutsu

    label dashutsu:
    scene bg dashutsu with fade
    show naoya stare with dissolve
    label dashutsu1:
    call screen dashutsu_game with dissolve

    label dashutsu2:
    scene bg dashutsu with fade
    show naoya read2 with dissolve
    male0 "I'm back."
    male0 "Did'ja miss me?"
    call screen dashutsu_game with dissolve

    label dashutsu3:
    scene bg dashutsu with fade
    show naoya read2 with dissolve
    male0 "You're back already?"
    male0 "That was quick."
    male0 "Let me go get my pencil and paper."
    scene bg blank with fade
    $ status = "alert"
    pause (2.0)
    scene bg dashutsu
    show naoya write
    with fade
    male0 "Alright, lets get started."
    call screen dashutsu_game with dissolve

    label dashutsu4:
    $ status = "alert"
    scene bg dashutsu
    show naoya write
    with fade
    male0 "What took you so long?"
    male0 "I was waiting for you, yknow."
    male0 "It shouldn't take that long for girls to use the bathroom, right?"
    male0 "I would know from first-hand experience."
    male0 "Anyways, I think I'm almost done."
    male0 "Hurry up so we can check our answers when we finish."
    call screen dashutsu_game with dissolve

    label dashutsu5:
    $ status = "alert"
    scene bg dashutsu
    show naoya stare
    with fade
    male0 "I just woke up."
    call screen dashutsu_game with dissolve

    label escape2:
    scene bg dashutsu
    show naoya read1
    with fade
    call screen dashutsu_game with dissolve

    label escape3:
    scene bg dashutsu
    show naoya write
    with fade
    call screen dashutsu_game with dissolve

    label escape4:
    scene bg dashutsu
    if status == "alert":
        show naoya stare
    elif status == "sleeping":
        show naoya sleep
    with fade
    call screen dashutsu_game with dissolve

    screen dashutsu_game:
        add "images/escape notepad.png" xalign 0 yalign 0
        if not dashutsu_end:
            textbutton _("{size=20}Talk{/size}") xpos 102 ypos 125 focus_mask True action Jump("dashutsu_talk") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/choice_click.wav"
            textbutton _("{size=20}Think{/size}") xpos 102 ypos 180 focus_mask True action Jump("dashutsu_think") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/choice_click.wav"
            textbutton _("{size=20}Escape{/size}") xpos 102 ypos 238 focus_mask True action Jump("dashutsu_escape") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/choice_click.wav"
        else:
            textbutton _("{size=20}???{/size}") xpos 102 ypos 125 focus_mask True action Jump("dashutsu_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/choice_click.wav"
            textbutton _("{size=20}???{/size}") xpos 102 ypos 180 focus_mask True action Jump("dashutsu_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/choice_click.wav"
            textbutton _("{size=20}???{/size}") xpos 102 ypos 238 focus_mask True action Jump("dashutsu_after") hovered [Play("sound", "audio/choice_click.wav")] activate_sound "audio/choice_click.wav"

        imagebutton:
            xpos 545
            ypos 200
            idle "blindspot.png"
            if  persistent.eyes_poked:
                action Quit(confirm=False)
            action Jump("eyes_poked")


        if escpoints == 3:
            add "images/escape heart3.png" xalign 0.95 yalign .95
        elif escpoints == 2:
            add "images/escape heart2.png" xalign 0.95 yalign 0.95
        elif escpoints == 1:
            add "images/escape heart1.png" xalign 0.95 yalign 0.95

        if status == "alert":
            add "images/ct_status alert.png" xalign 0 yalign 0
        elif status == "reading":
            add "images/ct_status reading.png" xalign 0 yalign 0
        elif status == "distracted":
            add "images/ct_status distracted.png" xalign 0 yalign 0
        elif status == "sleeping":
            add "images/ct_status sleeping.png" xalign 0 yalign 0
        elif status == "away":
            add "images/ct_status away.png" xalign 0 yalign 0
        elif status == "error":
            add "images/ct_status error.png" xalign 0 yalign 0

    label dashutsu_talk:
        default talk = 0
        if status == "away":
            jump d_escape
        elif talk == 10:
            jump d_talk10
        elif talk == 9:
            jump d_talk9
        elif talk == 8:
            jump d_talk8
        elif talk == 7:
            jump d_talk7
        elif talk == 6:
            jump d_talk6
        elif talk == 5:
            jump d_talk5
        elif talk == 4:
            jump d_talk4
        elif talk == 3:
            jump d_talk3
        elif talk == 2:
            jump d_talk2
        elif talk == 1:
            jump d_talk1
        elif talk == 0:
            jump d_talk0

        label d_talk0:
        mc "How long are you going to keep me here for?"
        male0 "All eternity."
        male0 "I mean, theres no way I'm letting you out of my sight ever again."
        male0 "I didn't think you'd actually go through with it though."
        mc ". . ."
        mc "With what?"
        male0 "Y,know..."
        male0 "The whole harem thing."
        male0 "I've known you for the longest time, you've never been interested in guys."
        male0 "I honestly thought Ishida was a turn off."
        male0 "Afterall, how could you fall for such a dork like him?"
        male0 "The whole harem thing was a joke."
        male0 "Do you think those actually exist in the real world?"
        male0 "Unless, you're into polyamory or something..."
        male0 "I thought you'd laugh it off..."
        male0 "But I guess this is what I get for testing my boundaries."
        male0 "I just couldn't stand watching every single guy win you over while I had to wait on the sidelines."
        male0 "You understand how I feel right?"
        mc ". . ."
        $ talk = 1
        jump dashutsu

        label d_talk1:
        male0 "Hmmm? What is it?"
        male0 "Oh, you want to find a way out?"
        male0 "Hahaha, sorry, no can do."
        male0 "If you want to do something, my best bet is that we either sit here and play rock paper scissors or read a book."
        mc "..."
        mc "Do you think you could go get one for me?"
        mc "A book I mean."
        male0 "Oh, sure."
        male0 "I think they're in the library, let me go check."
        male0 "Oh yea, I forgot to ask."
        male0 "What genre do you like?"

        label choices26:
            menu:
                "Romance":
                    pass
                "Horror":
                    pass
                "Comedy":
                    pass
                "Historical Fiction":
                    pass
        male0 "Nevermind, you don't have to answer that I already know what you like."
        male0 "I'll go get a book for myself too."
        male0 "Maybe we could read together."
        male0 "..."
        male0 "Don't you dare think about escaping while I'm gone okay?"
        centered "{w=2}{nw}"
        scene bg blank with fade
        centered "He's gone"
        centered "Now's your chance."
        scene bg dashutsu with fade
        $ talk = 2
        $ status = "away"
        jump dashutsu1

        label d_talk2:
            show naoya read2
            male0 "So..."
            male0 "Did you have a nice break in the hallways?"
            mc "!!!" with vpunch
            male0 "Hehe, don't worry, I already know that you searched through my bag."
            male0 "You have the key right?"
            male0 "Now be a good girl and give me back the key."
            menu:
                "Give him the key.":
                    pass
                "Don't give him the key.":
                    jump dashutsu_gameover
            male0 "Good girl."
            $ status = "reading"
            $ talk = 3
            jump escape2

        label d_talk3:
            show naoya read1
            mc ". . ."
            show naoya read2
            male0 "What is it?"
            male0 "Is something bothering you?"
            mc "Whats going on?"
            male0 "Oh?"
            male0 "You mean the school?"
            male0 "You're probably wondering why everything is black and white."
            male0 "Yea..."
            male0 "Warping time and space does that."
            male0 "I think you probably noticed that theres no one at the school."
            male0 "Also..."
            male0 "Its really dark in here."
            male0 "I don't think you can really see anything in here."
            male0 "Be careful not to bump into anything though."
            $ talk = 4
            jump escape2

        label d_talk4:
            show naoya read2
            male0 "Hi."
            male0 "Do you need something?"
            mc "Uhm..."
            mc "What about school?"
            male0 "Oh yea, school."
            show naoya read1
            male0 "So last week we were reviewing quadratic equations right?"
            mc "Uh... I guess?"
            show naoya read2
            male0 "Haru Chan, you never study do you?"
            male0 "But you know what, I'm giving you a free pass."
            male0 "We might be stuck in time and space but you still have to take care of your education."
            male0 "You can borrow the keys, you might be able to find some textbooks outside."
            male0 "When you come back, we could go over some equations."
            $ talk = 5
            $ status = "distracted"
            jump escape2

        label d_talk5:
            if not esc_memory2:
                male0 "Hold on, I'm reading something."
                jump escape2
            else:
                male0 "Whats up?"
                mc "What number are you on?"
                male0 "Oh, I'm on 17."
                male0 "You?"
                mc ". . ."
                mc "5."
                male0 "You're not a fast one are ya?"
                male0 "Lets see..."
                male0 "..."
                male0 "Alright, this question is fairly simple, all you have to do is combine like terms, then factor."
                mc "I see..."
                $ talk = 6
                jump escape3

        label d_talk6:
            mc "Can I ask you something?"
            male0 "Oh, sure, whats up?"
            mc "I have to go to the bathroom."
            mc "Can I go?"
            male0 "..."
            male0 "Let me think about it..."
            male0 ". . ."
            male0 "Okay, I guess you could go."
            male0 "Just don't take too long okay?"
            male0 "I'll miss you."
            $ status = "distracted"
            $ talk = 7
            jump escape3

        label d_talk7:
            if not esc_memory3:
                "He's solving equations."
                jump escape3
            else:
                show naoya stare with fade
                male0 "I think I'm done."
                male0 "How about you?"
                mc ". . ."
                male0 "Still not done yet?"
                male0 "Its okay."
                male0 "I can wait for you to finish."
                male0 "Take your time."
                $ talk = 8
                jump escape4

        label d_talk8:
            male0 "Oh, did you get me something?"
            male0 "A melon tea?"
            male0 "Awe, thats so sweet of you."
            show naoya upset
            male0 "Wait..."
            male0 "It's been opened."
            mc "Oh... thats because..."
            mc "I test drank it before giving it to you!"
            mc "I wanted to make sure you like it."
            show naoya stare
            male0 "Aweee."
            male0 "Thats adorbs."
            male0 "Well, I guess, since you drank from it already you could consider this an indirect kiss."
            male0 "Hehe, just kidding."
            male0 "Or not."
            $ talk = 9
            jump escape4

        label d_talk9:
            show naoya reflect
            male0 "Y,know..."
            male0 "Looking back at my old life it was quite a handful looking after my younger sister and all."
            male0 "You might not really notice it at first..."
            male0 "But my step-mom always tells me to look after her because she has autism."
            show naoya upset
            male0 "Alot of people just think that she's shy."
            male0 "She just has a hard time communicating with people, thats all."
            show naoya reflect
            male0 "Other than that she can pretty much handle herself but..."
            show naoya upset
            male0 "My parents insist that she needs extra help."
            male0 "It can get quite annoying sometimes."
            show naoya reflect
            male0 "..."
            male0 "Man, I'm feeling kind of tired about now."
            show naoya upset
            male0 "Like, its really quiet..."
            male0 "Theres nobody else around."
            male0 "Just me and you..."
            show naoya stare
            male0 "Its quite peaceful."
            male0 "I could stay like this forever."
            scene bg blank with fade
            centered "{size=30}A few minutes later{/size}"
            scene bg dashutsu with fade
            show naoya sleep with dissolve
            "..."
            "He's knocked out cold."
            $ status = "sleeping"
            $ talk = 10
            jump escape4

        label d_talk10:
            male0 ". . ."
            jump escape4

        label d_escape:
            scene bg blank with fade
            centered "He's gone."
            centered "Try to use this time to escape instead."
            scene bg dashutsu with fade
            jump dashutsu1

    jump dashutsu

    label dashutsu_think:
        if talk == 10:
            jump d_think10
        elif talk == 9:
            jump d_think9
        elif talk == 8:
            jump d_think8
        elif talk == 7:
            jump d_think7
        elif talk == 6:
            jump d_think6
        elif talk == 5:
            jump d_think5
        elif talk == 4:
            jump d_think4
        elif talk == 3:
            jump d_think3
        elif talk == 2:
            jump d_think2
        elif talk == 1:
            jump d_think1
        elif talk == 0:
            jump d_think0

        label d_think0:
            "Maybe try talking to him?"
            jump dashutsu
        label d_think1:
            "I should be able to convince him somehow..."
            jump dashutsu
        label d_think2:
            if not esc_memory1:
                mc "(I think he's gone.)"
                mc "(Quick, I should start looking around for stuff before he comes back!)"
                jump dashutsu1
            else:
                "He seems calm."
                "Is there something on his mind?"
                jump escape2

        label d_think3:
            "He's reading his book."
            jump escape2

        label d_think4:
            "Maybe I should try asking him another question?"
            jump escape2

        label d_think5:
            if not esc_memory2:
                mc "(He said I could look around.)"
                mc "(Strange.)"
                jump escape2
            else:
                "He seems calm."
                "Is there something on his mind?"
                jump escape3


        label d_think6:
            "He's doing some equations."
            jump escape3

        label d_think7:
            "..."
            jump escape3

        label d_think8:
            "I should try giving him the drink I found earlier."
            "He should knock out from the sleeping pills I mixed in there."
            jump escape4

        label d_think9:
            "It should take a while."
            jump escape4

        label d_think10:
            "He's asleep."
            "I should find a way out before he wakes up."
            jump escape4


    label dashutsu_escape:
        scene bg blank
        pause (2.0)
        if status == "alert":
            label dashutsu_gameover:
            stop music
            play sound "audio/stab.mp3"
            show flash red
            pause (3.0)
            centered "It's no use trying to escape."
            $ renpy.quit(relaunch=True, status=0, save=True)
        elif status == "reading":
            stop music
            play sound "audio/stab.mp3"
            show flash red
            pause (3.0)
            centered "It's no use trying to escape."
            $ renpy.quit(relaunch=True, status=0, save=True)



        default esc_key1 = False
        default esc_key2 = False
        default esc_key3 = False
        default esc_key4 = False
        default esc_key5 = False
        default esc_note1 = False
        default esc_idea1 = False
        default esc_pills = False
        default esc_melontea = False
        default esc_boxcutter = False

        default esc_memory1 = False
        default esc_memory2 = False
        default esc_memory3 = False
        default esc_memory4 = False
        default esc_memory5 = False
        default esc_memory6 = False

        default esc_memory1_unlocked = False
        default esc_memory2_unlocked = False
        default esc_memory3_unlocked = False
        default esc_memory4_unlocked = False
        default esc_memory5_unlocked = False
        default esc_memory6_unlocked = False

        label escroom1:
        call screen esc_room1 with dissolve
        label escroom1_bag:
            scene bg blank with fade
            if not esc_key1:
                show hr_thoughts with dissolve
                centered "It's Naoya's bag."
                centered "He left the key in here."
                centered "Why would he leave this behind?"
                centered "Did he want me to find this?"
                centered "Maybe he's testing me."
                centered "I should take it just incase."
                hide hr_thoughts
                $ esc_key1 = True
                jump escroom1
            else:
                show hr_thoughts with dissolve
                centered "I already searched this."
                hide hr_thoughts
                jump escroom1
        label escroom1_trash:
            scene bg blank with fade
            show hr_thoughts with dissolve
            centered "Its a pile of trash."
            centered "Doesn't seem very useful."
            hide hr_thoughts
            jump escroom1
        label escroom1_worksheet:
            if escpoints == 2:
                scene bg blank with fade
                show hr_thoughts with dissolve
                centered "Just a math worksheet."
                hide hr_thoughts with dissolve
                scene bg blank with fade
                centered "{size=30}You lost a heart.{/size}"
                $ escpoints -= 1
                jump escroom1
            else:
                jump escroom1
        label escroom1_kokuban:
            scene kokuban
            pause
            scene bg blank
            jump escroom1


        label escroom2:
        if not esc_key1:
            scene bg blank with fade
            show hr_thoughts with dissolve
            centered "This door is locked."
            hide hr_thoughts
            jump escroom1
        else:
            call screen esc_room2
        label escroom2_poster:
            if not esc_memory1_unlocked:
                scene bg blank with fade
                show hr_thoughts with dissolve
                centered "Its the poster for the art club."
                centered "I made it with my friend Nao."
                hide hr_thoughts with fade
                play sound "audio/unlock.wav"
                $ esc_memory1_unlocked = True
                centered "You've unlocked a memory."
            else:
                scene bg blank with fade
                show hr_thoughts with dissolve
                centered "I already saw this."
                hide hr_thoughts with fade
            jump escroom2
        label escroom2_paper:
            scene bg blank with fade
            show hr_thoughts with dissolve
            centered "Some paperwork from Kaoru's office has dropped on the floor."
            centered "Theres a note."
            centered "\"To do list:\nFinish council committee's approval form,\nOrganize Hiro's paper work,\nMeet with headmaster,\nRespond to headmaster's voicemails.\""
            centered "It seems as if Kaoru is doing Hiro's portion of his work."
            centered "Is that why he kept getting so many calls?"
            hide hr_thoughts
            jump escroom2


        label escroom3:
        call screen esc_room3
        label escroom3_pills:
            scene bg blank with fade
            if not esc_memory3:
                show hr_thoughts with dissolve
                centered "Its a bottle of sleeping pills."
                centered "Maybe I could use these."
                centered "I just need a drink or something to put them in."
                $ esc_pills = True
                $ esc_memory3_unlocked = True
            else:
                show hr_thoughts with dissolve
                centered "I already took some of these."
            hide hr_thoughts
            jump escroom3
        label escroom3_drawing:
            scene bg blank with fade
            show hr_thoughts with dissolve
            centered "Its a kid's drawing of a happy family."
            centered "I wonder if the nurse has a kid."
            hide hr_thoughts
            jump escroom3


        label escroom4:
        call screen esc_room4
        label escroom4_trash:
            if escpoints == 1:
                scene bg blank with fade
                show hr_thoughts with dissolve
                centered "Its just more trash."
                centered "Nothing useful."
                centered "Wait, there's a notebook in here."
                scene bg blank
                show notebook
                pause
                show shade with dissolve
                pause
                centered "Dear Haru,{p}I just want you to know...{p} if you find this{p}promise me that you'll be okay, alright?"
                centered "- Hiro"
                hide notebook
                hide hr_thoughts
                $ escpoints -= 1
                scene bg blank with fade
                centered "{size=30}You lost all of your hearts.{/size}"
                centered "{size=30}Now, Nao hates you.{/size}"
                jump dashutsu_end
            else:
                jump escroom4
        label escroom4_heart:
            if escpoints == 3:
                scene bg blank with fade
                show hr_thoughts with dissolve
                centered "The last day marked on the calendar was a couple weeks ago."
                centered "..."
                centered "Poor Hiro."
                hide hr_thoughts with dissolve
                $ escpoints -= 1
                scene bg blank with fade
                centered "{size=30}You lost a heart.{/size}"
            else:
                jump escroom4
            jump escroom4
        label escroom4_item1:
            scene bg blank with fade
            if not esc_boxcutter:
                show hr_thoughts with dissolve
                centered "There it is."
                play sound "audio/unlock.wav"
                centered "Got it."
                centered "The box cutter."
                $ esc_boxcutter = True
            else:
                show hr_thoughts with dissolve
                centered "I already used this."
            hide hr_thoughts
            jump escroom4
        label escroom4_item2:
            if not esc_key4:
                scene bg blank
                show hr_thoughts
                with fade
                centered "It's locked."
                hide hr_thoughts
            else:
                if not esc_key5:
                    scene bg blank with fade
                    show hr_thoughts with dissolve
                    centered "Theres something in his desk."
                    centered "Another key?"
                    centered "Are there keys all over the place?"
                    $ esc_key5 = True
                else:
                    scene bg blank with fade
                    show hr_thoughts with dissolve
                    centered "I don't see anything else in this drawer."
            hide hr_thoughts
            jump escroom4


        label escroom5:
        call screen esc_room5
        label escroom5_item1:
            scene bg blank with fade
            show hr_thoughts with dissolve
            centered "Theres something shining in the foilage."
            play sound "audio/unlock.wav"
            centered "Its a key."
            hide hr_thoughts
            $ esc_key2 = True
            jump escroom5
        label escroom5_item2:
            scene bg blank with fade
            show hr_thoughts with dissolve
            centered "Something written on the board."
            centered "\"Finals week, next month! Don't forget to study!\""
            centered "I wonder who wrote this."
            hide hr_thoughts
            jump escroom5
        label escroom5_door:
            jump escroom6

        label escroom6:
        call screen esc_room6
        label escroom6_item1:
            scene bg blank with fade
            if not esc_note1:
                if not esc_key5:
                    show hr_thoughts with dissolve
                    centered "Its locked."
                    centered "It needs a key."
                    hide hr_thoughts
                    jump escroom6
                else:
                    if not esc_memory4:
                        jump escroom6
                    centered "There's something in here."
                    centered "Its a picture?"
                    play sound "audio/unlock.wav"
                    centered "You've unlocked a memory."
                    $ esc_note1 = True
                    $ esc_memory5_unlocked = True
                    hide hr_thoughts
                    jump escroom6
            else:
                centered "I searched this already."
                jump escroom6
        label escroom6_item2:
            scene bg blank with fade
            if not esc_boxcutter:
                show hr_thoughts with dissolve
                centered "Its a box."
                centered "Needs a box cutter."
                centered "Maybe I could find one in Hiro's office."
                centered "I remember opening boxes in his room."
                $ esc_idea1 = True
            else:
                if not esc_memory2:
                    show hr_thoughts with dissolve
                    centered "There are some algebra textbooks in here."
                    centered "I think Nao would need this."
                    $ esc_memory2_unlocked = True
                    hide hr_thoughts
                else:
                    show hr_thoughts with dissolve
                    centered "I already looked through this."
            hide hr_thoughts
            jump escroom6
        label escroom6_item3:
            scene bg blank with fade
            if not esc_memory4:
                show hr_thoughts with dissolve
                centered "I think I saw something outside."
                hide hr_thoughts
                jump escroom6
            if not esc_key4:
                call screen loveletters with fade
            else:
                show hr_thoughts with dissolve
                centered "I already looked through this."
                hide hr_thoughts
                jump escroom6




        label kaoru_letter1:
            show kaoru_letter1 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter2:
            show kaoru_letter2 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter3:
            show kaoru_letter3 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter4:
            show kaoru_letter4 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter5:
            show kaoru_letter5 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter6:
            show kaoru_letter6 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter7:
            show kaoru_letter7 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter8:
            show kaoru_letter8 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter9:
            show kaoru_letter9 with dissolve
            pause
            jump escroom6_item3
        label kaoru_letter0:
            show kaoru_letter0 with dissolve
            pause
            jump escroom6_item3

        label kaorus_note:
            show hr_thoughts with dissolve
            centered "Theres a note."
            centered "He left a key to Hiro's desk."
            menu:
                "Take the Key.":
                    $ esc_key4 = True
                    scene bg blank
                    jump escroom6
                "Look through the desk a bit more":
                    scene bg blank with fade
                    call screen loveletters


        label escroom7:
        call screen esc_room7

        label escroom8:
        call screen esc_room8
        label escroom8_umbrella:
            scene bg blank with fade
            if not esc_key3:
                show hr_thoughts with dissolve
                centered "Its my umbrella."
                centered "I forgot to take it home."
                centered "Huh?"
                centered "Whats this?"
                centered "Theres something inside the handle..."
                centered "It's a key and a note from Kaoru."
                centered "\"This is the key to my drawer, put it to good use.\""
                $ esc_key3 = True
                $ esc_memory4_unlocked = True
            else:
                show hr_thoughts with dissolve
                centered "I saw this already."
            hide hr_thoughts
            jump escroom8

        label escroom9:
        call screen esc_room9

        label escroom10:
        call screen esc_room10


        label escroom_memory1:
            stop music
            scene bg blank with fade
            play sound "audio/shatter.mp3"
            pause (3.0)
            scene lost memory with fade
            show text "{color=f44336}{size=30}Theres something that you forgot a long time ago but you can't remember what it is.{/size}{/color}":
                top
                yoffset 60
            with dissolve
            pause
            $ status = "alert"
            $ esc_memory1 = True
            play music "audio/run.mp3" fadein 1.0 volume 0.5
            jump dashutsu2
        label escroom_memory2:
            stop music
            scene bg blank with fade
            play sound "audio/shatter.mp3"
            pause (3.0)
            scene lost memory with fade
            show text "{color=f44336}{size=30}Theres something else that you forgot a long time ago but you can't remember what it is.{/size}{/color}":
                top
                yoffset 60
            with dissolve
            pause
            $ status = "reading"
            $ esc_memory2 = True
            play music "audio/run.mp3" fadein 1.0 volume 0.5
            jump dashutsu3
        label escroom_memory3:
            stop music
            scene bg blank with fade
            play sound "audio/shatter.mp3"
            pause (3.0)
            scene lost memory with fade
            show text "{color=f44336}{size=30}Theres something else that you forgot a long time ago but you can't remember what it is.{/size}{/color}":
                top
                yoffset 60
            with dissolve
            pause
            $ esc_memory3 = True
            play music "audio/run.mp3" fadein 1.0 volume 0.5
            scene bg blank with fade
            jump escroom3
        label escroom_memory4:
            stop music
            scene bg blank with fade
            play sound "audio/shatter.mp3"
            pause (3.0)
            mc "Ow!!!"
            "???" "Hey!"
            "???" "Watch out!"
            show bg childhood with fade
            show cg nao1 with dissolve
            bff "Do you need help?"
            mc "?"
            show cg nao2 with dissolve
            centered ""
            show cg nao3 with dissolve
            mc "Uhm, thanks."
            mc "Here's a flower."
            mc "Thanks for helping me up."
            play sound "audio/kiss.wav"
            scene bg childhood
            show cg nao4
            bff "Thanks."
            mc "Ugh!"
            scene lost memory with fade
            pause 3.0
            scene lost memory
            play sound "audio/glitter.wav"
            show found memory with dissolve
            pause 3.0
            show text "{size=30}You finally remembered something.{/size}":
                top
                yoffset 60
            with dissolve
            pause
            scene bg blank with fade
            pause (1.5)
            show hr_thoughts
            with fade
            centered "You found a bottle of melon tea right beside the bench."
            centered "Its time to head back now."
            hide hr_thoughts with fade
            scene bg blank
            $ esc_melontea = True
            $ status = "alert"
            $ esc_memory4 = True
            play music "audio/run.mp3" fadein 1.0 volume 0.5
            jump dashutsu4
        label escroom_memory5:
            stop music
            scene bg blank with fade
            play sound "audio/shatter.mp3"
            pause (1.5)
            stop music
            play sound "audio/amogus2.wav" volume 0.5 fadein 4.0
            scene bg blank
            pause (3.0)
            scene cg coma1
            pause 5.0
            scene cg coma2
            pause 5.0
            stop music
            scene bg blank
            pause (1.5)
            stop sound fadeout 1.0
            scene lost memory with fade
            show text "{color=f44336}{size=30}Theres something else that you forgot a long time ago. . .\nbut you can't quite remember what it is.{/size}{/color}":
                top
                yoffset 60
            with dissolve
            pause
            scene bg blank
            pause (3.0)
            $ esc_memory5 = True
            $ esc_memory6_unlocked = True
            play music "audio/run.mp3" fadein 1.0 volume 0.5
            jump escroom7
        label escroom_memory6:
            stop music
            scene white
            show shade
            with fade
            pause 3.0
            show awaken
            pause (10.0)
            scene bg blank with fade
            pause 3.0
            centered "Where am I?"
            $ esc_memory6 = True
            play music "audio/run.mp3" fadein 1.0 volume 0.5
            jump escroom9

        label escroom_choice:
        scene bg blank
        menu:
            "Bathroom":
                jump escroom7
            "Nurse's office":
                jump escroom3
            "Rooftop":
                jump escroom9
            "Back":
                jump escroom2

        screen esc_room1:
            add "images/esc room1.png"
            if not esc_memory1:
                imagebutton auto "images/esc_room1 bag_%s.png" xpos 760 ypos 430 action Jump("escroom1_bag") activate_sound "audio/choice_click.wav"
                if esc_memory4:
                    imagebutton auto "images/esc_room1 worksheet_%s.png" xpos 826 ypos 370 action Jump("escroom1_worksheet") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room1 trash_%s.png" xpos 225 ypos 420 action Jump("escroom1_trash") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room1 arrow_%s.png" xpos 771 ypos 298 action Jump("escroom2") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room sparkle1_%s.png" xpos 563 ypos 240 action Jump("escroom1_kokuban") activate_sound "audio/choice_click.wav"
                if esc_memory1_unlocked:
                    imagebutton auto "images/esc_room sparkle2_%s.png" xpos 315 ypos 345 action Jump("escroom_memory1") activate_sound "audio/choice_click.wav"
            else:
                imagebutton auto "images/esc_room1 bag_%s.png" xpos 760 ypos 430 action Jump("escroom1_bag") activate_sound "audio/choice_click.wav"
                if esc_memory4:
                    imagebutton auto "images/esc_room1 worksheet_%s.png" xpos 826 ypos 370 action Jump("escroom1_worksheet") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room1 trash_%s.png" xpos 225 ypos 420 action Jump("escroom1_trash") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room1 arrow_%s.png" xpos 771 ypos 298 action Jump("escroom2") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room sparkle1_%s.png" xpos 563 ypos 240 action Jump("escroom1_kokuban") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room2:
            add "images/esc room2.png"
            if not esc_memory2:
                imagebutton auto "images/esc_room2 poster_%s.png" xpos 502 ypos 287 action Jump("escroom2_poster") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room2 paper_%s.png" xpos 696 ypos 462 action Jump("escroom2_paper") activate_sound "audio/choice_click.wav"
                if esc_memory2_unlocked:
                    imagebutton auto "images/esc_room sparkle1_%s.png" xpos 377 ypos 600 action Jump("escroom_memory2") activate_sound "audio/choice_click.wav"
                if esc_memory1:
                    imagebutton auto "images/esc_room2 arrowup_%s.png" xpos 654 ypos 322 action Jump("escroom5") activate_sound "audio/choice_click.wav"
                if esc_memory2:
                    imagebutton auto "images/esc_room2 arrowdown_%s.png" xpos 608 ypos 588 action Jump("escroom_choice") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom1") activate_sound "audio/choice_click.wav"
            else:
                imagebutton auto "images/esc_room2 poster_%s.png" xpos 502 ypos 287 action Jump("escroom2_poster") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room2 paper_%s.png" xpos 696 ypos 462 action Jump("escroom2_paper") activate_sound "audio/choice_click.wav"
                if esc_memory1:
                    imagebutton auto "images/esc_room2 arrowup_%s.png" xpos 654 ypos 322 action Jump("escroom5") activate_sound "audio/choice_click.wav"
                if esc_memory2:
                    imagebutton auto "images/esc_room2 arrowdown_%s.png" xpos 608 ypos 588 action Jump("escroom_choice") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom1") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room3:
            add "images/esc room3.png"
            if not esc_memory3:
                imagebutton auto "images/esc_room3 pills_%s.png" xpos 145 ypos 487 action Jump("escroom3_pills") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room3 drawing_%s.png" xpos 847 ypos 278 action Jump("escroom3_drawing") activate_sound "audio/choice_click.wav"
                if esc_memory3_unlocked:
                    imagebutton auto "images/esc_room sparkle1_%s.png" xpos 1107 ypos 545 action Jump("escroom_memory3") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom2") activate_sound "audio/choice_click.wav"
            else:
                imagebutton auto "images/esc_room3 pills_%s.png" xpos 145 ypos 487 action Jump("escroom3_pills") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room3 drawing_%s.png" xpos 847 ypos 278 action Jump("escroom3_drawing") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom2") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room4:
            add "images/esc room4.png"
            if esc_memory1:
                imagebutton auto "images/esc_room4 heart_%s.png" xpos 1150 ypos 245 action Jump("escroom4_heart") activate_sound "audio/choice_click.wav"
            if esc_memory6:
                imagebutton auto "images/esc_room4 trash_%s.png" xpos 210 ypos 512 action Jump("escroom4_trash") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room sparkle1_%s.png" xpos 635 ypos 600 action Jump("escroom4_item1") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room sparkle2_%s.png" xpos 545 ypos 405 action Jump("escroom4_item2") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom5") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room5:
            add "images/esc room5.png"
            if not esc_key2:
                imagebutton auto "images/esc_room sparkle1_%s.png" xpos 313 ypos 422 action Jump("escroom5_item1") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room sparkle2_%s.png" xpos 58 ypos 200 action Jump("escroom5_item2") activate_sound "audio/choice_click.wav"
            if esc_key2:
                imagebutton auto "images/esc_room sparkle2_%s.png" xpos 558 ypos 312 action Jump("escroom6") activate_sound "audio/choice_click.wav"
            if esc_memory3:
                imagebutton auto "images/esc_room5 arrowleft_%s.png" xpos 34 ypos 305 action Jump("escroom8") activate_sound "audio/choice_click.wav"
            if esc_idea1:
                imagebutton auto "images/esc_room5 arrowright_%s.png" xpos 955 ypos 305 action Jump("escroom4") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom2") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room6:
            add "images/esc room6.png"
            imagebutton auto "images/esc_room sparkle2_%s.png" xpos 77 ypos 368 action Jump("escroom6_item1") activate_sound "audio/choice_click.wav"
            if esc_key3:
                imagebutton auto "images/esc_room sparkle1_%s.png" xpos 477 ypos 420 action Jump("escroom6_item3") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room sparkle1_%s.png" xpos 1025 ypos 545 action Jump("escroom6_item2") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom5") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room7:
            add "images/esc room7.png"
            if not esc_memory5:
                if esc_memory5_unlocked:
                    imagebutton auto "images/esc_room sparkle1_%s.png" xpos 167 ypos 427 action Jump("escroom_memory5") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom2") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room8:
            add "images/esc room8.png"
            if not esc_memory4:
                imagebutton auto "images/esc_room8 umbrella_%s.png" xpos 1077 ypos 299 action Jump("escroom8_umbrella") activate_sound "audio/choice_click.wav"
                if esc_key3:
                    imagebutton auto "images/esc_room8 arrow_%s.png" xpos 1071 ypos 554 action Jump("escroom10") activate_sound "audio/choice_click.wav"
                if esc_melontea:
                    imagebutton auto "images/esc_room sparkle1_%s.png" xpos 652 ypos 233 action Jump("escroom_memory4") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom5") activate_sound "audio/choice_click.wav"
            else:
                imagebutton auto "images/esc_room8 umbrella_%s.png" xpos 1077 ypos 299 action Jump("escroom8_umbrella") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room8 arrow_%s.png" xpos 1071 ypos 554 action Jump("escroom10") activate_sound "audio/choice_click.wav"
                imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom5") activate_sound "audio/choice_click.wav"
            add custom_cursor(cursorlist)

        screen esc_room9:
            add "images/esc room9.png"
            if not esc_memory6:
                if esc_memory6_unlocked:
                    imagebutton auto "images/esc_room sparkle1_%s.png" xpos 500 ypos 427 action Jump("escroom_memory6") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom2") activate_sound "audio/choice_click.wav"

        screen esc_room10:
            add "images/esc room10.png"
            if not esc_memory4:
                if esc_memory4_unlocked:
                    imagebutton auto "images/esc_room sparkle1_%s.png" xpos 757 ypos 577 action Jump("escroom_memory4") activate_sound "audio/choice_click.wav"
            imagebutton auto "images/esc_room return_%s.png" xpos 1047 ypos 24 action Jump("escroom8") activate_sound "audio/choice_click.wav"


    label dashutsu_end:
        stop music
        scene bg dashutsu with fade
        show naoya end with dissolve
        $ status = "error"
        $ dashutsu_end = True
        call screen dashutsu_game with dissolve

    label dashutsu_after:
    $ achievement.grant("escaped_achievement")
    $ achievement.sync()
    $ persistent.dashutsu_end = True
    $ persistent.escape = False
    play music "audio/ponder_ost.mp3" fadein 1.0 volume 0.5
    scene bg past1 with fade
    show shoujo1 normal with dissolve
    shoujo1 "Hello there."
    mc "?!?!?"
    show shoujo1 smug
    shoujo1 "Or should I say, long time no see?"
    mc "..."
    mc "Who are you?"
    show shoujo1 normal
    shoujo1 "Oh cmon Chiharu Chan... I know we don't get along too well, but don't you think it's rude to forget about people?"
    shoujo1 "Especially, your best friend."
    mc "You're not my best friend..."
    shoujo1 "Wow, you're really stubborn aren't you?"
    show shoujo1 smug
    shoujo1 "Well, maybe I should jog your memory a bit, since you're so insistent on forgetting who I am."
    mc "?!?!?"
    shoujo1 "Chiharu chan?"
    shoujo1 "I think its about time we stop wasting time here."
    shoujo1 "Oh, and don't worry about Naoya."
    shoujo1 "You can escape the game now if you want."
    shoujo1 "Just come back whenever you feel like it."
    shoujo1 "Don't worry, the game will save."
    mc "..."
    mc "Who are you?"
    shoujo1 "You REALLY can't remember?"
    play sound "audio/error.wav"
    show bg cyberspace_glitch behind shoujo1
    show shoujo1 smug
    shoujo1 "Well, let me jog your memory a little bit."
    shoujo1 "You've always liked going to school right?"
    shoujo1 "Even though you barely managed to pass every subject and nearly failed all of your classes, despite all the bad things, at least you're not alone at school right?"
    shoujo1 "So lets play a little game that you'd normally play with your friends to kill time during the afternoon break."
    shoujo1 "It's simple."
    shoujo1 "Rock. Paper. Scissors."
    shoujo1 "You know the rules right?"
    jump bossbattle


    default rps_beats = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]

    default player_max_hp = 150
    default boss_max_hp = 120
    default attacknum = 1

    image flash:
        "images/bg blank.png"
        0.5
        "images/white.png" with dissolve

    image moteko_bossdmg:
        "images/moteko boss.png"
        0.25
        "images/moteko boss_dmg1.png"
        0.25
        "images/moteko boss.png"

    image binary_float_one = Fixed(SnowBlossom("images/binary_one.png", 20, xspeed=(0, 0), yspeed=(-350, -125), start=15))
    image binary_float_zero = Fixed(SnowBlossom("images/binary_zero.png", 20, xspeed=(0, 0), yspeed=(-350, -125), start=15))

    transform panning_loop:
        truecenter zoom 1.0
        ease 0.9 zoom 1.1
        ease 0.9 zoom 1.0
        repeat

    image rps_scissors0:
        "images/rps_scissors1.png"
        0.20
        "images/rps_scissors2.png"
        0.20
        repeat

    default rps_dialogue = 1

    label rps_dialogue0:

        if rps_dialogue == 1 and boss_max_hp == 120:
            jump rps_dialogue1
        elif rps_dialogue == 2 and boss_max_hp == 90:
            jump rps_dialogue2
        elif rps_dialogue == 3 and boss_max_hp == 75:
            jump rps_dialogue3
        elif rps_dialogue == 4 and boss_max_hp == 60:
            jump rps_dialogue4
        elif rps_dialogue == 5 and boss_max_hp == 45:
            jump rps_dialogue5
        elif rps_dialogue == 6 and boss_max_hp == 30:
            jump rps_dialogue6
        elif rps_dialogue == 7 and boss_max_hp == 15:
            jump rps_dialogue7
        else:
            jump rps_dialogue_end

    label rps_dialogue1:
        scene bg blank
        show moteko sketch:
            truecenter zoom 2.0 ypos 550 xoffset 300
        with fade
        shoujo1 "Chiharu, Chiharu, Chiharu."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 2.0 ypos 550 xoffset -200
        shoujo1 "No matter how many times you replay through your past life memories."
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 2.5 ypos 620 xoffset -75
        shoujo1 "No matter how much you wish it could change."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 1.0
        shoujo1 "You're never going to get the happy ending that you wanted."
        shoujo1 "Do you remember the wish you made that day?"
        shoujo1 "You wanted more friends, remember?"
        $ rps_dialogue = 2
        jump rps_dialogue_end

    label rps_dialogue2:
        scene bg blank
        show moteko sketch:
            truecenter zoom 1.0
        with fade
        shoujo1 "You should know more than anyone else that Naomi would never do something like that."
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 2.5 ypos 620 xoffset -75
        shoujo1 "Wasn't she the one you trusted most?"
        shoujo1 "And even after everything you still doubt her."
        shoujo1 "She cares about you more than anybody else."
        shoujo1 "Poor girl has personal issues to deal with, her mom is dead but she still visits her grave every year on her birthday to leave her a present."
        shoujo1 "She was such a sweet girl."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 1.0
        shoujo1 "So why did you have to make her into some sort of crazy serial killer?"
        show moteko sketch:
            ease 0.5 zoom 1.5
        shoujo1 "Are you that paranoid?"
        $ rps_dialogue = 3
        jump rps_dialogue_end

    label rps_dialogue3:
        scene bg blank
        show moteko sketch:
            truecenter zoom 3.0 ypos 100 xoffset -95
            ease 2.0 zoom 3.0 ypos 700 xoffset -95
        with fade
        shoujo1 "Y,know it's really funny."
        show moteko sketch:
            ease 1.5 zoom 2.0 rotate 25 ypos 400
        shoujo1 "You act like you're the one in control here."
        show moteko sketch:
            ease 1.5 zoom 1.8 rotate -10 ypos 400
        shoujo1 "Pathetic, isn't it?"
        show moteko sketch:
            ease 1.5 zoom 1.5 rotate 0 ypos 400
        shoujo1 "Being here this long is only going to delay the inevitable."
        shoujo1 "At some point, you're going to have to come back to reality."
        shoujo1 "I'm not going to entertain your delusions."
        shoujo1 "This world isn't real, and you have to wake up."
        shoujo1 "So why don't you just give it up?"
        shoujo1 "You can't change anything."
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 2.5 ypos 620 xoffset -75
        shoujo1 "But you know that already don't know?"
        shoujo1 "So enough with the games. Stop fighting. Stop resisting. Wake up."
        $ rps_dialogue = 4
        jump rps_dialogue_end

    label rps_dialogue4:
        scene bg blank
        show moteko sketch
        with fade
        shoujo1 "I know that you probably miss all of your friends."
        shoujo1 "But its already too late to turn back."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 2.0 ypos 550 xoffset -400
        shoujo1 "After all, you already came this far."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 2.0 ypos 550 xoffset 400
        shoujo1 "Kaoru, that air-headed idiot that has too much fun messing around and doesn't know when enough means enough."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 2.0 ypos 550 xoffset -400
        shoujo1 "Hiro, that stubborn frustrating piece of trash thats difficult for no reason."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 2.0 ypos 550 xoffset 400
        shoujo1 "Yuusuke... who was he again?"
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 1.0 xoffset 0
        shoujo1 "What was he, some sort of imaginary friend?"
        shoujo1 "Did you know how crazy you looked talking to thin-air?"
        shoujo1 "I feel sorry for your friends."
        shoujo1 "But wait I have good news for you."
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 2.5 ypos 620 xoffset -75
        shoujo1 "It never even happened."
        $ rps_dialogue = 5
        jump rps_dialogue_end


    label rps_dialogue5:
        scene bg blank
        show moteko sketch
        with fade
        shoujo1 "Then there was Ishida."
        shoujo1 "You miss him the most don't you?"
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 3.5 rotate 180 yoffset 1800 xoffset 100
        shoujo1 "I'm sorry to break it to you Haru chan, but he was never interested in you to begin with."
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 3.5 rotate 90 yoffset 2300 xoffset 100
        shoujo1 "You spent your whole life chasing after high school boys."
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 3.5 rotate 270 yoffset 2200 xoffset 100
        shoujo1 "And you ended up hurting the person that was closest to you."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 1.0 rotate 0 yoffset 0 xoffset 0
        shoujo1 "And who was that, you may ask?"
        $ rps_dialogue = 6
        jump rps_dialogue_end

    label rps_dialogue6:
        scene bg blank
        centered "Did you guess?"
        centered "It was Naomi."
        centered "Your best friend."
        centered "Remember?"
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 1.0
        with vpunch
        shoujo1 "The one that you threw under the bus?"
        play sound "audio/error.wav"
        show moteko sketch:
            zoom 2.5 ypos 620 xoffset -75
        with vpunch
        shoujo1 "The one that you abandoned."
        play sound "audio/error.wav"
        show moteko sketch:
            truecenter zoom 1.0
        with vpunch
        shoujo1 "She supported you this entire time."
        shoujo1 "You honestly deserve this."
        shoujo1 "You don't deserve any pity."
        $ rps_dialogue = 7
        jump rps_dialogue_end

        label rps_dialogue7:
            show moteko sketch:
                truecenter zoom 1.0
            with fade
            shoujo1 "If you're that miserable, maybe you should be careful for what you wish for next time."
            shoujo1 "Oh wait, there won't be a next time, oops."
            shoujo1 "Well, either way fighting isn't going to do you any good."
            play sound "audio/error.wav"
            show moteko sketch:
                truecenter zoom 2.0 yoffset 200 xoffset -50
            shoujo1 "Even if you fight, you're not winning no matter what you do."
            shoujo1 "Quit wasting time."
            play sound "audio/error.wav"
            show moteko sketch:
                truecenter zoom 8.5 yoffset 825 xoffset -210
            shoujo1 "Give up."
            $ rps_dialogue = 8
            jump rps_dialogue_end

        label rps_dialogue_end:
        if (rps_player, rps_npc) in rps_beats:
            jump hitboss
        elif (rps_npc, rps_player) in rps_beats:
            jump attack
        else:
            jump rps_tie

        label hitboss:
            $ boss_max_hp -= 15
            scene bg cyberspace
            show moteko boss
            with fade
            play sound "audio/explode.wav"
            show moteko_bossdmg
            centered "{w=2}{nw}"
            "Attack was effective.{w=2}{nw}"
            centered "{nw}"
            jump endturn

        label rps_tie:
            scene bg cyberspace
            show moteko boss
            with fade
            centered "{w=1}{nw}"
            play sound "audio/fail.wav"
            "Attack was ineffective.{w=2}{nw}"
            centered "{nw}"
            jump endturn


    label bossbattle:
        $ player_max_hp = 150
        $ boss_max_hp = 120
        $ rps_dialogue = 1

        play music "audio/electric.mp3" fadein 1.0 volume 0.5
        scene bg blank with fade
        pause 1.0
        show moteko boss with dissolve:
            truecenter zoom 3.0 ypos 100 xoffset 65
            ease 5.0 zoom 3.0 ypos 800 xoffset 65
        pause 5.0
        play sound "audio/typing.wav"
        centered "{size=45}{b}{color=#61fadb}{font=binxchr.ttf}{cps=15}Your Best Friend Moteko.{/cps}{/font}{/color}{/b}{w=1}{nw}{/size}"
        scene white with dissolve
        pause 1.0
        scene bg cyberspace with dissolve
        show binary_float_one
        show binary_float_zero
        with dissolve
        show moteko boss at panning_loop
        call screen stats with dissolve

    label rock:
        scene bg blank with fade
        show flash
        play sound "audio/rpsselect.wav"
        show rps_rock0:
            truecenter zoom 0.5
            ease 1.0 zoom 1.0
            ease 0.5 rotate 360
        centered "{w=2}{nw}"
        scene bg blank with fade
        play sound "audio/rps.wav"
        centered "{size=50}{color=#ffffff}{b}You played rock.{/b}{/color}{/size}{w=2.5}{nw}" with dissolve
        hide rps_rock0
        $ rps_player = "rock"
        $ rps_npc = renpy.random.choice(["rock", "paper", "scissors"])
        if (rps_player, rps_npc) in rps_beats:
            jump rps_dialogue0

        elif (rps_npc, rps_player) in rps_beats:
            jump rps_dialogue0

        else:
            jump rps_dialogue0


    label scissors:
        scene bg blank with fade
        show flash
        play sound "audio/rpsselect.wav"
        show rps_scissors1:
            truecenter zoom 0.5
            ease 1.0 zoom 1.0
            ease 0.5 rotate 360
        centered "{w=1.5}{nw}"
        hide rps_scissors1
        show rps_scissors0
        centered "{w=0.5}{nw}"
        scene bg blank with fade
        pause 1.0
        play sound "audio/rps.wav"
        centered "{size=50}{color=#ffffff}{b}You played scissors.{/b}{/color}{/size}{w=2.5}{nw}"
        hide rps_scissors0
        $ rps_player = "scissors"
        $ rps_npc = renpy.random.choice(["rock", "paper", "scissors"])
        if (rps_player, rps_npc) in rps_beats:
            jump rps_dialogue0
        elif (rps_npc, rps_player) in rps_beats:
            jump rps_dialogue0
        else:
            jump rps_dialogue0

    label paper:
        scene bg blank with fade
        play sound "audio/rpsselect.wav"
        show rps_paper0:
            truecenter zoom 0.5
            ease 1.0 zoom 1.0
            ease 0.5 rotate 360
        centered "{w=2}{nw}"
        scene bg blank with fade
        play sound "audio/rps.wav"
        centered "{size=50}{color=#ffffff}{b}You played paper.{/b}{/color}{/size}{w=2.5}{nw}" with dissolve
        hide rps_paper0
        $ rps_player = "paper"
        $ rps_npc = renpy.random.choice(["rock", "paper", "scissors"])
        if (rps_player, rps_npc) in rps_beats:
            jump rps_dialogue0

        elif (rps_npc, rps_player) in rps_beats:
            jump rps_dialogue0

        else:
            jump rps_dialogue0

    label endturn:
        if boss_max_hp <= 0:
            stop music
            scene bg blank
            show moteko boss
            with dissolve
            pause 1.0
            play sound "audio/defeat.wav"
            show moteko boss_dmg1
            pause 0.15
            show moteko boss
            pause 0.15
            show moteko boss_dmg1
            pause 0.15
            show moteko boss
            pause 0.15
            show moteko boss_defeat
            pause 1.0
            scene bg blank with fade
            pause 2.0
            centered "You defeated Moteko."
            centered "Or did you?"
            $ persistent.moteko_defeat = True
            jump lastscene

        elif player_max_hp <= 0:
            stop music
            scene bg blank with fade
            centered "Your health points reached zero."
            centered "You've lost."
            jump finalboss_endgame

        scene bg cyberspace with dissolve
        show binary_float_one
        show binary_float_zero
        with dissolve
        show moteko boss at panning_loop
        call screen stats with dissolve

    label attack:
        init python:
            import random
        $ attack_num = renpy.random.randint(1,5)
        image attack1:
            "images/scribble1.png"
            0.15
            "images/scribble2.png"
            0.15
            "images/scribble3.png"
            0.15
            "images/scribble4.png"
            0.15
            "images/scribble3.png"
            0.15
            "images/scribble2.png"
            0.15
            repeat

        image attack2 = Movie(size = (1280, 720), channel = "movie", play = "images/static.ogv", loop = True)

        image attack3:
            At("binary.png", scrollup)


        transform scrollup:
            truecenter zoom 3.0 ypos 120
            linear 0.25 zoom 3.0 ypos 620
            repeat

        image attack4:
            "images/stare_red.png"
            0.75
            "images/stare_glitch.png"
            0.25
            repeat

        image attack5:
            At("images/moteko boss.png", glitch)
            pause 0.2
            At("images/moteko boss_defeat.png", chromatic_offset)
            pause 0.15
            At("images/moteko boss.png", glitch)
            pause 0.05
            At("images/moteko boss_dmg1.png", chromatic_offset)
            pause 0.3
            At("images/moteko boss.png", glitch)
            pause 0.05
            At("images/moteko boss.png", chromatic_offset)
            pause 0.2
            "images/moteko boss_defeat.png"
            pause 0.15
            repeat

        if attack_num == 1:
            play sound "audio/dialtone.wav"
            show attack1
            pause 3.0
            scene bg blank
            play sound "audio/fail.wav"
            centered "{cps=0}{size=150}{color=#f44336}{font=DejaVuSans.ttf}-2{/font}{/color}{/size}{/cps}{w=1}{nw}" with vpunch
            $ player_max_hp -= 2

        if attack_num == 2:
            play sound "audio/static.wav"
            show attack2
            centered "{w=3}{nw}"
            scene bg blank
            play sound "audio/fail.wav"
            centered "{cps=0}{size=150}{color=#f44336}{font=DejaVuSans.ttf}-4{/font}{/color}{/size}{/cps}{w=1}{nw}" with vpunch
            $ player_max_hp -= 4
        if attack_num == 3:
            play sound "audio/beep.wav"
            scene bg blank
            show attack3
            pause 3.0
            scene bg blank
            show static
            play sound "audio/static.wav"
            centered "{w=3}{nw}"
            scene bg blank
            play sound "audio/fail.wav"
            centered "{cps=0}{size=150}{color=#f44336}{font=DejaVuSans.ttf}-5{/font}{/color}{/size}{/cps}{w=1}{nw}" with vpunch
            $ player_max_hp -= 5
        if attack_num == 4:
            play sound "audio/glitch.wav"
            scene bg blank
            show attack4
            pause 3.0
            play sound "audio/fail.wav"
            centered "{cps=0}{size=150}{color=#f44336}{font=DejaVuSans.ttf}-10{/font}{/color}{/size}{/cps}{w=1}{nw}" with vpunch
            $ player_max_hp -= 10
        if attack_num == 5:
            play sound "audio/glitch.wav"
            scene bg blank
            show attack5
            pause 3.0
            play sound "audio/fail.wav"
            centered "{cps=0}{size=150}{color=#f44336}{font=DejaVuSans.ttf}-20{/font}{/color}{/size}{/cps}{w=1}{nw}" with vpunch
            $ player_max_hp -= 20

        jump endturn



    label lastscene:
    scene bg past1 with fade
    show shoujo1 smug with dissolve
    shoujo1 "Chiharu..."
    shoujo1 "Why don't you realize that no matter how many times you replay through your past life memories..."
    shoujo1 "No matter how much you wish it could change, you're never going to get the happy ending that you wanted."
    shoujo1 "You're dead."
    shoujo1 "And all of your friends have moved on without you, Chiharu chan."
    shoujo1 "Or should I say... Yumeko?"
    mc "???"
    play sound "audio/error.wav"
    scene bg bsb1
    show shoujo1 normal
    shoujo1 "Remember the wish that you made to me that day?"
    mc "..."
    shoujo1 "\"I wish that I had friends.\""
    shoujo1 "Remember?"
    play music "audio/memory.mp3" fadein 1.0 volume 0.5
    shoujo1 "That was the wish you sold your soul to me for."
    shoujo1 "Too bad you never knew that you'd die so early."
    shoujo1 "And all of your friends..."
    shoujo1 "Ishida, the shy socially awkward closeted introvert that gained enough confidence to be himself after he met a certain group of friends."
    shoujo1 "Hiro, the frustrated rich kid with a sick mother and a scam artist for a father."
    shoujo1 "His friend, Kaoru, the hopeless people pleaser that loves messing around pulling pranks on people."
    shoujo1 "And lastly, your best friend Naomi, the tomboy that constantly hides her emotions and wears a mask to make others happy."
    shoujo1 "Afterall, you know that she would never do something like this."
    shoujo1 "Even though she was jealous of you and felt like you could never understand her..."
    shoujo1 "She still accepted you for who you were."
    shoujo1 "And it looks like you've also brought somebody with you."
    shoujo1 "Whats your name?"
    $ playername = renpy.input("{color=#000000}Whats YOUR name?{/color}")
    $ playername = playername.strip()
    if playername == "Moteko":
        show shoujo1 smug
        shoujo1 "Thats more like it."
        $ playername = "Moteko"
        show shoujo1 normal
    if playername == "moteko":
        show shoujo1 smug
        shoujo1 "Thats more like it."
        $ playername = "Moteko"
        show shoujo1 normal

    if playername == "":
        shoujo1 "I'll just name you myself if you don't wanna give yourself a name."
        $ playername = "Anonymous"

    if playername == "Yuusuke":
        show shoujo1 smug
        shoujo1 "What?"
        $ playername = "#######"
        jump error_name

    if playername == "#######":
        show shoujo1 smug
        shoujo1 "What?"
        $ playername = "Who"
        jump error_name

    label goodbye:
    shoujo1 "[playername]."
    shoujo1 "[playername], thank you for helping Yumeko throughout her journey."
    shoujo1 "But it is time for her to wake up now."
    shoujo1 "Yumeko, you can't stay here forever."
    show shoujo1 smug
    shoujo1 "Yumeko~"
    shoujo1 "It's time for you to wake up!"
    show shoujo1 normal
    shoujo1 "You can't fix your past mistakes."
    shoujo1 "You just have to live with them."
    shoujo1 "Wake up!"
    stop music
    scene bg blank
    pause (3.0)
    play music "audio/ponder_ost.mp3" fadein 1.0 volume 0.5
    scene bg ishida_game
    show cg wakeup
    with dissolve
    pause (1.5)
    shoujo2 "My name is Yumeyume Yumeko."
    shoujo2 "and I have been trapped in this game for as long as I can remember."
    shoujo2 "It was a long time ago when I played that game..."
    shoujo2 "And I still have dreams about it even now..."
    shoujo2 "Reoccuring dreams of my past life."
    shoujo2 "They still haunt me until this day."
    shoujo2 "Every night, I have a dream about me and my friends..."
    shoujo2 "And the person who took that all away from me..."
    shoujo2 "And now I am living the rest of my existence in an artificial man-made simulation."
    shoujo2 "For all eternity..."
    $ achievement.grant("endgame_achievement")
    $ achievement.sync()
    "True End"
    "Who am I kidding?"
    "Why are we still acting like this is a multiple ending game?"
    "This is the only end."
    $ persistent.endgame = True
    $ persistent.naomi = False
    $ persistent.naoya = False

    label credits:
    stop music
    #play sound "audio/dreamare.mp3" volume 1.0 fadein 1.0 fadeout 5.0
    scene bg blank
    show screen credits_screen with fade
    $ renpy.pause(90.0, hard=True)
    centered "{w=90}{nw}"
    hide screen credits_screen
    centered "And a special thanks to the Astrofunkers!"

    label grave_scene:
    stop music
    scene bg blank
    pause 5.0
    show red skies at drifting
    show cg naomi_grave1
    pause 5.0
    show cg naomi_grave2 with dissolve
    pause 5.0
    scene bg blank
    centered "Haru Chan..."
    centered "I miss you."

    $ renpy.quit(relaunch=False, status=0, save=True)

label endgame_wish:
    if persistent.no_turning_back:
        jump noturningback
    play music "audio/fuzzytube.mp3" fadein 1.0 volume 0.5
    scene bg blank with fade
    show moteko sketch with dissolve
    shoujo1 "Hello there."
    shoujo1 "I thought you would've ran away."
    shoujo1 "..."
    shoujo1 "You're probably wondering..."
    shoujo1 "What did you just see, right?"
    shoujo1 "Yeah..."
    shoujo1 "That was the last human I worked with."
    shoujo1 "She just had a bad dream."
    shoujo1 "She wasn't very happy with her wish."
    shoujo1 "And I just wanted to show you that..."
    shoujo1 "When you make a soul binding contract, you should know what you're getting yourself into first."
    shoujo1 "But selling your soul doesn't have to be such a bad thing."
    shoujo1 "Just don't be like the fool that wishes for friends."
    shoujo1 "You could wish for wealth, wisdom, immortality."
    shoujo1 "And in exchange you just have to work with me for a few thousand years in the after life."
    shoujo1 "It might sound like a lot to you humans, but I promise it will pass by in no time."
    shoujo1 "Or you could gamble your chances on ending up into heaven."
    shoujo1 "But, I'm going to be honest, that probably won't happen."
    stop music
    play sound "audio/error.wav"
    show moteko sketch:
        truecenter zoom 2.0 yoffset 200 xoffset -50
    shoujo1 "No one gets into that place."
    shoujo1 "You could make a contract with me and spend millenias in limbo, waiting for the day of redemption."
    shoujo1 "Or you could end up burning in the very depths of firey hell, for all eternity."
    shoujo1 "The chances are, you're not going to heaven anyways."
    play sound "audio/error.wav"
    show moteko sketch:
        truecenter zoom 1.0 yoffset 0 xoffset 0
    shoujo1 "That place is already full of corruption and nepotism, only people with connections can get in."
    shoujo1 "So why not enjoy your life while you can?"
    $ persistent.wishproposal = True
    label wishproposal:
    scene bg blank
    centered "{size=50}Will you make a wish?{/size}"
    menu:
        "Yes":
            shoujo1 "Wise decision."
            jump makeawish
        "No":
            shoujo1 "Still don't trust me?"
            shoujo1 "Well, feel free to come back if you ever change your mind."
            $ renpy.quit(relaunch=False, status=0, save=True)

    default playerwish = ""
    label makeawish:
        $ playerwish = renpy.input("{color=#000000}Whats your wish?{/color}")
        $ playerwish = playerwish.strip()
        if playerwish == "":
            jump nowish
        $ achievement.grant("wish_achievement")
        $ achievement.sync()
        shoujo1 "Alright, a deal's a deal."
        shoujo1 "I'm not telling you when, but it will be granted some day."
        shoujo1 "You know the price."
        shoujo1 "Oh, I also forgot to mention..."
        shoujo1 "No refunds."
        $ persistent.wish = True
        $ renpy.quit(relaunch=False, status=0, save=True)

label nowish:
    shoujo1 "Nothing, huh?"
    shoujo1 "Well, I don't have time to waste."
    shoujo1 "Come back when you decide what you want to wish for."
    $ renpy.quit(relaunch=False, status=0, save=True)

label wishgranted:
    scene bg blank with fade
    centered "Its too late to change your mind now."
    centered "Do you want to relive through your terrible dreams again?"
    menu:
        "yes":
            $ persistent._clear()
            $ persistent.no_turning_back = True
            $ renpy.quit(relaunch=False, status=0, save=True)
        "no":
            $ renpy.quit(relaunch=False, status=0, save=True)

label noturningback:
    $ achievement.grant("noreturn_achievement")
    $ achievement.sync()
    $ achievement.grant("wish_achievement")
    $ achievement.sync()
    scene bg blank with fade
    centered "You already made your wish. Remember?"
    play sound "audio/glitch.wav"
    scene bg blank
    show bsb_glitch
    $ renpy.pause(4.0, hard=True)
    centered "{w=4.0}{nw}"
    scene bg blank
    play sound "audio/beep.wav"
    show bsb_cursed
    $ renpy.pause(7.0, hard=True)
    centered "{w=7.0}{nw}"
    scene bg blank
    $ persistent._clear()
    $ renpy.quit(relaunch=False, status=0, save=True)
    return

label error_name:
    stop music
    scene bg blank
    pause (3.0)
    centered "Do you know what happens to people who wish that they never existed?"
    pause (1.0)
    centered "They become nothing."
    pause (1.0)
    centered "Is this what you wanted?"
    pause (3.0)
    centered "Where are you, you may ask?"
    pause (2.0)
    show red skies at drifting with fade
    pause (5.0)
    centered "A very dark place."
    centered "A very... very..."
    centered "dark place."
    play music "audio/tension.mp3" fadein 3.0
    centered "A long time ago, beings like you thought that everything was in their control."
    centered "Everything, right within the palms of their hands."
    centered "Convenient, isn't it?"
    centered "Well, not if you have to build everything from scratch."
    centered "So, the worlds that you created..."
    centered "I would say, were nothing short of a shoddy mess."
    centered "Absolute abominations."
    centered "You are here to witness one of those abominations."
    centered "With that being said..."
    centered "You no longer have the authority to create anything."
    centered "{cps=5}Not ever again.{/cps}"
    centered "You are nowhere."
    centered "And you will cease to be."
    centered "You cannot escape your fate."
    stop music
    scene bg blank
    centered "{color=#f44336}{b}{size=+10}{fast}{font=DejaVuSans.ttf}You know that right?{/font}{/size}{/b}{/color}"
    $ achievement.grant("vanished_achievement")
    $ achievement.sync()
    play sound "audio/static.wav"
    show static
    $ renpy.pause(3.0, hard=True)
    scene bg blank
    $ persistent._clear()
    $ renpy.quit(relaunch=False, status=0, save=False)

label complete_restart:

    $ persistent.restartnum += 1
    $ renpy.quit(relaunch=True, status=0, save=True)
    return

label reset:
    stop music
    scene bg blank
    centered "It seems that you already played a bit of this game."
    centered "So, we're going to be resetting your data in order to prevent any bugs."
    centered "Goodluck!"
    $ persistent._clear()
    $ renpy.quit(relaunch=True, status=0, save=True)

label datareset:
    if persistent.no_turning_back:
        $ persistent._clear()
        $ persistent.no_turning_back = True
        $ renpy.quit(relaunch=True, status=0, save=True)
    else:
        $ persistent._clear()
        $ renpy.quit(relaunch=True, status=0, save=True)

label choices1_endgame:
    play music("audio/sad_theme.mp3") fadein 1.0 volume 2.0
    call screen gameOver_screen0 with fade

label choices3_endgame:
    play music "audio/sad_theme.mp3" fadein 1.0 volume 2.0
    call screen gameOver_screen1 with fade

label choices9_endgame:
    play music "audio/sad_theme.mp3" fadein 1.0 volume 2.0
    call screen gameOver_screen2 with fade

label yuusukeroute_end:
    play music "audio/sad_theme.mp3" fadein 1.0 volume 2.0
    call screen gameOver_screen3 with fade

label finalboss_endgame:
    play music "audio/sad_theme.mp3" fadein 1.0 volume 2.0
    call screen gameOver_screen4 with fade
