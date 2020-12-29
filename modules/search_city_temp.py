from selenium import webdriver
import pytest
from common.object_repository.ndtv_home import NDTVHome
from common.util.constants import Constants

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

def test_search_city_temperature(test_pyfixtureInit):

    ndtv_obj_repo = NDTVHome()
    print("Search City Temperature Test Started")
    driver.get(con.NDTV_url)

    btn_latest = driver.find_element_by_xpath(ndtv_obj_repo.link_latest)
    btn_latest.click()

    link_section = driver.find_element_by_xpath(ndtv_obj_repo.link_latest)
    link_section.click()

    link_weather = driver.find_element_by_xpath(ndtv_obj_repo.link_weather)
    link_weather.click()

