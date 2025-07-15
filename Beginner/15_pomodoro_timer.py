import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

def main():
    print("Pomodoro Timer")
    while True:
        try:
            work_minutes = int(input("Enter work duration in minutes: "))
            break_minutes = int(input("Enter break duration in minutes: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        print("Work session started.")
        countdown(work_minutes)
        print("Work session finished. Take a break!")
        countdown(break_minutes)
        print("Break finished. Time to get back to work!")

if __name__ == "__main__":
    main()
