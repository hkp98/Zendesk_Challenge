""" 
Performing tests for the Zendesk Ticket Viewer
Testing 3 modules: 
 1. Model ->  API_connection.py
 2. View -> view.py 
 3. Presenter -> presenter.py
 
"""

import unittest
from unittest.mock import patch
import json
import sys
from os.path import dirname,abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from view.view import  ApplicationView
from model.API_connection import ZenApi
from presenter.presenter import  AppPresenter

class ApiTest:
    def __init__(self: object,json_data: dict = "",status_response: str =""):
        self.json_data = json_data
        self.status_response = status_response
    
    def json(self):
        return self.json_data
    
def test_fetch_single_ticket(url: str = "", auth: str = ""):
    read_file = open('data_sample_ticket.json','r')
    data = json.load(read_file)
    read_file.close()
    test_object = ApiTest(read_file,200)
    return test_object

def test_fetch_single_ticket(url: str = "", auth: str = ""):
    read_file = open('data_sample_tickets.json','r')
    data = json.load(read_file)
    read_file.close()
    test_object = ApiTest(read_file,200)
    return test_object

def test_bad_request_error(url: str = "", auth: str = ""):
    test_object = ApiTest(status_response=401)
    return test_object

def test_api_unavailable_error(url: str = "", auth: str = ""):
    test_object = ApiTest(status_response=503)
    return test_object

def test_invalid_ID_error(url: str = "", auth: str = ""):
    test_object = ApiTest({'error': 'RecordNotFound', 'description': 'Not found'},status_response=404)
    return test_object

# Testing for module API_connection.py
class ModelTester(unittest.TestCase):

    @patch('model.API_connection.requests.get', side_effect=test_fetch_single_ticket)

    def test_fetch_single_ticket(self,test_get):
        api = ZenApi()
        


