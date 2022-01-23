------------
## SET UP AND RUN
Version requirements: python3.8 / python3.9

`preparing`
1. virtualenv dummy
2. dummy/bin/activate
3. pip3 install -r requirements.txt

`launch`
1. pytest --html=reports/test.html --self-contained-html  # running and generating a report in html format
2. python3.8 reports/report.py # flask application for html report output



## APITEST

**employee_create_test**:
`apitest/employee_create_test.py`  
1. Generation of random data to create employee
2. POST request to create employee + check status code
3. Reconciliation of data values after creating a record
4. Check internal status
5. Check message 
6. Sending POST request with empty data
7. Data integrity check, expected result - no record should be created


**employee_list_test**:
`apitest/employee_list_test.py`  
1. Send GET request to output employee list + check status code
2. Reconcile data type (waiting for list)
3. Checking for an empty list of employee data
4. Check internal status 
5. Message check


**employee_test**:
`apitest/employee_test.py`  
1. Send GET request to output employee information by ID + check status code
2. Reconcile the data type of each key in the array
3. Check expected ID 
4. Check internal status 
5. Message check
6. Sending POST request to check information with incorrect ID value 
7. Check expected status 400 
8. Check message
9. Sending POST request to verify information with a non-existent ID value 
10. Checking data for emptiness
11. Check message