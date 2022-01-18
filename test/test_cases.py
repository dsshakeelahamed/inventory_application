import json
import os
import unittest

import utility.utility as utils
import create_table as ct
os.environ["environment"] = "test"
cfg = utils.get_environment_configs()
ct.create_table(cfg.inventory_table)

from rest.rest import app
import test.test_data as td


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.client = self.app.test_client()
        pass

    def tearDown(self) -> None:
        pass

    def test_a_insert_record_success(self):
        print("1")
        payload = td.insert_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_response_success)
        self.assertEqual(response.status_code, 200)

    def test_b_insert_record_fail(self):
        print("2")
        payload = td.insert_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_response_failure)
        self.assertEqual(response.status_code, 200)

    def test_c_insert_record_invalid_id(self):
        payload = td.insert_invalid_id_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_invalid_id_response)
        self.assertEqual(response.status_code, 400)

    def test_d_insert_record_invalid(self):
        payload = td.insert_invalid_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_e_get_success(self):
        print("3")
        payload = td.get_request_success
        response = self.client.get("/inventory", data=json.dumps(payload))
        status_code = response.status_code
        response = json.loads(response.data)
        try:
            response[0].pop("created")
            response[0].pop("updated")
        except:
            pass
        self.assertEqual(response, td.get_response_success)
        self.assertEqual(status_code, 200)

    def test_f_get_failure(self):
        print("4")
        payload = td.get_request_failure
        response = self.client.get("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.get_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_g_get_invalid(self):
        payload = td.get_invalid_request
        response = self.client.get("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.get_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_h_update_success(self):
        payload = td.put_request_success
        response = self.client.put("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.put_response_success)
        self.assertEqual(response.status_code, 200)

    def test_i_update_failure(self):
        payload = td.put_request_failure
        response = self.client.put("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.put_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_j_update_invalid(self):
        payload = td.put_invalid_request
        response = self.client.put("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.put_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_k_delete_success(self):
        payload = td.delete_request_success
        response = self.client.delete("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.delete_response_success)
        self.assertEqual(response.status_code, 200)

    def test_l_delete_failure(self):
        payload = td.delete_request_failure
        response = self.client.delete("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.delete_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_m_delete_invalid(self):
        payload = td.delete_invalid_request
        response = self.client.delete("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.delete_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_n_get_all_failure(self):
        print("11")
        response = self.client.get("/inventory/all")
        self.assertEqual(json.loads(response.data), td.get_all_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_o_restore_success(self):
        print("10")
        payload = td.restore_request_success
        response = self.client.put("/inventory/undo", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.restore_response_success)
        self.assertEqual(response.status_code, 200)

    def test_p_restore_failure(self):
        print("11")
        payload = td.restore_request_failure
        response = self.client.put("/inventory/undo", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.restore_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_q_restore_invalid(self):
        payload = td.restore_invalid_request
        response = self.client.put("/inventory/undo", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.restore_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_r_get_all_success(self):
        print("11")
        payload = td.get_all_request_success
        self.client.post("/inventory", data=json.dumps(payload))
        response = self.client.get("/inventory/all")
        status_code = response.status_code
        response = json.loads(response.data)
        self.assertEqual(2, len(response))
        self.assertEqual(status_code, 200)


