import time


def cap_test():
    is_single = str.upper(input("Type of capacitor [Single or Dual]: "))
    time.sleep(.600)
    cap_rating = float(input("What is the MFD rating on the capacitor?: "))
    time.sleep(.600)
    cap_tolerance = str(input("What is the tolerance percentage? [3%, 5%, 6%, 7%, or 10%]: "))
    while cap_tolerance == ["3%", "5%", "6%", "7%", "10%"]:
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
            print("Please select one of the following tolerances and include percentage operator: [3%, 5%, 6%, 7%, or 10%]... ")
            cap_tolerance = str(input("What is the tolerance percentage? [3%, 5%, 6%, 7%, or 10%]: "))
    while is_single == "SINGLE" or is_single == "DUAL":
        if is_single == "SINGLE":
            cap_v1 = float(input("Voltage between COMMON and RUN on the capacitor: "))
            cap_a1 = float(input("Amperage of the motor RUN wire: "))
            cap_actual1 = round(cap_v1 / (cap_a1 * float(2650.0), 2))
            print(f"This capacitor is operating at {cap_actual1} uF.")
            time.sleep(1.5)
            if cap_rating * (cap_tolerance + 1) >= cap_actual1 > cap_rating * (-1 * cap_tolerance + 1):
                print(f"Rated uF -- {cap_rating}...")
                time.sleep(.600)
                print(f"Actual uF -- {cap_actual1}...")
                time.sleep(.600)
                print("Capacitor is within tolerance. No replacement needed.")
                return True




cap_test()
