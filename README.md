# selenium-buy-product-on-amazon
This is a simple selenium program based on page object modal to buy a TV (3rd item) on amazon. 

Use the following to execute the pytest test cases. 

$ python3 -m venv venv
```

Activate the Python virtual environment


On Unix or Mac OS, run:

```
$ source venv/bin/activate
```

Use pip to install dependencies for the sample application

```
$ pip install -r requirements.txt
```


In order to update the requirements.txt use the following command:
pip3 freeze > requirements.txt

Run the following command to run tests in chrome
```
$pytest --browser=chrome
````

Run the following command to run tests in edge
```
$pytest --browser=edge
````

Run the following command to run tests in firefox
```
$pytest --browser=firefox
````

Run the following command to run parallel tests in chrome
```
$pytest -n 3 --browser=chrome
```