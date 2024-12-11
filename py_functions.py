def greet_user(username):
    print(f"Hello {username.title()}!")

greet_user('jesse')

def describe_pet(pet_type, pet_name):
    """display info about a pet"""
    print(f"\nI have a {pet_type}.")
    print(f"My {pet_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'daphne')

def make_shirt(shirt_size="Large", shirt_message="I Love Python"):
    """order a shirt with a specific size and message"""
    print(f"The shirt you ordered was a size {shirt_size}, and the message you wanted printing on the shirt was, '{shirt_message}.")

make_shirt()
make_shirt('Medium')

make_shirt(shirt_size='X-Large', shirt_message='FEAR is the mind killer')

# returning simple values when functions are called

def get_formatted_name(first_name, last_name):
    """return a full name that is neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# making arguments optional
def get_formatted_name_v2(first_name, last_name, middle_name=''):
    """return a full name that is neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name_v2('jimi', 'hendrix')
print(musician)

musician = get_formatted_name_v2('john', 'hooker', 'lee')
print(musician)

# returning a dictonary
def build_person(first_name, last_name):
    """return a dict of info about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person_v2(first_name, last_name, age=None):
    """return a dict of info about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    
    return person

musician = build_person_v2('jimi', 'hendrix', age=27)
print(musician)

# functions and while loops
def get_formatted_name_v3(first_name, last_name):
    """return full name neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nplease tell me your name")
    print("(enter 'q' at anytime to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name_v3(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

    # passing a list to a function
def greet_users(names):
    """print a sample greeting to each user in a given list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
    
usernames = ['jan', 'bob', 'clive', 'ty', 'margot']
greet_users(usernames)

# modify a list in a function
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs, completed_models):
    """ simulate printing each design until none are left"""
    """ move each design to completed_models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ show all the models that were printed"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_designs[:], completed_models) # the [:] sends a copy of the list to the function to preseve the original list
show_completed_models(completed_models)
print(unprinted_designs)

# passing an arbitrary number of arguements to a function

def make_pizza(*toppings):
    """print the list of toppings that have been requested"""
    print("\nMaking a pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

# mixing positional and arbitrary arguements

def make_pizza2(size, *toppings):
    """summarise the pizza's we are about to make"""
    print(f"\nMaking a {size} - inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza2(16, 'pepperoni')
make_pizza2(12, 'mushroom', 'green peppers', 'extra cheese')

# using arbitrary keyword arguements

def build_profile(first, last, **user_info):
    """build a dict of everything we need to know about a user"""
    user_info['first_name'] = first
    user_info['lasr_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field = 'physics')

print(user_profile)



