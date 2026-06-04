Charging_level = 20
electricity_status = True 
while(Charging_level <= 100):
    if(electricity_status):
        print("Battry Level :",Charging_level,"%")
        Charging_level = Charging_level +10
    else:
        break
print("full charge")