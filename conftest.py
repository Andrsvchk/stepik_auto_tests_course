import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                                      help="Choose language: ru, en, etc.")


#for Chrome
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
          print("\nstart chrome browser for test..")
    else:
          raise pytest.UsageError("--browser should be chrome")

    if user_language is not None:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("Language should have correct locale code")

    yield browser
    print("\nquit browser..")
    browser.quit()

    if __name__ == "__main__":
        unittest.main()


