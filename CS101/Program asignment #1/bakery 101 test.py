#Nathan Gregorian Bailey
#Section 0003
#Program 1
#Created on September 6th 2021
#Due September 9th 2021
print('Welcome to 101 Bakery\n')
pizzaDough = int(input('How much pizza dough do you plan to make today?\n'))
breadDough = int(input('\nHow much bread dough do you plan to make today?\n'))
cookiesDozen = int(input('\nHow many dozen(s) of cookies do you plan to make today?\n'))
if pizzaDough > 0:
	pizzaFlour = pizzaDough * 2
	pizzaYeast = pizzaDough
	pizzaSugar = pizzaDough * (3/2)
	pizzaSalt = pizzaDough * (3/4)
	pizzaOil = pizzaDough * (1/4)
else:
	pizzaFlour = 0
	pizzaYeast = 0
	pizzaSugar = 0
	pizzaSalt = 0
	pizzaOil = 0
if breadDough > 0:
	breadFlour = breadDough * 6
	breadYeast = breadDough * (3/2)
	breadSugar = breadDough * (1/2)
	breadSalt = breadDough * (3/2)
	breadOil = breadDough * (1/4)
else:
	breadFlour = 0
	breadYeast = 0
	breadSugar = 0
	breadSalt = 0
	breadOil = 0
if cookiesDozen > 0:
	cookiesFlour = cookiesDozen * 8
	cookiesSugar = cookiesDozen * 2
	cookiesButter = cookiesDozen * (5/2)
	cookiesEggs = cookiesDozen * 2
else:
	cookiesFlour = 0
	cookiesSugar = 0
	cookiesButter = 0
	cookiesEggs = 0
flourNeeded = float(pizzaFlour + breadFlour + cookiesFlour)
yeastNeeded = float(pizzaYeast + breadYeast)
sugarNeeded = float(pizzaSugar + breadSugar + cookiesSugar)
saltNeeded = float(pizzaSalt + breadSalt)
oilNeeded = float(pizzaOil + breadOil)
butterNeeded = float(cookiesButter)
eggsNeeded = int(cookiesEggs)
print()
print()
print()
print('\nYou will need to order\n')
print(flourNeeded,'cups of flour\n')
print(yeastNeeded,'packets of yeast\n')
print(sugarNeeded,'cups of sugar\n')
print(saltNeeded,'spoons of salt\n')
print(oilNeeded,'cups of oil\n')
print(butterNeeded,'cups of butter\n')
print(eggsNeeded,'eggs\n')
