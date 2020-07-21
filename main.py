def on_forever():
    basic.show_leds("""
        . # . # .
        # # # # #
        # # # # #
        . # # # .
        . . # . .
        """)
    basic.pause(500)
    basic.show_leds("""
        . # . # .
        # # . . #
        . # # . #
        . # # . .
        . . # . .
        """)
    basic.pause(100)
basic.forever(on_forever)
