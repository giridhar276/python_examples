"""
Program 29:
Built-in library: datetime module examples.
"""

from datetime import datetime, date, timedelta

today = date.today()
now = datetime.now()

print("Today's date:", today)
print("Current datetime:", now)

# Formatting date
formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted datetime:", formatted_date)

# Date after 7 days
future_date = today + timedelta(days=7)
print("Date after 7 days:", future_date)

# Date before 5 days
past_date = today - timedelta(days=5)
print("Date before 5 days:", past_date)
