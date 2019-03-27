from BasePage import BasePage
import time


class SystemDevices(BasePage):
    """description of class"""
    deviceManagement = ('Xpath', ".//*[@id='sidebarMenu']/div/div[2]/ul/li[5]/a/span[1]")
    deviceMaintain = ('Xpath', ".//*[@id='sidebarMenu']/div/div[2]/ul/li[5]/ul/li[1]/a")
    proxySever = ('Xpath', ".//*[@id='neu-proxies']/ul/li")
    refreshButton = ('Xpath', ".//*[@id='proxyTab']/div/div[1]/div[1]/span[2]/i[1]")

    def refresh(self):
        self.click(self.getElement(self.deviceManagement))
        self.click(self.getElement(self.deviceMaintain))
        time.sleep(2)
        severList = self.getElementList(self.proxySever)
        for i in severList:
            self.click(i)
            self.click(self.getElement(self.refreshButton))

        # searchBox = self.driver.find_element(*self.searchbox)
        # searchBox.send_keys(searchContent+Keys.RETURN)
