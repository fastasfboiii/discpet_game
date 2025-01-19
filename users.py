from time_calc import time_min_f,time_hour_f, time_second_f, last_feed_f, last_play_f, age_f, genesis_f

class User:
    def __init__(self,user_id):
        self.bal = 100
    def Check_bal(self):
        return self.bal
    def Buy(self,user_id):
        if self.bal <= 0:
            x=1
            print("Bitch you'r broke how can you buy something when you're that broke HAHAHAHA")
            return "Bitch you'r broke how can you buy something when you're that broke HAHAHAHA",x
        else:
            x = 0
            if user_id == 310429717893349378 or user_id == 997896073270018128 or user_id == 377158352733732864:
                self.bal = self.bal+50
            self.bal = self.bal-50
            print (self.bal)
            return self.bal,x



    def part_time(self):
        currentTime = time_hour_f(self)
        if lastTimeCalled == None:
            lastTimeCalled = 0
        else: 
            partTimePay = (currentTime - lastTimeCalled)*10
            self.bal += partTimePay
            return lastTimeCalled
        




