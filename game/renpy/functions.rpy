init python:

## Save Namer ##################################################################

    def save_namer(value):
        setattr(renpy.store, "save_name", value)

## Hover Notify ################################################################

    def show_hover_notify(what):
        setattr(renpy.store, "notify_timeout", False)
        renpy.notify(what)

    def hide_hover_notify():
        setattr(renpy.store, "notify_timeout", True)
        renpy.hide_screen("notify")

## Audio Functions #############################################################

    def stop_all_sound():
        renpy.music.stop('music')
        renpy.music.stop('music2')
        renpy.music.stop('sound')
        renpy.music.stop('sound2')
        renpy.music.stop('voice')
        renpy.music.stop('voice2')

    def pause_all_sound():
        renpy.music.set_pause(True, channel = 'music' )
        renpy.music.set_pause(True, channel = 'music2')
        renpy.music.set_pause(True, channel = 'sound' )
        renpy.music.set_pause(True, channel = 'sound2')
        renpy.music.set_pause(True, channel = 'voice' )
        renpy.music.set_pause(True, channel = 'voice2')
