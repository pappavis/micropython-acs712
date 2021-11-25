# demo AC stroom uitlezen met ACS712 sensor
from acs712 import ACS712

class clsMain:
  def __init__(self):
    pass
  
  def main(self):
    acs = ACS712()
    acs.calibrate()
    
    for i in range(1,50):
      currA = acs.getCurrentAC(freq=50)
      print("Amps=", currA)

print("App start")
m1 = clsMain()
m1.main()
print("App eind")
