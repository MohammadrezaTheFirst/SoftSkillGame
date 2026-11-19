################################################################################
## Meqdārdehi-ye ebtedāyi
################################################################################

## Gozāre-ye init offset bā'es mišavad meqdārdehi-hā-ye ebtedāyi-ye dāxel-e in
## file qabl az gozāre-hā-ye init-e dāxel-e file-hā-ye digar ejrā šavad.
init offset = -2

## Farāxāni-ye gui.init sabk-hā rā be pišfarz-hā-ye ma'qulāne bāznešāni mikonad,
## va arz va ertefā'-e bāzi rā tanzim mikonad.
init python:
    gui.init(1920, 1080)

## Fa'āl kardan-e ček-hā-ye marbut be vižegi-hā-ye nāpāydār yā nāmo'tabar dar
## safahāt yā tabdilāt
define config.check_conflicting_properties = True


################################################################################
## Moteqayyer-hā-ye peykarbandi-ye rābet-e kārbari-ye gerāfiki
################################################################################


## Rang-hā #####################################################################
##
## Rang-hā-ye matn-e rābet.

## Yek rang-e ta'kidi-ye estefāde šode dar sarāsar-e rābet barā-ye porrang
## kardan va barčasb zadan-e matn.
define gui.accent_color = '#0099cc'

## Rangi ke barā-ye dokme-ye matndār hengāmi ke na entexāb šode va na hover šode
## estefāde mišavad.
define gui.idle_color = '#888888'

## small color barā-ye motun-e riz estefāde mišavad ke bāyad barā-ye hamān hālat
## rošantar/tiretar bāšand.
define gui.idle_small_color = '#aaaaaa'

## Rangi ke barā-ye dokme-hā va mile-hāyi ke hover šodeand estefāde mišavad.
define gui.hover_color = '#66c1e0'

## Rangi ke barā-ye dokme-ye matndār hengāmi ke entexāb šode vali focus našode
## ast, estefāde mišavad. Yek dokme zamāni entexāb šode ast ke meqdār-e tarjihāt
## yā safhe-ye fe'li bašad.
define gui.selected_color = '#ffffff'

## Rangi ke barā-ye dokme-ye matndar hengāmi estefāde mišavad ke nemitavān ān rā
## entexāb kard.
define gui.insensitive_color = '#8888887f'

## Rang-hāyi ke barā-ye qesmat-hāyi az mile-hā estefāde mišavand ke por
## našodeand. In-hā be surat-e mostaqim estefāde nemišavand, vali dar hengām-e
## bāztolid-e file-hā-ye tasvir-e mile-hā estefāde mišavand.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## Rang-hāyi ke barā-ye diālog va entexāb-hā-ye menu estefāde mišavad.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Font-hā va andāze-ye font-hā ################################################

## Fonti ke barā-ye matn-e darun-e bāzi estefāde mišavad.
define gui.text_font = "Vazirmatn-RD-UI-Light.ttf"

## Fonti ke barā-ye nām-e šaxsiyat-hā estefāde mišavad.
define gui.name_text_font = "Vazirmatn-RD-UI-Light.ttf"

## Fonti ke barā-ye matn-e xārej az bāzi estefāde mišavad.
define gui.interface_text_font = "Vazirmatn-RD-UI-Light.ttf"

## Andāze-ye matn-e diālog-e ma'muli
define gui.text_size = 33

## Andāze-ye nām-e šaxsiyat-hā
define gui.name_text_size = 45

## Andāze-ye matn-e dāxel-e rābet-e kārbari-ye bāzi.
define gui.interface_text_size = 33

## Andāze-ye barčasb-hā dāxel-e rābet-e kārbari-ye bāzi.
define gui.label_text_size = 36

## Andāze-ye matn dar safhe-ye ettelā' resāni.
define gui.notify_text_size = 24

## Andāze-ye titr-e bāzi.
define gui.title_text_size = 75


## Menu-hā-ye asli va bāzi #####################################################

## Tasāviri ke barāye menu-hā-ye asli va bāzi estefāde mišavand.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diālog ######################################################################
##
## In moteqayyer-hā nahve-ye namāyeš-e diālog dar safhe be surat-e xat be xat rā
## tanzim mikonand.

## Ertefā'-e ja'be-ye matn-e dārā-ye diālog.
define gui.textbox_height = 278

## Nahve-ye qarārgiri-ye ja'be-ye matn be surat-e amudi dar safhe. 0.0 barā-ye
## bālā, 0.5 barā-ye vasat, va 1.0 barā-ye pāyin.
define gui.textbox_yalign = 1.0


## Nahve-ye qarārgiri-ye nām-e šaxsiyati ke sohbat mikonad, nesbat be ja'be-ye
## matn. In-hā mitavānand te'dād-e sahihi az pixel az čap yā bālā, yā 0.5 barā-
## ye vasat bāšand.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Tarāz-e ofoqi-ye nām-e šaxsiyat-hā. In mitavānad 0.0 barā-ye čap tarāz, 0.5
## barā-ye motemarkez, va 1.0 barā-ye rāst tarāz bašand.
define gui.name_xalign = 0.0

## Arz, ertefā', va hāšiye-hā-ye ja'be-ye dārā-ye nām-e šaxsiyat, yā None barā-
## ye andāzebandi-ye xodkār.
define gui.namebox_width = None
define gui.namebox_height = None

## Hāšiye-hā-ye ja'be-ye dārā-ye nām-e šaxsiyat, be tartib dar čap, bālā, rāst,
## pāyin.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Agar True bāšad, paszamine-ye ja'be-ye nām kāšikāri xāhad šod, agar False
## bāšad, paszamine-ye ja'be-ye nām meqyāsbandi xāhad šod.
define gui.namebox_tile = False


## Nahve-ye qarārgiri-ye diālog nesbat be ja'be-ye matn. In-hā mitavānand
## te'dād-e sahihi az pixel az čap yā bālā, yā 0.5 barā-ye vasat bāšand.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Hadd-e aksar arz-e matn-e diālog, be pixel.
define gui.dialogue_width = 1116

## Tarāz-e ofoqi-ye matn-e diālog. In mitavānad 0.0 barā-ye čap tarāz, 0.5 barā-
## ye motemarkez, va 1.0 barā-ye rāst tarāz bašand.
define gui.dialogue_text_xalign = 0.0


## Dokme-hā ####################################################################
##
## In moteqayyer-hā, be hamrāh-e file-hā-ye tasvir-e dāxel-e gui/button, janbe-
## hā-ye nahve-ye namāyeš-e dokme-hā rā tanzim mikonad.

## Arz va ertefā'-e yek dokme, be pixel. Agar None bāšad, Ren'Py andāze rā
## mohāsebe mikonad.
define gui.button_width = None
define gui.button_height = None

## Hāšiye-hā-ye har samt-e dokme, be tartib dar čap, bālām rāst, pāyin.
define gui.button_borders = Borders(6, 6, 6, 6)

## Agar True bāšad, tasvir-e paszamine kāšikāri xāhad šod. Agar False bāšad,
## tasvir-e paszamine be surat-e xatti meqyāsbandi xāhad šod.
define gui.button_tile = False

## Fonti ke tavassot-e dokme estefāde mišavad.
define gui.button_text_font = gui.interface_text_font

## Andāze-ye matni ke tavassot-e dokme estefāde mišavad.
define gui.button_text_size = gui.interface_text_size

## Rang-e dokme-ye matndār dar vaz'iyat-hā-ye moxtalef.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Tarāzbandi-ye ofoqi-ye dokme-ye matndār. (0.0 barā-ye čap, 0.5 barā-ye vasat,
## 1.0 barā-ye rāst).
define gui.button_text_xalign = 0.0


## In moteqayyer ha tanzimāt-e dokme-hā-ye moxtalef rā bāznevisi mikonand.
## Lotfan barā-ye mošāhede-ye anvā'-e dokme-hā-ye mojud, va inke har yek barā-ye
## če čizi estefāde mišavand, be mostanad-e gui morāje'e konid.
##
## In šaxsisāzi-hā tavassot-e rābet-e pišfarz estefāde mišavand:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Šoma hamčenin mitavānid šaxsisāzi-hā-ye xodetān rā az tariq-e ezāfe kardan-
## e moteqayyer-hāyi bā nām-e monāseb, ezāfe konid. Be onvān-e mesāl, mitavānid
## xatt-e zir rā barā-ye tanzim kardan-e arz-e yek dokme-ye hedāyati, uncomment
## konid.

# define gui.navigation_button_width = 250


## Dokme-hā-ye entexāb #########################################################
##
## Dokme-hā-ye entexāb dar menu-hā-ye darun-e bāzi estefāde mišavand.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Dokme-hā-ye xāne-ye file ####################################################
##
## Dokme-ye xāne-ye file yek dokme-ye xāssi ast. In dokme dārā-ye tasvir-e
## thumbnail, va matni ast ke mohtaviyāt-e xāne-ye zaxire rā tosif mikonad. Har
## xāne-ye zaxire, mānand-e har no' dokme-ye digar, az file-hā-ye tasviri-ye
## dāxel-e gui/button estefāde mikonad.

## Dokme-ye xāne-ye zaxire.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Arz va ertefā'-e thumbnail-hā-ye estefāde šode tavassot-e xāne-hā-ye zaxire.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Te'dād-e sotun-hā va satr-hā dar šabake-ye xāne-hā-ye zaxire.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Moqe'iyat bandi va Fāsele bandi #############################################
##
## In moteqayyer-hā moqe'iyat va fāsele bani-ye anāsor-e moxtalef-e rābet-e
## kārbari rā tanzim mikonand.

## Moqe'iyat-e samt-e čap-e dokme-hā-ye hedāyati, nesbat be samt-e čap-e safhe.
define gui.navigation_xpos = 60

## Moqe'iyat-e amudi-ye nešāngar-e rad kardan.
define gui.skip_ypos = 15

## Moqe'iyat-e amudi-ye safhe-ye ettelā' resāni.
define gui.notify_ypos = 68

## Fāsele bandi-ye beyn-e entexāb-hā-ye menu.
define gui.choice_spacing = 33

## Dokme-hā-ye dāxel-e baxš-e hedāyati-ye menu-hā-ye asli va bāzi.
define gui.navigation_spacing = 6

## Meqdār-e fāsele-ye beyn-e tarjihāt rā tanzim mikonad.
define gui.pref_spacing = 15

## Meqdār-e fāsele-ye beyn-e dokme-hā-ye tarjihāt rā tanzim mikonad.
define gui.pref_button_spacing = 0

## Fāsele-ye beyn-e dokme-hā-ye safhe-ye file.
define gui.page_spacing = 0

## Fāsele-ye beyn-e xāne-hā-ye file.
define gui.slot_spacing = 15

## Moqe'iyat-e matn-e menu-ye asli.
define gui.main_menu_text_xalign = 1.0


## Qāb-hā ######################################################################
##
## In moteqayyer-hā zāher-e qāb-hā, ke mitavānand dārā-ye ajzā-ye rābet-e
## kārbari hengām-e nabud-e panjare va ya jāygozāšt bāšand rā tanzim mikonand.

## Qāb-hā-ye hamegāni.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Qābi ke be onvān-e qesmati az safhe-ye ta'id estefāde mišavad.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Qābi ke be onvān-e qesmati az safhe-ye rad kardan estefāde mišavad.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Qābi ke be onvān-e qesmati az safhe-ye ettelā' resāni estefāde mišavad.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Āyā paszamine-ye qāb-hā kāšikāri šavand?
define gui.frame_tile = False


## Mile-hā, scrollbar-hā, va ahrom-hā-ye laqzande ##############################
##
## In-hā zāher va andāze-ye mile-hā, scrollbar-hā, va ahrom-hā-ye laqzande rā
## tanzim mikonand.
##
## GUI-e pišfarz faqat az ahrom-hā-ye laqzande va scrollbar-hā-ye amudi estefāde
## mikonad. Tamām-e mile-hā-ye digar faqat dar safhe-hā-ye nevešte šode
## tavassot-e sāzande-hā estefāde mišavand.

## Ertefā'-e mile-hā-ye ofoqi, scrollbar-hā, va ahrom-hā-ye laqzande. Arz-e
## mile-hā-ye ofoqi, scrollbar-hā, va ahrom-hā-ye laqzande.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## Dar surati ke tasavir bāyad kāšikāri šavand, True bāšad. Dar surati ke ān-hā
## bāyad be surat-e xatti meqyāsbandi šavand, True bāšad.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Hāšiye-hā-ye ofoqi.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Hāšiye-hā-ye amudi.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Kari ke bar ru-ye scrollbar-hā-ye qeyr-e qābel-e scroll anjam mišavad. "hide"
## ān-hā rā penhān mikonad, dar hāli ke None ān-hā rā namāyeš midahad.
define gui.unscrollable = "hide"


## Tārixče #####################################################################
##
## Safhe-ye Tārixče diālogi ke bāzigar rad karde ast rā namāyeš midahad.

## Te'dād-e block-hā-ye tārixče-ye diālog ke Ren'Py negāh midārad.
define config.history_length = 250

## Ertefā'-e yek vorudi-ye safhe-ye tārixče, yā None barā-ye moteqayyer kardan-e
## ertefā' be qeymat-e amalkard.
define gui.history_height = 210

## Afzudan-e fazā-ye bištar beyn-e vorudi-hā-ye safhe-ye tārixče.
define gui.history_spacing = 0

## Moqe'iyat, arz, va tarāzbandi-ye barčasb-e nām-e šaxsiyat-e dar hāl-e sohbat.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Moqe'iyat, arz, va tarāzbandi-ye matn-e diālog.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## Safhe-ye NVL-mode diālogi ke tavassot-e šaxsiyat-hā-ye NVL-mode sohbat
## mišavad rā namāyeš midahad.

## Hāšiye-hā-ye paszamine-ye panjare-ye paszamine-ye NVL-mode.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Hadd-e aksar te'dād-e vorudi-hā-ye NVL-mode ke Ren'Py namayeš midahad. Vaqti
## te'dāde vorudi-hā az in had begozarand, qadimi tarin vorudi hazf xāhad šod.
define gui.nvl_list_length = 6

## Ertefā'-e har vorudi-ye NVL-mode. Barā-ye tanzim be surat-e puyā, in rā None
## begozārid.
define gui.nvl_height = 173

## Fāselebandi-ye beyn-e vorudi-hā-ye NVL-mode hengāmi ke gui.nvl_height None
## ast, va beyn-e vorudi-hā-ye NVL-mode va yek menu-ye NVL-mode.
define gui.nvl_spacing = 15

## Moqe'iyat, arz, va tarāzbandi-ye barčasb-e nām-e šaxsiyat-e dar hāl-e sohbat.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Moqe'iyat, arz, va tarāzbandi-ye matn-e diālog.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Moqe'iyat, arz, va tarāzbandi-ye matn-e nvl_thought (matni ke tavassot-e
## šaxsiyat-e nvl_narrator gofte mišavad.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Moqe'iyat-e nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Bumisāzi ####################################################################

## In mahall-e qābel-e qabul barā-ye noxat ra tanzim mikonad. Meqdār-e pišfarz
## barā-ye bištar-e zabān-hā monāseb ast. Yek list az tamām-e meqdār-hā-ye mojud
## rā mitavān dar https://www.renpy.org/doc/html/style_properties.html#style-
## property-language yāft

define gui.language = "unicode"


################################################################################
## Dastgāh-hā-ye hamrāh
################################################################################

init python:

    ## In andāze-ye dokme-hā-ye sari' rā afzāyeš midahad tā lams kardan-e ānhā
    ## rā dar tablet-hā va guši-hā āsāntar konad.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## In andāze va fāselebandi-ye anāsor-e GUI-e moxtalef rā barā-ye tazmin-e
    ## qābel-e mošāhede budan-e ānha dar guši-hā taqir midahad.
    @gui.variant
    def small():

        ## Andāze-ye font-hā.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Tanzim-e mahall-e ja'be-ye matn.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Taqir-e andāze va fāselebandi-ye čiz-hā-ye moxtalef.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## čidemān-e dokme-hā-ye file.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
