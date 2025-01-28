import pytest
from selenium import webdriver
from browsermobproxy import Server


server = Server("C:\Users\Serjan777\miniconda3\Lib\site-packages\browsermobproxy")
server.start()
proxy = server.create_proxy()
options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={proxy.proxy}')
driver = webdriver.Chrome(options=options)
proxy.new_har("500", options={'captureHeaders': True, 'captureContent': True})
driver.get("https://pizzeria.skillbox.cc/cart/")

@pytest.fixture()
def send_500_response():
    for entry in proxy.har['log']['entries']:
        request_url = entry['request']['url']
        if 'pizzeria.skillbox.cc/cart' in request_url:
            proxy.rewrite_url(request_url, "https://pizzeria.skillbox.cc/cart/500")
            proxy.add_header(request_url, "HTTP/1.1 500 Internal Server Error")

    yield driver
    driver.quit()
    server.stop()


