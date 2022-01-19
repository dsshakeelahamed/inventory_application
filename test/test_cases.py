import json
import os
import unittest

import utility.utility as utils
import create_table as ct

# Setting environment to test and creating test table
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
        """
        Test case to verify successful record insertion
        :return:
        """
        payload = td.insert_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_response_success)
        self.assertEqual(response.status_code, 200)

    def test_b_insert_record_fail(self):
        """
        Test case to verify record insertion failure when record already exists
        :return:
        """
        payload = td.insert_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_response_failure)
        self.assertEqual(response.status_code, 200)

    def test_c_insert_record_invalid_id(self):
        """
        Test case to verify when input contains invalid inventory id
        :return:
        """
        payload = td.insert_invalid_id_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_invalid_id_response)
        self.assertEqual(response.status_code, 400)

    def test_d_insert_record_invalid(self):
        """
        Test case to verify when invalid input is provided
        :return:
        """
        payload = td.insert_invalid_request
        response = self.client.post("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.insert_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_e_get_success(self):
        """
        Test case to verify successful record retrieval
        :return:
        """
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
        """
        Test case when record to retrieve does not exist
        :return:
        """
        payload = td.get_request_failure
        response = self.client.get("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.get_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_g_get_invalid(self):
        """
        Test case to verify when invalid input is provided
        :return:
        """
        payload = td.get_invalid_request
        response = self.client.get("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.get_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_h_update_success(self):
        """
        Test case to verify successful inventory update
        :return:
        """
        payload = td.put_request_success
        response = self.client.put("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.put_response_success)
        self.assertEqual(response.status_code, 200)

    def test_i_update_failure(self):
        """
        Test case to verify inventory update failure when record does not exist
        :return:
        """
        payload = td.put_request_failure
        response = self.client.put("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.put_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_j_update_invalid(self):
        """
        Test case to verify when invalid input is provided
        :return:
        """
        payload = td.put_invalid_request
        response = self.client.put("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.put_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_k_delete_success(self):
        """
        Test case to verify successful inventory deletion
        :return:
        """
        payload = td.delete_request_success
        response = self.client.delete("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.delete_response_success)
        self.assertEqual(response.status_code, 200)

    def test_l_delete_failure(self):
        """
        Test case to verify inventory deletion failure when record does not exist
        :return:
        """
        payload = td.delete_request_failure
        response = self.client.delete("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.delete_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_m_delete_invalid(self):
        """
        Test case to verify when invalid input is provided
        :return:
        """
        payload = td.delete_invalid_request
        response = self.client.delete("/inventory", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.delete_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_n_get_all_failure(self):
        """
        Test case to verify inventory retrieval failure when record does not exist
        :return:
        """
        response = self.client.get("/inventory/all")
        self.assertEqual(json.loads(response.data), td.get_all_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_o_restore_success(self):
        """
        Test case to verify successful inventory restoration
        :return:
        """
        payload = td.restore_request_success
        response = self.client.put("/inventory/undo", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.restore_response_success)
        self.assertEqual(response.status_code, 200)

    def test_p_restore_failure(self):
        """
        Test case to verify inventory restoration failure when record does not exist
        :return:
        """
        payload = td.restore_request_failure
        response = self.client.put("/inventory/undo", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.restore_response_failure)
        self.assertEqual(response.status_code, 404)

    def test_q_restore_invalid(self):
        """
        Test case to verify when invalid input is provided
        :return:
        """
        payload = td.restore_invalid_request
        response = self.client.put("/inventory/undo", data=json.dumps(payload))
        self.assertEqual(json.loads(response.data), td.restore_invalid_response)
        self.assertEqual(response.status_code, 400)

    def test_r_get_all_success(self):
        """
        Test case to verify successful all records retrieval
        :return:
        """
        payload = td.get_all_request_success
        self.client.post("/inventory", data=json.dumps(payload))
        response = self.client.get("/inventory/all")
        status_code = response.status_code
        response = json.loads(response.data)
        self.assertEqual(2, len(response))
        self.assertEqual(status_code, 200)


