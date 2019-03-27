from BasePage import BasePage


class UTFHomePage(BasePage):
    """description of class"""
    userName = ('ID', 'username')
    password = ('ID', 'password')
    submit = ('ID', 'login-btn')


    def adminLogin(self):
        self.write(self.getElement(self.userName), 'admin')
        self.write(self.getElement(self.password), '1')
        self.click(self.getElement(self.submit))
        # searchBox = self.driver.find_element(*self.searchbox)
        # searchBox.send_keys(searchContent+Keys.RETURN)
