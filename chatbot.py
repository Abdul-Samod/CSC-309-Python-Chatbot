import datetime

# 1. Ask the user for their name
name = input("Hello! What is your name?\n> ")

# 2. Respond with a personalized greeting
print(f"Nice to meet you, {name}!")

# 3. Get the current date
current_date = datetime.datetime.now()

# 4. Format the date (e.g., November 14, 2024)
# %B = Month name, %d = Day, %Y = Year
formatted_date = current_date.strftime("%B %d, %Y")

# 5. Display the date in a friendly format
print(f"Today’s date is {formatted_date}.")
