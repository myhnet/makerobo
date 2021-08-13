let D = 0
basic.showIcon(IconNames.Happy)
I2C_LCD1602.LcdInit(39)
cbit_小车类.CarCtrlSpeed(cbit_小车类.CarState.Car_Stop, 0)
basic.forever(function () {
    D = Math.floor(cbit_小车类.Ultrasonic_Car())
    I2C_LCD1602.ShowString(D, 0, 0)
    basic.pause(1000)
})
