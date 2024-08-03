init python:

## Audio Channels ##############################################################

    renpy.music.register_channel("music2", "music")
    renpy.music.register_channel("sound2", "sfx")
    renpy.music.register_channel("voice2", "voice")

## Navigation ##################################################################

    for i in ("gm_start", "gm_hist", "gm_save", "gm_load", "gm_end", "gm_mm", "gm_pref", "gm_lang", "gm_replay", "gm_end", "gm_discord", "gm_patreon", "gm_help", "gm_about", "gm_quit", "gm_return", "gm_page", "gallery_help"):
        style.button[i].idle_background             = "gui/gamemenu/{0}_idle.png".format(i)
        style.button[i].hover_background            = "gui/gamemenu/{0}_hover.png".format(i)
        style.button[i].selected_background         = "gui/gamemenu/{0}_selected.png".format(i)
        style.button[i].selected_idle_background    = "gui/gamemenu/{0}_selected.png".format(i)
        style.button[i].selected_hover_background   = "gui/gamemenu/{0}_hover.png".format(i)
        style.button[i].insensitive_background      = "gui/gamemenu/{0}_ins.png".format(i)
        style.button[i].left_padding                = 50
        style.button[i].top_padding                 = 3
    style.button["gm_page"].selected_idle_foreground        = None
    style.button["gm_page"].selected_hover_foreground       = None
    style.button["gallery_help"].left_padding               = 0
    style.button["gallery_help"].selected_idle_foreground   = None
    style.button["gallery_help"].selected_hover_foreground  = None
    style.button["gallery_help"].left_padding               = 50
    style.button["gallery_help"].top_padding                = 4

## Language Menu ###############################################################

    for i in ("lang_en", "lang_cn", "lang_pt", "lang_es", "lang_ko", "lang_it", "lang_ms", "lang_tr", "lang_ru"):
        j = i[5:]
        style.button[i].idle_background             = "images/utilities/flags/flag_{0}_idle.webp".format(j)
        style.button[i].hover_background            = "images/utilities/flags/flag_{0}_hover.webp".format(j)
        style.button[i].selected_background         = "images/utilities/flags/flag_{0}_selected.webp".format(j)
        style.button[i].selected_idle_background    = "images/utilities/flags/flag_{0}_selected_idle.webp".format(j)
        style.button[i].selected_hover_background   = "images/utilities/flags/flag_{0}_hover.webp".format(j)
        style.button[i].xsize                       = 300
        style.button[i].ysize                       = 210
        style.button[i].top_padding                 = 170

## Others ######################################################################

    notify_timeout = True

## Dev Functions ###############################################################

    if config.developer is True:
        config.keymap['screenshot'].remove('noshift_K_s')
        config.keymap['fast_skip'].append('noshift_K_s')
        config.keymap['screenshot'].append('noshift_K_q')
