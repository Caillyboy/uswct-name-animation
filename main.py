def on_button_pressed_a():
    basic.show_string("-CAILLIN-")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(5)
    basic.show_number(4)
    basic.show_number(3)
    basic.show_number(2)
    basic.show_number(1)
    basic.show_number(0)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        . # # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # # . . .
        . . # # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # # # . .
        . . . # #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # # # # .
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . .
        . # # # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # . . .
        . . # # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # .
        . . . . #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # . # #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # . . . #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        # . . . #
        . . . . .
        . . . . .
        . . . . .
        # . . . #
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # . .
        . # . # .
        . . # . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . . . .
        . # . # .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . # . #
        . # . # .
        . . # . .
        """)
    basic.show_leds("""
        . . . . .
        . # # # .
        # . # . #
        . # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . . # . .
        # # # # #
        . . # . .
        . . # . .
        """)
    basic.show_leds("""
        . # # # .
        . # # # .
        # # # # #
        . # # # .
        . # # # .
        """)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.show_leds("""
        # # # # .
        # # # # #
        # # # # #
        # # # # #
        . # # # #
        """)
    basic.show_leds("""
        # # # . .
        # # # # #
        # # # # #
        # # # # #
        . . # # #
        """)
    basic.show_leds("""
        # # . . .
        # # # # #
        # # # # #
        # # # # #
        . . . # #
        """)
    basic.show_leds("""
        # . . . .
        # # # # #
        # # # # #
        # # # # #
        . . . . #
        """)
    basic.show_leds("""
        . . . . .
        # # # # #
        # # # # #
        # # # # #
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # # # #
        # # # # #
        # # # # .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . # # #
        # # # # #
        # # # . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . # #
        # # # # #
        # # . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . #
        # # # # #
        # . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . # # # .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.show_leds("""
        . . # . .
        . # # # .
        # . # . #
        # . . . #
        . # # # .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HAPPY)