import requests
import pandas as pd
import json

class ZenApi:
    def __init__(self):
        self.URL = ""
        self.data = {}
        self.loginID = "hkp49@scarletmail.rutgers.edu"
        self.password = "H007@123!"
        self.subdomain = "zccharsh"
        self.errorCode = None

    def requestZenApi(self, id:int = ""):
        self.URL = "https://" + self.subdomain + ".zendesk.com/api/v2/tickets.json"
        response = requests.get(self.URL, auth=(self.loginID, self.password))
        self.data = response.json()
        next_page = []
        new = self.data
        print(response.status_code)
        # print(self.data)
        while new["next_page"] is not None and new["next_page"] not in next_page:
            self.URL = new["next_page"]
            next_page.append(self.URL)
            response = requests.get(self.URL, auth=(self.loginID, self.password))
            new = response.json()
            # print("Next: ", new["next_page"])
            self.data["tickets"].extend(new["tickets"]) 
        df = pd.DataFrame(self.data)
        print(df.tickets[1])


x = ZenApi()
x.requestZenApi()