from config import Config

class WeatherMap:

    config = Config

    img_weather_logo = "//div[@id='logo']/img"
    lbl_pin_city = "//span[contains(text(),'Pin your City')]"
    txt_search_city = "//input[@id='searchBox']"

    # Parameterized elements based on city name given in .env
    chk_search_city = f"//input[@id='{config.city_name}' and @type='checkbox']"
    lbl_degree_temp_on_map = f"//div[@title='{config.city_name}']//span[@class='tempRedText']"