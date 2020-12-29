from selenium import webdriver
import pytest
from common.object_repository.ndtv_home import NDTVHome
from common.util.constants import Constants


class CommonMethods():

    def test_navigate_to_weather_map(self, driver):

        ndtv_obj_repo = NDTVHome()
        con = Constants()
        driver.get(con.NDTV_url)

        btn_latest = driver.find_element_by_xpath(ndtv_obj_repo.link_latest)
        btn_latest.click()

        link_section = driver.find_element_by_xpath(ndtv_obj_repo.link_latest)
        link_section.click()

        link_weather = driver.find_element_by_xpath(ndtv_obj_repo.link_weather)
        link_weather.click()
