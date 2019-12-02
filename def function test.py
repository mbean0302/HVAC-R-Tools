import time

o2 = float()
co2 = float()
ex_a = float()
actual_efficiency = float()
stack_t = float()
co_ambient = int()
co_af = int()
calibrate_ok = True
comb_ok = False


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


combustion_test()
