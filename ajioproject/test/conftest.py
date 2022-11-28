import pytest
import time
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

#Cross browsing
@pytest.fixture(params=["Chrome","Edge","Firefox"])
def _driver(request):


    if request.param=="Firefox":
        options = Options()
        options.binary_location=r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=Config.Firefox_Driver_path,options=options)
        driver.get(Config.URL)
        driver.maximize_window()
        driver.find_element("xpath","//div[@class='ic-close-quickview']").click()
        time.sleep(10)




    elif request.param=="Edge":
      driver=webdriver.Edge(Config.Edge_Driver_path)
      driver.get(Config.URL)
      driver.maximize_window()


    elif request.param=="Chrome":
        driver= webdriver.Chrome(Config.Chrome_Driver_path)
        driver.get(Config.URL)
        driver.maximize_window()




    driver.implicitly_wait(80)
    yield driver
    print(driver.title)
    driver.save_screenshot("radhika.png")
    driver.close()