from sqlalchemy import create_engine, MetaData, Table, and_
from inventory_application.config import config as cfg


class DatabaseModule:
    """
    Module which connects to database and executes queries
    """
    def __init__(self):
        """
        Initialize database engine
        """
        try:
            engine = create_engine(
                "mysql://%s:%s@%s:%s/%s" % (cfg.mysql_user, cfg.mysql_password, cfg.mysql_host, cfg.mysql_port, cfg.database))
            self.connection = engine.connect()
            metadata = MetaData()
            self.inventory_table = Table(cfg.inventory_table, metadata, autoload=True, autoload_with=engine)

        except Exception as e:
            print(e.args)
            raise Exception("Could not connect to mysql")

    def __execute(self, query):
        """
        Execute a given query
        :param query: query to be executed
        :return: query response
        """
        return self.connection.execute(query)

    def insert(self, **data):
        """
        To build insert query for inventory
        :param data: dictionary of inventory object
        :return: query response
        """
        query = self.inventory_table.insert().values(data).prefix_with("IGNORE")
        return self.__execute(query)

    def get(self, **data):
        """
        To build get query for a particular inventory
        :param data: dictionary of inventory object
        :return: query response
        """
        query = self.inventory_table.select().where(and_(self.inventory_table.columns.id == data.get("id"), self.inventory_table.columns.is_deleted == 0))
        return self.__execute(query)

    def get_all(self):
        """
        To build get query for all inventory
        :param data: dictionary of inventory object
        :return: query response
        """
        query = self.inventory_table.select().where(and_(self.inventory_table.columns.is_deleted == 0))
        return self.__execute(query)

    def update(self, **data):
        """
        To build update query for a particular inventory
        :param data: dictionary of inventory object
        :return: query response
        """
        query = self.inventory_table.update().values(data)
        query = query.where(and_(self.inventory_table.columns.id == data.get("id"), self.inventory_table.columns.is_deleted == 0))
        return self.__execute(query)

    def delete(self, **data):
        """
        To build delete query for a particular inventory where is_deleted is set to 1 to mark it delete (soft delete)
        :param data: dictionary of inventory object
        :return: query response
        """
        query = self.inventory_table.update().values(is_deleted=1, deletion_comments = data.get("deletion_comments", ""))
        query = query.where(self.inventory_table.columns.id == data.get("id"))
        return self.__execute(query)

    def reverse_delete(self, id):
        """
        To build reverse delete query for a particular inventory where is_deleted is set to 0 to mark it delete (soft delete)
        :param data: dictionary of inventory object
        :return: query response
        """
        query = self.inventory_table.update().values(is_deleted=0)
        query = query.where(self.inventory_table.columns.id == id)
        return self.__execute(query)


