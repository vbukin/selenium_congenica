from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.constans.enums import Browser


def driver_init(config, screen_size):
    if config.browser == Browser.CHROME.value:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.set_window_size(screen_size.value[0], screen_size.value[1])
    elif config.browser == Browser.FIREFOX.value:
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.set_window_size(screen_size.value[0], screen_size.value[1])
    else:
        raise ValueError(f"Invalid browser: {config.browser}")

    return driver