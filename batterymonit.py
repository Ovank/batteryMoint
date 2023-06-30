import wmi
import winsound
import time

__BASE_FREQUENCY = 525
__MULTIPLIER = 1.05
__PEROID = 800

__SLEEP = 900

'''
Function :- battery_info.
Return :-
      BatteryStatus - Charging,On Battery.
      EstimatedChargeRemaining - Current Battery Percentage.
      EstimatedRunTime - On battery time period.
      Status 
      System Name.
'''
def battery_info():
  
  c = wmi.WMI()

  battery = c.query('select * from Win32_Battery')

  return (battery[0].BatteryStatus,battery[0].EstimatedChargeRemaining,battery[0].EstimatedRunTime,battery[0].Status,battery[0].SystemName)
  
'''
Function :- Generate Beep Noise.
'''
def make_sound(frequency,duration):
  print(frequency)
  winsound.Beep(frequency, duration)


while(1):
  time.sleep(1.5)

  make_sound(__BASE_FREQUENCY,__PEROID)

  (Battery_status,charge_status,time_remain,status,system_name) = battery_info()

  if Battery_status == 2 :

    print("Percentage Charged : %s Battery Status : %s" %(charge_status,"Charging"))

  if Battery_status == 1 :

    print("Percentage Charged : %s Battery Status : %s" %(charge_status,"Not Charging"))

  if (Battery_status == 2 and charge_status == 100 ) :

    make_sound(__BASE_FREQUENCY,__PEROID)

  else :

    time.sleep(__SLEEP)
