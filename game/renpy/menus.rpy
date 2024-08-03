################################################################################
## Initialization
################################################################################

init offset = -1

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"

            imagebutton auto "gui/quickmenu/qm_rollback_%s.png" action Rollback()
            imagebutton auto "gui/quickmenu/qm_skip_%s.png" action Skip() alternate Skip(fast=True, confirm=False) alternate_keysym 'shift_K_s'
            imagebutton auto "gui/quickmenu/qm_auto_%s.png" action Preference("auto-forward", "toggle")
            imagebutton auto "gui/gamemenu/gm_save_%s.png" action ShowMenu('save')
            imagebutton auto "gui/gamemenu/gm_pref_%s.png" action ShowMenu('preferences')

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_hbox:
    xalign 0.5
    yalign 0.99
    spacing 30

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        if main_menu:
            button id "gm_start":
                text _("Play")
                style style.button["gm_start"]
                action Start()

        else:
            button id "gm_mm":
                text _("Main Menu")
                style style.button["gm_mm"]
                action MainMenu()

            button id "gm_hist":
                text _("History")
                style style.button["gm_hist"]
                action ShowMenu("history")

            if not _in_replay:
                button id "gm_save":
                    text _("Save")
                    style style.button["gm_save"]
                    action ShowMenu("save")

        if not _in_replay:
            button id "gm_load":
                text _("Load")
                style style.button["gm_load"]
                action ShowMenu("load")

        button id "gm_pref":
            text _("Preferences")
            style style.button["gm_pref"]
            action ShowMenu("preferences")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            button id "gm_help":
                text _("Help")
                style style.button["gm_help"]
                action ShowMenu("help")

        button id "gm_about":
            text _("About")
            style style.button["gm_about"]
            action ShowMenu("about")

        button id "gm_quit":
            text _("Quit")
            style style.button["gm_quit"]
            action Quit(confirm=not main_menu)

style navigation_vbox:
    xpos gui.navigation_xpos
    yalign 0.5
    spacing gui.navigation_spacing

style navigation_text:
    font gui.interface_text_font
    size 35
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    selected_hover_color gui.selected_hover_color
    xsize 350

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    tag menu

    add gui.game_menu_background
    add "gui/overlay/game_menu.png"
    add "gui/overlay/game_menu_line.png"

    use navigation

    label "[config.name]" style "game_menu_label"

    if gui.show_name is True:
        hbox:
            style_prefix "mm_version"
            text "v[config.version]"

style mm_version_hbox:
    xalign 0.99
    yalign 0.99

style mm_version_text:
    size 25
    color "#333333"
    outlines [(1, "#d6d6d6", 0, 0)]
    kerning 2

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    on 'show' action Function(hide_hover_notify)
    on 'show' action Function(pause_all_sound)

    style_prefix "game_menu"

    add gui.game_menu_background
    add "gui/overlay/game_menu.png"

    frame:
        style "game_menu_outer_frame"

        hbox:

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
                        arrowkeys True
                        side_yfill True
                        vbox:
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
                        transclude

                else:
                    transclude

    use navigation

    vbox:
        style_prefix "gm_return"

        button id "gm_return":
            text _("Return")
            style style.button["gm_return"]
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

    background "gui/overlay/game_menu_line.png"

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
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style gm_return_vbox:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style gm_return_text:
    font gui.interface_text_font
    size 35
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color
    xsize 350

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:
            if gui.about:
                label "[config.name]" xalign 0.0 style "game_menu_label"
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

transform scale(percent):
    zoom percent

style about_text is gui_text

style about_label_vbox:
    spacing 8

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto"), quick=_("Quick"))
    $ pager = Pager()

    use game_menu(title):

        fixed:
            hbox:
                style_prefix "renamer"
                hbox:
                    style "page_label"
                    button:
                        style style.button["gm_page"]
                        key_events True
                        xalign 0.0
                        action page_name_value.Toggle()
                        input:
                            style "page_label_text"
                            value page_name_value
                            pixel_width 200

                if CurrentScreenName() == "save":
                    hbox:
                        style_prefix "save_name_toggle"
                        add "gui/gamemenu/gm_edit_hover.png"
                        text (_("Naming save file:"))
                        textbutton _("Enabled" ) selected (persistent.save_name_prompt) action SetVariable("persistent.save_name_prompt", True)
                        text "/"
                        textbutton _("Disabled") selected (not persistent.save_name_prompt) action [SetVariable("persistent.save_name_prompt", False), SetVariable("save_name", "")]
                else:
                    hbox:
                        style_prefix "save_sync"
                        textbutton _("Ren'Py Save Sync") action ShowMenu("save_sync_menu")

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    button:
                        if title == "Load":
                            action FileAction(slot)
                        else:
                            if persistent.save_name_prompt is True and FileCurrentPage() != "auto":
                                action [SetVariable("slot_name", slot), ShowMenu("save_name")]
                            else:
                                action FileAction(slot)
                        has vbox
                        spacing -4
                        add FileScreenshot(slot) xalign 0.5
                        null height 30
                        text FileTime(slot, format=_("{#file_time}%b %d %Y, %H:%M"), empty=_("Empty Slot")):
                            style "slot_time_text"
                        null height 5
                        text FileSaveName(slot):
                            style "slot_name_text"
                        if FileLoadable(slot):
                            imagebutton auto "gui/others/gm_delete2_%s.png" action FileDelete(slot) xalign 1.0 ypos -60
                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                if pager.int > 10:
                    textbutton _("«") action FilePage(pager.int - 10)
                if pager.int > 1:
                    textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")
                for page in pager.rng:
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()
                textbutton _("»") action FilePage(pager.int + 10)

style renamer_hbox:
    xsize 1250
    xpos 80
    ypos 0

style save_name_toggle_hbox:
    xalign 1.0
    xanchor 1.0
    spacing 10

style save_sync_hbox:
    xalign 1.0

style save_sync_button:
    left_padding 54
    top_padding 4
    xalign 0.5
    idle_background "gui/gamemenu/gm_sync_idle.png"
    hover_background "gui/gamemenu/gm_sync_hover.png"

style save_name_toggle_text:
    font gui.interface_text_font
    xalign 1.0
    yalign 0.5
    color gui.hover_color

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style slot_grid:
    xalign 0.5
    yalign 0.5
    spacing gui.slot_spacing

style page_hbox:
    xanchor 0.5
    xalign 0.5
    yalign 1.0
    spacing gui.page_spacing

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:
            hbox:
                box_wrap True
                spacing 80

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        hbox:
                            add "gui/others/pref_display.png" yalign 0.8
                            label _("Display")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                        textbutton "1920 x 1080" action Preference("display", 1.0)
                        textbutton "1600 x 900" action Preference("display", 0.83333333333)
                        textbutton "1280 x 720" action Preference("display", 0.666666666667)
                        textbutton "960 × 540" action Preference("display", 0.5)

                vbox:
                    style_prefix "radio"
                    hbox:
                        add "gui/others/pref_rollbackside.png" yalign 0.8
                        label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    hbox:
                        add "gui/others/pref_skip.png" yalign 0.8
                        label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    hbox:
                        add "gui/others/pref_textspeed.png" yalign 0.8
                        label _("Text Speed")
                    bar value Preference("text speed")
                    hbox:
                        add "gui/others/pref_autoforward.png" yalign 0.8
                        label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                    hbox:
                        add "gui/others/pref_textbox.png" yalign 0.8
                        label _("Dialogue Box Opacity")
                    bar value FieldValue(persistent, "dialogueboxopacity", range = 1.0, style = "slider")

                vbox:
                    if config.has_music or config.has_sound or config.has_voice:
                        hbox:
                            add "gui/others/pref_master.png" yalign 0.8
                            label _("Master Volume")
                        hbox:
                            bar value Preference("mixer main volume")

                    if config.has_music:
                        hbox:
                            add "gui/others/pref_music.png" yalign 0.8
                            label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        hbox:
                            add "gui/others/pref_volume.png" yalign 0.8
                            label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        hbox:
                            add "gui/others/pref_voice.png" yalign 0.8
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
                            xpos 0

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

style radio_hbox:
    spacing 10

style radio_button:
    xpos 30
    left_padding 50
    properties gui.button_properties("radio_button")
    idle_foreground "gui/gamemenu/gm_empty_idle.png"
    hover_foreground "gui/gamemenu/gm_empty_hover.png"
    selected_idle_foreground "gui/gamemenu/gm_yes_selected.png"
    selected_hover_foreground "gui/gamemenu/gm_yes_hover.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_hbox:
    spacing 10

style check_button:
    xpos 30
    left_padding 50
    properties gui.button_properties("check_button")
    idle_foreground "gui/gamemenu/gm_empty_idle.png"
    hover_foreground "gui/gamemenu/gm_empty_hover.png"
    selected_idle_foreground "gui/gamemenu/gm_yes_selected.png"
    selected_hover_foreground "gui/gamemenu/gm_yes_hover.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525
style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

style slider_hbox:
    spacing 10


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

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
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")
    size 48

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
