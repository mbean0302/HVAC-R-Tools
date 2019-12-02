# Module Imports #

from Functions_and_Global_Variables import *
from tabulate import tabulate

# Change version after each revision. #

version = "Alpha 1.6"

print(f"Gas Furnace Maintenance Checklist (Induced Draft Appliances ONLY) -- {version}")

# Call Details and Variables #

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
            tstat_ok = True
            break
        elif battery_change == "N":
            print("Change batteries...")
            time.sleep(1.5)
            tstat_ok = True
            break
        else:
            print("Please specify [Y] or [N].")
            battery_change = str(input("Were the batteries changed within the last 12 months? [Y/N]: "))

print("Set the thermostat to [Heat] and the temperature set-point [Above] the current room temperature.")
time.sleep(1.5)
is_call = str.upper(input("Did the appliance initiate a call for heat? [Y/N]: "))
while is_call == "Y" or is_call == "N":
    if is_call == "Y":
        tstat_ok = True
        break
    elif is_call == "N":
        print("Troubleshooting the thermostat may be required...")
        tstat_ok = False
        break
    else:
        print("Please specify Yes or No [Y/N]...")
        is_call = str.upper(input("Did the appliance initiate a call for heat? [Y/N]: "))

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
    voltage_ok = True
    time.sleep(1.5)
else:
    print("Line Voltage is out of tolerance.")
    voltage_ok = False
    time.sleep(1.5)

lv_rating = float(input("What is the rated control voltage of the appliance? "))
time.sleep(.650)
low_voltage = float(input("Enter Measured Control Voltage: "))
if round((lv_rating * 125) / 100) >= round(low_voltage) > round((lv_rating * 75 / 100)):
    print("Control Voltage is within allowable range.")
    voltage_ok = True
    time.sleep(1.5)
else:
    print("Control Voltage is out of tolerance.")
    time.sleep(1.5)
    voltage_ok = False

ignitor_resistance = float(input("Ignitor Resistance (When Cold): "))
time.sleep(.650)
if 20 <= ignitor_resistance < 120:
    print("Ignitor resistance value is within acceptable range.")
    ignitor_ok = True
    time.sleep(.650)
else:
    print("Ignitor should be replaced.")
    ignitor_ok = False
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
        inducer_ok = True
        time.sleep(.650)
        break
    elif ind_amp >= ind_fla and is_noisy == "Y":
        print("Inducer Motor should be replaced due to high run amperage and a worn bearing.")
        inducer_ok = False
        time.sleep(1.5)
        break
    elif ind_amp <= ind_fla and is_noisy == "Y":
        print("Inducer Motor should be replaced due to a worn bearing.")
        inducer_ok = False
        time.sleep(1.5)
        break
    elif ind_amp >= ind_fla and is_noisy == "N":
        print("Inducer Motor should be replaced due to high run amperage.")
        inducer_ok = False
        time.sleep(1.5)
        break
    else:
        print("Please specify whether or not the bearings are noisy? [Y/N]")
        is_noisy = str(input("Are the bearings noisy? [Y/N]: "))

time.sleep(.650)

ind_has_cap = str.upper(input("Does the inducer motor have a capacitor? [Y/N]: "))
while ind_has_cap == "Y" or ind_has_cap == "N":
    if ind_has_cap == "Y":
        cap_test1()
        break
    elif ind_has_cap == "N":
        time.sleep(1.5)
        break
    else:
        print("Please specify Yes or No [Y/N]...")
        time.sleep(.600)
        ind_has_cap = str.upper(input("Does the inducer motor have a capacitor? [Y/N]: "))

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

# Fuel Type #

is_natural = str.upper(input("Fuel Type [Natural or LP]: "))
while is_natural == "NATURAL" or "LP":
    if is_natural == "NATURAL":
        is_natural = True
        break
    elif is_natural == "LP":
        is_natural = False
        break
    else:
        print("Please specify fuel type as [Natural] or [LP]...")
        is_natural = str.upper(input("Fuel Type [Natural or LP]: "))

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

blower_has_cap = str.upper(input("Does the appliance blower motor have a capacitor? [Y/N]: "))
while blower_has_cap == "Y" or blower_has_cap == "N":
    if blower_has_cap == "Y":
        cap_test1()
        break
    elif blower_has_cap == "N":
        time.sleep(1.5)
        break
    else:
        print("Please specify Yes or No [Y/N]...")
        time.sleep(.600)
        ind_has_cap = str.upper(input("Does the appliance blower motor have a capacitor? [Y/N]: "))

# Delta T #

if stage_query == "ONE":
    print("Check Delta T after 5 minutes of run-time...")
    single_stage_deltat()
    time.sleep(1.5)

elif stage_query == "TWO":
    print("Initiate a call for first stage heating and check Delta T after 5 minutes of run-time... ")
    two_stage_low_deltat()
    time.sleep(1.5)
    print("Initiate a call for second stage heating and check Delta T after 5 minutes of run-time... ")
    two_stage_high_deltat()
    time.sleep(1.5)

elif stage_query == "MODULATING":
    print("Initiate a call for heat in the lowest firing rate possible (Usually 35%) and check Delta T after 5 minutes of run-time... ")
    time.sleep(1.5)
    mod_stage_least_deltat()
    time.sleep(1.5)
    print("Initiate a call for heat at the max firing rate possible (100% capacity) and check Delta T after 5 minutes of run-time... ")
    time.sleep(1.5)
    mod_stage_max_deltat()
    time.sleep(1.5)

# BTU/h and Efficiency Calculation #

print("Calculate the BTU/h Output of the appliance...")
time.sleep(1.5)
btu_calc()

# Condensing or Non-Condensing Check #

condensing_check()

# CFM on Highest Stage #

print("Calculating CFM on highest heat stage..........")
time.sleep(2.5)
cfm_calc()

# Drain Check #

if is_condensing == "Condensing":
    print("Check the condensate drain for proper operation using the following method...")
    time.sleep(1.5)
    cond_drain_clear()
    time.sleep(1.5)

# Combustion Testing #

print("Perform Combustion Testing on appliance during normal operation on highest heating stage, after the appliance has been running for a minimum of 5 minutes...")
time.sleep(1.5)
if is_natural:
    print("Perform zeroing of combustion analyser outside of home and set analyser to Natural Gas.")
    time.sleep(2)
    print("While outside, set analyser for ambient CO detection and return indoors making your way to mechanical room while checking for ambient CO readings...")
    time.sleep(10)
    print("Locate test port in exhaust piping of appliance, or drill a small hole for analyser wand if one is not already present.")
    time.sleep(2)
    print("Perform Combustion Analysis...")
    combustion_test()
elif not is_natural:
    print("Perform zeroing of combustion analyser outside of home and set analyser to LP Gas.")
    time.sleep(2)
    print("While outside, set analyser for ambient CO detection and return indoors making your way to mechanical room while checking for ambient CO readings...")
    time.sleep(10)
    print("Locate test port in exhaust piping of appliance, or drill a small hole for analyser wand if one is not already present.")
    time.sleep(2)
    print("Perform Combustion Analysis...")
    combustion_test()

time.sleep(2)
input("When ready, press [Enter] to generate a report...")

# Maintenance Report #

maint_report = [["Thermostat", ]]

print(tabulate(maint_report, headers=["Item Checked", "Actual Reading"]))
