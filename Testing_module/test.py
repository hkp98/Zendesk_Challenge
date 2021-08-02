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

