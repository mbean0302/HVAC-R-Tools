import time
import numpy

# Global Variables #

tech = str("")
date = str("")
od_ambient = int()
name = str("")
call_num = int()
svc_req = str("")
btu_input = int(0)
btu_output = int(0)
actual_deltat = float(0)
actual_cfm = int(0)
efficiency_percentage = float()
is_condensing = str("")
has_uv = False
has_hum = False
is_natural = True

# Condition Reporting Variables #

is_call = str()
tstat_ok = True
on_arrival = True
voltage_ok = True
ignitor_resistance_ok = True
inducer_ok = True
indcap_ok = True
pressure_switch_ok = True
ignitor_ok = True
gas_valve_ok = True
flame_proving_ok = True
indoor_blower_ok = True
drain_ok = True
capacity_ok = True
cfm_ok = True
safety_ok = True
comb_ok = True
hum_ok = False
uv_ok = False

o2 = float()
co2 = float()
ex_a = float()
actual_efficiency = float()
stack_t = float()
co_ambient = int()
co_af = int()
calibrate_ok = True

# Defined Functions #


def single_stage():
    rated_pressure_1 = float(input("What is the rated fuel pressure of the appliance in [in wc]?: "))
    actual_pressure_1 = float(input("What is the measured fuel pressure in [in wc]?: "))
    if actual_pressure_1 == rated_pressure_1:
        print("Fuel pressure is set perfectly. Do not adjust...")
        return
    elif rated_pressure_1 * 1.10 > actual_pressure_1 > rated_pressure_1 * .90:
        print(f"Fuel pressure is within allowable range, but should be adjusted to {rated_pressure_1} in wc. ")
        return
    else:
        print(f"""Fuel pressure is out of range. Adjust fuel pressure from {round(actual_pressure_1, 2)} to between 
{round(rated_pressure_1 * .90, 2)} and {round(rated_pressure_1 * 1.10, 1)}. Optimal fuel pressure should be {round(rated_pressure_1, 2)}.""")
        return


def two_stage_low():
    rated_pressure_1 = float(
        input("What is the rated fuel pressure of the appliance when in FIRST STAGE? in [in wc]?: "))
    actual_pressure_1 = float(input("What is the measured fuel pressure in FIRST STAGE? in [in wc]?: "))
    if actual_pressure_1 == rated_pressure_1:
        print("Fuel pressure is set perfectly. Do not adjust...")
        return
    elif rated_pressure_1 * 1.10 > actual_pressure_1 > rated_pressure_1 * .90:
        print(f"Fuel pressure is within allowable range, but should be adjusted to {rated_pressure_1} in wc. ")
        return
    else:
        print(f"""Fuel pressure is out of range. Adjust fuel pressure from {round(actual_pressure_1, 2)} to between 
{round(rated_pressure_1 * .90, 2)} and {round(rated_pressure_1 * 1.10, 1)}. Optimal fuel pressure should be {round(rated_pressure_1, 2)}.""")
        return


def two_stage_high():
    rated_pressure_1 = float(
        input("What is the rated fuel pressure of the appliance when in SECOND STAGE? in [in wc]?: "))
    actual_pressure_1 = float(input("What is the measured fuel pressure in SECOND STAGE? in [in wc]?: "))
    if actual_pressure_1 == rated_pressure_1:
        print("Fuel pressure is set perfectly. Do not adjust...")
        return
    elif rated_pressure_1 * 1.10 > actual_pressure_1 > rated_pressure_1 * .90:
        print(f"Fuel pressure is within allowable range, but should be adjusted to {rated_pressure_1} in wc. ")
        return
    else:
        print(f"""Fuel pressure is out of range. Adjust fuel pressure from {round(actual_pressure_1, 2)} to between 
{round(rated_pressure_1 * .90, 2)} and {round(rated_pressure_1 * 1.10, 1)}. Optimal fuel pressure should be {round(rated_pressure_1, 2)}.""")
        return


def mod_stage_least():
    rated_pressure_1 = float(
        input("What is the rated fuel pressure of the appliance when in lowest possible firing rate? in [in wc]?: "))
    actual_pressure_1 = float(input("What is the measured fuel pressure in the lowest possible firing rate? [in wc]: "))
    if actual_pressure_1 == rated_pressure_1:
        print("Fuel pressure is perfect. Move on to next step in the maintenance...")
        return True
    elif rated_pressure_1 * 1.10 > actual_pressure_1 > rated_pressure_1 * .90:
        print("Fuel pressure is within allowable range, but should be noted for re-check at next maintenance. ")
        return True
    else:
        print("Fuel pressure is out of range. Modulating gas valves are not adjustable. Replace the gas valve.")
        return False


def mod_stage_max():
    rated_pressure_1 = float(
        input("What is the rated fuel pressure of the appliance when in highest possible firing rate? in [in wc]?: "))
    actual_pressure_1 = float(
        input("What is the measured fuel pressure in the highest possible firing rate? [in wc]: "))
    if actual_pressure_1 == rated_pressure_1:
        print("Fuel pressure is perfect. Move on to next step in the maintenance...")
        return True
    elif rated_pressure_1 * 1.10 > actual_pressure_1 > rated_pressure_1 * .90:
        print("Fuel pressure is within allowable range, but should be noted for re-check at next maintenance. ")
        return True
    else:
        print("Fuel pressure is out of range. Modulating gas valves are not adjustable. Replace the gas valve.")
        return False


def flame_rod():
    strike_count = 0
    flame_prove = str.upper(input("After ignition, did the burners stay lit? [Y/N]: "))
    time.sleep(.650)
    while flame_prove == "Y":
        if flame_prove == "Y" and strike_count < 2:
            flame_signal = float(input("After flame stabilizes, what is the measured flame signal? [uA]: "))
            if 16.00 > flame_signal >= 2.50:
                print("Flame signal is within allowable range and cleaning/replacement not required.")
                return True
            elif 0.50 < flame_signal < 2.50 and strike_count == 0:
                print("Flame signal is low. Remove and clean the flame sensor and re-test...")
                strike_count += 1
                time.sleep(1.5)
            elif 0.50 < flame_signal < 2.50 and strike_count == 1:
                print("Cleaning the flame sensor did not provide an adequate flame signal. Replacement of flame sensor required.")
                time.sleep(.600)
                return False
            elif flame_signal < .50 or flame_signal > 16:
                print("Flame sensor is either shorted or open. Replacement of flame sensor required.")
                return False
    while flame_prove == "N":
        strike_count = 0
        print("Remove and clean the flame sensor prior to testing flame signal...")
        strike_count += 1
        time.sleep(1.5)
        flame_prove = str.upper(input("After ignition, did the burners stay lit? [Y/N]: "))
        if flame_prove == "N" and strike_count == 1:
            print("Cleaning the flame sensor did not provide an adequate flame signal. Replacement of flame sensor required.")
            time.sleep(.600)
            return False
        elif flame_prove == "Y" and strike_count < 2:
            flame_signal = float(input("After flame stabilizes, what is the measured flame signal? [uA]: "))
            if 16.00 > flame_signal >= 2.50:
                print("Flame signal is within allowable range and cleaning/replacement not required.")
                return True
            elif 0.50 < flame_signal < 2.50 and strike_count == 0:
                print("Flame signal is low. Remove and clean the flame sensor and re-test...")
                strike_count += 1
                time.sleep(1.5)
            elif 0.50 < flame_signal < 2.50 and strike_count == 1:
                print("Cleaning the flame sensor did not provide an adequate flame signal. Replacement of flame sensor required.")
                time.sleep(.600)
                return False
            elif flame_signal < .50 or flame_signal > 16:
                print("Flame sensor is either shorted or open. Replacement of flame sensor required.")
                return False


def tcouple():
    print("Remove the thermocouple connection from the gas valve and measure the mV DC signal voltage with pilot lit...")
    time.sleep(1.5)
    strike_count = 0
    mv_reading = float(input("What is the measured mV DC reading of the thermocouple?: "))
    while strike_count < 2:
        if mv_reading < 27.01 and strike_count == 0:
            print("Thermocouple signal voltage is out of range. Remove and attempt cleaning of thermocouple. Re-test when cleaning is complete...")
            strike_count += 1
            time.sleep(1.5)
            mv_reading = float(input("What is the measured mV DC reading of the thermocouple?: "))
        elif mv_reading >= 27.01:
            print("Thermocouple signal voltage is within allowable range. Cleaning/Replacement is not required.")
            time.sleep(.600)
            return False
        elif mv_reading < 27.01 and strike_count == 1:
            print("Thermocouple signal voltage is still out of range. Replace the thermocouple.")
            return True


def cap_test1():
    cap_rating = float(input("What is the uF rating on the capacitor?: "))
    time.sleep(2)
    cap_list = ["3%", "5%", "6%", "7%", "10%"]
    cap_tolerance = str(input("What is the tolerance percentage? [3%, 5%, 6%, 7%, or 10%]: "))
    while cap_tolerance in cap_list:
        if cap_tolerance == "3%":
            cap_tolerance = 0.03
            break
        elif cap_tolerance == "5%":
            cap_tolerance = 0.05
            break
        elif cap_tolerance == "6%":
            cap_tolerance = 0.06
            break
        elif cap_tolerance == "7%":
            cap_tolerance = 0.07
            break
        elif cap_tolerance == "10%":
            cap_tolerance = 0.10
            break
        else:
            print("Please select one of the following tolerances and include the percentage operator: [3%, 5%, 6%, 7%, or 10%]... ")
            cap_tolerance = str(input("What is the tolerance percentage? [3%, 5%, 6%, 7%, or 10%]: "))
    print("Verify that the motor associated with the capacitor being checked is running...")
    time.sleep(.600)
    cap_v1 = float(input("Voltage between COMMON and RUN on the capacitor: "))
    round(cap_v1, 2)
    cap_a1 = float(input("Amperage of the motor RUN wire: "))
    round(cap_a1, 2)
    cap_actual1 = (cap_a1 * 2650.0) / cap_v1
    time.sleep(1.5)
    if cap_rating * (cap_tolerance + 1) >= cap_actual1 > cap_rating * (-1 * cap_tolerance + 1):
        print(f"Rated uF -- {cap_rating}...")
        time.sleep(.600)
        print(f"Actual uF -- {round(cap_actual1, 2)}...")
        time.sleep(.600)
        print("Capacitor is within tolerance. No replacement needed.")
        return True
    else:
        print(f"Rated uF -- {cap_rating}...")
        time.sleep(.600)
        print(f"Actual uF -- {round(cap_actual1, 2)}...")
        time.sleep(.600)
        print("Capacitor is out of tolerance. Replacement required.")
        return False


def single_stage_deltat():
    global actual_deltat
    rated_deltat = range(int(input("What is the lowest recommended temperature rise (Delta T) of the appliance?: ")),
                         int(input("What is the highest allowable temperature rise (Delta T) of the appliance?: ")) + 1)
    deltat_ok = 0
    while deltat_ok < 2:
        ra_temp = float(input("What is the measured return air temperature?: "))
        round(ra_temp)
        ra_temp = int(ra_temp)
        sa_temp = float(input("What is the measured supply air temperature?: "))
        round(sa_temp)
        sa_temp = int(sa_temp)
        actual_deltat = sa_temp - ra_temp
        if actual_deltat in rated_deltat:
            print("Temperature rise (Delta T) is within allowable range. No blower speed adjustment necessary...")
            time.sleep(.600)
            return True
        elif actual_deltat not in rated_deltat and deltat_ok < 1:
            print("Temperature rise (Delta T) is out of allowable range. Verify/Adjust blower speed setting and re-check temperature rise (Delta T)...")
            deltat_ok += 1
            time.sleep(1.5)
        else:
            print("Temperature rise (Delta T) is still out of allowable range. Further troubleshooting is needed to verify issue....")
            time.sleep(1.5)
            print("Complete remainder of maintenance, if possible...")
            time.sleep(.600)
            return False


def two_stage_low_deltat():
    global actual_deltat
    rated_deltat = range(int(input("What is the lowest recommended temperature rise (Delta T) of the appliance in FIRST stage heating?: ")),
                         int(input("What is the highest allowable temperature rise (Delta T) of the appliance in FIRST stage heating?: ")) + 1)
    deltat_ok = 0
    while deltat_ok < 2:
        ra_temp = float(input("What is the measured return air temperature?: "))
        round(ra_temp)
        ra_temp = int(ra_temp)
        sa_temp = float(input("What is the measured supply air temperature?: "))
        round(sa_temp)
        sa_temp = int(sa_temp)
        actual_deltat = sa_temp - ra_temp
        if actual_deltat in rated_deltat:
            print("Temperature rise (Delta T) is within allowable range. No blower speed adjustment necessary...")
            time.sleep(.600)
            return True
        elif actual_deltat not in rated_deltat and deltat_ok < 1:
            print("Temperature rise (Delta T) is out of allowable range. Verify/Adjust blower speed setting and re-check temperature rise (Delta T)...")
            deltat_ok += 1
            time.sleep(1.5)
        else:
            print("Temperature rise (Delta T) is still out of allowable range. Further troubleshooting is needed to verify issue....")
            time.sleep(1.5)
            print("Complete second stage temperature rise (Delta T) test and remainder of maintenance, if possible...")
            time.sleep(.600)
            return False


def two_stage_high_deltat():
    global actual_deltat
    rated_deltat = range(int(input("What is the lowest recommended temperature rise (Delta T) of the appliance in SECOND stage heating?: ")),
                         int(input("What is the highest allowable temperature rise (Delta T) of the appliance in SECOND stage heating?: ")) + 1)
    deltat_ok = 0
    while deltat_ok < 2:
        ra_temp = float(input("What is the measured return air temperature?: "))
        round(ra_temp)
        ra_temp = int(ra_temp)
        sa_temp = float(input("What is the measured supply air temperature?: "))
        round(sa_temp)
        sa_temp = int(sa_temp)
        actual_deltat = sa_temp - ra_temp
        if actual_deltat in rated_deltat:
            print("Temperature rise (Delta T) is within allowable range. No blower speed adjustment necessary...")
            time.sleep(.600)
            return True
        elif actual_deltat not in rated_deltat and deltat_ok < 1:
            print("Temperature rise (Delta T) is out of allowable range. Verify/Adjust blower speed setting and re-check temperature rise (Delta T)...")
            deltat_ok += 1
            time.sleep(1.5)
        else:
            print("Temperature rise (Delta T) is still out of allowable range. Further troubleshooting is needed to verify issue....")
            time.sleep(1.5)
            print("Complete the remainder of the maintenance, if possible...")
            time.sleep(.600)
            return False


def mod_stage_least_deltat():
    global actual_deltat
    rated_deltat = range(int(input("What is the lowest recommended temperature rise (Delta T) of the appliance in the LOWEST firing rate (Usually 35%)?: ")),
                         int(input("What is the highest allowable temperature rise (Delta T) of the appliance in the LOWEST firing rate (Usually 35%)?: ")) + 1)
    deltat_ok = 0
    while deltat_ok < 2:
        ra_temp = float(input("What is the measured return air temperature?: "))
        round(ra_temp)
        ra_temp = int(ra_temp)
        sa_temp = float(input("What is the measured supply air temperature?: "))
        round(sa_temp)
        sa_temp = int(sa_temp)
        actual_deltat = sa_temp - ra_temp
        if actual_deltat in rated_deltat:
            print("Temperature rise (Delta T) is within allowable range. No blower speed adjustment necessary...")
            time.sleep(.600)
            return True
        elif actual_deltat not in rated_deltat and deltat_ok < 1:
            print("Temperature rise (Delta T) is out of allowable range. Verify/Adjust blower speed setting and re-check temperature rise (Delta T)...")
            deltat_ok += 1
            time.sleep(1.5)
        else:
            print("Temperature rise (Delta T) is still out of allowable range. Further troubleshooting is needed to verify issue....")
            time.sleep(1.5)
            print("Complete the remainder of the maintenance, if possible...")
            time.sleep(.600)
            return False


def mod_stage_max_deltat():
    global actual_deltat
    rated_deltat = range(int(input("What is the lowest recommended temperature rise (Delta T) of the appliance in the HIGHEST firing rate (100% Capacity)?: ")),
                         int(input("What is the highest allowable temperature rise (Delta T) of the appliance in the HIGHEST firing rate (100% Capacity)?: ")) + 1)
    deltat_ok = 0
    while deltat_ok < 2:
        ra_temp = float(input("What is the measured return air temperature?: "))
        round(ra_temp)
        ra_temp = int(ra_temp)
        sa_temp = float(input("What is the measured supply air temperature?: "))
        round(sa_temp)
        sa_temp = int(sa_temp)
        actual_deltat = sa_temp - ra_temp
        if actual_deltat in rated_deltat:
            print("Temperature rise (Delta T) is within allowable range. No blower speed adjustment necessary...")
            time.sleep(.600)
            return True
        elif actual_deltat not in rated_deltat and deltat_ok < 1:
            print("Temperature rise (Delta T) is out of allowable range. Verify/Adjust blower speed setting and re-check temperature rise (Delta T)...")
            deltat_ok += 1
            time.sleep(1.5)
        else:
            print("Temperature rise (Delta T) is still out of allowable range. Further troubleshooting is needed to verify issue....")
            time.sleep(1.5)
            print("Complete the remainder of the maintenance, if possible...")
            time.sleep(.600)
            return False


def btu_calc():
    global btu_input, btu_output, efficiency_percentage
    btu_input = int(input("What is the BTU Input rating of the appliance?: "))
    time.sleep(.600)
    efficiency_percentage = float(input("What is the rated efficiency of the appliance? [ex. 80, 95, etc...]: ")) / 100
    btu_output = f"{int(btu_input * efficiency_percentage)} BTU/h"
    time.sleep(.600)
    print(f"The BTU Output rating of the furnace is {btu_output}.")


def condensing_check():
    global is_condensing
    if efficiency_percentage < .90:
        is_condensing = "Non-Condensing"
        print(f"This appliance has been categorized as a {is_condensing} appliance...")
        time.sleep(.600)
    elif efficiency_percentage >= .90:
        is_condensing = "Condensing"
        print(f"This appliance has been categorized as a {is_condensing} appliance...")
        time.sleep(.600)


def cfm_calc():
    global actual_cfm
    actual_cfm = btu_output / (1.08 * actual_deltat)
    print(f"The CFM on highest heat stage is {int(actual_cfm)}.")


def cond_drain_clear():
    global drain_ok
    strike_counter = 0
    print("Take the lowest hose off of the header box and check for backed up water, indicating a clogged drain...")
    time.sleep(2.5)
    is_clogged = str.upper(input("Is there any water backed up in the header box? [Y/N]: "))
    time.sleep(1)
    print("Use the clean-out on the trap, if provided, to flush the trap assembly with fresh water. Make sure to refill trap when finished...")
    time.sleep(4.5)
    print("Ask home-owner for a small amount of bleach or vinegar to treat the standing water in the trap. If no bleach or vinegar available, then skip this step.")
    time.sleep(4.5)
    print("Observe the appliance operating under normal conditions, and check for a free-flowing condensate drain...")
    time.sleep(2.5)
    is_clear = str.upper(input("Is the drain clear? [Y/N]: "))
    while is_clear == "Y" or is_clear == "N" and strike_counter < 3:
        if is_clear == "Y":
            drain_ok = True
            time.sleep(.600)
            print("The condensate drain system is clear. No further action required.")
            return
        elif is_clear == "N" and strike_counter < 1:
            print("Repeat the above process and re-check condensate drain for proper drainage...")
            time.sleep(1.5)
            print("Take the lowest hose off of the header box and check for backed up water, indicating a clogged drain...")
            time.sleep(1.5)
            is_clogged = str.upper(input("Is there any water backed up in the header box? [Y/N]: "))
            print("Use the clean-out on the trap, if provided, to flush the trap assembly with fresh water. Make sure to refill trap when finished...")
            time.sleep(.600)
            print("Ask home-owner for a small amount of bleach or vinegar to treat the standing water in the trap. If no bleach or vinegar available, then skip this step.")
            time.sleep(1.5)
            print("Observe the appliance operating under normal conditions, and check for a free-flowing condensate drain...")
            time.sleep(1.5)
            is_clear = str.upper(input("Is the drain clear? [Y/N]: "))
            strike_counter += 1
        elif is_clear == "N" and strike_counter == 1:
            print("Remove all pressure switches from appliance, if any, and use pressurized CO2 or Nitrogen to clear all lines...")
            time.sleep(1.5)
            print("Observe the appliance operating under normal conditions, and check for a free-flowing condensate drain...")
            time.sleep(1.5)
            is_clear = str.upper(input("Is the drain clear? [Y/N]: "))
            if is_clear == "Y":
                time.sleep(.600)
                print("The condensate drain system is clear. No further action required.")
                return
            elif is_clear == "N":
                strike_counter += 1
        elif strike_counter == 2:
            print("Condensate drain system requires further troubleshooting, and may need to be re-piped and/or the trap replaced.")
            drain_ok = False
            return


def combustion_test():
    global o2, co2, ex_a, actual_efficiency, stack_t, co_ambient, co_af, calibrate_ok, comb_ok
    strike_counter = 0
    is_ok = str.upper(input("Did the Combustion Analyser Zero properly? [Y/N]: "))
    while is_ok == "Y" or is_ok == "N" and strike_counter <= 2:
        if is_ok == "Y":
            calibrate_ok = True
            break
        elif is_ok == "N" and strike_counter < 2:
            print("Calibration must be performed outdoors in a location not suspected of having carbon monoxide...")
            time.sleep(.600)
            calibrate_ok = False
            print("Redo Calibration...")
            strike_counter += 1
            time.sleep(1)
            is_ok = str.upper(input("Did the Combustion Analyser Zero properly? [Y/N]: "))
        elif is_ok == "N" and strike_counter == 2:
            print("Calibration can not be performed and Combustion Analyser should be sent off for testing/repair...")
            calibrate_ok = False
            return
        else:
            print("ERROR: Please specify Yes or No. [Y/N].")
            is_ok = str.upper(input("Did the Combustion Analyser Zero properly? [Y/N]: "))
    time.sleep(1.5)
    co_ambient = int(input("What was the peak Ambient CO reading detected in the home? [ex. 0, 4, 25]: "))
    time.sleep(1.5)
    print("Start the analyser in the 'combustion test' mode and place the wand in the flue pipe test port...")
    time.sleep(2)
    print("Continue the combustion testing until the [Stack Temperature] and [CO Air Free] readings are stable...")
    time.sleep(1)
    o2 = float(input("O2 Reading without percentage operator [ex. 4.0, 6.7, 10]: "))
    time.sleep(.600)
    co2 = float(input("CO2 Reading without percentage operator [ex. 4.0, 6.7, 10]: "))
    time.sleep(.600)
    ex_a = float(input("Excess Air reading without percentage operator [ex. 25.0, 31.6, 50]: "))
    time.sleep(.600)
    actual_efficiency = float(input("Actual Efficiency(Gross Efficiency) reading without percentage operator [ex. 4, 6, 10]: "))
    time.sleep(.600)
    stack_t = float(input("Stack Temperature reading [ex. 4, 6, 10]: "))
    time.sleep(.600)
    co_af = int(input("Carbon Monoxide Air-Free(Undiluted) reading without percentage operator [ex. 10, 14, 25]: "))
    time.sleep(1.5)
    print("Combustion Test Complete!")
    time.sleep(.600)
    print("Analysing Results..........")
    time.sleep(5)
    if co_af <= 50 and co_ambient <= 10:
        print(f"This appliance is safe to operate. Ambient CO is {co_ambient} ppm. CO Air-Free is {co_af} ppm.")
        comb_ok = True
        return
    elif co_af <= 50 and co_ambient > 10:
        print(f"CO Air-Free of appliance being testing is within allowable range. Ambient CO is {co_ambient} ppm. This is above acceptable limits! Check ALL fuel burning appliances until a source is discovered, and recommend repairs to customer.")
        comb_ok = False
        return
    elif 50 < co_af < 100 and co_ambient <= 10:
        print(f"Ambient CO is {co_ambient} ppm and within allowable limits, but CO Air-Free of appliance being tested is {co_af} ppm. This is a potentially unsafe situation and repairs should be recommended.")
        comb_ok = False
        return
    elif 50 < co_af < 100 and co_ambient > 10:
        print(f"Ambient CO is {co_ambient} ppm. This is above allowable limits! CO Air-Free of appliance being tested is {co_af} ppm. This is an unsafe situation and repairs should be recommended for the appliance.")
        time.sleep(.600)
        print("Also, check ALL fuel burning appliances until a source of ambient CO is discovered, and recommend repairs to customer, regardless if appliance being tested is the issue.")
        comb_ok = False
        return
    elif co_af >= 100:
        print(f"CO Air-Free is {co_af} ppm! This is an unsafe appliance and it is required that the appliance be shut down and labeled unsafe. Recommend repairs or replacement and document everything on the service invoice along with a customer signature acknowledging the issue!")
        comb_ok = False
        return
