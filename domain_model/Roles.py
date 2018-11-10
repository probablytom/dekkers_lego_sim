import theatre_ag as theatre

from Queue import PriorityQueue
from functools import partial

from utils import *


# ===== Superclasses
class SimulationAgent(theatre.Actor):
    def __init__(self, *args, **kwargs):
        super(SimulationAgent, self).__init__(*args, **kwargs)
        self.inbox = PriorityQueue()  # This effectively works as our work queue.

    def act_on(self, message):
        '''
        To be implemented by an actor in the simulation.
        :param message: Any object which represents work passed to this actor by another.
        :return: A function representing a workflow which processes the work indicated by the message passed.
        '''
        return partial(self.work_on, message)

    def get_next_task(self):
        '''
        Overriding theatre.Actor.get_next_task. This gets the next task for our actor.
        :return: A function representing a workflow step.
        '''

        # Idle if there's nothing to do
        if self.inbox.empty():
            return self.idling.idle

        return self.act_on(self.inbox.get())

    def work_on(self, order):
        '''
        To be implemented by a subclass. Generate the work that a given part of the process does for an order.
        :param order: An OrderForm representing work to be done.
        :return: Nothing, this is a workflow step.
        '''
        raise NotImplemented()


class StoringAgent(object):
    def __init__(self):
        self.storage = None

    @theatre.default_cost(1)
    def store_work(self, message):
        '''
        Sends work to storage.
        :param message: An OrderForm representing work to be put into storage.
        :return: Nothing, this is a workflow step.
        '''
        self.storage.store(message)

    @theatre.default_cost(1)
    def retrieve_possible_work(self, message):
        try:
            return self.storage.retrieve_matching_work(message, self)
        except NoWorkAvailable:
            return None



# ===== Internal production elements
class ProductionPlanning(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(ProductionPlanning, self).__init__(*args, **kwargs)
        self.goods_receipts = None


class GoodsReceipts(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(GoodsReceipts, self).__init__(*args, **kwargs)
        self.supplier = None
        self.shop_floor_control = None


class Supplier(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(Supplier, self).__init__(*args, **kwargs)
        self.goods_receipts = None


class ShopFloorControl(SimulationAgent, StoringAgent):
    def __init__(self, *args, **kwargs):
        super(ShopFloorControl, self).__init__(*args, **kwargs)
        self.production = None
        self.orders_db = None

    def act_on(self, message):
        '''
        Chooses what to do next.
        :param message: An OrderForm
        :return:
        '''
        # If our message is an ATO and is order_anticipated, SFC must *pause here*, putting work into Storage.
        # Remember: messages take the form ((order_type, order_number), order_object).
        # We *ALWAYS* process placed orders, even under different OPPs.
        if is_anticipated(message) and message.OPP == "ATO":
            return partial(self.store_work, message)
        else:

        return super(ShopFloorControl, self).act_on(message)


class Production(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(Production, self).__init__(*args, **kwargs)
        self.quality_assurance = None


class QualityAssurance(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(QualityAssurance, self).__init__(*args, **kwargs)
        self.storage = None
        self.production_planning = None
        self.delivery = None


class Storage(SimulationAgent):
    '''
    A class for storing things for the production company, such as parts or assembled units in the case of MTS
    '''
    def __init__(self, *args, **kwargs):
        super(Storage, self).__init__(*args, **kwargs)
        self.work_stored = {}

    @theatre.default_cost(1)
    def store(self, work, agent):
        if agent not in self.work_stored.keys():
            self.work_stored[agent] = []

        self.work_stored[agent].append(work)

    def charge_for_storage(self):
        '''
        TODO: A method which calculates invoices for organisations.
        :return:
        '''
        pass

    @theatre.default_cost(1)
    def retrieve_matching_work(self, order_placed, agent):
        '''
        Get work which matches a placed order from stored orders.
        Raises a NoWorkAvailable exception if the work can't be found in storage.
        TODO: Should this raise `NoWorkAvailable` or return `None`?
        :param order_placed: An Order object
        :param agent: The agent who is looking for stored work (usually `self` for the caller)
        :return: the other if found, or raises NoWorkAvailable otherwise.
        '''

        if order_placed not in self.work_stored[agent]:
            raise NoWorkAvailable

        self.work_stored[agent].remove(order_placed)
        return order_placed


# ===== Customer Interaction Elements

class Delivery(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(Delivery, self).__init__(*args, **kwargs)
        self.customer = None


class Customer(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(Customer, self).__init__(*args, **kwargs)
        self.sales = None


class Sales(SimulationAgent):
    def __init__(self, *args, **kwargs):
        super(Sales, self).__init__(*args, **kwargs)
        self.production_planning = None
        self.orders_db = None

# ====== Ancillary classes


class OrdersDB(dict):
    '''
    A database to hold orders. This is basically just a dict, but I'm making it a class in case I need to add functionality later.
    '''
    def __init__(self, *args, **kwargs):
        super(OrdersDB, self).__init__(*args, **kwargs)
