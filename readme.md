This is a readme. You have had enough now. Get on with it.

To run this service:

Start the virtual environment with this command in a terminal/command prompt: venv\Scripts\activate 

To make a new database migration based on the models: flask db migrate

To upgrade the current database to the current database version: flask db upgrade

Run the following command to start the service: flask run

To run the unit tests, run: python -m unittest tests\tests.py

Notes To Self:
For login, it'll work like this:
Assuming that login is at "/login", My server would receive a response at that endpoint. For a GET, it will check if there is a login cookie that was passed as part of the request. If there is, I'll redirect to the main page. If there isn't, I'll load the page. If there is a POST, it'll collect the username and password, and call your login API using that info, and wait for a response.
If it is a 2XX response, I'll be expecting a login cookie to bind to the client. If it's a 4XX response, I'll say that the login credentials were bad. If it's a 5XX response, I'll just say something went wrong and reload the login page.

But please don't forget your swagger doc/documentation
It's sort of like an agreement between an api provider and api consumer.
In order for a consumer to consume, they need to know things like how the response will be formatted, in which scenarios different status codes will be written, etc.
All this information is compiled in one place
Which is the documentation for the API.

https://swagger.io/docs/specification/about/
https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md

C:\xampp\mysql\bin\mysql.exe -u root -p <password>
