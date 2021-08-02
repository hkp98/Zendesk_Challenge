import sys
from os.path import dirname,abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))

from view.view import  ApplicationView
from model.API_connection import ZenApi

class AppPresenter:
    def __init__(self):
        self.view = ApplicationView() # the main view
        self.api = ZenApi() # api connection and data processing
        self.input = "" # Inputs from user
        self.current_id = -1 # random initialization
        self.currrent_page = 999  # random initialization

    def run(self): # driver function to run the application
        self.diplayMainMenu()
    
    def getInput(self): # Get user Input 
        self.input = input()
    
    def displayMainMenu(self): # Main menu for user to interact with the application
        self.view.mainMessage()
        while True:
            self.getInput()
            if self.input == "menu":
                self.view.printMenu()
            elif self.input == '1':
                user_input = self.printTickets()
                if user_input is None:
                    self.view.displayInputMessage("\nEnter a command, to print menu, type 'menu': ",0)
            elif self.input == '2':
                user_input = self.printTicket()
                if user_input is False:
                    self.view.displayInputMessage("\nEnter a command, to print menu, type 'menu': ",0)
            elif self.input == 'q':
                sys.exit(self.view.quit())
            else:
                self.view.displayInputMessage("Invalid Input,please enter a valid option. To view the options type 'menu': ",1)
            self.input = "" 
    
    def printTickets(self):
        try:
            self.view.fetchTickets("all")
            tickets = self.api.getTickets()
            assert tickets not in [0,-1,401,403,404,503]
            page = self.view.printTickets(tickets,1)
        except AssertionError as e:
            self.view.errorCode = self.api.errorCode
            if tickets == -1: # no tickets on account
                self.view.displayErrors("There are 0 tickets on account to display")
            elif 