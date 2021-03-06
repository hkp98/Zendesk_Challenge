# This class helps us to perform user authentication, fetch the tickets using the API call and data processing

import requests
import datetime
import json
from model.user_info import user

class ZenApi:
    def __init__(self: object):
        self.URL = ""
        self.data = {}
        self.loginID = user().loginID
        self.password = user().password
        self.subdomain = user().subdomain
        self.errorCode = None
    
    # this function fetches the data from the Api
    def requestZenApi(self, fetch_all_tickets: bool = True, fetch_ticket_id: int = None)-> object:
        if fetch_all_tickets:
            self.URL = "https://" + self.subdomain + ".zendesk.com/api/v2/tickets.json"
        else:
            self.URL = "https://" + self.subdomain + \
                ".zendesk.com/api/v2/tickets/" + str(fetch_ticket_id) + ".json"
        try:
            response = requests.get(
                self.URL, auth=(self.loginID, self.password))
            if response.status_code != 200:
                # print("Bad request. Error getting data from API. Error Code: ", r.status_code)
                self.errorCode = response.status_code
                # this error is for invalid credentials or authentication
                if response.status_code == 401 or response.status_code == 403:
                    return response.status_code
                elif response.status_code == 404:  # this error is for No tickets or invalid ticket ID error or subdomain invalid error
                    return response.status_code
                elif response.status_code == 503:  # this error is for API unavailable
                    return response.status_code
                return 0  # Other bad requests

            self.data = response.json()
            new = self.data
            next_page = []  # single API call reads only 100 tickets we use next page URL to fetch all the tickets
            while fetch_all_tickets and new["next_page"] is not None and new["next_page"] not in next_page:
                self.URL = new["next_page"]
                next_page.append(self.URL)
                response = requests.get(
                    self.URL, auth=(self.loginID, self.password))
                new = response.json()
                self.data["tickets"].extend(new["tickets"])

            if fetch_all_tickets == True:  # formatting the date-time field for tickets = all or individual ticket
                for i in range(len(self.data["tickets"])):
                    create_date = str(datetime.datetime.strptime(
                        self.data['tickets'][i]['created_at'], "%Y-%m-%dT%H:%M:%SZ"))
                    update_date = str(datetime.datetime.strptime(
                        self.data['tickets'][i]['updated_at'], "%Y-%m-%dT%H:%M:%SZ"))
                    self.data["tickets"][i]["created_at"] = str(create_date)
                    self.data["tickets"][i]["updated_at"] = str(update_date)

            elif fetch_all_tickets == False:
                # print(self.data)
                created_date = str(datetime.datetime.strptime(
                    self.data['ticket']['created_at'], "%Y-%m-%dT%H:%M:%SZ"))
                updated_date = str(datetime.datetime.strptime(
                    self.data['ticket']['updated_at'], "%Y-%m-%dT%H:%M:%SZ"))
                self.data["ticket"]["created_at"] = str(created_date)
                self.data["ticket"]["updated_at"] = str(updated_date)
            return self.data
        except requests.exceptions.RequestException as e:
            return 0
        except ConnectionError:
            return 0

    # this function calls the Api function or returns error if any
    def getTickets(self, fetch_ticket_id: int = None)-> object:
        tickets_data = None
        if fetch_ticket_id == None:
            tickets_data = self.requestZenApi(True)
            # print(type(tickets_data))
            if type(tickets_data) == int and tickets_data == 0:
                return 0
            elif type(tickets_data) == dict and tickets_data['count'] == 0:
                return -1
            return tickets_data
        else:
            tickets_data = self.requestZenApi(False, fetch_ticket_id)
            if type(tickets_data) == int and tickets_data == 0:
                return 0
            return tickets_data
        return tickets_data

    

# x = ZenApi()
# x.getTickets()
