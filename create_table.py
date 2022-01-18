from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, text, BOOLEAN
from config import config as cfg
from dao.db_module import DatabaseModule


def create_table():
    try:
        print("Creating table %s " % cfg.inventory_table)
        dbm = DatabaseModule()
        Table(cfg.inventory_table, dbm.metadata, Column("id", Integer(), primary_key=True),
                                            Column("name", String(255)),
                                            Column("type", String(255)),
                                            Column("cost", Integer()),
                                            Column("quantity", Integer()),
                                            Column("location", String(255)),
                                            Column("is_deleted", BOOLEAN()),
                                            Column("created", TIMESTAMP(), server_default=text('CURRENT_TIMESTAMP')),
                                            Column("updated", TIMESTAMP(), server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
                                            Column("deletion_comments", String(255)))
        dbm.metadata.create_all(dbm.engine)
        print("Table %s created successfully" % cfg.inventory_table)
    except Exception as e:
        print("Error while creating Table %s" % cfg.inventory_table)
        print(e)


if __name__ == "__main__":
    create_table()
