blower_fla = float(input("Inducer Motor Rated Amperage [FLA/RLA]: "))
blower_amp = float(input("Inducer Motor Amperage on Highest Stage: "))
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





