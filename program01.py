#this is an example file
import random
def random_number():
    number_gen = random.randint(1,20)
    print(f"You have ${number_gen}")

random_number()

def random_food():
    food_list = ["an apple", "pie", "soup", "a danish"]
    random_index = random.randint(0,3)
    list_selection = food_list[random_index]
    print(f"I'm in the mood for {list_selection}")

random_food()