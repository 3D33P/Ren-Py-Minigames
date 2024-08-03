## Nonogram ####################################################################

screen nonogram_selector():

    add "black"

    text "Select Nonogram Puzzle -"

    style_prefix "nonogram_selector"

    grid 10 6:
        for idx, puzzle in enumerate(nonogram_puzzle_list):
            textbutton str(idx + 1) action (SetVariable("seleced_puzzle", puzzle), Jump("nonogram_game"))

screen nonogram_game():

    add "black"

    frame:
        style_prefix "nonogram_base"
        vbox:
            frame:
                style_prefix "nonogram_top"
                grid grid_cols nono_hints_max:
                    allow_underfull True
                    spacing grid_padding
                    transpose True
                    for h in nono_row_hints:
                        frame:
                            style_prefix "nonogram_hints"
                            xsize 73
                            ysize 50
                            text "[h]" xalign 0.5 yalign 0.5
            hbox:
                frame:
                    style_prefix "nonogram_left"
                    grid nono_hints_max grid_rows:
                        allow_underfull True
                        spacing grid_padding
                        for h in nono_col_hints:
                            frame:
                                style_prefix "nonogram_hints"
                                xsize 50
                                ysize 73
                                text "[h]" xalign 0.5 yalign 0.5
                frame:
                    style_prefix "nonogram_blocks"
                    grid grid_cols grid_rows:
                        spacing grid_padding
                        transpose True
                        for b in nono_buttons_list:
                            imagebutton idle b.get_button_image() action Function(b.button_function) alternate Function(b.button_alt_function)
    use nonogram_ui

screen nonogram_ui():

    if nonogram_submit is False:
        timer 1 action Function(mt.add, 0, 0, 1) repeat True

    frame:
        style_prefix "nonogram_controls"
        frame:
            style_prefix "nonogram_timer"
            text "[mt.minigame_timer]"
        hbox:
            imagebutton:
                auto "images/nonogram/nonogram_help_%s.webp"
                action OpenURL("https://activityworkshop.net/puzzlesgames/nonograms/tutorial.html")
            imagebutton:
                auto "images/nonogram/nonogram_reset_%s.webp"
                action Function(Nonogram.clear_puzzle, nono_buttons_list)
            imagebutton:
                auto "images/nonogram/nonogram_submit_%s.webp"
                action (SetVariable("nonogram_submit", True), Show("nonogram_result"))

screen nonogram_result():

    modal True

    add "gui/overlay/confirm.png"

    frame:
        style_prefix "nonogram_result"
        if Nonogram.check_puzzle(nono_buttons_list, grid_rows, grid_cols):
            text _("You have coded the solution in [mt.minigame_timer]")
        else:
            text _("You have failed to code the solution")
        textbutton _("Continue") action (Hide("nonogram_result"), Jump("nonogram_done"))

style nonogram_result_text:
    xalign 0.5
    yalign 0.3
    text_align 0.5

style nonogram_result_button:
    xalign 0.5
    yalign 0.8

style nonogram_result_button_text:
    idle_color "#FFFFFF"
    hover_color gui.accent_color

style nonogram_result_frame:
    background Frame(Solid("#2a4032"))
    xsize 700
    ysize 300
    xalign 0.5
    yalign 0.5

style nonogram_base_frame:
    xalign 0.33
    yalign 0.45
    left_padding 0
    top_padding 0
    right_padding 0
    bottom_padding 0
    background Frame(Solid("#2a4032"))

style nonogram_top_frame:
    xalign 1.0
    left_padding 18
    top_padding 27
    right_padding 28
    bottom_padding 16
    background Frame(Solid("#2a4032"))

style nonogram_left_frame:
    yalign 1.0
    left_padding 27
    top_padding 16
    right_padding 16
    bottom_padding 26
    background Frame(Solid("#2a4032"))

style nonogram_hints_frame:
    background Frame(Solid("#0f1712"))

style nonogram_hints_text:
    font gui.interface_text_font
    color "#A3D39C"

style nonogram_blocks_frame:
    left_padding 19
    top_padding 17
    right_padding 27
    bottom_padding 27
    background Frame(Solid("#2a4032"))

style nonogram_controls_frame:
    background Frame(Solid("#2a4032"))
    xsize 300
    ysize 265
    xalign 0.7
    yalign 0.5

style nonogram_timer_frame:
    background Frame(Solid("#0f1712"))
    left_padding 25
    top_padding 25
    right_padding 25
    bottom_padding 25
    xalign 0.5
    yalign 0.2

style nonogram_timer_text:
    font "fonts/e1234.ttf"
    color "#A3D39C"
    size 40

style nonogram_controls_hbox:
    spacing 10
    xalign 0.5
    yalign 0.86

style nonogram_selector_grid:
    xalign 0.5
    yalign 0.6
    spacing 50

style nonogram_selector_text:
    xalign 0.05
    yalign 0.05
    color gui.accent_color
    size 50

style nonogram_selector_button:
    xalign 0.5
    yalign 0.5

style nonogram_selector_button_text:
    size 50
