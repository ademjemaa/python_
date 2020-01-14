dictionary = {
    'sandwich': {
        'ingredients': [
            'ham',
            'bread',
            'cheese',
            'tomatoes'],
        'meal': 'lunch',
        'prep_time': '10'},
    'cake': {
        'ingredients': [
            'flour',
            'sugar',
            'eggs'],
        'meal': 'dessert',
        'prep_time': '60'},
    'salad': {
        'ingredients': [
            'avocado',
            'argula',
            'tomatoes',
            'spinach'],
        'meal': 'lunch',
        'prep_time': '15'}}


def book_print():
    if dictionary:
        for i in dictionary:
            cookbook(i)
            print()
    else:
        print("Cookbook is empty")


def recipe_sayab(name, ings, meal, prep):
    dicto = {}
    dicto['ingredients'] = ings
    dicto['meal'] = meal
    dicto['prep_time'] = prep
    dictionary[name] = dicto


def add_recipe(var):
    text = ''
    t = []
    while text != 'done':
        text = input("Enter ingredients, if done write 'done'\n")
        if text != 'done':
            t.append(text)
    text = input("Enter meal type\n")
    prep = input("Enter preparation time\n")
    recipe_sayab(var, t, text, prep)


def delete_recipe(var):
    for i in dictionary:
        if i == var:
            del dictionary[var]
            return
    print("Meal does not exist")


def cookbook(meal):
    for i in dictionary:
        if i == meal:
            print("Recipe for " + meal)
            for x in dictionary.get(i):
                if x == 'ingredients':
                    print("Ingredients list: ", end='')
                    print(dictionary.get(i).get(x))
                if x == 'meal':
                    print("To be eaten for ", end='')
                    print(dictionary.get(i).get(x), end='.\n')
                if x == 'prep_time':
                    print("Takes ", end='')
                    print(dictionary.get(i).get(x), end=' ')
                    print("minutes of cooking.")


var = ''
while var != '5':
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    var = input("5: Quit\n")
    if var == '1':
        var = input("Enter recipe name\n")
        add_recipe(var)
    elif var == '2':
        var = input("Enter recipe name\n")
        delete_recipe(var)
    elif var == '3':
        var = input("Please enter the recipe's name to get its details:\n")
        cookbook(var)
    elif var == '4':
        book_print()
    elif var != '5':
        print("This option does not exist,", end='')
        print("please type the corresponding number")
        print("To exit, enter 5")
print("Cookbook closed")
