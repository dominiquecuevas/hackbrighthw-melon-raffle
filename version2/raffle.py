"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

import random #removed 'import choice'

from customers import get_customers_from_file

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)

    print("Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        ))


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)

if __name__=="__main__": # make sure does run_raffle function so doesn't run from another file in same directory
    run_raffle()