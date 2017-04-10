import time as t

class MyTimer():
    def __init__(self):
        self.unit = [' year',' month',' day',' hour',' minute',' second']
        self.prompt = 'NOT START ! '
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __str__(self):
        return self.prompt


    __repr__ = __str__

    def __add__(self,other):
        prompt = 'sum is :'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    
    def start(self):
        self.begin=t.localtime()
        self.prompt = "Tips : Pls use stop method next !"
        print('START...')

    def stop(self):
        if not self.begin:
            print("Tips: Pls use start method first ! ")
        else:
            self.end=t.localtime()
            self._calc()
            print('END!')

    def _calc(self):
        self.lasted=[]
        self.prompt='Lasted time is :'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]))+self.unit[index]
        self.begin=0
        self.end=0
         
