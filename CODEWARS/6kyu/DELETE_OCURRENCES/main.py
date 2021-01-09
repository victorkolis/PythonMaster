def delete_nth(order, max_e):
    order.reverse()
    try:
        for index in range(len(order)):
            while order.count(order[index]) > max_e:
                order.remove(order[index])
    except IndexError:
        pass
    order.reverse()
    return order


print(delete_nth([39, 28, 28, 15, 20, 37, 39, 9, 15, 20, 37, 28, 39, 25, 25, 39, 9, 20, 28], 2))
