import datetime
import time

while True:
    # Get the current date and time
    current_time = datetime.datetime.now()

    # Display the time to the user
    print(f"Current Time: {current_time.strftime('%H:%M:%S')}")

    # Wait for 1 second before updating the time
    time.sleep(500)

