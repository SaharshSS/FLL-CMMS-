from pybricks import version
from micropython import const, opt_level, mem_info, qstr_info, stack_use
import usys
from pybricks.hubs import PrimeHub

hub = PrimeHub()

print(usys.implementation)
print(usys.version)
print(version)
print("Name: " + str(hub.system.name()))
mem_info(True)
qstr_info(True)
if (hub.system.reset_reason() == 2):
    print("Rebooting from error")
print(" ________________________________")   
print("|Information       |Value/t/t|")
print("|------------------+-------------|")
print("|Battery voltage   |" + str(hub.battery.voltage()) + " mV/t|")
print("|Battery current   |" + str(hub.battery.current()) + " mA/t|")
print("|BLE version       |" + hub.ble.version() + " /t|")
print("|BLE power         |" + str(hub.ble.signal_strength())) + "Dpm/t|"
print("|Controller Limits |" + str(hub.control.limits())) + "/t|"
print("|Controller Pid    |" + str(hub.control.pid()))+ "/t|"
print("'--------------------------------'")
if hub.charger.connected():
  if (hub.charger.status() == 1):
    print("Charging")
  else:
    print("Battery full")
