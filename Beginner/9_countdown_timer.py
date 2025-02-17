from time import sleep

# Prompt the user for a time to countdown from
time = input("Enter the time to countdown from (MM:SS): ")

# Check the format of the input
if len(time) != 5 or time[2] != ":":
    print("Invalid time format")
    exit()

# Extract the minutes and seconds
minutes = int(time[:2])
seconds = int(time[3:])
total_seconds = minutes * 60 + seconds

# Countdown
for i in range(total_seconds, 0, -1):
    print(f"{i//60:02}:{i%60:02}")
    sleep(1)

print("00:00")
print("Time's up!")