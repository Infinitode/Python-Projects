#!/usr/bin/env python3
# Made by @Ericwasepic127 - with helpful comments

import datetime # Imports module of datetime for gather current datetime
import time # Imports module of time for poll

def get_hour_min(): 
    # Defines reusable function for getting hour & minute
    current = datetime.datetime.now() # Gets datetime object with current date and time
    hour = current.hour # Extract Hour
    minute = current.minute # Extract Minute
    second = current.second # Extract Seconds 
    now = (hour, minute, second) # Combine into tuple
    return now # Give the tuple

def get_int(prompt=""): 
    # Defines function to get integer from input
    user = input(prompt) # Get input
    if not user.isdigit(): # Detect is it only has digits (even dot isn't allowed)
        print("Not a number")
        return # Return nothing
    return int(user)

def get_hour(): 
    # Hour getting function - makes pretty reusable
    hour_get = False # let's make variable for our while loop
    while not hour_get: # Create while loop
        hour = get_int("Enter hour to alarm: ")
        if hour is None: # in case user didn't gave integer
            print()
            continue
        if hour >= 24:
            # Can't be above 24 hour
            print("Exceeded hour!\n")
            continue
        elif hour < 0:
            # Can't below 0
            print("Decreased hour!\n")
            continue
        else:
            hour_get = True # Say I got the hour to our while loop!
    return hour

def get_min(): 
    # Minute getting function - makes pretty reusable
    min_get = False # let's make variable for our while loop
    while not min_get: # Create while loop
        minute = get_int("Enter minute to alarm: ")
        if minute is None: # in case user didn't gave integer
            print()
            continue
        if minute >= 60:
            # Can't be above 60 minute
            print("Exceeded hour!\n")
            continue
        elif minute < 0:
            # Can't below 0
            print("Decreased hour!\n")
            continue
        else:
            min_get = True # Say I got the minute to our while loop!
    return minute

def get_alarm(): 
    # Reusable function to get tuple of alarm time!
    alarm = (
        get_hour(), # Get hour using our function
        get_min(), # Get minute too!
        0 # for second
    )
    # Let's make confirmation system to avoid unwanted alarm time!
    print(f"Set alarm to {alarm[0]}:{alarm[1]}!")
    user_confirm = input("Is this correct (y/n)? ")
    user_confirm = user_confirm.strip() # Clean any blank spaces
    if user_confirm != "y" or not user_confirm.startswith("y"): # Not y
        print("\nGetting again ...")
        alarm = get_alarm() # Do recursive call
    return alarm

def time_left(alarm):
    # Reusable function for time left calculation
    now = get_hour_min() # Get current staticmethod
    # Convert everything to seconds
    now_sec = now[0]*3600 + now[1]*60 + now[2]
    alarm_sec = alarm[0]*3600 + alarm[1]*60 + alarm[2]
    diff = alarm_sec - now_sec # Calculate difference
    if diff <= 0: # Negative
        diff += 86400  # Next day
    h = diff // 3600 # Hour
    if h == 24: # As 24 Hour
        h = 0 # go to 0
    m = (diff % 3600) // 60 # Minute
    s = diff % 60 # Second
    diff_tuple = (h, m, s) # Make into one tuple
    return diff_tuple

def main():
    # Main section 
    print("===Welcome to Alarm app!===")
    print("Please set alarm!")
    alarm = get_alarm()
    print("Ctrl-C to stop alarm!\n")
    while True: 
        # Make while loop but infinity
        left = time_left(alarm) # Get left-time
        left_hour = left[0] # Get Hour
        left_min = left[1] # Get Minute
        left_sec = left[2] # Get Seconds
        if left_hour == 0 and left_min == 0 and left_sec == 0:
            print("ALARM!!!!!!!!!!!!\007") # \007 is bell chapter 
            break
        formatted_left = f"{left_hour:02d}:{left_min:02d}:{left_sec:02d}" # Format left-time
        print(f"Left: {formatted_left}", end="\r")
        time.sleep(1) # Sleep to rest CPU 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Exitted! Goodbye")
  
