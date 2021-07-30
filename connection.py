import requests
import pandas as pd
import json
import math
class ZenApi:
    def __init__(self):
        self.URL = ""
        self.data = {}
        self.loginID = "hkp49@scarletmail.rutgers.edu"
        self.password = "H007@123!"
        self.subdomain = "zccharsh"
        self.errorCode = None

    def requestZenApi(self,fetch_all_tickets: bool = True,fetch_id: int = ""):
        if fetch_all_tickets:
            self.URL = "https://" + self.subdomain + ".zendesk.com/api/v2/tickets.json"
        else:
            self.URL = "https://" + self.subdomain + ".zendesk.com/api/v2/tickets/" + str(fetch_id) + ".json"
        try:
            response = requests.get(self.URL, auth=(self.loginID, self.password))
            if response.status_code != 200:
                # print("Bad request. Error getting data from API. Error Code: ", r.status_code)
                self.errorCode = response.status_code
                if response.status_code == 401 or response.status_code == 403:  # Authentication or invalid user credentials error
                    return response.status_code 
                elif response.status_code == 404:  # 404 = No tickets or invalid ticket ID error
                    return response.status_code
                elif response.status_code == 503:  # API unavailable error
                    return response.status_code
                return 0  # Other bad requests
            self.data = response.json() 
            new = self.data
            next_page = [] # single API call reads only 100 tickets we use next page URL to fetch all the tickets 
            while all and new["next_page"] is not None and new["next_page"] not in next_page:
                self.URL = new["next_page"]
                next_page.append(self.URL)
                response = requests.get(self.URL, auth=(self.loginID, self.password))
                new = response.json()
                self.data["tickets"].extend(new["tickets"])  
            
            return self.data
        except requests.exceptions.RequestException as e:
            return 0
        except ConnectionError:
            return 0

x = ZenApi()
x.requestZenApi()