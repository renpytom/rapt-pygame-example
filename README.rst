RAPT Pygame Example
===================

This serves as an example of how to get a simple Pygame game working on
Android.

Step 0: Ready the game.
-----------------------

Please ensure that the main file of your game is named main.py.

Please ensure that your game will run with pygame_sdl2. Generally, this
consists of adding the lines::

    try:
        import pygame_sdl2
        pygame_sdl2.import_as_pygame()
    except ImportError:
        pass

to the top of your main.py file, before the first import of pygame. (However,
note that pygame_sdl2 does not yet implement all of pygame.)

For now, RAPT supports only python2.7.

This repository serves as a simple pygame_sdl2-ready game.

Step 1: Install dependencies.
-----------------------------

RAPT depends on your computer having a JDK in the path, and Python 2.7 installed.
On Windows, you'll need a 32-bit JDK if you're using a 32-bit Python 2.7.

You may also need to install device drivers and permissions to ensure that
the Android SDK will talk to your device.

Step 2: Download and unzip RAPT.
--------------------------------

Download the latest nightly build of RAPT from
http://nightly.renpy.org/current/ . The file you want will end in -rapt.zip.
Unzip the file. All further commands should be run from inside the rapt
directory.


Step 3: Install the Android SDK.
--------------------------------

This can be done by running::

    python android.py installsdk

RAPT will prompt you to accept various license, and create a signing key.
This has to be done only once per RAPT install.


Step 4: Configure the game.
---------------------------

Configure the game::

    python android.py configure /path/to/rapt-pygame-example

The correct answers vary depending on the game. For our example, we used:

* Full Name: Android Test
* Short Name: Android Test
* Package Name: org.renpy.android_test
* Human-readable Version: 1.0
* Version Code: 100
* Orientation: 1) Landscape
* Expansion APK: 1) No
* Android Version: 3) Android 4.0
* Application Layout: 1) Single directory, device internal storage.
* Include Source Code: no
* Permissions: VIBRATE
* SQlite3: no (may not work)
* PIL: no (may not work)

This must be done once per game.


Step 5: Build, Install, and Run the game.
-----------------------------------------

This can be done with the command::

    python android.py --launch build /path/to/rapt-pygame-example release install

This must be done each time the game changes, to ensure the latest version is
on the device.
