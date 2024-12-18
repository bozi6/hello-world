"""Az if használata egy sorban."""

#  egysorif.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 10. 07. 17:53

# Alapbaj
weather = "sunny"
if weather == "sunny":
    print("I should take a walk outside!")
elif weather == "cloudy":
    print("I'm not sure it will rain. Maybe I will take a walk?")
elif weather == "rainy":
    print("It is raining. I will stay at home.")
else:
    print("I don't know what the weather is...")

# Röviden a lényeg
# if <expression>: <perform_action></perform_action></expression>

weather = "sunny"
if weather == "sunny": print("I should take a walk outside!")

# többsoros
# if <expression>: <perform_action_01>; <perform_action_02>; <perform_action_03>

weather = "sunny"
if weather == "sunny": print("It's sunny."); print("I should take a walk outside!"); print("The sun is very warm.")

# if <expression_01>: <perform_action_01>
# elif <expression_02>: <perform_action_02>
# elif <expression_03>: <perform_action_03>
# else : <perform_another_action>
# </perform_action_03></perform_action_02></perform_action_01>

weather = "sunny"

if weather == "sunny":
    print("I should take a walk outside!")
elif weather == "cloudy":
    print("I'm not sure it will rain. Maybe I will take a walk?")
elif weather == "rainy":
    print("It is raining. I will stay at home.")
else:
    print("I don't know what the weather is...")

# value = <value_if_true> if <expression> else <value_if_false>

age = 8

if age < 5:
    is_baby = True
else:
    is_baby = False

print(is_baby)

age = 8
is_baby = True if age < 5 else False

print(is_baby)
