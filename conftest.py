import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es, fr, ru")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    
    defined_languages = {
        "es": "es-ES",
        "fr": "fr-FR",
        "ru": "ru-RU"}
    if language in defined_languages:
        user_language = defined_languages[language]
        options = Options()
        options.add_argument("--log-level=3")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        browser = None
        raise pytest.UsageError("--language should be: es, fr, ru")

    yield browser
    print("\nquit browser..")
    browser.quit()
    

@pytest.fixture(scope="module")
def lang(request):
    return request.config.getoption("language")
