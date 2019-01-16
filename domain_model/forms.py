class A(object):
    def __init__(self, product_code):
        self.product_code = product_code


class B(object):
    def __init__(self):
        order_number = None
        chassis_type = None
        product_code = None
        time_order_placed = None
        scheduled_lead_time = None
        scheduled_delivery_time = None
        contract_price = None
        actual_delivery_time = None
        time_difference = None

    @property
    def penalty_for_delay(self):
        return 30 * self.time_difference

    @property
    def revenue(self):
        return self.contract_price - self.penalty


class D(object):

    @staticmethod
    def calculate_contract_price(delivery_time, model):
        '''
        Gets the price our company charges to make a given model in a given amount of time.
        :param delivery_time: The time a customer requires the car delivered in
        :param model: the car being constructed
        :return: the cost, as an integer
        '''

        model_costs = {
            "FST270Y": 470,
            "FDR371Y": 490,
            "FDE461X": 510,
            "PST350Y": 480,
            "PDR251Y": 500,
            "PDE471X": 520,
            "SST370Y": 510,
            "SDR271Y": 520,
            "SDE461X": 550,
            "AST260Y": 530,
            "ADR260Y": 540,
            "ADE350X": 570,
            "C SSB0Y": 670,  # Added a space so indexing matches up
            "T SSB0Y": 700,  # Added a space so indexing matches up
        }

        delta_for_delivery_time = (delivery_time-1) * model_costs[model]

        return model_costs[model] - delta_for_delivery_time

class E(object):

    class Entry(object):

        def __init__(self,
                     order_number=None,
                     product_code=None,
                     time_recieved=None,
                     scheduled_lead_time=None):

            self.order_number = order_number
            self.product_code = product_code
            self.time_recieved = time_recieved
            self.scheduled_lead_time = scheduled_lead_time

        @property
        def scheduled_delivery_time(self):
            if self.time_recieved is None or self.scheduled_lead_time is None:
                class IncompleteEntryException(Exception):
                    pass
                raise IncompleteEntryException("Scheduled Delivery Time for an entry in Form E cannot be calculated.")
            return self.time_recieved + self.scheduled_lead_time

    def __init__(self):
        self.entries = []

    def add_entry(self,
                  *args):
        if len(args) is 0:
            raise Exception("Called add_entry on form E with zero arguments")

        elif len(args) is 1 and type(args[0]) is Entry:
            self.entries.append(args[0])

        else:
            self.entries.append(Entry(*args))


class F(object):

    standard_base = [100007, 100020, 100020, 100238, 100238, 100238, 100238]

    bill_of_materials = {  # TODO lists unfinished
        "FST27": [100007],
        "FDR37": [100007],
        "FDE46": [100007],
        "PST35": [100007, 100020, 100020, 100152, 100221, 100221, 100221, 100221, 100238, 100238, 100238, 100238, 100385, 100385, 100385, 100385, 100521, 100538, 100538, 100857, 100879, 100976, 300452, 300482, 300985],
        "PDR25": [300987, 300985, 300482, 300452, 100976, 100879, 100857, 100538, 100538, 100521, 100385, 100385, 100385, 100385, 100007, 100020, 100020, 100152, 100220, 100220, 100220, 100220, 100238, 100238, 100238, 100238],
        "PDE47": [300987, 300985, 300482, 300452, 100976, 100879, 100857, 100538, 100538, 100523, 100397, 100384, 100384, 100384, 100384, 100007, 100020, 100020, 100222, 100222, 100222, 100222, 100238, 100238, 100238, 100238],
        "SST37": [800343, 800343, 400914, 400332, 400241, 400048, 100976, 100879, 100879, 100857, 100538, 100538, 100523, 100385, 100385, 100385, 100385, 100238, 100238, 100238, 100238, 100221, 100221, 100221, 100221, 100007, 100020, 100020, 100152],
        "SDR27": [800343, 800343, 400914, 400332, 400241, 400048, 100976, 100879, 100879, 100857, 100538, 100538, 100523, 100385, 100385, 100385, 100385, 100238, 100238, 100238, 100238, 100220, 100220, 100220, 100220, 100007, 100020, 100020, 100152],
        "SDE46": [800342, 800342, 400914, 400332, 400241, 400048, 100976, 100879, 100879, 100857, 100538, 100538, 100522, 100397, 100384, 100384, 100384, 100384, 100238, 100238, 100238, 100238, 100222, 100222, 100222, 100222, 100007, 100020, 100020],
        "AST26": [100007],
        "ADR26": [100007],
        "ADE35": [100007],
        "C SSB": [],
        "T SSB": [],
    }

    def get_material_list(model):
        material_list = []

        # Set GPS option
        if model[-2] == "1":
            material_list.append(100937)

        # Set bumper option
        bumper_options = {
            "X": 100432,
            "Y": 100431,
            "S": 500431,
            "B": 500858,
        }
        material_list.append( bumper_options[model[-1]] )

        # Lookup the rest of the models against the bill of materials
        # (set as a class attribute to keep this method readable)
        material_list.append( bill_of_materialls[model[:-2]] )

        return material_list


    def __init__(self, product_code):
        self.materials_needed = F.get_material_list(product_code)
