import time


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


