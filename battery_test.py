# Testing modlue battery_status function

import smbus
import sys
import UPS_Lite_module

data = UPS_Lite_module.ups_lite.battery_status.rough_soc
print data
