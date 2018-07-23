class OrderForm(object):
    def __init__(self):
        self.customer = None  # This is set at different points in time depending on whether we're MTO, ATO or MTS.
        self.current_state = None  # This determines where in the process we are (goods receipts, quality assurance...)

        # Details for the actual car construction. Just ints, zero-indexed, that indicate what kind of car we're looking for.
        self.seat_type = None         # range: 0 to 2 inclusive
        self.headlight_colour = None  # range: 0 to 3 inclusive
        self.gps_option = None        # range: 0 to 1 inclusive
        self.engine_type = None       # range: 0 to 1 inclusive
