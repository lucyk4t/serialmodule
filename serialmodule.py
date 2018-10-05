import serial as ser
import serial.tools.list_ports as listport
import re


class SerialPortControl:
    def __init__(self):
        self.regex_vplogVID = re.compile(r'{\S+}_VID')

    def getPort(self):
        try:
            for port in listport.comports():
                if re.findall(self.regex_vplogVID, port.hwid):
                   return port.device
                   break
            else:  # no break encountered
                raise ValueError("COM port not found")
        except Exception as e:
            print(e)

    def serialObjectCreate(self, device):
        try:
            serialobj = ser.Serial(device, baudrate=9600, bytesize=ser.EIGHTBITS, parity=ser.PARITY_NONE)
        except Exception as e:
            print(e)
