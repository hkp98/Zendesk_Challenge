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

    def test_bad_request(self: object,test_get)-> None:
         api = ZenApi()
         api = api.requestZenApi()
         self.assertEqual(api.requestZenApi(),0)
         self.assertEqual(api.getTickets(), False)
         self.assertEqual(api.getTickets(1), False)
    
    @patch('model.API_connection.requests.get', side_effect=test_unauthorized_access_error)

    def test_unauthorized_access(self: object,test_get)-> None:
        api = ZenApi()
        self.assertEqual(api.requestZenApi(),None)
        self.assertEqual(api.getTickets(), 401)
        self.assertEqual(api.getTickets(1), 401)
    
    @patch('model.API_connection.requests.get', side_effect=test_api_unavailable_error)

    def test_api_unavailable(self: object,test_get)-> None:
        api = ZenApi()
        self.assertEqual(api.requestAPI(), 503)
        self.assertEqual(api.getTickets(), 503)
        self.assertEqual(api.getTickets(1),503)

class ViewTester(unittest.TestCase):

    def test_View(self: object)-> None:
        f1 = test_fetch_single_ticket()
        f2 = test_fetch_all_tickets()
        view = ApplicationView()
        self.assertEqual(view.printTicket(f1.json_data),0)
        self.assertEqual(view.printTickets(f2.json_data,1),1)
        self.assertEqual(view.mainMessage(),0)
        self.assertEqual(view.printMenu(),0)
        self.assertEqual(view.printTickets("all",0))
        self.assertEqual(view.quit(),0)
        
class PresenterTester(unittest.TestCase):

     @patch("builtins.input", return_value='q') # test user quitting correctly
     def test_user_quit(self: object,input)-> None:
         presenter =  AppPresenter()
         with self.assertRaises(SystemExit) as cm:
             presenter.displayMainMenu()
         self.assertEqual(cm.exception.code, 0)
    
     @patch("builtins.input", side_effect=['1', 'q', '1', 'd', 'q'])
     @patch('model.API_connection.requests.get', side_effect=test_fetch_all_tickets)

     def test_print_all(self: object,input,test_get)-> None:
         presenter = AppPresenter()
         with self.assertRaises(SystemExit) as cm:
            presenter.displayMainMenu()
         self.assertEqual(cm.exception.code, 0)
         with self.assertRaises(SystemExit) as cm:
            presenter.displayMainMenu()
         self.assertEqual(cm.exception.code, 0)
         self.assertEqual(presenter.currrent_page, 2)
    
     @patch("builtins.input", side_effect=['2', '3', '4'])
     @patch('model.API_connection.requests.get', side_effect=test_fetch_single_ticket)
     
     def test_print_one(self: object,input,test_get)-> None:
         presenter = AppPresenter()
         self.assertEqual(presenter.printTicket(), 0)
         self.assertEqual(presenter.current_id, 2)
         self.assertEqual(presenter.printTicket(), 0)
         self.assertEqual(presenter.current_id, 3)
         self.assertEqual(presenter.printTicket(), 0)
         self.assertEqual(presenter.current_id, 4)
     
     @patch("builtins.input", side_effect=['1999'])
     @patch('model.API_connection.requests.get', side_effect=test_invalid_ID_error)
     def test_invalid_ID(self: object,input,test_get):
         presenter = AppPresenter()
         self.assertEqual(presenter.printTicket(), False)

if __name__ == "__main__":
    unittest.main()



    





