image nonogram_block_idle = Solid("#000000", xsize = 73, ysize = 73)
image nonogram_block_selected = Solid("#A3D39C", xsize = 73, ysize = 73)
image nonogram_block_empty = Solid("#F5989D", xsize = 73, ysize = 73)

init python:

    import random

    class Nonogram(object):
        def __init__(self, num, random_number):
            self.num = num
            self.random_number = random_number

            self.value = 0
            self.striked = False

        def toggle_value(self):
            if self.value == 0:
                self.value = 1
            else:
                self.value = 0

        def toggle_strike(self):
            if self.striked is False:
                self.striked = True
            else:
                self.striked = False

        def get_button_image(self):
            if self.striked is False:
                if self.value == 0:
                    button_image = "nonogram_block_idle"
                elif self.value == 1:
                    button_image = "nonogram_block_selected"
            else:
                button_image = "nonogram_block_empty"

            return button_image

        def button_function(self):
            if self.striked is False:
                self.toggle_value()
            else:
                self.toggle_value()
                self.toggle_strike()

        def button_alt_function(self):
            if self.striked is False:
                if self.value == 0:
                    self.toggle_strike()
                elif self.value == 1:
                    self.toggle_value()
                    self.toggle_strike()
            else:
                self.toggle_strike()

        def clear_buttons(self):
            self.value = 0
            self.striked = False

        @staticmethod
        def get_random_click_sound():
            return random.choice([audio.sfx_nonogram_green1, audio.sfx_nonogram_green2, audio.sfx_nonogram_green3])

        @staticmethod
        def generate_buttons():
            global nono_buttons_list

            number = 0
            for i in range(grid_size):
                number += 1
                random_number = random.randint(1, 35)
                nono_buttons_list.append(Nonogram(number, random_number))

        @staticmethod
        def generate_hints(base64, rows, cols):
            global nono_col_hints
            global nono_row_hints
            global nono_match_col
            global nono_match_row
            global nono_hints_max

            base64_conversion_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

            binary = ""
            for char in base64:
                index = base64_conversion_table.find(char)
                if index < 0:
                    raise ValueError("Invalid base 64 character")
                for bit in range(6):
                    binary += "1" if index % 2 else "0"
                    index >>= 1

            grid_count = cols * rows
            binary_string = binary[:grid_count]

            grid_cols = [binary_string[i::cols] for i in range(cols)]
            grid_rows = [binary_string[i:i+cols] for i in range(0, len(binary_string), cols)]

            col_hints = [[len(group) for group in col.split("0") if group] for col in grid_cols]
            row_hints = [[len(group) for group in row.split("0") if group] for row in grid_rows]

            nono_match_col = col_hints
            nono_match_row = row_hints

            max_hint_len = max(max(len(hint) for hint in row_hints), max(len(hint) for hint in col_hints))
            nono_hints_max = max_hint_len

            col_hints = [[''] * (max_hint_len - len(hint)) + hint for hint in col_hints]
            row_hints = [[''] * (max_hint_len - len(hint)) + hint for hint in row_hints]

            nono_col_hints = [str(item) for sublist in col_hints for item in sublist]
            nono_row_hints = [str(item) for sublist in row_hints for item in sublist]

        @staticmethod
        def check_puzzle(nono_buttons_list, rows, cols):
            global nono_match_col
            global nono_match_row

            nono_player_input = ""

            for b in nono_buttons_list:
                nono_player_input += str(b.value)

            grid_rows = [nono_player_input[i:i+cols] for i in range(0, len(nono_player_input), cols)]
            grid_cols = [nono_player_input[i::cols] for i in range(cols)]

            row_hints = [[len(group) for group in row.split("0") if group] for row in grid_rows]
            col_hints = [[len(group) for group in col.split("0") if group] for col in grid_cols]

            if col_hints == nono_match_col and row_hints == nono_match_row:
                return True
            else:
                return False

        @staticmethod
        def clear_puzzle(nono_buttons_list):
            for b in nono_buttons_list:
                b.clear_buttons()
