class OrderForm(object):
    orders = 0
    def __init__(self, seat_type,
                 headlight_colour,
                 gps_option,
                 engine_type,
                 order_type=0,   # Default to an order_placed. Order_anticipated is 1.
                 opp="MTO",
                 customer=None):
        self.customer = customer   # This is set at different points in time depending on whether we're MTO, ATO or MTS.
        self.current_state = None  # This determines where in the process we are (goods receipts, quality assurance...)
        self.OPP = opp             # "MTO" or "ATO" or "MTS"

        self.order_number = OrderForm.orders
        OrderForm.orders += 1
        self.order_type = order_type

        # Details for the actual car construction.
        self.seat_type = seat_type         # range: 0 to 2 inclusive
        self.headlight_colour = headlight_colour  # range: 0 to 3 inclusive
        self.gps_option = gps_option       # range: 0 to 1 inclusive
        self.engine_type = engine_type       # range: 0 to 1 inclusive

    def __eq__(self, other):
        if type(other) != type(self):
            return False

        return self.seat_type == other.seat_type \
            and self.headlight_colour == other.headlight_colour \
            and self.engine_type == other.engine_type \
            and self.gps_option == other.gps_option

    def __lt__(self, other):
        if type(other) != type(self):
            raise ValueError("Can't compare order form to something with type " + type(other))

        if self.order_type != other.order_type:
            return self.order_type < other.order_type

        return self.order_number < other.order_number

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def sortable_tuple_representation(self):
        '''
        DEPRECIATED! Now that we have the magic methods for comparison implemented, we should be able to sort OrderForms
        without using their sortable tuple representations.
        :return:
        '''
        return ((self.order_type, self.order_number), self)

