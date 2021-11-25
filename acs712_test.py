# demo AC stroom uitlezen met ACS712 sensor
from acs712 import ACS712

class clsMain:
  def __init__(self):
    pass
  
  def main(self):
    acs = ACS712()
    print("Calibreren..")
    acs.calibrate()
    print("Zeropoint=", acs.zeroPoint, "sensitivity=", acs.sensitivity)
    
    print("Start met meten")
    for i in range(1,50):
      currA = acs.getCurrentAC(freq=50)
      print("Amps=", currA)

print("App start")
m1 = clsMain()
m1.main()
print("App eind")

