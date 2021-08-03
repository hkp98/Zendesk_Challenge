# Zendesk_Coding_Challenge

In this challenge I am building zendesk ticket viewer, fetching tickets using the zendesk api. Proper testing of the functionality is performed in the testing module.

This app has been tested to work on 64-bit: Windows 10 and Mac OS.

## Application Architecture-> MVP Architecture:

The MVP or Model-View-Presenter, which is mostly used to build the user interface (UI).In this model, the Presenter is counted as the “middle man” and all program logic is sent to the Presenter. 

1. Model: Acts as an interface and defines the data to be in the user interface.
2. View: Displays the data and sends the user commands to the Presenter.
3. Presenter: It is like a bridge between Model and View. Presenter retrieves various data from Model repositories and prepares them for display in View.

![image](https://user-images.githubusercontent.com/76500390/127947169-2d9900c4-9fe0-4bbe-b807-f2cc7912417a.png)

In this project,
1. model -> API_connection.py
2. view -> view.py
3. presenter -> presenter.py (This integrates both API_connection.py & view.py)

## Installation & Set-up:
Python 3 Installation:
Windows 10:
To install Python 3.9.6, head to https://www.python.org/downloads/ and download the file which says "Windows x86-64 executable installer". After downloading, run the executable and chose Add Python 3.9 to PATH option. Then follow the instrcutions to get a full installation of Python 3.9.6 on your system.

Mac OS:
For installing Python 3.9.6 on Mac, head to https://www.python.org/downloads/ and under "Python 3.9.6" click on "Download Mac OS X 64-bit/32-bit installer" and download the one suitable for your machine. Run the installer and follow the steps to get a full standard installation of Python 3.9.6 on your system.

Using the Application: (in windows 10)
1. Clone the git-hub repository named Zendesk_Coding_Challenge in a new folder
2. Open the folder in any IDE
3. Now, create an venv using command ( virtualenv env ) 
4. Here, activate the venve using command ( .\env\Scripts\activate.ps1 ) 
5. Now,install the requirements.txt file using command ( pip install -r requirements.txt)
6. Now, run python presenter.py or presenter/presenter.py (if gives location error)

or

Another way (Mac or Windows)

To start using this app, download the git repository or the zip file. Open terminal/command line and go in the presenter folder of this app through cd commands. Then type:

python presenter.py (Windows)

or

python3.9 presenter.py (Mac)

You will see this scren: 
![image](https://user-images.githubusercontent.com/76500390/127950954-119d0b1a-c39e-4bf1-91ec-45c87e5484c0.png)


## Application Tesing:

For testing this app, go to the "Testing_module" folder within the app on command line/terminal by using cd commands. Then type:

python test.py -b (Windows)

or

python3.9 test.py -b (Mac)

Output Screen for test.py Shows

![image](https://user-images.githubusercontent.com/76500390/127952652-4446f260-34db-4f12-9d05-99222a2a9971.png)




### References:
1. https://www.globo.tech/learning-center/5-most-common-http-error-codes-explained/   (For possible error codes)
2. https://docs.python.org/3/library/datetime.html                                     (for date-time)
3. https://docs.python-requests.org/en/master/                                          (for requests library)
4. https://ducmanhphan.github.io/2019-08-05-MVP-architectural-pattern/ (The MVP Architecture)
5. https://docs.python.org/3/library/unittest.html (Testing)
6. https://www.geeksforgeeks.org/unit-testing-python-unittest/
7. 
