import os
import pytest

from appium import webdriver
from helpers import take_screenhot_and_logcat


APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '9'
appNameTest = 'kg.o.nurtelecom.internal_test'
appName = 'kg.o.nurtelecom'

class capsAnroid:
    @pytest.fixture(scope="function")
    def driver(self, request, device_logger):
        desired_caps = {
            'appPackage': appName,
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': 'Nexus_5X_API_26_AV8',
            'appActivity': '.ui.splash.SplashScreenActivity',
            'autoGrantPermissions': 'true'
        }
        calling_request = request._pyfuncitem.name

        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

        def fin():
            take_screenhot_and_logcat(driver, device_logger, calling_request)
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value