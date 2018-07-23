# ===== Internal production elements

class ProductionPlanning(object):
    def __init__(self):
        self.goods_receipts = None

    def 

class GoodsReceipts(object):
    def __init__(self):
        self.supplier = None
        self.shop_floor_control = None

class Supplier(object):
    def __init__(self):
        self.goods_receipts = None

class ShopFloorControl(object):
    def __init__(self):
        self.storage = None
        self.production = None
        self.orders_db = None

class Production(object):
    def __init__(self):
        self.quality_assurance = None

class QualityAssurance(object):
    def __init__(self):
        self.storage = None
        self.production_planning = None
        self.delivery = None

class Storage(object):
    '''
    A class for storing things for the production company, such as parts or assembled units in the case of MTS
    '''
    def __init__(self):
        pass

# ===== Customer Interaction Elements

class Delivery(object):
    def __init__(self):
        self.customer = None

class Customer(object):
    def __init__(self):
        self.sales = None

class Sales(object):
    def __init__(self):
        self.production_planning = None
        self.orders_db = None

# ====== Ancillary classes

class OrdersDB(dict):
    '''
    A database to hold orders. This is basically just a dict, but I'm making it a class in case I need to add functionality later.
    '''
    def __init__(self, *args, **kwargs):
        super(OrdersDB, self).__init__(*args, **kwargs)
