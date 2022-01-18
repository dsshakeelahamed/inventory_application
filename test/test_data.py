import random
id = random.randint(99999, 999999)
insert_request = {"id": id, "name": "inventory_test", "cost": 100, "location": "test_location"}
insert_response_success = {"message": "Successfully inserted inventory for id %s" % id}
insert_response_failure = {"message": "Record for id %s already exists" % id}

insert_invalid_id_request = {"id": "abc", "name": "inventory_test", "cost": 100, "location": "test_location"}
insert_invalid_id_response = {"message": "Invalid Inventory ID"}

insert_invalid_request = "invalid request"
insert_invalid_response = {"message": "Error while parsing data"}

get_request_success = {"id": id}
get_request_failure = {"id": random.randint(99999, 999999)}
get_response_success = [{'id': id, 'name': 'inventory_test', 'type': None, 'cost': 100, 'quantity': None, 'location': 'test_location'}]
get_response_failure = {'message': 'No records found for id %s' % get_request_failure["id"]}

get_invalid_request = "invalid request"
get_invalid_response = {"message": "Error while parsing data"}

put_request_success = {"id": id, "name": "inventory_test_update", "cost": 555, "location": "test_location_update"}
put_request_failure = {"id": random.randint(99999, 999999), "name": "inventory_test_update", "cost": 555, "location": "test_location_update"}
put_response_success = {"message": "Successfully updated inventory for id %s" % id}
put_response_failure = {"message": "No records found for id %s" % put_request_failure["id"]}

put_invalid_request = "invalid request"
put_invalid_response = {"message": "Error while parsing data"}

delete_request_success = {"id": id, "deletion_comments": "Inventory record deleted"}
delete_response_success = {"message": "Successfully deleted inventory for id %s" % id}
delete_request_failure = {"id": random.randint(99999, 999999), "deletion_comments": "Inventory record deleted"}
delete_response_failure = {"message": "No records found for id %s" % delete_request_failure["id"]}

delete_invalid_request = "invalid request"
delete_invalid_response = {"message": "Error while parsing data"}

# restore = {"id": 999}
restore_request_success = {"id": id}
restore_response_success = {"message": "Successfully restored inventory for id %s" % id}
restore_request_failure = {"id": random.randint(99999, 999999)}
restore_response_failure = {"message": "No records found for id %s" % restore_request_failure["id"]}

restore_invalid_request = "invalid request"
restore_invalid_response = {"message": "Error while parsing data"}

get_all_request_success = {"id": random.randint(99999, 999999), "name": "inventory_test", "cost": 100, "location": "test_location"}
get_all_response_failure = {"message": "No records found"}
