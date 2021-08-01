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
        
 