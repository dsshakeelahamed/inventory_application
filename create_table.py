import os
import sys

# if environment has not been set (this is set in test cases before create table is called), then pick from command line arguments
if not os.getenv("FLASK_ENV", ""):
    # default environment
    env = "dev"
    if len(sys.argv) > 1:
        if sys.argv[1].lower() in ["dev", "test"]:
            env = sys.argv[1].lower()
    os.environ["FLASK_ENV"] = env

from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, text, BOOLEAN, BIGINT
from dao.db_module import DatabaseModule
import utility.utility as utils


def create_table(table_name):
    try:
        print("Creating table %s " % table_name)
        dbm = DatabaseModule()
        Table(table_name, dbm.metadata, Column("id", BIGINT(), primary_key=True),
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
        print("Table %s created successfully" % table_name)
    except Exception as e:
        print("Error while creating Table %s" % table_name)
        print(e)


if __name__ == "__main__":
    cfg = utils.get_environment_configs()
    create_table(cfg.inventory_table)
