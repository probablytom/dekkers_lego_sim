class ProductionCompany(object):
    def __init__(self):
        self.SalesDep = Sales()
        self.LogisticsDep = Logistics()
        self.Manufactoring = Manufacturing()
        self.FinancialAdminDep = FinancialAdminDepartment()
        self.Management = Management()

    def recieveForm(self, form):
        '''
        TODO
        '''
        pass

    def processForm(self):
        '''
        TODO: should this be separate to 'recieve form'?
        :return: None
        '''
        pass

    def MTO(self):
        pass

    def JIT(self):
        pass

# === Departments
class Department(object):
    pass

class Sales(Department):
    pass

class Logistics(Department):
    pass

class Manufacturing(Department):
    pass

class FinancialAdminDepartment(Department):
    pass

class Management(Department):
    pass