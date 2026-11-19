################################################################################
## Meqdārdehi-ye ebtedāyi
################################################################################

init offset = -1


################################################################################
## Style-hā
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Menu-hā-ye darun-e bāzi
################################################################################


## Safhe-ye goftār #############################################################
##
## Safhe-ye goftār barā-ye namāyeš-e diālog be bāzigar estefāde mišavad. In
## safhe do pārāmetr-e who va what rā migirad, ke be tartib nām-e šaxsiyat-e
## dar hāl-e sohbat va matn-e namāyeš dāde mišavad hastand. (pārāmetr-e who dar
## surat-e adam-e zekr-e nām mitavānad None bāšad.)
##
## In safhe bāyad yek displayable-e matni bā šenāse-ye "what" besāzad, čerā ke
## Ren'Py az in barā-ye modiriyat-e namāyeš-e matn estefāde mikonad. In safhe
## hamčenin mitavānad displayable-hāyi bā šenāse-hā-ye "who" va "window" barā-ye
## e'māl-e vižegi-hā-ye style besāzad.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Agar tasvir-e kenāri vojud dāšte bāšad, bālā-ye matn namāyeš bede. Dar
    ## hālat-e guši namāyeš nade, zirā fazā-ye kāfi nist.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Ja'be-ye nām rā barā-ye style kardan az tariq-e šey'e Character mojud bekon.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos 0.5
    xanchor 0.5
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=0.5)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.5
    yalign 0.5
    textalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xanchor 0.5
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    textalign 0.5
    xalign 0.5
    adjust_spacing False

## Safhe-ye vorudi #############################################################
##
## In safhe barā-ye namāyeš-e renpy.input estefāde mišavad. Pārāmetr-e prompt
## barā-ye ersāl-e yek darxāst-e matn estefāde mišavad.
##
## In safhe bāyad yek displayable-e vorudi bā šenāse-ye "input" barā-ye daryāft-
## e pārāmetr-hā-ye vorudi-ye moxtalef besāzad.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Safhe-ye entexāb ############################################################
##
## In safhe barā-ye namāyeš-e entexāb-hā-ye darun-e bāzi-ye erā'e šode tavassot-
## e gozāre-ye menu estefāde mišavad. Tanhā pārāmetr-e ān, items, yek list az
## ašiyā' ast, ke har kodām dārā-ye xāne-hā-ye onvān va amal hastand.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action [Play("sound", "audio/select.mp3"), i.action]


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.95

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    reading_order "rtl"


## Safhe-ye menu-ye sari' ######################################################
##
## Menu-ye sari' dāxel-e bāzi barā-ye farāham kardan-e dastresi-ye sari' be
## menu-hā-ye birun-e bāzi namāyeš dāde mišavad.

screen quick_menu():

    ## Motma'en sāxtan az inke in bar ru-ye safahāt-e digar zāher bešavad.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("عقب") action Rollback()
            textbutton _("تاریخچه") action ShowMenu('history')
            textbutton _("رد کردن") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("اتوماتیک") action Preference("auto-forward", "toggle")
            textbutton _("ذخیره") action ShowMenu('save')
            textbutton _("ذخیرۀ سریع") action QuickSave()
            textbutton _("بارگذاری سریع") action QuickLoad()
            textbutton _("ترجیحات") action ShowMenu('preferences')


## In code az namāyeš dāde šodan-e safhe-ye quick_menu dāxel-e bāzi hengāmi ke
## bāzigar sarihan rābet rā penhān nakarde ast motma'en misāzad.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Safhe-hā-ye menu-ye asli va bāzi
################################################################################

## Safhe-ye peymāyeš ###########################################################
##
## In safhe dar menu-hā-ye asli va bāzi vojud dāšte, va peymāyeš be menu-hā-ye
## digar, va šoru'-e bāzi rā farāham mikonad.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("شروع") action Start()

        else:

            textbutton _("تاریخچه") action ShowMenu("history")

            textbutton _("ذخیره") action ShowMenu("save")

        textbutton _("بارگذاری") action ShowMenu("load")

        textbutton _("ترجیحات") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("پایان بازپخش") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("منوی اصلی") action MainMenu()

        textbutton _("درباره") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Komak barā-ye dastgāh-hā-ye hamrāh elzāmi va yā be ān-hā mortabet
            ## nist.
            textbutton _("کمک") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Dokme-ye xoruj dar iOS mamnu' šode va dar Android va Web elzāmi
            ## nist.
            textbutton _("خروج") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Safhe-ye menu-ye asli #######################################################
##
## Barā-ye namāyeš-e menu-ye asli hengām-e šoru'-e Ren'Py estefāde mišavad.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## In az jāygozini-ye har menu-ye digar motma'en misāzad.
    tag menu

    add gui.main_menu_background

    ## In qāb-e xāli menu-ye asli rā tiretar mikonad.
    frame:
        style "main_menu_frame"

    ## Gozāre-ye use yek safhe-ye digar rā dāxel-e in safhe šāmel mikonad. Xod-e
    ## mohtaviyāt-e menu-ye asli dar safhe-ye peymāyeš qarār dārand.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Safhe-ye menu-ye bāzi #######################################################
##
## In sāxtār-e bonyādi-ye omumi-ye safhe-ye menu-ye bāzi rā mičinad. In bā titr-
## e safhe farāxāni mišavad, va paszamine, titr, va peymāyeš rā namāyeš midahad.
##
## Pārāmetr-e scroll mitavānad None, va yā yeki az "viewport" yā "vpgrid" bāšad.
## In safhe barā-ye estefāde bā yek yā čand farzand, ke dar ān tarāgonjānide
## (qarār gerefte) šode ast dar nazar gerefte šode ast.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Fazā-ye reserve šode barā-ye baxš-e hedāyati.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("برگشت"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Safhe-ye darbāre ############################################################
##
## In safhe ettelā'āt-e e'tebār-hā (credit) va haqq-e taksir-e (copyright)
## marbut be bāzi va Ren'Py rā namāyeš midahad.
##
## Hič čiz-e xāssi darbāre-ye in safhe vojud nadārad, va az in ru in safhe yek
## mesāl az čegunegi-ye sāxt-e yek safhe-ye šaxtisāzi šode ast.

screen about():

    tag menu

    ## Gozāre-ye use šāmel-e safhe-ye game_menu-ye dāxel-e in mišavad. Farzand-e
    ## vbox pas az in dar viewport-e dāxel-e safhe-ye game_menu šāmel mišavad.
    use game_menu(_("درباره"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("نسخۀ [config.version!t]\n")

            ## gui.about ma'mulan dar options.rpy tanzim mišavad.
            if gui.about:
                text "[gui.about!t]\n"

            text _("ساخته شده با {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Safahāt-e bārgozāri vā zaxire ###############################################
##
## In safahāt be bāzigar emkān-e zaxire va bārgozāri-ye mojaddad-e bāzi rā
## midahand. Az ānjāyi ke taqriban hame čizešan moštarak ast, har do be surat-e
## yek safhe-ye sevvom, file_slots, piyādesāzi mišavand.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("ذخیره"))


screen load():

    tag menu

    use file_slots(_("بارگذاری"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("صفحۀ {}"), auto=_("ذخیره‌های خودکار"), quick=_("ذخیره‌های سریع"))

    use game_menu(title):

        fixed:

            ## In az gereftan-e ruydād-e vorud tavassot-e vorudi qabl az har yek
            ## az dokme-hā motma'en misāzad.
            order_reverse True

            ## Nām-e safhe, ke mitavānad bā click kardan bar ru-ye yek dokme
            ## taqir dāde šavad.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## Šabake-ye xāne-hā-ye file-hā.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d %B %Y, %H:%M"), empty=_("خانۀ خالی")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Dokme-hāyi barā-ye dastresi be safahāt-e digar.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) a'dād-e 1 tā 9 rā midahad.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("آپلود همگام‌سازی"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("دانلود همگام‌سازی"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Safhe-ye tarjihāt ###########################################################
##
## Safhe-ye tarjihāt be bāzigar in emkan rā midahad ke bāzi rā towri tanzim
## konad barāyaš monāsebtar bāšad.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("ترجیحات"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("نمایش")
                        textbutton _("پنجره") action Preference("display", "window")
                        textbutton _("تمام‌صفحه") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("رد کردن")
                    textbutton _("متن نادیده") action Preference("skip", "toggle")
                    textbutton _("بعد از انتخاب‌ها") action Preference("after choices", "toggle")
                    textbutton _("گذارها") action InvertSelected(Preference("transitions", "toggle"))

                ## vbox-hā-ye bištar az no'-e "radio_pref" yā "check_pref"
                ## rā mitavān barā-ye ezāfe kardan-e tarjihāt-e ta'rif šode
                ## tavassot-e sāzande-ye bištar injā ezāfe kard.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("سرعت متن")

                    bar value Preference("text speed")

                    label _("زمان عبور خودکار")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("بلندی موسیقی")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("بلندی صوت")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("تست") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("بلندی گفتار")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("تست") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("بی‌صدا کردن همه"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Safhe-ye tārixče ############################################################
##
## In safheyi ast ke tārixče-ye diālog rā be bāzigar namāyeš midahad. Agar če
## hič čiz-e xāssi darbāre-ye in safhe vojud nadārad, in safhe bāyad be tārixče-
## ye diālog-e zaxire šode dar _history_list dastresi dāšte bāšad.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Jelowgiri az pišbini-ye in safhe, čerā ke besiyār bozorg mitavānad bāšad.
    predict False

    use game_menu(_("تاریخچه"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## In dar surati ke history_height None bāšad, be dorosti hame
                ## čiz rā mičinad.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Rang-e matn-e who rā, dar surāti ke tanzim šode
                        ## bāšad, az Character begir.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("تاریخچۀ دیالوگ خالی است.")


## In ta'in mikonad če tag-hāyi rā mitavān dar safhe-ye tārixče namāyeš dād.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Safhe-ye komak ##############################################################
##
## Safheyi ke dar mowred-e kelidbandi vā tanzimāt-e mušvāre ettelā'āt midahad.
## In az safahāt-e digar (keyboard_help, mouse_help, and gamepad_help) barā-ye
## namāyeš-e xod-e komak estefāde mikonad.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("کمک"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("صفحه‌کلید") action SetScreenVariable("device", "keyboard")
                textbutton _("موشواره") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("دستۀ بازی") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("دیالوگ را پیش می‌برد و رابط را فعال می‌کند.")

    hbox:
        label _("Space")
        text _("دیالوگ را بدون انتخاب گزینه‌ها پیش می‌برد.")

    hbox:
        label _("کلیدهای جهت")
        text _("پیمایش رابط")

    hbox:
        label _("Escape")
        text _("دسترسی به منوی بازی")

    hbox:
        label _("Ctrl")
        text _("هنگام فشرده نگه داشته شدن، دیالوگ را رد می‌کند.")

    hbox:
        label _("Tab")
        text _("روشن یا خاموش کردن رد کردن دیالوگ")

    hbox:
        label _("Page Up")
        text _("به دیالوگ قبلی عقب‌گرد می‌کند.")

    hbox:
        label _("Page Down")
        text _("به دیالوگ بعدی جلورفت می‌کند.")

    hbox:
        label "H"
        text _("رابط کاربری را پنهان می‌کند.")

    hbox:
        label "S"
        text _("یک اسکرین‌شات می‌گیرد.")

    hbox:
        label "V"
        text _("{a=https://www.renpy.org/l/voicing}گفتار خودکار{/a} کمکی را روشن یا خاموش می‌کند.")

    hbox:
        label "Shift+A"
        text _("منوی دسترس‌پذیری را باز می‌کند.")


screen mouse_help():

    hbox:
        label _("کلیک چپ")
        text _("دیالوگ را پیش می‌برد و رابط را فعال می‌کند.")

    hbox:
        label _("کلیک وسط")
        text _("رابط کاربری را پنهان می‌کند.")

    hbox:
        label _("کلیک راست")
        text _("دسترسی به منوی بازی")

    hbox:
        label _("اسکرول به بالا")
        text _("به دیالوگ قبلی عقب‌گرد می‌کند.")

    hbox:
        label _("اسکرول به پایین")
        text _("به دیالوگ بعدی جلورفت می‌کند.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/دکمۀ پایین")
        text _("دیالوگ را پیش می‌برد و رابط را فعال می‌کند.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("به دیالوگ قبلی عقب‌گرد می‌کند.")

    hbox:
        label _("Right Shoulder")
        text _("به دیالوگ بعدی جلورفت می‌کند.")

    hbox:
        label _("‏D-Pad، آنالوگ‌ها")
        text _("پیمایش رابط")

    hbox:
        label _("‏Start، Guide، B/دکمۀ راست")
        text _("دسترسی به منوی بازی")

    hbox:
        label _("‏Y/دکمۀ بالا")
        text _("رابط کاربری را پنهان می‌کند.")

    textbutton _("واسنجی") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Safahāt-e ezāfi
################################################################################


## Safhe-ye ta'id ##############################################################
##
## Safhe-ye ta'id hengāmi farāxāni mišavad ke Ren'Py bexāhad az bāzigar yek
## porseš-e bale yā xeyr beporsad.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Az gereftan-e vorudi tavassot-e safahāt-e digar hengām-e namāyeš-e in
    ## safhe xoddāri mikonad.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("بله") action yes_action
                textbutton _("خیر") action no_action

    ## Click rāst va escape "xeyr" javāb midahand.
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Safhe-ye nešāngar-e rad kardan ##############################################
##
## Safhe-ye skip_indicator barā-ye nešān dādan-e dar hāl-e rad kardan budan
## namāyeš dāde mišavad.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("در حال رد کردن")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## In tabdil barā-ye češmak zadan-e peykān-hā yeki pas az digari estefāde
## mišavad.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Bāyad az yek font ke dārā-ye glyph-e BLACK RIGHT-POINTING SMALL TRIANGLE
    ## bāšad estefāde konim.
    font "DejaVuSans.ttf"


## Safhe-ye ettelā' resāni #####################################################
##
## Safhe-ye ettelā' resāni barā-ye namāyeš dādan-e yek payām be bāzigar estefāde
## mišavad. (Be onvān-e mesāl, hengāmi ke bāzi zaxire-ye sari' šode va yā yek
## screenshot gerefte šode ast.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Safhe-ye NVL ################################################################
##
## In safhe barā-ye diālog va menu-hā-ye NVL-mode estefāde mišavad.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Diālog rā be surat-e yek vpgrid yā vbox namāyeš midahad.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Menu rā, dar surati ke dāde šode bāšad, namāyeš midahad. Menu momken
        ## ast be surat-e nādorost namāyeš dāde šavad agar config.narrator_menu
        ## be True tanzim šode bāšad.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## In hadd-e aksar te'dād-e vorudi-hā-ye NVL-mode ke mitavānand ham zamān
## namāyeš dāde šavand rā control mikonad.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Safhe-ye abr ################################################################
##
## Safhe-ye abr barā-ye namāyeš-e diālog be bāzigar hengām-e estefāde az
## abrnevise estefāde mišavad. Safhe-ye abr parametr-hā-ye yeksāni ba safhe-
## ye goftār migirad, bāyad yek displayable bā šenāse-ye "what" besāzad, va
## mitavānad displayable-hāyi bā šenāse-hā-ye "namebox", "who", va "window"
## besāzad.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Hālat-hā-ye hamrāh
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Az ānjāyi ke yek mušvāre momken ast mowjud nabāšad, mā menu-ye sari' rā bā
## yek nosxe ke az dokme-hā-ye kamtar va bozorgtar ke barā-ye lams kardan rāhat
## tarand estefāde mikonim.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("عقب") action Rollback()
            textbutton _("رد کردن") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("اتوماتیک") action Preference("auto-forward", "toggle")
            textbutton _("منو") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
