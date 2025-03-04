from time import time
from run import *
from users import *

def start_work (msg.author.name, self.bal):
    # this function will be called when the user wants to work and if the user work he will earn 10$ and after he finish his work he need to wait 3 minutes to work again
    if msg.content.split(" ")[1] == "work":
        print (f"Ok {msg.author.name},You Are Working now and for your information for every time you work you will earn 10$ ")
        self.bal += 10 
        print (f"Your balance is now {self.bal}")
        x = time.sleep (10)
        print (x)
    else:
        print ("You can't work after you work for 3 minutes Ya N****,try again after 3 minutes ")
        x = time.sleep (10)
        print (x)