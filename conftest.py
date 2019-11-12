import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, fr, es")

@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("language")
    if language == "ru":
        print("\nrussian language for test..")
        return language
    elif language == "fr":
        print("\nfrance language for test..")
        return language
    elif language == "es":
        print("\nspanish language for test..")
        return language
    else:
        raise pytest.UsageError("--language should be ru, fr, es")
    
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()