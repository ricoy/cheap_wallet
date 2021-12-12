import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

STOCKS = str(os.environ.get("STOCKS")).split(",")
URL_STOCKS = str(os.environ.get("URL_STOCKS"))
XPATH_STOCKS_PVP = str(os.environ.get("XPATH_STOCKS_PVP"))
XPATH_STOCKS_DY = str(os.environ.get("XPATH_STOCKS_DY"))
XPATH_STOCKS_PRICE = str(os.environ.get("XPATH_STOCKS_PRICE"))

FIIS = str(os.environ.get("FIIS")).split(",")
URL_FIIS = str(os.environ.get("URL_FIIS"))
XPATH_FIIS_PVP = str(os.environ.get("XPATH_FIIS_PVP"))
XPATH_FIIS_DY = str(os.environ.get("XPATH_FIIS_DY"))
XPATH_FIIS_PRICE = str(os.environ.get("XPATH_FIIS_PRICE"))
