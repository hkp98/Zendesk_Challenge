import math 

class ApplicationView():
    def __init__(self: object): 
        self.page_limit = 25
        self.errorCode = None
    
    def mainMessage(self: object)-> int: # display the intial view of Application
        print("********** Welcome to Zendesk Ticket Viewer Interface **********")
        print(" The Interface lets the User to view tickets on a particular Zendesk Account ")
        print(" Type menu to view the options or Type q to exit the Application: ",end=" ")
        return 0
    
    def displayInputMessage(self,message: str,code: int)-> int:
        print(message,end="")
        return code
    
    def printMenu(self: object)-> int:
        print("\nSelect View Options")
        print("Press 1 to print all tickets")
        print("Press 2 to print a single ticket information")
        print("Press q to quit the application")
        print("Type 'menu' to display view options")
        print("Enter your choice: ",end="")
        return 0
    
    def fetchTickets(self: object,ticketID: str)-> int:
        if ticketID == "all":
            print("\n Fetching all the tickets, please wait ...")
        else: 
            print("\nFetching the ticket", ticketID + "," + "please wait ...")
        return 0
    
    def printTickets(self: object,tickets_data: dict,pageNo: int)-> int:
        tickets = tickets_data["tickets"]
        # calculating total pages to parse 
        total_pages = math.ceil(float(len(tickets)) / float(self.page_limit))

        if pageNo > total_pages:
            pageNo = 1
        elif pageNo < 1:
            pageNo = total_pages
        
        tickets_paging = 0
        tickets_per_page = (pageNo-1)*self.page_limit
        
        for i in range(int(tickets_per_page),int(self.page_limit + tickets_per_page)):
            if i < len(tickets):
                if tickets[i]["id"] == None:
                    continue
                else:
                    print("<<" + tickets[i]["status"] + ">>", "Ticket ID:", tickets[i]["id"],"Priority:","'{0}'".format(tickets[i]["priority"]), 
                    "Opened by",tickets[i]["requester_id"], "Updated at", tickets[i]["updated_at"],
                    "Subject:", "'{0}'".format(tickets[i]["subject"])
                    )
                tickets_paging += 1    

        print("\nDisplayed", tickets_paging, "tickets on page", pageNo, "of", total_pages)
        print("\nEnter 'd' to go down, 'u' to go up, 'menu' for menu or 'q' for quit: ", end="")
        return pageNo  # Current page no

    def printTicket(self: object,tickets_data: dict)-> int:
        if "ticket" in tickets_data:
            print("<<" + tickets_data["ticket"]["status"] + ">>", "Ticket ID:", tickets_data["ticket"]["id"],"Priority:","'{0}'".format(tickets_data["ticket"]["priority"]), "Opened by",tickets_data["ticket"]["requester_id"], 
                  "Updated at", tickets_data["ticket"]["updated_at"],"Subject:", "'{0}'".format(tickets_data["ticket"]["subject"]))
            print("\n Type menu to display the 'menu' options: ",end="")
            return 0
        else:
            return 1
    
    def quit(self: object)-> int:
        print("\n...Thank you for using the Zendesk Ticket Viewer...")
        return 0
    
    def displayErrors(self: object,error_message: str)-> int:
        if self.errorCode is not None:
            print("\nError fetching data from the API: ",self.errorCode)
        print(error_message)
        return 1
            

 





