# Cytron Maker Pi RP2040 Motors Library

This project became redundant the second I found CytronTechnologies repositories, to be more specific [MAKER-PI-PICO](https://github.com/CytronTechnologies/MAKER-PI-PICO). However this may serve a test platform for more libraries to come in micropython. As you may be able to see, I'm a noobie programmer, any suggestions are welcomed to improve the libraries. This update keep the two original libraries which are intended to control motors independently. Those being [motor.py](/src/motor.py) and [motor_flex](/src/motor_flex.py). The former is intended to control both motor ports found in the Cytron Maker Pi Pico, with this library you would type <code> motor = MotorDriver(1)</code> for Motor 1 and <code> motor = MotorDriver(2)</code> for Motor 2. The latter is meant for the user to decide which pins to use for the motors for example <code> motor = MotorFlex(8,9)</code>, this one may come in handy for the Motion 2350 Pro, which has 4 motor ports.

## Some examples for [motor.py](/src/motor.py):

    import motor, time

    motor = motor.MotorDriver() #This will use Motor 1 by default
    motor.forward(100) # Moves the motor forward at 100%
    time.sleep(1)
    motor.stop() # Stops the motor
    time.sleep(1)
    motor.reverse(100) # Moves the motor backwards at 100%
    time.sleep(1)
    motor.stop()
    time.sleep(1)

    for i in range(-100, 100): # Tests the move function from -100 to 100
        motor.move(i)
        time.sleep_ms(100)

    time.sleep(1)
    motor.stop() 

In case the motor is spinning the wrong direction you can use the swap function as shown here.

    import motor, time

    motor = motor.MotorDriver() #This will use Motor 1 by default
    motor.forward(100) # Moves the motor forward at 100%
    time.sleep(1)
    motor.stop()
    motor.swap() # Used when the motor is not spinning in the desired direction
    time.sleep(1)
    motor.forward(100)
    time.sleep(1)
    motor.stop()

## Some examples for [motor_flex](/src/motor_flex.py):

Mostly the same as [motor.py](/src/motor.py), it only has minor differences. The equivalent to the firts example would be: 

    import motor_flex, time

    motor = motor_flex.MotorFlex(8,9) #Here you have to specify the pins to use
    motor.forward(100) # Moves the motor forward at 100%
    time.sleep(1)
    motor.stop() # Stops the motor
    time.sleep(1)
    motor.reverse(100) # Moves the motor backwards at 100%
    time.sleep(1)
    motor.stop()
    time.sleep(1)

    for i in range(-100, 100): # Tests the move function from -100 to 100
        motor.move(i)
        time.sleep_ms(100)

    time.sleep(1)
    motor.stop() 

Apart from having to specify the pins and a different name for the class, everything else should behave the same way.


## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.