print("how many kilometers did you cycle today?")
#input gets a value from the command line user and saves
# it to a variable
kms = float(input())
miles = kms/1.60934
print(f"Okay, you said {round(miles, 2)} miles")
#lets round it 
#rount(thing to round , decimal points)