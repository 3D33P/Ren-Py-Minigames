## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

# FL: priority set to 1 because "is_extended_edition" is created through a define statement (priority == zero)
init 1 python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.
    build.classify("**~"                                 , None)
    build.classify("**.bak"                              , None)
    build.classify("**.bat"                              , None)
    build.classify("**.rar"                              , None)
    build.classify("**.psd"                              , None)
    build.classify("**.txt"                              , None)
    build.classify("**.json"                             , None)
    build.classify("**.zip"                              , None)
    build.classify("**/.**"                              , None)
    build.classify("**/#**"                              , None)
    build.classify("**/thumbs.db"                        , None)
    build.classify("**/desktop.ini"                      , None)

    # Exclude script RPY files
    build.classify("game/**.rpy"                         , None)

    # Excludes the debug file
    build.classify("game/code/debug.rpy"                 , None)
    build.classify("game/code/debug.rpyc"                , None)

    # Excludes the cache files
    build.classify("game/cache/**"                       , None)

    # Excludes the python tools and their reports
    build.classify("game/**.py"                          , None)
    build.classify("game/**.pyc"                         , None)
    build.classify("game/**.txt"                         , None)

    # Excludes all saves and persistent files
    build.classify("game/saves/persistent"               , None)
    build.classify("game/saves/*.save"                   , None)

    # Excludes the translation guide
    build.classify("game/**.md"                          , None)
    build.classify("game/tl/media/**"                    , None)

    # Excludes unused media files
    build.classify("game/audio/**/test/**"               , None)
    build.classify("game/audio/**/unused/**"             , None)

    ## To archive files, classify them as 'archive'.

    # Create the archives
    build.archive("code"                                 , "all")
    build.archive("images"                               , "all")
    build.archive("audio"                                , "all")
    build.archive("video"                                , "all")
    build.archive("fonts"                                , "all")

    # Put script RPYC files into the scripts archive.
    build.classify("game/**.rpyc"                        , "code")

    # Put images into the images archive.
    build.classify("game/**.webp"                        , "images")
    build.classify("game/**.png"                         , "images")
    build.classify("game/**.jpg"                         , "images")

    # Put audio files into the audio archive.
    build.classify("game/**.ogg"                         , "audio")
    build.classify("game/**.mp3"                         , "audio")
    build.classify("game/**.wav"                         , "audio")

    # Put video files into the video archive.
    build.classify("game/**.mp4"                         , "video")
    build.classify("game/**.avi"                         , "video")
    build.classify("game/**.webm"                        , "video")

    # Put font files into the video archive.
    build.classify("game/**.ttf"                         , "fonts")
    build.classify("game/**.otf"                         , "fonts")

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"

## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

# define config.log = "vnlog.txt"

# define analytics.tracking_id = ""
