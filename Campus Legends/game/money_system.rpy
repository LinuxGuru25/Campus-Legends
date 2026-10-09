default mc_money = 100



init python:

    class MoneyAPI:

        def add(self, amount):
            store.mc_money += amount
            return amount

        def spend(self, amount):
            if store.mc_money >= amount:
                store.mc_money -= amount
                return True
            return False

        def can_afford(self, amount):
            return store.mc_money >= amount

    money_api = MoneyAPI()

