

#importing CuteCreature 
from CuteCreature import CuteCreature

class EvolvableCuteCreature(CuteCreature):

	def __init__(self, Species, Level, MHP, CHP, AR, DR, XP, CXP ,XPV, is_special, EVL, EV, EVT):
		CuteCreature.__init__(self, Species, Level, MHP, CHP, AR, DR, XP, CXP ,XPV, is_special)

		self.EVL = EVL 
		self.EV = EV
		self.EVT = None
		# doesnt have type yet cuz it hasnt evolved




	def __str__(self):
		result = CuteCreature.__str__(self) + f'\n Type: {"":>3}{self.EVT}'

		return result

	def level_up(self):

		CuteCreature.level_up(self)

		if self.EVL == self.Level:
			print(f'{self.Species} is evolving')

			if self.Species[0] in ('ABCDEFabcdef'):
				self.EVT = 'Light' 
				print(f"{self.Species} is now {self.EVT} type")
			elif self.Species[0] in ('GHIJKLghijkl'):
				self.EVT = "Dark"
				print(f"{self.Species} is now {self.EVT} type")
			elif self.Species[0] in ('MNOPQRmnopqr'):
				self.EVT = "Nature"
				print(f"{self.Species} is now {self.EVT} type")
			elif self.Species[0] in ('STUVWXYZstuvwxyz'):
				self.EVT = "Tech"
				print(f"{self.Species} is now {self.EVT} type")


		# THIS IS WHERE THE EVOLUTION PROCESS IS DONE
	def special_attack(self, target):
		# checking to see if it is an evolved creature
		if self.EVT == None:
			print(f'{self.Species} has no special attack')

		#checking to make sure the target is still alive	
		elif target.CHP > 0:
			#start of special attack 


			#to check if the types are the same
			if target.EVT == self.EVT:
				print(f'{target.EVT} took no damage')


			#Light resistance and vulnerablities
			elif target.EVT == "Light":
				#resitant
				if self.EVT == "Tech":

					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - (target.DR*5))
						print(f'{target.Species} took {damage_taken}')
						

					else:
						damage_taken = target.take_damage(0)
						print(f'{target.Species} took {damage_taken}')
						

				#vulernable
				elif self.EVT == "Dark":

					if self.AR > target.DR:
						damage_taken = target.take_damage(5*(self.AR) - target.DR)
						print(f'{target.Species} took {damage_taken}')

					else:
						damage_taken = target.take_damage(10)
						print(f'{target.Species} took {damage_taken}')
						

				else:
					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - target.DR)
						print(f'{target.Species} took {damage_taken}')
						


					else:
						damage_taken = target.take_damage(1)
						




			#Dark resistance and vulnerablities
			elif target.EVT == "Dark":
				#resitant
				if self.EVT == "Nature":

					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - (target.DR*5))
						print(f'{target.Species} took {damage_taken}')
						

					else:
						damage_taken = target.take_damage(0)
						print(f'{target.Species} took {damage_taken}')
						

				#vulernable
				elif self.EVT == "Tech":

					if self.AR > target.DR:
						damage_taken = target.take_damage(5*(self.AR) - target.DR)
						print(f'{target.Species} took {damage_taken}')
						


					else:
						damage_taken = target.take_damage(10)
						print(f'{target.Species} took {damage_taken}')
						

				else:
					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - target.DR)
						print(f'{target.Species} took {damage_taken}')
						


					else:
						damage_taken = target.take_damage(1)
						

			#Nature resistance and vulnerablities
			elif target.EVT == "Nature":
				#resitant
				if self.EVT == "Dark":

					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - (target.DR*5))
						print(f'{target.Species} took {damage_taken}')
						

					else:
						damage_taken = target.take_damage(0)
						print(f'{target.Species} took {damage_taken}')
						

				#vulernable
				elif self.EVT == "Tech":

					if self.AR > target.DR:
						damage_taken = target.take_damage(5*(self.AR) - target.DR)
						print(f'{target.Species} took {damage_taken}')
						


					else:
						damage_taken = target.take_damage(10)
						print(f'{target.Species} took {damage_taken}')
						

				else:
					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - target.DR)
						print(f'{target.Species} took {damage_taken}')
						


					else:
						damage_taken = target.take_damage(1)
						

			#Nature resistance and vulnerablities
			elif target.EVT == "Tech":
				#resitant
				if self.EVT == "Light":
					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - (target.DR*5))
						print(f'{target.Species} took {damage_taken}')
						

					else:
						damage_taken = target.take_damage(0)
						print(f'{target.Species} took {damage_taken}')
						  

				#vulernable
				elif self.EVT == "Nature":

					if self.AR > target.DR:
						damage_taken = target.take_damage(5*(self.AR) - target.DR)
						print(f'{target.Species} took {damage_taken}')
						


					else:
						damage_taken = target.take_damage(10)
						print(f'{target.Species} took {damage_taken}')
						

				else:
					if self.AR > target.DR:
						damage_taken = target.take_damage(self.AR - target.DR)
						print(f'{target.Species} took {damage_taken}')
						


					else:
						damage_taken = target.take_damage(1)
						




		else:
			print(f'Error!\n{target.Species} can no longer fight.\n')
			


			


haunter = EvolvableCuteCreature('Haunter', 1, 100, 100, 15, 25, 200, 0, 300, True, 2, 0, 0)
Luxio = EvolvableCuteCreature('Nuxio', 1, 100, 100, 15, 25, 200, 0, 300, True, 2, 0, 0)

#print(haunter)
#haunter.special_attack(haunter)
#haunter.gain_xp(300)
#haunter.level_up()
#print(haunter)
#haunter.special_attack(haunter)
haunter.EVL == haunter.Level
haunter.level_up()
print(haunter)

Luxio.EVL == Luxio.Level
Luxio.level_up()
print(Luxio)


print(haunter.special_attack(Luxio))
print(Luxio.special_attack(haunter))

print(haunter)
print(Luxio)








