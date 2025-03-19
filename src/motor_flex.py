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
    
from machine import Pin, PWM

class Motor():
    
    """A flexible motor control class for MicroPython PWM-driven motors.
    
    Example:
        motor_a = Motor(8, 9)  # Define motor pins
        motor_a.forward(50)    # Set speed to 50%
    """
        
    def __init__(self, pin1, pin2):
        """Initialize motor with two PWM pins."""
        self.A = PWM(Pin(pin1))
        self.B = PWM(Pin(pin2))
        self.A.freq(1000)
        self.B.freq(1000)
        
    def __del__(self):
        """ Object is deleted"""
        self.deinit()
        del self
        
    def deinit(self):
        self.A.deinit()
        self.B.deinit()
        
    def swap(self): 
        """In case the motor is spinning the wrong direction, use this function."""
        self.Exchange = self.A
        self.A = self.B
        self.B = self.Exchange
    
    def forward(self, speed):
        """Input value from 0 - 100."""
        if not 0 <= speed <= 100:
            raise ValueError("Out of range, try a value from 0 - 100")
        else:
            self.A.duty_u16(int(((speed - 0) * (65536) / 100)+0))
            self.B.duty_u16(0)
        
    def reverse(self, speed): 
        """Input value from 0 - 100."""
        if not 0 <= speed <= 100:
            raise ValueError("Out of range, try a value from 0 - 100")
        else:
            self.A.duty_u16(0)
            self.B.duty_u16(int(((speed - 0) * (65536) / 100)+0))
        
    def stop(self):
        """The motor will brake"""
        self.A.duty_u16(0)
        self.B.duty_u16(0)
        
    def coast(self):
        """The motor will be freewheeling, might not work with geared motors"""
        self.A.duty_u16(65536)
        self.B.duty_u16(65536)