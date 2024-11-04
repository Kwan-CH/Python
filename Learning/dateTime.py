import datetime
import time

currentDate = datetime.date.today()
print(currentDate.strftime('%Y %b %d'))
print(currentDate.month)
print(currentDate.day)
print(currentDate.year)
print(f'{currentDate.day}-{currentDate.month}-{currentDate.year}')

print(datetime.datetime.today().strftime('%d %m %Y %H:%M:%S'))
print(len(datetime.datetime.today().strftime('%d %m %Y %H:%M:%S')))

# day = input('what is your birthday (mm/dd/yyyy): ')
# birth = datetime.datetime.strptime(day, '%m/%d/%Y').date()
# differences = currentDate - birth
# age = differences.days/365
# print('you are {0:.0f} years old'.format(age))
#
# currentTime = datetime.datetime.now()
# print(currentTime)
# print(currentTime.hour)
# print(currentTime.minute)
# print(currentTime.second)
#
# # print format
# print('I have {0:d} cats and {1:d} dogs'.format(6, 2))