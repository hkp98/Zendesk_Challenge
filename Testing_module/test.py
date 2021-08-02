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

def test_fetch_all_tickets(url: str = "", auth: str = ""):
    read_file = open('data_sample_tickets.json','r')
    data = json.load(read_file)
    read_file.close()
    test_object = ApiTest(read_file,200)
    return test_object

def test_bad_request_error(url: str = "", auth: str = ""):
    test_object = ApiTest(status_response=400)
    return test_object

def test_unauthorized_access_error(url: str = "", auth: str = ""):
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

    def test_api_fetch_single_ticket(self: object,test_get)-> None:
        api = ZenApi()
        ticket_raw = api.requestZenApi(False, 2) # Raw ticket withunformatted dates 
        self.assertEqual(len(ticket_raw),1)
        assert "ticket" in ticket_raw
        self.assertEqual(ticket_raw["ticket"]["id"],2)
        ticket = api.getTickets(2)
        self.assertEqual(len(ticket),1)
        assert "ticket" in ticket
        self.assertEqual(ticket["ticket"]["id"],2)
    
    @patch('model.API_connection.requests.get', side_effect=test_fetch_all_tickets)

    def test_api_fetch_all_tickets(self: object,test_get)-> None:
         api = ZenApi()
         ticket_raw = api.requestZenApi(True)
         self.assertEqual(len(ticket_raw["tickets"]),100)
         assert "tickets" in ticket_raw
         assert "next_page" in ticket_raw
         assert "previous_page" in ticket_raw
         assert "count" in ticket_raw
         ticket = api.getTickets() # processing with formatted dates
         self.assertEqual(len(ticket["tickets"]),100)
         assert "tickets" in ticket
         assert "next_page" in ticket
         assert "previous_page" in ticket
         assert "count" in ticket
    
     @patch('model.API_connection.requests.get', side_effect=test_bad_request_error)

     def test_bad_request(self: object,test_get):
         api = ZenApi()
         api = api.requestZenApi()
         self.assertEqual(api.requestZenApi(),0)
         

    





