class Book:
	name = ''
	last_update = ''
	creation_date = ''
	recipes_list = {}
	def __init__(self, n, l, c, r):
		name = n
		last_update = r
		creation_date = l
		recipes_list = r
	def __str__(self):
		print("the recipe " + self.name + " was created at " + self.creation_date, end ='')
		print(" and was last edited at " + self.last_update + " and contains", end ='')
		print("the fllowing recipes ", end ='')
		for x in self.recipes_list:
			print(self.recipes_list[x])
	def get_recipe_by_name(self, name):
		for x in recipes_list:
			if x.name == name:
				print(name)
	def get_recipes_by_types(self, recipe_type):
		for x in recipes_list[recipe_type]:
			print(x.name, end ='')
	def add_recipe(self, recipe):
		if not (isinstance(recipe, Recipe)):
			print("this is not a recipe ! what is you doing ?!")
			quit()
		self.recipes_list[recipe.recipe_type].append(recipe)
