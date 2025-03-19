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

class Motor_1():
    
    def __init__(self):
        """Initializing the motor instance"""
        self.A = PWM(Pin(10))
        self.B = PWM(Pin(11))
        self.A.freq(120)
        self.B.freq(120)
        
    def deinit(self):
        """De-initialize the PWM pins"""
        self.A.deinit()
        self.B.deinit()

    def swap(self): 
        """Swaps the pins if it is moving in the wrong direction."""
        self.Exchange = self.A
        self.A = self.B
        self.B = self.Exchange
        
    def forward(self, speed):
        """Input value from 0 - 100."""
        self.A.duty_u16(int(((speed - 0) * (65536) / 100)+0))
        self.B.duty_u16(0)
    
    def reverse(self, speed):
        """Input value from 0 - 100.""" 
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
        
class Motor_2():
    
    def __init__(self):
        """Initializing the motor instance"""
        self.C = PWM(Pin(8))
        self.D = PWM(Pin(9))
        self.C.freq(120)
        self.D.freq(120)
        
    def deinit(self):
        """De-initialize the PWM pins"""
        self.C.deinit()
        self.D.deinit()

    def swap(self):
        """Swaps the pins if it is moving in the wrong direction."""
        self.Exchange = self.C
        self.C = self.D
        self.D = self.Exchange
        
    def forward(self, speed):
        """Input value from 0 - 100.""" 
        self.C.duty_u16(int(((speed - 0) * (65536) / 100)+0))
        self.D.duty_u16(0)
    
    def reverse(self, speed):
        """Input value from 0 - 100.""" 
        self.C.duty_u16(0)
        self.D.duty_u16(int(((speed - 0) * (65536) / 100)+0))
        
    def stop(self):
        """The motor will brake"""
        self.C.duty_u16(0)
        self.D.duty_u16(0)
    
    def coast(self):
        """The motor will be freewheeling, might not work with geared motors"""
        self.C.duty_u16(65536)
        self.D.duty_u16(65536)