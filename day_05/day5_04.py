import datetime

# Get current date and time
current_datetime = datetime.datetime.now()

# Display current date and time
print("Current Date and Time:", current_datetime)

# Print day of the week
day_of_week = current_datetime.strftime("%A")
print("Day of the Week:", day_of_week)
