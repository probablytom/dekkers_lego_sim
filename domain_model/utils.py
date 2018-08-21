def is_anticipated(order):
    '''
    Determines whether an order is an order_anticipated. Really just syntactic sugar.
    :param order: Order of the form ((order_type, order_number), order_object)
    :return: bool
    '''
    return order[0][0] == 1  # Anticipated orders are ((1, a), b). Placed orders are ((0, a), b).

def is_placed(order):
    '''
    Determines whether an order is an order_placed. Really just syntactic sugar.
    :param order: Order of the form ((order_type, order_number), order_object)
    :return: bool
    '''
    return order[0][0] == 0  # Anticipated orders are ((1, a), b). Placed orders are ((0, a), b).


class NoWorkAvailable(Exception):
    pass
