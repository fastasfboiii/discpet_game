from users import *
from time_calc import work_timer_f

def start_work (self):
    # this function will be called when the user wants to work and if the user work he will earn 10$ and after he finish his work he need to wait 10 secound to work again 
    print (f"Ok,You Are Working now and for your information for every time you work you will earn 10$ and you must wait 10 secound to work again")
    self.bal += 10 
    print (f"Your balance is now {self.bal}")