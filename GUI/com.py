import serial
import serial.tools.list_ports

def get_available_com_ports(verbose=0):
    ports = serial.tools.list_ports.comports()
    ports = sorted(ports)
    if verbose >= 1: 
        for port in ports: print("{}: {}".format(port.name, port))
    return [port.device for port in ports]

class arduino():
    def __init__(self, verbose=0):
        self.connected = False
        self.ser = None
        self.verbose = verbose

    def connect_arduino(self, COMport):
        self.connected = False
        try:
            if self.connected:
                self.ser.close()
                self.connected = False
            self.ser = serial.Serial(COMport, 9600)
            self.connected = True
            if self.verbose >= 1: 
                print("Connected to Arduino on port: " + COMport)
        except serial.SerialException as e:
            if self.verbose >= 1: 
                print("Failed to connect to Arduino on port: " + COMport)
                print(e)
        return self.connected

    def disconnect_arduino(self):
        self.connected = False
        self.ser.close()
        if self.verbose >= 1: 
            print("Disconnected from Arduino")
    
    def send_data_to_arduino(self, data):
        if not self.connected:
            if self.verbose >= 1: 
                print("Not connected to Arduino")
            return False
        if self.verbose >= 1: 
            print("Sending data to Arduino: " + str(data))
        self.ser.write(str(data).encode())
        return True
    
    def get_status(self):
        return self.connected

    def read_data(self):
        if not self.connected:
            if self.verbose >= 1: 
                print("Not connected to Arduino")
            return False
        if self.verbose >= 1: 
            print("Reading data from Arduino")
        data = 7 
        return data