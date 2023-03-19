def on_button_pressed_a():
    global StopAll
    StopAll = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global StopAll
    StopAll = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def changeLedColor(isToGreen: bool):
    i = 0
    while i < 1024:
        if StopAll == 1:
            pins.digital_write_pin(DigitalPin.P0, 0)
            pins.digital_write_pin(DigitalPin.P1, 0)
            break
        i = i + 10
        if 1024 - i < 0 or i >= 1024:
            break
        if isToGreen:
            pins.analog_write_pin(AnalogPin.P0, i)
            pins.analog_write_pin(AnalogPin.P1, 1024 - i)
        else:
            pins.analog_write_pin(AnalogPin.P0, 1024 - i)
            pins.analog_write_pin(AnalogPin.P1, i)
        basic.pause(20)
        i += 1
StopAll = 0

def on_forever():
    changeLedColor(True)
    basic.pause(100)
    changeLedColor(False)
    basic.pause(100)
basic.forever(on_forever)
