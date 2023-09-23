from random import randint

class Timer:
    def __init__(self,time:float):
        self.time = float(time)
        self.timer = 0


    def reset(self):
        self.timer = 0


    def is_finish(self):
        return self.timer >= self.time


    def get_current_time_float(self)->float:
        return self.timer


    def get_current_time(self):
        return int(self.timer)


    def randon(self):
        self.timer = randint(0,self.time-1)


    def update(self, dt):
        # print(self.timer, " < ", self.time, self.is_finish())
        aux_timer = self.timer + dt
        if self.time >= int(aux_timer):
            self.timer = aux_timer


    def get_porcent(self)->float:
        return self.time / self.timer
