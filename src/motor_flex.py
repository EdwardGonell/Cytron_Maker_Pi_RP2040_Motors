# Copyright (c) 2025 Edward Gonell
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
import machine

class MotorFlex():
    
    """A flexible motor control class for MicroPython machine.PWM-driven motors.
    
    Example:
        motor_a = Motor(8, 9)  # Define motor pins
        motor_a.forward(50)    # Set speed to 50%
    """
        
    def __init__(self, pin1: int, pin2: int) -> None:
        """Initialize motor with two PWM pins."""
        self.A = machine.PWM(machine.Pin(pin1))
        self.B = machine.PWM(machine.Pin(pin2))
        self.A.freq(1000)
        self.B.freq(1000)
        self.stop()
        self.current_speed = 0
        
    def deinit(self) -> None:
        """De-initialize the PWM pins"""
        self.A.deinit()
        self.B.deinit()
        
    def swap(self) -> None: 
        """In case the motor is spinning the wrong direction, use this function."""
        self.Exchange = self.A
        self.A = self.B
        self.B = self.Exchange
    
    def forward(self, speed) -> None:
        """Input value from 0 - 100."""
        if not 0 <= speed <= 100:
            raise ValueError("Out of range, try a value from 0 - 100")
        else:
            self.A.duty_u16(int(((speed - 0) * (65536) / 100)+0))
            self.B.duty_u16(0)
        
    def reverse(self, speed) -> None: 
        """Input value from 0 - 100."""
        if not 0 <= speed <= 100:
            raise ValueError("Out of range, try a value from 0 - 100")
        else:
            self.A.duty_u16(0)
            self.B.duty_u16(int(((speed - 0) * (65536) / 100)+0))
            
    def move(self, speed: int) -> None:
        """Input a value from -100 to 100, negative values move reverse, positive values move forward"""
        if speed >= 0 and speed <= 100:
            self.forward(speed)
        elif speed < 0 and speed >= -100:
            self.reverse(-speed)
        else:
            raise ValueError("Out of range, try a value from -100 - 100")
        
    def read_speed(self) -> int:
        """Returns the value of the current speed"""
        return self.current_speed
    
    def stop(self) -> None:
        """The motor will brake"""
        self.A.duty_u16(0)
        self.B.duty_u16(0)
        
    def coast(self) -> None:
        """The motor will be freewheeling, might not work with geared motors"""
        self.A.duty_u16(65536)
        self.B.duty_u16(65536)