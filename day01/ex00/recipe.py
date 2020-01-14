class Recipe:
	name = ''
	cooking_lvl = 0
	cooking_time = 0
	ingredients= []
	description = ''
	recipe_type = ''
	def __init__(self, n, cl, ct, ing, des, r):
		name = n
		if name == '':
			print("Recipe name can't be empty")
			quit()
		cooking_lvl = cl
		if cooking_lvl < 1 and cooking_lvl > 5:
			print("Invalid cooking level")
			quit()
		cooking_time = ct
		if cooking_time < 0 :
			print("Invalid cooking minutes")
			quit()
		ingredients = ing
		for i in ingredients:
			if not (isinstance(i, str)):
				print("Element in list not valid")
				quit()
		description = des
		recipe_type = r
		if r != 'starter' and r != 'lunch' and r != 'dessert':
			print("Wrong type ")
			quit()
	
	def __str__(self):
		print("the recipe name is " + self.name + " its cooking level is ", end ='')
		print(self.cooking_lvl + "it takes " + self.cooking_time + " to cook", end ='')
		print("its ingredients are :", end ='')
		for i in ingredients:
			print(i + " ", end ='')
		print("and the recipe is for " + self.recipe_type)
