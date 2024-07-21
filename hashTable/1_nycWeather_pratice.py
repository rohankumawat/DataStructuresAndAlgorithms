"""
The best data structure to use here is a list because all we wanted was access of temperature elements.
"""
arr = [] # create an empty list

with open("nyc_weather.csv","r") as f: # open the file in read mode
    for line in f: # for each line in the file
        tokens = line.split(',') # split the line by comma
        try: # try block to handle the exception
            temperature = int(tokens[1]) # convert the temperature to integer
            arr.append(temperature) # append the temperature to the list
        except: # except block to handle the exception
            print("Invalid temperature. Ignore the row") # print the message

print(arr) # print the list of temperatures

# What was the average temperature in first week of Jan

print(sum(arr[0:7])/len(arr[0:7])) # print the average temperature of the first week of January

# What was the maximum temperature in first 10 days of Jan

print(max(arr[0:10])) # print the maximum temperature of the first 10 days of January

# What was the temperature on Jan 9?
"""
The best data structure to use here is a dictionary (internally a hash table) 
because we wanted to know temperature for specific day, requiring key, value pair 
access where you can look up an element by day using O(1) complexity.
"""
weather_dict = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")

print(weather_dict) # print the dictionary of temperatures

# What was the temperature on Jan 9?

print(weather_dict['Jan 9']) # print the temperature of January 9th

# What was the temperature on Jan 4?

print(weather_dict['Jan 4']) # print the temperature of January 4th