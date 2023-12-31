"""This file stores selectors"""
APP_PREFIX = "kg.dcb.mobilebanking.debug:id/"

def find_element_by_id(el_id, driver):
    return driver.find_element("id", f"{APP_PREFIX}{el_id}")

def find_element_by_xpath(el_path, driver):
    return driver.find_element("xpath", el_path)

def find_elements_by_accessibility_id(el_acs, driver):
    return driver.find_elements_by_accessibility_id(f"{APP_PREFIX}{el_acs}")

