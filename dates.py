from datetime import datetime, timedelta, date

# get the current date and time
# includes the year, month, day, hour, minute, second, and microsecond
current_date = datetime.now()
print(current_date)


# get the current year, month, day
current_year = current_date.year
current_day = current_date.day
current_month = current_date.month

print(current_year)
print(current_day)
print(current_month)


print('-------------------')

# actual date year, month, day
current_day = date.today()
print(current_day)



# when we subtract two dates, we get a timedelta object
# like this we created a date 
date1 = datetime(year=2023, month=11, day=1)
date2 = datetime(year=2020, month=11, day=1)

# when we subtract two dates, we get a timedelta object 
# and the result is the difference in days between the two dates
diff = date1 - date2
print(diff)


print(current_day - timedelta(days=1))

