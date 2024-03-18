class InterestBearingItem:
    pass

class Asset:
    pass

class InsurableItem:
    pass



class RealEstate(Asset, InsurableItem):
    pass



class Security(InterestBearingItem, Asset):
    pass

class Stock(Security):
    pass

class Bond(Security):
    pass



class BankAccount(InterestBearingItem, Asset, InsurableItem):
    pass

class SavingAccount(BankAccount):
    pass

class CheckingAccount(BankAccount):
    pass

