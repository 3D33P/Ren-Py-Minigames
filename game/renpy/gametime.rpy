init -1 python:

    import datetime

    class GameTime(object):

        def __init__(self, dt):
            self._start_dt = datetime.datetime.strptime(dt, "%d %b %a %H %M %S")
            self._dt = self._start_dt

        def __repr__(self):
            return _strftime("%d %b %a %I:%M:%S %p", self._dt.timetuple())

        def update(self, hr, mn, sc):
            self._dt = self._dt.replace(hour=hr, minute=mn, second=sc, microsecond=0)

        def add(self, hr, mn, sc):
            global curr_location
            global curr_sublocation
            global curr_position
            self._dt += datetime.timedelta(hours=hr, minutes=mn, seconds=sc)

        @property
        def minigame_timer(self):
            return self._dt.time().strftime("%M:%S")

        @property
        def minigame_length(self):
            t = self._dt.time()
            return t.hour * 3600 + t.minute * 60 + t.second
