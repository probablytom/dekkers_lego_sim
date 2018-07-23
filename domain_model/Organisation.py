from domain_model.Roles import *


class Organisation(object):
    def __init__(self):
        # Set up the organisation's constituent parts
        self.customer = Customer()
        self.sales = Sales()
        self.production_planning = ProductionPlanning()
        self.goods_receipts = GoodsReceipts()
        self.supplier = Supplier()
        self.shop_floor_control = ShopFloorControl()
        self.production = Production()
        self.quality_assurance = QualityAssurance()
        self.delivery = Delivery()
        self.storage = Storage()

        self.orders_db = OrdersDB()

        # Make sure everything's aware of what it needs to be
        self.customer.sales = self.sales

        self.sales.orders_db = self.orders_db
        self.sales.production_planning = self.production_planning

        self.production_planning.goods_receipts = self.goods_receipts

        self.goods_receipts.shop_floor_control = self.shop_floor_control
        self.goods_receipts.supplier = self.supplier

        self.supplier.goods_receipts = self.goods_receipts

        self.shop_floor_control.production = self.production
        self.shop_floor_control.orders_db = self.orders_db
        self.shop_floor_control.storage = self.storage

        self.production.quality_assurance = self.quality_assurance

        self.quality_assurance.storage = self.storage
        self.quality_assurance.production_planning = self.production_planning
        self.quality_assurance.delivery = self.delivery

        self.delivery.customer = self.customer
