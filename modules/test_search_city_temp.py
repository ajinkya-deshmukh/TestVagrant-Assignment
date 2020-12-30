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
from config import Config


@pytest.fixture
def test_pyfixtureInit():
    global driver
    global con
    global URL
    driver = webdriver.Chrome()
    con = Constants()
    url = con.NDTV_url
    driver.get(url)
    driver.maximize_window()
    yield
    print("Initiating Tear Down")
    #driver.quit()

def test_verify_weather_map(test_pyfixtureInit):
    print("Search City Temperature Test Started")

    common_methods = CommonMethods()
    temp_service = TemperatureService()
    ndtv_obj_repo = NDTVHome()
    weather_map = WeatherMap()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, ndtv_obj_repo.btn_accept_alert)))
    driver.find_element_by_xpath(ndtv_obj_repo.btn_accept_alert).click()
    common_methods.test_navigate_to_weather_map(driver)

    # Verify elements on the weather map
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, weather_map.img_weather_logo)))
    common_methods.function_is_present(driver, weather_map.img_weather_logo, "Weather Map Logo")
    common_methods.function_is_present(driver, weather_map.lbl_pin_city, "Pin City Label")
    common_methods.function_is_present(driver, weather_map.txt_search_city, "Search Text field")

    # Search for city in map
    config = Config
    driver.find_element_by_xpath(weather_map.txt_search_city).send_keys(config.city_name)
    is_checked = driver.find_element_by_xpath(weather_map.chk_search_city).is_selected()
    if not is_checked:
        driver.find_element_by_xpath(weather_map.chk_search_city).click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, weather_map.lbl_degree_temp_on_map)))
    driver.find_element_by_xpath(weather_map.lbl_degree_temp_on_map).click()

    # Fetch city temp from map
    ui_map_temp = driver.find_element_by_xpath(weather_map.lbl_degree_temp_on_map).text
    ui_map_temp = ui_map_temp.strip("℃")

    # Compare temperature from weather map UI and from API
    common_methods.function_compare_temperature(ui_map_temp, temp_service.function_get_city_temp())









