

class Operator:
    def __init__(self,name,hp,lv):
        self.name = name
        self.hp = hp
        self.lv = lv

class Suzuran(Operator):
    def __init__(self,name,hp,lv,attack):
        super().__init__(name,hp,lv)
        self.attack = attack
    
    def info(self):
        print(f"Name {self.name} HP {self.hp} LV {self.lv} Attack {self.attack}")

obj = Suzuran("Suzuran","1590","80","550")

obj.info()