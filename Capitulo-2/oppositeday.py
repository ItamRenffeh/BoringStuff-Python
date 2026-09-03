
today_is_opposite_day = False

if today_is_opposite_day == True :   
    say_it_ipposite_day = True
else: say_it_ipposite_day = False

#If it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == True :
    say_it_ipposite_day = not say_it_ipposite_day
    
# say what day it is 
if say_it_ipposite_day == True:
    print("Today is Opposite-Day.")
else : 
    print("Today is not Opposite day")



