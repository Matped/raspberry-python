from Firebase import *


def increment_user():
    user_amount = db.reference('/Items/TheBar/Users').get() + 1
    ref.update({'Users': user_amount})

def decrement_user():
    user_amount = db.reference('/Items/TheBar/Users').get() - 1
    ref.update({'Users': user_amount})

