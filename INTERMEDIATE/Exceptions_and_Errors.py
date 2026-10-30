#exceptions - errors that occur while a program is running
#raising an exception means creating an error intentionally

try:
    result=2/0
    #code that might cause an error
except ZeroDivisionError:
    print("You can't divide by zero")#runs when division by zero occurs
    #handles the error

#except <ERROR2>:
    #handles another type of error
#else:
    #runs if no exception occurs

finally:#runs whether an exception occurs or not
    result = 1
    #code that must run in any case

print(result)
