from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.object_repository.ndtv_home import NDTVHome
from common.util.constants import Constants
from common.util.common_methods import CommonMethods
from common.services.fetch_temperature import TemperatureService
from common.object_repository.weather_map import WeatherMap

@pytest.mark.smokeTestDebug
@pytest.fixture
def test_pyfixtureInit():
    global driver
    global con
    global URL
    driver = webdriver.Chrome()
    con = Constants()
    url = con.NDTV_url
    #change this driver.get later
    driver.get("https://social.ndtv.com/static/Weather/report/")
    driver.maximize_window()
  #  alert = Alert(driver)
  #  alert.accept()
    yield
    print("Initiating Tear Down")
    #driver.quit()

def test_verify_weather_map(test_pyfixtureInit):
    print("Search City Temperature Test Started")

    common_methods = CommonMethods()
    temp_service = TemperatureService()
    ndtv_obj_repo = NDTVHome()
    weather_map = WeatherMap()

    # 3 lines to be uncommented for test current test purpose

   # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, ndtv_obj_repo.btn_accept_alert)))

   # driver.find_element_by_xpath(ndtv_obj_repo.btn_accept_alert).click()
   # common_methods.test_navigate_to_weather_map(driver)

    # This is a bypass and should be removed

   # driver.get("https://social.ndtv.com/static/Weather/report/")

    # Verify elements on the weather map

    temp_service.function_get_city_temp()

    txt_search = driver.find_element_by_xpath(weather_map.img_weather_logo)







