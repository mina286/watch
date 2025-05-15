
from time import strftime ,localtime,gmtime
from datetime import datetime
class Watch :
    def __init__(self):
        print("Watch is created")

    def fun_show_time(self):
        self.date = datetime.now()
        print(f"date = {self.date.strftime('%d-%m-%Y')}")
        print("--------------")
        self.localtime = localtime()
        print(f"localtime ={strftime("%I - %M - %S -%p",self.localtime)}")
        print("--------------")
        self.worldtime = gmtime()
        print(f"worldtime ={strftime("%I - %M - %S -%p",self.worldtime)}")




w = Watch()
w.fun_show_time()