import pytest
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope = "session")
def driver():
   edge_options = Options()
   driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
   driver.get("https://www.demoblaze.com/")
   yield driver
   driver.quit()



