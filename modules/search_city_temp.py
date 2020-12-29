from selenium import webdriver
import pytest
from common.object_repository.ndtv_home import NDTVHome
from common.util.constants import Constants
from common.util.common_methods import CommonMethods

@pytest.mark.smokeTestDebug
@pytest.fixture
def test_pyfixtureInit():
    global driver
    global con
    global URL
    driver = webdriver.Chrome()
    con = Constants()
    URL = con.URL
    driver.get(URL)
    driver.maximize_window()
    yield
    print("Initiating Tear Down")
    #driver.quit()

def test_verify_weather_map(test_pyfixtureInit):
    print("Search City Temperature Test Started")

    common_methods = CommonMethods()
    common_methods.test_navigate_to_weather_map()

    # Verify elements on the weather map








