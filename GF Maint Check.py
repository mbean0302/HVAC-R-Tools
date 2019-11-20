# Module Imports #

import time
from hvac_defined_functions import *

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
        time.sleep(1.5)
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
            time.sleep(1.5)
            break
        else:
            print("Please specify [Y] or [N].")
            battery_change = str(input("Were the batteries changed within the last 12 months? [Y/N]: "))

print("Set the thermostat to [Heat] and the temperature set-point [Above] the current room temperature.")
time.sleep(1.5)

heat_on = str(input("Did the appliance complete the sequence of operations on a call for heat? [Y/N] "))
while heat_on != "Y" or "N":
    if heat_on == "Y":
        print("The appliance appears to be working normally on arrival. Continue with maintenance.")
        time.sleep(.650)
        break
    elif heat_on == "N":
        print("There may be an issue with the appliance that will require troubleshooting.")
        time.sleep(1.5)
        break
    else:
        print("Please specify [Y] or [N]. ")
        heat_on = str(input("Did the appliance complete the sequence of operations on a call for heat? [Y/N] "))

# Before Start-up Electrical Readings #

hv_rating = float(input("What is the line voltage rating of the appliance? "))
time.sleep(.350)
high_voltage = float(input("Enter Measured Line Voltage: "))
if (hv_rating * 115) / 100 >= high_voltage > (hv_rating * 85 / 100):
    print("Line Voltage is within allowable range.")
    time.sleep(1.5)
else:
    print("Line Voltage is out of tolerance.")
    time.sleep(1.5)

lv_rating = float(input("What is the rated control voltage of the appliance? "))
time.sleep(.650)
low_voltage = float(input("Enter Measured Control Voltage: "))
if round((lv_rating * 125) / 100) >= round(low_voltage) > round((lv_rating * 75 / 100)):
    print("Control Voltage is within allowable range.")
    time.sleep(1.5)
else:
    print("Control Voltage is out of tolerance.")
    time.sleep(1.5)

ignitor_resistance = float(input("Ignitor Resistance (When Cold): "))
time.sleep(.650)
if 20 <= ignitor_resistance < 120:
    print("Ignitor resistance value is within acceptable range.")
    time.sleep(.650)
else:
    print("Ignitor should be replaced.")
    time.sleep(1.5)








# Next Steps #

print("Initiate a call for heat from the thermostat, or by jumping [R] and [W].")
time.sleep(.650)

ind_fla = float(input("Inducer Motor Rated Amperage [FLA/RLA]: "))
ind_amp = float(input("Inducer Motor Amperage on Highest Stage: "))
is_noisy = input("Are the bearings noisy? [Y/N]: ")

while is_noisy != "Y" or "N":
    if ind_amp < ind_fla and is_noisy == "N":
        print("Inducer Motor operating within acceptable limits.")
        time.sleep(.650)
        break
    elif ind_amp >= ind_fla and is_noisy == "Y":
        print("Inducer Motor should be replaced due to high run amperage and a worn bearing.")
        time.sleep(1.5)
        break
    elif ind_amp <= ind_fla and is_noisy == "Y":
        print("Inducer Motor should be replaced due to a worn bearing.")
        time.sleep(1.5)
        break
    elif ind_amp >= ind_fla and is_noisy == "N":
        print("Inducer Motor should be replaced due to high run amperage.")
        time.sleep(1.5)
        break
    else:
        print("Please specify whether or not the bearings are noisy? [Y/N]")
        is_noisy = str(input("Are the bearings noisy? [Y/N]: "))

time.sleep(.650)

# Safety 1 Check #

ps_check = str(input("Did all of the pressure switch contacts close without giving an error code? [Y/N]: "))
while ps_check != "Y" or "N":
    if ps_check == "Y":
        time.sleep(.650)
        break
    elif ps_check == "N":
        print(
            "One or more pressure switches may be faulty, or you may have a flue or drain obstruction. Further action required.")
        time.sleep(1.5)
        break
    else:
        print("Please specify Yes or No. [Y/N]: ")
        ps_check = str(input("Did all of the pressure switch contacts close without giving an error code? [Y/N]: "))

# Ignition Check #

ign_type = str.upper(input("Type of Ignition Device [HSI, Spark, Manual Standing Pilot]: "))

time.sleep(.650)

if ign_type == "HSI":
    hsi_ok = str.upper(input("Did the HSI complete the warm-up period and ignite the burners? [Y/N]: "))
    while hsi_ok != "Y" or "N":
        if hsi_ok == "Y":
            print("Ignitor is operating normally.")
            time.sleep(.650)
            break
        elif hsi_ok == "N":
            print("HSI should be replaced.")
            time.sleep(1.5)
            break
        else:
            print("Please specify Yes or No. [Y/N]: ")
            hsi_ok = str.upper(input("Did the HSI complete the warm-up period and ignite the burners? [Y/N]: "))

elif ign_type == str.upper("Spark"):
    spark_ok = str.upper(input("Did the spark ingitor light the burners? [Y/N]: "))
    while spark_ok != "Y" or "N":
        if spark_ok == "Y":
            print("Ignitor is operating normally.")
            time.sleep(.650)
            break
        elif spark_ok == "N":
            print("Spark ignition device should be replaced.")
            time.sleep(1.5)
            break
        else:
            print("Please specify Yes or No. [Y/N]: ")
            spark_ok = str.upper(input("Did the spark ingitor light the burners? [Y/N]: "))

elif ign_type == str.upper("Manual Standing Pilot"):
    pilot_lit = str.upper(input("Is the pilot light lit?"))
    while pilot_lit != "Y" or "N":
        if pilot_lit == "Y":
            print("Ignition system is operating as expected.")
            time.sleep(.650)
            break
        elif pilot_lit == "N":
            print("Light the pilot before continuing with maintenance.")
            time.sleep(1.5)
            pilot_lit = "Y"
            break
        else:
            print("Please specify Yes or No. [Y/N]")
            pilot_lit = str.upper(input("Is the pilot light lit?"))
    if pilot_lit == "Y":
        pilot_ok = str.upper(input("Did the pilot light ignite the burners? [Y/N]: "))
        while pilot_ok != "Y" or "N":
            if pilot_ok == "Y":
                time.sleep(.650)
                break
            elif pilot_ok == "N":
                print("Clean or replace the pilot assembly and thermocouple.")
                time.sleep(1.5)
                break
            else:
                print("Please specify Yes or No. [Y/N]")
                pilot_ok = str.upper(input("Did the pilot light ignite the burners? [Y/N]: "))

time.sleep(.650)

# Stage Check  &  Gas Pressure Check #

stage_query = str.upper(input("How many stages of heat? [One, Two, <or> Modulating]: "))

while stage_query != "ONE" or "TWO" or "MODULATING":
    if stage_query == "ONE":
        single_stage()
        time.sleep(.650)
        break
    elif stage_query == "TWO":
        print("Initiate a call for first stage heating and check fuel pressure... ")
        two_stage_low()
        time.sleep(1.5)
        print("Initiate a call for second stage heating and check fuel pressure... ")
        two_stage_high()
        time.sleep(.650)
        break
    elif stage_query == "MODULATING":
        print("Initiate a call for heat in the lowest firing rate possible (Usually 35%)... ")
        time.sleep(.650)
        if mod_stage_least() is True:
            print("Initiate a call for heat at the max firing rate possible (100% capacity)... ")
            time.sleep(.650)
        if mod_stage_max() is True:
            gv_condition = 1
            time.sleep(.650)
            break
    else:
        print("ERROR: Please specify stages of heat. [One, Two, <or> Modulating].")
        stage_query = str.upper(input("How many stages of heat? [One, Two, <or> Modulating]: "))

# Flame Proving #

if ign_type == "HSI" or ign_type == "SPARK":
    flame_rod()


if ign_type == "MANUAL STANDING PILOT":
    tcouple()

# Indoor Blower Testing #

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
            is_clean = input(
                "Is the Indoor Blower free of dirt and debris on the motor housing and squirrel cage? [Y/N]: ")

btu_input = int(input("Enter the BTU/h input of appliance: "))
eff_percent = int(input("Enter the efficiency of appliance: "))
btu_output = int((btu_input * eff_percent) / 100)

cfm_target = int(input("Enter Target CFM on High Stage: "))
cfm_actual = btu_output
