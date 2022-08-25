#ref https:#www.instructables.com/Arduino-Energy-Meter-V20/
from machine import Pin, ADC
from time import sleep, time

class acs712meter:
    def __init__(self) -> None:
        '''Een class om 240V AC uit te lezen met ESP8266'''
        self.Sensor_Pin = 5 #io-pin 5
        self.Sensitivity = 185   # 185mV/A for 5A, 100 mV/A for 20A and 66mV/A for 30A Module
        self.Vpp = 0 # peak-peak voltage 
        self.Vrms = 0 # rms voltage
        self.Irms = 0 # rms current
        self.Supply_Voltage = 233.0           # reading from DMM
        self.Vcc = 5.0         # ADC reference voltage # voltage at 5V pin 
        self.power = 0         # power in watt              
        self.Wh =0              # Energy in kWh
        self.last_time =0
        self.current_time =0
        self.interval = 100
        self.calibration = 100  # V2 slider calibrates this
        self.pF = 85           # Power Factor default 95
        self.bill_amount = 0   # 30 day cost as present energy usage incl approx PF 
        self.energyTariff = 8.0 # Energy cost in INR per unit (kWh)
        self.start_time = time.ticks_ms()
        self.maxAnalogVal = 1024.0


    def getACS712(self):
        '''for AC.'''
        self.Vpp = self.getVPP()
        self.Vrms = (self.Vpp / 2.0) * 0.707 
        self.Vrms -= (self.calibration / 10000.0)     # calibtrate to zero with slider
        self.Irms = (self.Vrms * 1000)/self.Sensitivity 
        if((self.Irms > -0.015) and (self.Irms < 0.008)):  # remove low end chatter
            self.Irms = 0.0

        self.power= (self.Supply_Voltage * self.Irms) * (self.pF / 100.0) 
        last_time = current_time
        current_time = time.ticks_ms()    
        self.Wh += self.power *(( current_time -last_time) /3600000.0)  # calculating energy in Watt-Hour
        self.bill_amount = self.Wh * (self.energyTariff / 1000)
        print("Irms:  ", self.Irms, " A", self.power, " W", "  Bill Amount: INR", self.bill_amount) 


    def analogRead(self, pin):
        '''Lees een analoog pin waarde.'''
        adcPin = ADC(Pin(5))
        adcPin.atten(ADC.ATTN_11DB)
        pinVal = adcPin.read()

        return pinVal


    def getVPP(self):
        '''lees VPP waarden.'''
        result = 0 
        readValue = 0                
        maxValue = 0             
        minValue = 1024          
        ticksNow = self.start_time
        while((ticksNow-self.start_time) < 950): #read every 0.95 Sec
            readValue = self.analogRead(self.Sensor_Pin)    
            if (readValue > maxValue):
                maxValue = readValue

            if (readValue < minValue):
                minValue = readValue
        result = ((maxValue - minValue) * self.Vcc) / self.maxAnalogVal

        return result


    def runDemo(self):
        '''Maak een demo van stroom uitlezen'''
        print("Start demo uitlezen")
        for teller1 in range(0, 10):
            acmeting = self.getACS712()
            print(teller1, "AC meting:", acmeting)
            print("Slapen 2 seconden ZZZzzzzz..")
            time.sleep_ms(2000)

        print("Einde demo uitlezen")
