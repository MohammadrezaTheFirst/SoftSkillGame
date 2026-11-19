## In file šāmel-e tanzimāti ast ke mitavān barā-ye šaxsisāzi-ye bazi-ye xod
## estefāde kard.
##
## Xotuti ke bā do '#' šoru' mišavand comment hastand, va šomā nabāyad ānhā rā
## uncomment konid. Xotuti ke bā yek '#' šoru' mišavand code-hā-ye comment šode
## hastand, va šoma momken ast niāz bāšad āh-hā rā hengāmi ke monāseb dānestid,
## uncomment konid.


## Osul-e Avvaliye #############################################################

## Yeh nām-e xānā barā-ye bāzi. In barā-ye tanzim kardan-e titr-e pišfarz-e
## panjare estefāde šode, va dar rābet va gozāreš-hā-ye xatā-hā zāher mišavad.
##
## _() artāf-e rešte ān rā be onvān-e qābel-e tarjome budan nešāne gozāri
## mikonad.

define config.name = _("SoftSkillTest")


## Ta'in mikonad ke āyā titri ke dar bālā dāde šod dar safhe-ye menu-ye asli
## namāyeš dāde šavad. In rā barā-ye maxfi kardan-e titr be False tanzim konid.

define gui.show_name = True


## Nosxe-ye bāzi.

define config.version = "1.1"


## Matni ke dar safhe-ye darbāre-ye bāzi namāyeš dāde mišavad. Matn ra beyn-e se
## giyume qarār dāde, va beyn-e har band yek xatt-e xāli begozārid.

define gui.about = _p("""
""")


## Yeh nām-e kutāh barā-ye bāzi ke barā-ye file-hā-ye ejrāyi va puše-hā dar
## towzi'-e sāxte šode estefāde mišavad. In nām bāyad faqat ASCII bāšad, va
## nabāyad dārā-ye fāsele, do-noqte, yā noqte-virgul bāšad.

define build.name = "softtSkill"


## Sedā va musiqi ##############################################################

## In se moteqayyer mixer-hāyi rā ke be surat-e pišfarz be bazigar nešān dāde
## mišavand rā, dar kenār-e a'māl-e digar, control mikonand. Tanzim kardan-e har
## kodām az in-hā be False mixer-e motenāseb bā ān rā penhān mikonad.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Barā-ye ejāze dādan be kārbar barā-ye paxš kardan-e yek sedā-ye āzmāyeši dar
## kānāl-e sowti, yeki az xat-hā-ye zir rā uncomment karde va az ān barā-ye
## tanzim kardan-e yek sedā-ye āzmāyeši barā-ye paxš kardan estefāde konid.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Barā-ye tanzim kardan-e yek file-e sowti barā-ye paxš kardan hengāmi ke
## bāzigar dar menu-ye asli ast, xatt-e zir rā uncomment konid. Paxš-e in file
## dar bāzi tā zamāni ke motevaqqef šavad yā yek file-e digar paxš šavad, edāme
## xāhad dāšt.

define config.main_menu_music = "audio/menu_music.mp3"


## Gozār-hā ####################################################################
##
## In moteqayyer-hā gozār-hāyi ke dar surat-e rox dādan-e ruydād-hā-ye xās
## estefāde mišavand rā vaz' mikonand. Har moteqayyer bāyad motābeq-e yek gozār
## bāšad, yā barā-ye nešān dādan-e inke hič gozāri nabāyad estefāde šavad None
## bāšad.

## Vorud yā xoruj az menu-ye bāzi.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Beyn-e safahāt-e menu-ye bāzi.

define config.intra_transition = dissolve


## Yek gozār ke ba'd az bārgozāri-ye yek bāzi estefāde mišavad.

define config.after_load_transition = None


## Hengām-e vorud be menu-ye asli ba'd az pāyān-e bārgozāri-ye bāzi estefāde
## mišavad.

define config.end_game_transition = None


## Yek moteqayyer barā-ye vaz' kardan-e gozār hengāmi ke start-hā-ye bāzi vojud
## nadārand. Dar avaz, yek gozāre-ye with ba'd az namāyeš-e safhe-ye ebtedāyi
## estefāde konid.


## Modiriyat-e panjare #########################################################
##
## In zamān-e namāyeš-e panjare-ye diālog rā control mikonad. Agār "show" bāšad,
## hamiše namāyeš dāde mišavad. Agar "hide" bāšadm faqat hengāmi ke diālogi
## vojud dārad, namāyeš dāde mišavad. Agar "auto" bāšad, panjare qabl az gozāre-
## hā-ye sahne penhān šode, va hengām-e namāyeš-e mojaddad-e diālog, namāyeš
## dāde mišavad.
##
## Ba'd az šoru'-e bāzi, in rā mitavān bā gozāre-hā-ye "window show", "window
## hide", va "window auto" taqir dād.

define config.window = "auto"


## Gozār-hāyi ke barā-ye namāyeš va penhān kardan-e panjare-ye diālog estefāde
## mišavand.

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Pišfarz-hā-ye tarjihāt ######################################################

## Sor'at-e matn rā control mikonad. Pišfarz-e ān, 0, binahāyat ast, dar hāli ke
## haz adad-e digar šomāre-ye namāyeš-e nevise-hā bar sāniye ast.

default preferences.text_cps = 0


## Zamān-e ta'xir-e obur-e xodkār. A'dād-e bozorgtar mowjeb-e entezār-hā-ye
## bolandtar mišavad va az bāze-ye 0 tā 30 mowjud ast.

default preferences.afm_time = 15


## Puše-ye zaxireyi ############################################################
##
## Makān-e xāss-e har platformi ke Ren'Py file-hā-ye zaxireyi-ye bāzi rā qarār
## midahad. File-hā-ye zaxireyi dar in makān-hā negahdāri mišavand:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## In ma'mulan nabāyad taqir dāde šavad, va agar bešavad, bāyad hamiše yek
## rešte-ye rāstin-namād bāšad, na yek 'ebārat.

define config.save_directory = "softt-1794692686"


## Icon ########################################################################
##
## Iconi ke dar navār-e vazife yā dock namāyeš dāde mišavad.

define config.window_icon = "gui/window_icon.png"


## Tanzimāt-e sāxt #############################################################
##
## In baxš čegunegi-ye tabdil-e proje-ye šomā be file-hā-ye tozi'i tavassot-e
## Ren'Py rā control mikonad.

init python:

    ## Tābe'-hā-ye zir olgu-hā-ye filei rā migirand. Olgu-hā-ye filei be kušak
    ## yā bozorg budān-e horuf qeyr-e hassās hastand, va bā masir-e nesbat be
    ## puše-ye pāye bā va bedun-e yek / pišro motābeqat dāde mišavand. Agar čand
    ## olgu tatāboq dāšte bāšand, avvali estefāde xāhad šod.
    ##
    ## Dar yek olgu:
    ##
    ## / jodākonande-ye puše ast.
    ##
    ## * bā tamām-e nemive-hā be joz jodākonande-ye puše motābeqat dārad.
    ##
    ## ** bā tamām-e nemive-hā be hamrāh-e jodākonande-ye puše motābeqat dārad.
    ##
    ## Be 'onvān-e mesāl, "*.txt" bā file-hā-ye txt-e dāxel-e puše-ye pāye,
    ## "game/**.ogg" bā file-hā-ye ogg dār puše-ye bāzi yā tamām-e zir-puše-hā,
    ## va "**.psd" bā file-hā-ye psd dār har jā-ye proje motābeqat dārad.

    ## Barā-ye nādide gereftan-e file-hā az towzi'-hā-ye sāxte šode, ān-hā rā be
    ## onvān-e None dastebandi konid.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## Barā-ye bāygāni-ye file-hā, ānhā rā be onvān-e 'archive' dastebandi
    ## konid.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## File-hāyi ke bā olgu-hā-ye mostanad-hā motābeqat dārad, dar sāze-hā-ye
    ## barnāme-ye mac tekrār mišavand, banā bar in, ham dar barnāme va ham dar
    ## file-e zip zāher mišavand.

    build.documentation('*.html')
    build.documentation('*.txt')


## Yek kelid-e mojavvez-e Google Play barā-ye anjām-e xarid-hā-ye darun
## barnāmeyi niyaz ast. In rā mitavān dar console-e towse'e dahandegān dar
## "Monetize" > "Monetization Setup" > "Licensing" yāft.

# define build.google_play_key = "..."


## Nām-e kārbardi va nām-e projeyi ke bā yek proje-ye itch.io motābeqat dārand,
## jodā šode bā yek slash.

# define build.itch_project = "renpytom/test-project"
