# 9.10
from restaurant import Restaurant
from restaurant import IceCreamStand

if __name__ == '__main__':
    # 9.1 & 9.4
    my_restaurant = Restaurant('木桶饭', '炒菜')
    print(my_restaurant.restaurant_name)
    print(my_restaurant.cuisine_type)
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant_name()
    my_restaurant.increment_number_served()
    my_restaurant.increment_number_served()
    print(my_restaurant.number_served)

    # 9.6
    ice_cream_stand = IceCreamStand('美味冰淇淋', '零食')
    ice_cream_stand.add_flavors('绿豆味', '红豆味')
    ice_cream_stand.add_flavors('山楂味', '蜜桃味', '橙子味')
    ice_cream_stand.describe_restaurant()
    ice_cream_stand.show_flavors()
