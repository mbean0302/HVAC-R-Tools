# Module Imports #

import time

# Change version after each revision. #

version = "Alpha 1.0"
print(f"Gas Furnace Maintenance Checklist -- {version}")

# Call Details #

tech = input("Technician: ")
date = str(input("Date of Service: "))
od_ambient = int(input("Current Outdoor Temperature: "))
name = input("Customer Name: ")
call_num = input("Call-Slip #: ")
svc_req = str(input("Gas Furnace Maintenance [Y/N]: "))

# Maintenance Check? #

while svc_req != "Y" or "N":
    if svc_req == "Y":
        break
    elif svc_req == "N":
        print("This Checklist is for Gas Furnace Maintenance Only.")
        quit()
    else:
        print("Please Specify [Y] or [N].")
        svc_req = str(input("Gas Furnace Maintenance [Y/N]: "))

# General Overview of System #

tstat_has_battery = input("Does the Thermostat Have Batteries? [Y/N]: ")
while tstat_has_battery != "Y" or "N":
    if tstat_has_battery == "Y":
        print("Ask Customer when the batteries were last changed.")
        time.sleep(2)
        break
    elif tstat_has_battery == "N":
        break
    else:
        print("Please Specify [Y] or [N].")
        tstat_has_battery = input("Does the Thermostat Have Batteries? [Y/N]: ")

if tstat_has_battery == "Y":
    battery_change = str(input("Were the batteries changed within the last 12 months? [Y/N]: "))
    while battery_change != "Y" or "N":
        if battery_change == "Y":
            print("This is acceptable.")
            break
        elif battery_change == "N":
            print("Change batteries...")
            time.sleep(2)
            break
        else:
            print("Please specify [Y] or [N].")
            battery_change = str(input("Were the batteries changed within the last 12 months? [Y/N]: "))

print("Set the thermostat to [Heat] and the temperature set-point [Above] the current room temperature.")
time.sleep(2)

heat_on = str(input("Did the appliance complete the sequence of operations on a call for heat? [Y/N] "))
while heat_on != "Y" or "N":
    if heat_on == "Y":
        print("The appliance appears to be working normally on arrival. Continue with maintenance.")
        time.sleep(.500)
        break
    elif heat_on == "N":
        print("There may be an issue with the appliance that will require troubleshooting.")
        time.sleep(2)
    else:
        print("Please specify [Y] or [N]. ")
        heat_on = str(input("Did the appliance complete the sequence of operations on a call for heat? [Y/N] "))


# Before Start-up Electrical Readings #

hv_rating = float(input("What is the line voltage rating of the appliance? "))
time.sleep(.350)
high_voltage = float(input("Enter Measured Line Voltage: "))
if (hv_rating * 115) / 100 >= high_voltage > (hv_rating * 85 / 100):
    print("Line Voltage is within allowable range.")
    time.sleep(2)
else:
    print("Line Voltage is out of tolerance.")
    time.sleep(2)

lv_rating = float(input("What is the rated control voltage of the appliance? "))
time.sleep(.500)
low_voltage = float(input("Enter Measured Control Voltage: "))
if round((lv_rating * 125) / 100) >= round(low_voltage) > round((lv_rating * 75 / 100)):
    print("Control Voltage is within allowable range.")
    time.sleep(2)
else:
    print("Control Voltage is out of tolerance.")
    time.sleep(2)

ignitor_resistance = float(input("Ignitor Resistance (When Cold): "))
if 20 <= ignitor_resistance < 150:
    print("Ignitor resistance value is within acceptable range.")
    time.sleep(.500)
else:
    print("Ignitor should be replaced.")
    time.sleep(2)

# Next Steps #

print("Initiate a call for heat from the thermostat, or by jumping [R] and [W].")
time.sleep(.500)

ind_fla = float(input("Inducer Motor Rated Amperage [FLA/RLA]: "))
ind_amp = float(input("Inducer Motor Amperage on Highest Stage: "))
is_noisy = input("Are the bearings noisy? [Y/N]: ")


while is_noisy != "Y" or "N":
    if ind_amp < ind_fla and is_noisy == "N":
        print("Inducer Motor operating within acceptable limits.")
        time.sleep(.500)
        break
    elif ind_amp >= ind_fla and is_noisy == "Y":
        print("Inducer Motor should be replaced due to high run amperage and a worn bearing.")
        time.sleep(2)
        break
    elif ind_amp <= ind_fla and is_noisy == "Y":
        print("Inducer Motor should be replaced due to a worn bearing.")
        time.sleep(2)
        break
    elif ind_amp >= ind_fla and is_noisy == "N":
        print("Inducer Motor should be replaced due to high run amperage.")
        time.sleep(2)
        break
    else:
        print("Please specify whether or not the bearings are noisy? [Y/N]")
        is_noisy = str(input("Are the bearings noisy? [Y/N]: "))

ps_check = str(input("Did all of the pressure switch contacts close without giving an error code? [Y/N]: "))
while ps_check != "Y" or "N":
    if ps_check == "Y":
        time.sleep(.500)
        break
    elif ps_check == "N":
        print("One or more pressure switches may be faulty, or you may have a flue or drain obstruction. Further action required.")
        time.sleep(2)
        break
    else:
        print("Please specify Yes or No. [Y/N]: ")
        ps_check = str(input("Did all of the pressure switch contacts close without giving an error code? [Y/N]: "))



# gas pressure check #




flame_signal = float(input("Flame Sense Signal in mA: "))



blower_fla = float(input("Indoor Blower Motor Rated Amperage [FLA/RLA]: "))
blower_amp = float(input("Indoor Blower Motor Amperage on Highest Stage: "))
is_noisy = input("Are the bearings noisy? [Y/N]: ")


while is_noisy != "Y" or "N":
    if blower_amp < blower_fla and is_noisy == "N":
        print("Indoor Blower Motor operating within acceptable limits.")
        break
    elif blower_amp >= blower_fla and is_noisy == "Y":
        print("Indoor Blower Motor should be replaced due to high run amperage and a worn bearing.")
        break
    elif blower_amp <= blower_fla and is_noisy == "Y":
        print("Indoor Blower Motor should be replaced due to a worn bearing.")
        break
    elif blower_amp >= blower_fla and is_noisy == "N":
        print("Indoor Blower Motor should be replaced due to high run amperage.")
        break
    else:
        print("Please specify whether or not the bearings are noisy. [Y/N]")
        is_noisy = str(input("Are the bearings noisy? [Y/N]: "))

if blower_amp < blower_fla and is_noisy == "N":
    is_clean = input("Is the Indoor Blower free of dirt and debris on the motor housing and squirrel cage? [Y/N]: ")
    while is_clean != "Y" or "N":
        if is_clean == "Y":
            break
        elif is_clean == "N":
            print("Indoor Blower Motor and Housing should be pulled to clean thoroughly.")
            break
        else:
            print("Please specify whether or not the blower is clean. [Y/N]")
            is_clean = input("Is the Indoor Blower free of dirt and debris on the motor housing and squirrel cage? [Y/N]: ")








btu_input = int(input("Enter the BTU/h input of appliance: "))
eff_percent = int(input("Enter the efficiency of appliance: "))
btu_output = int((btu_input * eff_percent) / 100)











cfm_target = int(input("Enter Target CFM on High Stage: "))
cfm_actual = btu_output












