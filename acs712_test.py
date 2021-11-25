# demo AC stroom uitlezen met ACS712 sensor
from acs712 import ACS712

class clsMain:
  def __init__(self):
    pass
  
  def main(self):
    acs = ACS712()
    acs.calibrate()

print("App start")
m1 = clsMain()
m1.main()
print("App eind")
