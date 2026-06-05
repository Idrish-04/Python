month=input("Enter name of  month").capitalize()
if month in ["September","October" , "November"]:
    print("The season is Autumn")
elif month in ["December", "January", "February"]:
    print("The season is Winter")

elif month in ["March", "April", "May"]:
    print("The season is Spring")

elif month in ["June", "July", "August"]:
    print("The season is Summer")

else:
    print("Invalid month")
