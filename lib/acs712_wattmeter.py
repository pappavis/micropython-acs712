#demo AC watt meter met ACS712 sensor
from acs712 import ACS712

class clsMain:
  def __init__(self):
    self.acs = ACS712(ACS712type=5, debug=False)
  
  def main(self):
    print("Calibreren.. check dat alle apparaten uitstaat en geen stroom verbruikt worden.")
    self.acs.calibrate()
    print("Gekalibreerd. Zeropoint=", self.acs.zeroPoint, "sensitivity=", self.acs.sensitivity)

    print("Start met meten")
    U = 230  #normaal standaard EU-landen
    I = self.acs.getCurrentAC();    
    P = U * I
    
    print("I=", I, "A", "P=", P, "watt")

print("App start")
m1 = clsMain()
m1.main()
print("App eind")


