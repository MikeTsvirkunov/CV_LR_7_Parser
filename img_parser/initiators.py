import logging
from img_parser.constants import FilePathes
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import ioc


def driver_initiation():
    driver_path = FilePathes.driver_path
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'none'
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    # options.add_argument('--start-maximized')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    service = webdriver.ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(options=options, service=service)
    wait = WebDriverWait(driver, 120)
    ioc.provide('HH.Registration.WebDrivers.Main', driver)
    ioc.provide('HH.Registration.Waiters.Std', wait)
    logging.info('Created chrome driver')
