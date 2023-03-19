input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    StopAll = 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    StopAll = 0
})
function changeLedColor(isToGreen: boolean) {
    let i = 0
    while (i < 1024) {
        if (StopAll == 1) {
            pins.digitalWritePin(DigitalPin.P0, 0)
            pins.digitalWritePin(DigitalPin.P1, 0)
            break
        }
        
        i = i + 10
        if (1024 - i < 0 || i >= 1024) {
            break
        }
        
        if (isToGreen) {
            pins.analogWritePin(AnalogPin.P0, i)
            pins.analogWritePin(AnalogPin.P1, 1024 - i)
        } else {
            pins.analogWritePin(AnalogPin.P0, 1024 - i)
            pins.analogWritePin(AnalogPin.P1, i)
        }
        
        basic.pause(20)
        i += 1
    }
}

let StopAll = 0
basic.forever(function on_forever() {
    changeLedColor(true)
    basic.pause(100)
    changeLedColor(false)
    basic.pause(100)
})
