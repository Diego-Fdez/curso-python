import time

current_time = time.localtime()

if current_time.tm_hour == 19:
    print("It's 7 o'clock")
else:
    less_time = 19 - current_time.tm_hour
    print(f"It's {less_time} hours before 19 o'clock")