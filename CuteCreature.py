import random

class CuteCreature:

    #constructor for cute creature 
    def __init__(self, Species, Level, MHP, CHP, AR, DR, XP, CXP ,XPV, is_special):
        self.Species = Species
        self.Level = 1
        self.MHP = MHP
        self.CHP = MHP
        self.AR = AR
        self.DR = DR
        self.XP = XP
        self.CXP = 0
        self.XPV = XPV
        self.is_special = is_special


    def __str__(self):
        if self.is_special:
            return f'Level {self.Level} {self.Species}\n {"*** Special ***"} \n HP: {"":>5}{self.CHP}/{self.MHP}\n ATK: {"":>4}{self.AR}\n DEF: {"":>4}{self.DR}\n XP: {"":>5}{self.CXP}/{self.XP}\n XP Val: {"":>1}{self.XPV}'
            #print(f'{"*** Special ***" : ^30} \n {self.CHP}/{self.MHP}')
        else:
            return f'Level {self.Level} {self.Species}\n HP: {"":>5}{self.CHP}/{self.MHP}\n ATK: {"":>4}{self.AR}\n DEF: {"":>4}{self.DR}\n XP: {"":>5}{self.CXP}/{self.XP}\n XP Val: {"":>1}{self.XPV}'


    def level_up(self):
        print(f'{self.Species} is leveling up!!!')
        self.Level += 1
        if self.Level <= 9 and self.Level >= 2:
            self.MHP += 7
            self.AR += 3
            self.DR += 3
            self.XPV += 25
            self.CHP = self.MHP
        else:
            self.MHP += 2
            self.AR += 1
            self.DR += 1
            self.XPV += 25
            self.CHP = self.MHP
        print(f'{self.Species} is now level: {self.Level}')



    def gain_xp(self, amount):
        print(f'{self.Species} gained xp\n XP amount: {amount}/{self.XP}')
 #recursive way of leveling up 

        if amount < (self.XP - self.CXP):
            self.CXP += amount 
            return self.CXP
        else:
            self.level_up()
            self.CXP += amount
            amount = abs(self.XP - self.CXP)
            if self.Level < 2:
                self.XP += 200
                self.CXP = 0
                return self.gain_xp(amount)
            else:
                self.XP += 75
                self.CXP = 0
                return self.gain_xp(amount)

    def take_damage(self, amount):
        print(f'{self.Species}  has taken damage.')
        if amount < self.CHP:
            print(f' Damage taken: {amount}')
            self.CHP = self.CHP - amount

        else:
            print(f' Damage taken: {self.CHP}')
            print(f'{self.Species} has been knocked out')
            self.CHP = 0



    def attack(self, target):
        #still need to call gain xp after the target gets knocked out
        print(f'{self.Species} is attacking {target.Species}!\n')

        atk_percentage = random.randint(1,10)
        print(atk_percentage)

        if target.CHP > 0:


            if atk_percentage <= 7:
                #regular hit
                if self.AR > target.DR:
                    #do damage for the diff of
                    print(f'Hit! {target.Species} took {self.AR - target.DR} damage!')
                    target.take_damage(self.AR - target.DR)
                    print(f'{target.Species} now has {target.CHP}/{target.MHP} HP\n')
                    if target.CHP == 0: 
                        self.gain_xp(target.XPV)
                else:
                    #do one damage
                    target.take_damage(1)
                    print(f'{target.Species} now has {target.CHP}/{target.MHP} HP\n')
                    if target.CHP == 0: 
                        self.gain_xp(target.XPV)

                    



            elif atk_percentage == 8:
                #critical hit 
                if self.AR > target.DR:
                    #do damage for the diff of 
                    print(f'Critical hit! {target.Species} took {(self.AR - target.DR)*2} damage!')
                    target.take_damage((self.AR - target.DR)*2)
                    print(f'{target.Species} now has {target.CHP}/{target.MHP} HP\n')
                    if target.CHP == 0: 
                        self.gain_xp(target.XPV)


                else:
                    target.take_damage(2)
                    print(f'{target.Species} now has {target.CHP}/{target.MHP} HP\n')
                    if target.CHP == 0: 
                        self.gain_xp(target.XPV)
                    


            else:
                #miss 
                print(f'{target.Species} missed!')
                print(f'{target.Species} now has {target.CHP}/{target.MHP} HP\n')
        else:
            print(f'Error!\n{target.Species} can no longer fight.\n')




#Tests

if __name__ == '__main__':

    haunter = CuteCreature('Haunter', 1, 100, 100, 21, 10, 200, 0, 300, True)
    Luxio = CuteCreature('Luxio', 1, 100, 100, 21, 10, 200, 0, 300, False)


    while True: 
        if haunter.CHP > 0 and Luxio.CHP > 0:
            haunter.attack(Luxio)
            Luxio.attack(haunter)
        else:
            print(haunter)
            print(Luxio)
            break


