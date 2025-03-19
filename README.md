# Cytron Maker Pi RP2040 Motors Library

This project became redundant the second I found CytronTechnologies repositories, to be more specific [MAKER-PI-PICO](https://github.com/CytronTechnologies/MAKER-PI-PICO). However this may serve a test platform for more libraries to come in micropython. As you may be able to see, I'm a noobie programmer, any suggestions are welcomed to improve the libraries. This first commit includes two libraries to control motors independently. Those being [motor.py](/src/motor.py) and [motor_flex](/src/motor_flex.py). The former is intended to control both motor ports found in the Cytron Maker Pi Pico, referring to the ports as Motor_1 and Motor_2. The latter is meant for the user to decide which pins to use for the motors, this one may come in handy for the Motion 2350 Pro, which has 4 motor ports.

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.