
print(usys.implementation)
print(usys.version)
print(version)
print(hub.system.name())
mem_info(True)
qstr_info(True)
if (hub.system.reset_reason() == 2):
    print("Rebooting from error")
print("Booting") 
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
  elif (hub.charger.status() == 2):
    print("Battery full")
  else:
    print("Error!")
