
# ParaBank Automation Project with Selenium + pytest

This is an automation testing project for the ParaBank web application using Selenium and Pytest
This includes automated tests for:-  
1.Login   
2.Logout  
3.Registration  
4.Forget login info  
5.Opening New Account  
6.Transfer Funds  
7.Paying Bills  
8.Find Transaction   
9.Update Contact Info  
10.Requesting Loan  

The Reporting is implemented using pytest-html, with screenshots captured for failures and logs for tracking each procedure.


## Installation

1. Clone the repository:

```bash
git clone https://github.com/rickcache/ParaBank.git
```
2. Navigate to the project folder:  

```bash
cd ParaBank
```
3. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```
4. Install required packages:
```bash
pip install -r requirements.txt
```
5.Run tests:
```bash
pytest -v -s 
```
6. Generate HTML report:
```bash
pytest --html=report.html -v -s
```
7.Screenshots and logs will be automatically generated.

## Features

-Login: valid and invalid scenarios  
-Logout:  
-Registration: new user creation
-Forget login info: username/password retrieval  
-Opening New Account: creation of a new account for Transaction  
-Transfer Funds: invalid and invalid scenarios     
-Paying Bills: automated filling forms and checking success  
-Find Transaction: access of Transaction history   
-Update Contact Info: Update of personal information  
-Requesting Loan: Request for loan

## Reporting

HTML Report: report.HTML  
Screenshots: Captured automatically for test failures   
Logs: test_log.log contains detailed test execution logs
## Notes
This project is primarily for learning, practice, and freelance showcase purposes

You can clone and modify it for your own practice projects

The ParaBank site resets periodically, so test data might need refreshing
## Author

- [@rickcache](https://www.github.com/iamrexx)
