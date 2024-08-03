## Save Sync Menu ##############################################################

screen save_sync_menu():

    modal True

    add "gui/overlay/confirm.png"

    frame:
        style_prefix "save_sync_menu"

        vbox:
            text _("Sync your saves using Ren'Py Sync Server") style "save_sync_label"
            null height 5
            button:
                text _("Upload Saves")
                style "save_sync_upload"
                action UploadSync()
            button:
                text _("Download Saves")
                style "save_sync_download"
                action DownloadSync()
            button:
                text _("Back")
                style "save_sync_back"
                action Hide("save_sync_menu")

    key "game_menu" action Hide()

style save_sync_upload:
    left_padding 54
    top_padding 4
    xalign 0.5
    idle_background "gui/gamemenu/gm_upload_idle.png"
    hover_background "gui/gamemenu/gm_upload_hover.png"

style save_sync_download:
    left_padding 54
    top_padding 4
    xalign 0.5
    idle_background "gui/gamemenu/gm_download_idle.png"
    hover_background "gui/gamemenu/gm_download_hover.png"

style save_sync_back:
    left_padding 50
    top_padding 4
    xalign 0.5
    idle_background "gui/gamemenu/gm_return_idle.png"
    hover_background "gui/gamemenu/gm_return_hover.png"

style save_sync_menu_text:
    font gui.interface_text_font
    size 35
    idle_color gui.idle_color
    hover_color gui.hover_color

style save_sync_menu_frame:
    top_padding 50
    bottom_padding 40
    left_padding 50
    right_padding 50
    xalign 0.5
    yalign 0.5

style save_sync_menu_vbox:
    xalign 0.5
    spacing 20

style save_sync_label is gui_label_text

style save_sync_label:
    size 40
    xalign 0.5

## Save Name Input #############################################################

default slot_name = None

screen save_name():

    default dummy = str(save_name)

    modal True

    add "gui/overlay/confirm.png"

    frame:
        style_prefix "save_name"

        vbox:
            frame:
                style_prefix "save_name_label"
                text (_("How do you want to name your save?")) xalign 0.5

            frame:
                xsize 620
                ysize 60
                xalign 0.5
                input:
                    style "save_name_input"
                    value ScreenVariableInputValue("dummy", True, False)
                    pixel_width 350
                    allow ("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890!@#$&-_+?.,\'\":)(%;*/")

            frame:
                style_prefix "save_name_buttons"

                fixed:
                    button:
                        text _("Back")
                        style "save_name_return"
                        action Hide("save_name")
                        keysym ("K_ESCAPE", "mouseup_3")

                    button:
                        text _("Save")
                        style "save_name_save"
                        action [Function(save_namer, dummy), FileAction(slot_name), Hide("save_name")]
                        keysym ("K_RETURN", "K_KP_ENTER")

style save_name_frame:
    xsize 1000
    ysize 250
    xalign 0.5
    yalign 0.5
    xpadding 25
    ypadding 25

style save_name_vbox:
    order_reverse False
    spacing 25

style save_name_label_frame:
    xsize 950
    background None

style save_name_input:
    xanchor 0.0
    xalign 0.03
    yalign 0.5
    xfill True
    font gui.interface_text_font

style save_name_buttons_frame:
    xsize 950
    ysize 55
    background None

style save_name_return:
    left_padding 50
    top_padding 4
    xalign 0.0
    idle_background "gui/gamemenu/gm_back_idle.png"
    hover_background "gui/gamemenu/gm_back_hover.png"

style save_name_save:
    left_padding 50
    top_padding 4
    xanchor 1.0
    xalign 1.0
    idle_background "gui/gamemenu/gm_save_idle.png"
    hover_background "gui/gamemenu/gm_save_hover.png"

style save_name_buttons_text:
    font gui.interface_text_font
    size 35
    idle_color gui.idle_color
    hover_color gui.hover_color
