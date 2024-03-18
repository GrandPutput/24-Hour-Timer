'''Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
 If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
 Write a Python program to solve the general version of the above problem. Ask the user for the time now (in hours)
and then ask for the number of hours to wait for the alarm. 
Your program should output what the time will be on a 24-hour clock when the alarm goes off.'''

inital_time = 0
alarm_time = 0
new_time = 0
set_alarm = True
response = ''


print('Welcome')
print('')

while set_alarm == True:   
    inital_time = int(input('Please Enter Time: '))
    alarm_time = int(input('Please Enter How Many Hours From Alarm Time: '))
    print('')
    
    new_time = (inital_time + alarm_time) % 24 
    print('Alarm Will Go Off At', new_time, 'O\'clock')
    print('')

    response = input('Would You Like To Set A New Alarm Time? : ')
    print('')
    if response == 'no':
        set_alarm = False

print('Good Bye!')