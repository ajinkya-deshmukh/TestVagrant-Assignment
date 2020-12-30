from dotenv import load_dotenv
import os
load_dotenv()


class Config:
    path = '.env'
    load_dotenv(dotenv_path=path, verbose=True)
    ENV = os.getenv("ENV")
    URL = os.getenv("URL")
    API_KEY = os.getenv("API_KEY")
    city_name = os.getenv("city_name")
    range_variation_allowed = os.getenv("range_variation_allowed")