from selenium import webdriver


class initDriver(object):
    """description of class"""

    # webdriver instance
    def __init__(self, browser='chrome'):
        '''
        initialize selenium webdriver, use chrome as default webdriver
        '''
        browser = browser.lower()
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)

    def getDriver(self):
        return self.driver
