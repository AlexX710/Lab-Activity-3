

starting_day = int(input("Starting day of the week"))
lenght_of_stay = int(input("How many nights did you stay?"))
return_date = (starting_day + lenght_of_stay) % 7
print(return_date)