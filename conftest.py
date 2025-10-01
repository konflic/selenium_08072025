import pytest

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--base_url")
    parser.addoption("--drivers", default="/home/mikhail/Downloads/drivers")
    parser.addoption("--headless", action="store_true")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    driver = None

    if browser_name in ("chrome", "ch"):
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name in ("ff", "firefox"):
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "safari":
        driver = webdriver.Safari()
    elif browser_name in ("ya", "yandex"):
        service = ChromeService(executable_path=f"{drivers_folder}/yandexdriver")
        options = ChromeOptions()
        options.binary_location = "/home/mikhail/.local/share/flatpak/app/ru.yandex.Browser/x86_64/stable/6ccf4f48f29e5cc1b85c68cc971abd26dd8af90564e863677fa3ab5c70814863/files/yandex_browser/yandex-browser"
        driver = webdriver.Chrome(service=service, options=options)

    yield driver

    driver.close()


def something():
    pass
