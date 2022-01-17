import datetime


class Inventory:
    """
    A class to represent Inventory, any new inventory field in database must be added here
    """
    def __init__(self, **kwargs):
        self.id = kwargs.get("id", None)
        self.name = kwargs.get("name", None)
        self.type = kwargs.get("type", None)
        self.cost = kwargs.get("cost", None)
        self.quantity = kwargs.get("quantity", None)
        self.location = kwargs.get("location", None)
        self.is_deleted = 0
        self.created = datetime.datetime.now()
        self.updated = datetime.datetime.now()