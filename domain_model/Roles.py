from .Player import CompanyPlayer, ExternalPlayer

class FinancialAdminPlayer(CompanyPlayer):
    pass

class GoodsReciever(CompanyPlayer):
    pass

class Manager(CompanyPlayer):
    pass

class ProductionPlayer(CompanyPlayer):
    pass

class ProductionPlanner(CompanyPlayer):
    pass

class QualityAssurancePlayer(CompanyPlayer):
    pass

class SalesPlayer(CompanyPlayer):
    pass

class ShopFloorControl(CompanyPlayer):
    pass

class EmploymentAgencyPlayer(ExternalPlayer):
    pass

class Supplier(ExternalPlayer):
    pass

class YSWYGPlayer(ExternalPlayer):
    pass

class Customer(ExternalPlayer):  # TODO: is this external?
    pass
