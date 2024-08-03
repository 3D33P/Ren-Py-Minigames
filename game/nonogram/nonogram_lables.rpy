label play_nonogram:

    $ nono_row_hints = []
    $ nono_col_hints = []
    $ nono_match_col = []
    $ nono_match_row = []
    $ nono_hints_max = 0
    $ grid_padding = 5
    $ seleced_puzzle = []

    call screen nonogram_selector

label nonogram_game:

    $ base64_string = seleced_puzzle[0]
    $ grid_cols = seleced_puzzle[1]
    $ grid_rows = seleced_puzzle[2]
    $ grid_size = grid_rows * grid_cols
    $ Nonogram.generate_hints(base64_string, grid_rows, grid_cols)
    $ nono_buttons_list = []
    $ Nonogram.generate_buttons()

    $ nonogram_puzzle_solved = False

    $ mt = GameTime("01 Jan Mon 00 00 00")
    $ nonogram_submit = False

    call screen nonogram_game()

label nonogram_done:

    if Nonogram.check_puzzle(nono_buttons_list, grid_rows, grid_cols):
        $ nonogram_puzzle_solved = True

    $ renpy.block_rollback()

    jump start
