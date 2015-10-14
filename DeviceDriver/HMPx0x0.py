import serial,io,time
class HMPx0x0:
        def __init__(self,com):
            self.serial = serial.Serial(port=int(com-1),baudrate=9600,timeout=0.5)
            self.sio = io.TextIOWrapper(io.BufferedRWPair(self.serial, self.serial),newline = '\n',line_buffering = True)
            
        def __del__(self,com):
            self.serial.close()
            
        def sendCommand(self,command):
            self.sio.write(command)
            self.sio.flush()
            
        def readCommand(self,command):
            self.sio.write(command)
            self.sio.flush()
            return self.sio.readline().strip()
            
        def setChannel(self,channel,voltage,current,on):
            self.sendCommand("INST OUT"+str(channel)+"\n")
            self.sendCommand("VOLT "+str(voltage)+"\n")
            self.sendCommand("CURR "+str(current)+"\n")
            if(on==True):
                self.sendCommand("OUTP:SEL ON\n")
            else:
                self.sendCommand("OUTP:SEL OFF\n")

        def measureChannel(self,channel):
            self.sendCommand("INST OUT"+str(channel)+"\n")
            voltage=float(self.readCommand("MEAS:VOLT?\n"))
            current=float(self.readCommand("MEAS:CURR?\n"))
            return (voltage,current)
            
        def setGlobalOutputEnable(self,on):
            if(on==True):
                self.sendCommand("OUTP:GEN ON\n")
            else:
                self.sendCommand("OUTP:GEN OFF\n")
                
        def setOutputEnable(self,channel,on):
            self.sendCommand("INST OUT"+str(channel)+"\n")
            if(on==True):
                self.sendCommand("OUTP:SEL ON\n")
            else:
                self.sendCommand("OUTP:SEL OFF\n")
                        
        def reset(self):
            self.sendCommand("*RST\n")
            time.sleep(0.1)
            
        def getIDN(self):
            return self.readCommand("*IDN?\n")
        
        def setMixMode(self):
            return self.readCommand("SYST:MIX\n")

        def setManualMode(self):
            return self.readCommand("SYST:LOC\n")

        def setRemoteMode(self):
            return self.readCommand("SYST:REM\n")
