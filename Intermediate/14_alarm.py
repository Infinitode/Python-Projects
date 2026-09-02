#!/usr/bin/env python3
# Made by @Ericwasepic127 - with helpful comments

import datetime
import time


def get_current_time():
    """Returns the current local time as a (hour, minute, second) tuple."""
    now = datetime.datetime.now()
    return (now.hour, now.minute, now.second)


def get_int(prompt=""):
    """
    Prompts the user for an integer.
    Returns the integer on success, or None if the input is invalid.
    """
    user_input = input(prompt).strip()
    # Check if string contains only digits (rejects negative numbers and decimals)
    if not user_input.isdigit():
        print("Invalid input: Please enter a whole number.")
        return None
    return int(user_input)


def get_hour():
    """Prompts the user repeatedly until a valid hour (0-23) is entered."""
    while True:
        hour = get_int("Enter hour to alarm (0-23): ")
        if hour is None:
            print()
            continue
        if hour >= 24:
            print("Invalid hour! Must be less than 24.\n")
            continue
        if hour < 0:
            print("Invalid hour! Cannot be negative.\n")
            continue

        return hour


def get_min():
    """Prompts the user repeatedly until a valid minute (0-59) is entered."""
    while True:
        minute = get_int("Enter minute to alarm (0-59): ")
        if minute is None:
            print()
            continue
        if minute >= 60:
            print("Invalid minute! Must be less than 60.\n")
            continue
        if minute < 0:
            print("Invalid minute! Cannot be negative.\n")
            continue

        return minute


def get_alarm():
    """
    Gathers target hour and minute from user with confirmation prompt.
    Uses a loop instead of recursion to prevent potential stack depth issues.
    """
    while True:
        hour = get_hour()
        minute = get_min()
        alarm = (hour, minute, 0)

        print(f"\nSet alarm to {alarm[0]:02d}:{alarm[1]:02d}!")
        user_confirm = input("Is this correct (y/n)? ").strip().lower()

        if user_confirm.startswith("y"):
            return alarm

        print("\nLet's try again...\n")


def calculate_time_left(alarm):
    """
    Calculates the remaining time until the target alarm.
    Returns a (hours, minutes, seconds) tuple.
    """
    now = get_current_time()

    # Convert current time and alarm target into total seconds from midnight
    now_sec = now[0] * 3600 + now[1] * 60 + now[2]
    alarm_sec = alarm[0] * 3600 + alarm[1] * 60 + alarm[2]

    diff = alarm_sec - now_sec

    # If the target time has passed today, target the same time tomorrow (86400 secs in a day)
    if diff <= 0:
        diff += 86400

    hours = diff // 3600
    if hours == 24:
        hours = 0

    minutes = (diff % 3600) // 60
    seconds = diff % 60

    return (hours, minutes, seconds)


def main():
    print("=== Welcome to Alarm App! ===")
    print("Please set your alarm time.")
    alarm = get_alarm()

    print("\nAlarm running! Press Ctrl+C to exit.\n")

    while True:
        hours_left, mins_left, secs_left = calculate_time_left(alarm)

        # Trigger alarm when time reaches zero
        if hours_left == 0 and mins_left == 0 and secs_left == 0:
            print("\nALARM!!!!!!!!!!!!\007")  # \007 rings the system terminal bell
            break

        # Display countdown; padding clears remaining characters from previous print lines
        formatted_left = f"{hours_left:02d}:{mins_left:02d}:{secs_left:02d}"
        print(f"Time left: {formatted_left}   ", end="\r")

        # Sleep to keep CPU usage low during polling
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExited! Goodbye.")
