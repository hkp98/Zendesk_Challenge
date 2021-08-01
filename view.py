import math 

class ApplicationView():
    def __init__(self):
        self.page_limit = 25
        self.errorCode = None
    
    def mainMessage(self): # display the intial view of Application
        print("********** Welcome to Zendesk Ticket Viewer Interface **********")
        print(" The Interface lets the User to view tickets on a particular Zendesk Account ")
        print(" Type menu to view the options or Type q to exit the Application: ")
        return 0
    
    def displayErrors(self,error_message: str):
        if self.errorCode is not None:
            print("\nError fetching data form the API: ",self.errorCode)
        print(error_message)
        return 1
    
    def displayInputMessage(self,message: str,code: int):
        print(message)
        return code
    
    def printMenu(self):
        print("\nSelect View Options")
        print("Press 1 to print all tickets")
        print("Press 2 to print a single ticket information")
        print("Press q to quit the application")
        print("Type 'menu' to display view options")
        print("Enter your choice: ")
        return 0
    
    def quit(self):
        print("\n..Thank you for using the Zendesk Ticket Viewer...")
        return 0
    
    def fetchTickets(self,ticketID):
        if ticketID == "all":
            print("\n Fetching all the tickets, please wait ...")
        else: 
            print("\nFething the ticket", ticketID + ",","please wait ...")
        return 0
    
    def printTickets(self,tickets_data,pageNo):
        tickets = tickets_data["tickets"]
        # calculating total pages to parse 
        total_pages = math.ceil(float(len(tickets)) / float(self.page_limit))

        if pageNo > total_pages:
            pageNo = 1
        elif pageNo < 1:
            pageNo = total_pages
        
        tickets_paging = 0
        




