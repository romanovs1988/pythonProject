import logging
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure
from browsermobproxy import Server


"""@pytest.fixture()
def get_driver(pytestconfig):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Prepare {browser_name} browser...')
    if pytestconfig.getini("headless") == 'True' and browser_name == "chrome":
        options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    #pytestconfig.cls.driver = driver
    options.page_load_strategy = 'normal'
    driver = Remote(
        desired_capabilities={
            "browserName": pytestconfig.getini("browser_name"),
            "browserVersion": pytestconfig.getini("browser_version")
        },
        command_executor=pytestconfig.getini("get_driver_url"),
        options=options
    )
    logging.info(f'Browser {browser_name} has been started...')
    yield driver
    driver.quit()"""


@pytest.fixture()
def get_driver(pytestconfig):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Prepare {browser_name} browser...')
    logging.info(f'Browser {browser_name} has been started...')
    # request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture
def go_to_url(page):
    @allure.step('Открытие страницы {url}')
    def callback(url):
        page.goto(url, wait_until='domcontentloaded')
    return callback

@pytest.fixture()
def send_500_response():
    server = Server(r"C:\Program Files (x86)\browsermob-proxy-2.1.4-bin")
    server.start()
    proxy = server.create_proxy()
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server={proxy.proxy}')
    driver = webdriver.Chrome(options=options)
    proxy.new_har("500", options={'captureHeaders': True, 'captureContent': True})
    driver.get("https://pizzeria.skillbox.cc/cart/")
    for entry in proxy.har['log']['entries']:
        request_url = entry['request']['url']
        if 'pizzeria.skillbox.cc/cart' in request_url:
            proxy.rewrite_url(request_url, "https://pizzeria.skillbox.cc/cart/500")
            proxy.add_header(request_url, "HTTP/1.1 500 Internal Server Error")

    yield driver
    driver.quit()
    server.stop()
