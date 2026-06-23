class enemy:

    def __init__(self,name,HP,normal_attack,hard_attack):
        self.name = name
        self.HP = HP
        self.normal_attack = normal_attack
        self.hard_attack = hard_attack

    def take_damage(self,damage):
        self.HP -= damage

    def is_alive(self):
        if self.HP > 0 :
            return True
        else :
            return False
        


