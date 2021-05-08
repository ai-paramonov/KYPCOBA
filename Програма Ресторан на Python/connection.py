import datetime

from pymongo import *

client = MongoClient('localhost', 27017)

db = client['restaurant_program']


def get_dishes():
    dishes = db['dishes'].find()
    return [i for i in dishes]


def get_users():
    users = db['users'].find()
    return [i for i in users]


def get_orders():
    orders = db['orders'].find()
    return [i for i in orders]


def get_reserves():
    reserves = db['reserves'].find()
    return [i for i in reserves]


def insert_user(user):
    db['users'].insert_one(user)


def insert_dish(dish):
    db['dishes'].insert_one(dish)


def insert_reserve(reserve):
    db['reserves'].insert_one(reserve)


def get_order_by_username(username):
    for user in get_users():
        if user.get('username') == username:
            return get_order_by_user(user)


def get_user_by_id(user_id):
    return db['users'].find_one({'_id': user_id})


def get_order_by_user(user):
    return db['orders'].find_one({'user_id': user.get('_id')})


def confirm_order(user_id, table):
    db['orders'].update_one({'user_id': user_id},
                            {'$set': {'status': "confirmed", 'table': table, 'date': datetime.datetime.now().today()}})


def set_order_status(user_id, status):
    db['orders'].update_one({'user_id': user_id}, {'$set': {'status': status}})


def paid_order(user_id):
    db['orders'].update_one({'user_id': user_id}, {'$set': {'user_id': -1,'status':'paid'}})


def delete_dish_from_cart(user, dish_name):
    if db['orders'].find_one({'user_id': user.get('_id')}) is not None:
        dishes = db['orders'].find_one({'user_id': user.get('_id')}).get('dishes')
        for dish in dishes:
            if dish.get('name') == dish_name:
                dishes.remove(dish)
                break
        db['orders'].update_one({'user_id': user.get('_id')}, {'$set': {'user_id': user.get('_id'), 'dishes': dishes}})


def delete_reserve_by_user_id(user_id):
    db['reserves'].delete_one({'user_id': user_id})


def insert_dish_in_cart(user, dish):
    if db['orders'].find_one({'user_id': user.get('_id')}) is None:
        db['orders'].insert_one({'user_id': user.get('_id'), 'dishes': [dish]})
    else:
        dishes = db['orders'].find_one({'user_id': user.get('_id')}).get("dishes")
        dishes.append(dish)
        db['orders'].update_one({'user_id': user.get('_id')}, {'$set': {'user_id': user.get('_id'), 'dishes': dishes}})
