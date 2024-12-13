from smbus2 import SMBus
from .exceptions import *

class I2CComm:
    @property
    def available():
        try:
            SMBus(1)
            return True
        except ImportError:
            return False

    def __init__(self, address, port=1):
        if not self.available:
            raise UnsupportedPlatform("smbus2 is not installed")
        self.address = address
        self.bus = SMBus(port)
    
    def write_byte(self, data):
        self.bus.write_byte(self.address, data)
    
    def read_byte(self):
        return self.bus.read_byte(self.address)
