# TestVagrant Assignment

A Python, Selenium assignment project PyTest as runner for testing the assignment scenario verifying NDTV weather map with OpenWeather temperature.


### Installing

Run the requirements.txt to install all the dependencies


### Running the tests

Specify the City Name & The temperature range variation acceptable in .env file (Have put these aprameters in .env file to reduce hardcoding of these dynamic values)

Run the assignment using "pytest modules/"


### Break down into end to end tests

This test is for launching the ndtv home website, navigating to weather map and entering city name. After which the value from UI is fetched.

At the same time the same city temperautre is fetched using the OpenWeather API and the values are compared with a specified acceptable range.


### Built With

* Python
* Selenium
* Pytest-check


### Authors

* **Ajinkya Deshmukh** - (https://github.com/ajinkya-deshmukh/IncubyteAssignment)
