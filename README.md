# micropython-acs712
Measure AC current using ESP8266

Let op: 240V is LEVENSGEVAARLIJK!!

Voorbeels gebruik van de bibliotheek.
```python
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
```

Zo sluit je hem aan.
<img src="https://thesolaruniverse.files.wordpress.com/2019/06/046_hall_fig_01_96_dpi-1.png?w=611&h=489&zoom=2" width="40%" height="40%">

door: Michiel Erasmus
