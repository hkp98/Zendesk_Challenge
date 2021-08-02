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
    
    def printTickets(self): # function to print all tickets and handle its requests
        try:
            self.view.fetchTickets("all")
            tickets = self.api.getTickets()
            assert tickets not in [0,-1,401,403,404,503]
            page = self.view.printTickets(tickets,1)
        except AssertionError as e:
            self.view.errorCode = self.api.errorCode
            if tickets == -1: # no tickets on account
                self.view.displayErrors("There are 0 tickets on account to display")
            elif tickets == 401 or tickets == 403:
                self.view.displayErrors("API authentication failed or invalid user credentials")
            elif tickets == 404:
                self.view.displayErrors("Invalid ID requsted, please request a valid ID or domain unavailable")
            elif tickets == 503:
                self.view.displayErrors("API unavailable. Please try again later")
            elif tickets == 0:
                self.view.displayErrors("Bad Request "+ self.api.errorCode)
            self.view.errorCode = None
            self.api.errorCode = None
            return None
        
        while True:
            self.getInput()
            if self.input == 'q':
               sys.exit(self.view.quit())
            elif self.input == "menu":
                self.view.printMenu()
                break
            elif self.input == "d":
                page = page + 1
                page = self.view.printTickets(tickets,page)
            elif self.input == "u":
                page = page - 1
                page = page = self.view.printTickets(tickets,page)
            else:
                self.view.displayInputMessage(
                    "Page command error. 'd' go to next page, 'u' to previous page, 'menu' for menu or 'q' to quit the application",1)
            self.input = ""
            self.currrent_page =page
        return 0
    
    def printTicket(self): # function to print ticket with ID provided
        self.view.displayInputMessage("Enter the ticket ID: ",0)
        self.getInput()
        ticketID = self.input()
        self.input = ""
        try:
            self.view.fetchTickets(ticketID)
            ticket = self.api.getTickets(ticketID)
            assert ticket not in [0,-1,401,403,404,503]
            self.view.printTicket(ticket)
            self.current_id = int(ticketID)
            return 0
        except AssertionError as e:
            self.view.errorCode = self.api.errorCode
            if ticket == -1: # no tickets on account
                self.view.displayErrors("There are 0 tickets on account to display")
            elif ticket == 401 or ticket == 403:
                self.view.displayErrors("API authentication failed or invalid user credentials")
            elif ticket == 404:
                self.view.displayErrors("Invalid ID requsted, please request a valid ID or domain unavailable")
            elif ticket == 503:
                self.view.displayErrors("API unavailable. Please try again later")
            elif ticket == 0:
                self.view.displayErrors("Bad Request "+ self.api.errorCode)
            self.view.errorCode = None
            self.api.errorCode = None
            return False 

if __name__ == "__main__":
    application = AppPresenter()
    application.run() 