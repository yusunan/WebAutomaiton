import unittest
#from selenium import webdriver
from UTFHomePage import UTFHomePage
from SystemDevices import SystemDevices
import CommonConfiguration as comon
from TestCaseInfo import TestCaseInfo
from TestReport import TestReport
from datetime import datetime
import LogUtility
import time

class Test_TC_Login(unittest.TestCase):
    def setUp(self):
        self.base_url = comon.baseUrl()
        self.testCaseInfo = TestCaseInfo(id=1,name="UTF login",owner='yusunan')
        # self.testResult = TestReport()
        LogUtility.CreateLoggerFile("UTF login")

    def test_searchPython(self):
        try:
            self.testCaseInfo.starttime = comon.getCurrentTime()

            #Step1: open base site
            LogUtility.Log("Open Base site" + self.base_url)
            Homepage = UTFHomePage()

            Homepage.open(self.base_url)

            Homepage.adminLogin()

            time.sleep(2)

            sys = SystemDevices()
            sys.refresh()

            # assert('Python' in title)
            # print(title)

            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUtility.Log(("Got error: "+str(err)))
        finally:
            LogUtility.CreateLoggerFile("UTF login")
            # self.testCaseInfo.endtime = cc.getCurrentTime()
            # self.testCaseInfo.secondsDuration = cc.timeDiff(self.testCaseInfo.starttime,self.testCaseInfo.endtime)
        pass
    def tearDown(self):
        LogUtility.CreateLoggerFile("UTF login")
        #self.driver.close()
        # self.testResult.WriteHTML(self.testCaseInfo)

if __name__ == '__main__':
    unittest.main()
