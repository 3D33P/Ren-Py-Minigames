init -1 python:

    class Pager:
        def __init__(self):
            self.str    = FileCurrentPage()
            self.int    = 0 if (self.str in ["auto", "quick"]) else int(self.str)
            self.rng    = range(1,10) if (self.int < 6) else range(self.int - 4, self.int + 5)
