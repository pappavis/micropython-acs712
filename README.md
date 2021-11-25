# micropython-acs712
Measure AC current using ESP8266

Let op: 240V is **_LEVENSGEVAARLIJK_**. Je kunt zware electrische schok opdoen.

Deze bibliotheek default naar de ACS712 5A model: ACS712ELCTR-05B-T. Die is meest sensitief.

Voorbeeld gebruik van de bibliotheek.
```python
# demo AC stroom uitlezen met ACS712 sensor
from acs712 import ACS712

class clsMain:
  def __init__(self):
    pass
  
  def main(self):
    acs = ACS712()
    acs.calibrate()
    print("Zeropoint=", acs.zeroPoint, "sensitivity=", acs.sensitivity)
    
    for i in range(1,50):
      currA = acs.getCurrentAC(freq=50)
      print("Amps=", currA)

print("App start")
m1 = clsMain()
m1.main()
print("App eind")
```

Dan zie je output als deze:
```
>>> %Run -c $EDITOR_CONTENT
App start
Calibreren..
Zeropoint= 736.2 sensitivity= 0.185
Start met meten
Amps= 0.0
```

Zo sluit je hem aan.

<img src="https://thesolaruniverse.files.wordpress.com/2019/06/046_hall_fig_01_96_dpi-1.png?w=611&h=489&zoom=2" width="40%" height="40%">

door: Michiel Erasmus
