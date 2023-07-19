""" Standart test cases"""
import os

import allure
from allure_commons.types import AttachmentType
from confHelper.configHelperAndroid.selectorHelper import find_element_by_id, find_element_by_xpath, \
    find_elements_by_accessibility_id
from elements.elementsAndroid import elements, list_activity, elements_path
import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, \
    ElementNotSelectableException, \
    TimeoutException, StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException

directory = '%s/results/appiumscr/' % os.getcwd()
file_name = 'screenshot.png'
F_EXT = ".png"

def click_by_id(driver, id, sleep=None, scrn=None):
    try:
        driver.implicitly_wait(5)
        # Попытка найти элемент по идентификатору
        element = find_element_by_id(elements.get(id), driver)
        # Делать что-то с элементом, если он найден
        element.click()
    except NoSuchElementException:
        with allure.step("Элемент не найден на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не найден на экране", id)
    except ElementNotVisibleException:
        with allure.step("Элемент невидим на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент невидим на экране", id)
    except ElementNotSelectableException:
        with allure.step("Элемент не может быть выбран"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не может быть выбран", id)
    except TimeoutException:
        with allure.step("Превышено время ожидания"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Превышено время ожидания", id)
    except StaleElementReferenceException:
        with allure.step("Ссылка на элемент устарела или стала недействительной"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Ссылка на элемент устарела или стала недействительной", id)
    except ElementClickInterceptedException:
        with allure.step("Попытка клика на элемент прервана другим элементом"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Попытка клика на элемент прервана другим элементом", id)
    except ElementNotInteractableException:
        with allure.step("Элемент не доступен для взаимодействия"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не доступен для взаимодействия", id)

    if sleep is True:
        time.sleep(5)
    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.implicitly_wait(5)


def send_keys_by_id(driver, id, text, sleep=None, scrn=None):
    try:
        driver.implicitly_wait(5)
        # Попытка найти элемент по идентификатору
        element = find_element_by_id(elements.get(id), driver)
        # Делать что-то с элементом, если он найден
        element.send_keys(text)
    except NoSuchElementException:
        with allure.step("Элемент не найден на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не найден на экране", id)
    except ElementNotVisibleException:
        with allure.step("Элемент невидим на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент невидим на экране", id)
    except ElementNotSelectableException:
        with allure.step("Элемент не может быть выбран"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не может быть выбран", id)
    except TimeoutException:
        with allure.step("Превышено время ожидания"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Превышено время ожидания", id)
    except StaleElementReferenceException:
        with allure.step("Ссылка на элемент устарела или стала недействительной"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Ссылка на элемент устарела или стала недействительной", id)
    except ElementClickInterceptedException:
        with allure.step("Попытка клика на элемент прервана другим элементом"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Попытка клика на элемент прервана другим элементом", id)
    except ElementNotInteractableException:
        with allure.step("Элемент не доступен для взаимодействия"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не доступен для взаимодействия", id)

    if sleep is True:
        time.sleep(5)
    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.implicitly_wait(5)


def click_by_xpath(driver, path, sleep=None, scrn=None):
    try:
        driver.implicitly_wait(5)
        # Попытка найти элемент по идентификатору
        element = find_element_by_xpath(elements_path.get(path), driver)
        # Делать что-то с элементом, если он найден
        element.click()
    except NoSuchElementException:
        with allure.step("Элемент не найден на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не найден на экране", path)
    except ElementNotVisibleException:
        with allure.step("Элемент невидим на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент невидим на экране", path)
    except ElementNotSelectableException:
        with allure.step("Элемент не может быть выбран"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не может быть выбран", path)
    except TimeoutException:
        with allure.step("Превышено время ожидания"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Превышено время ожидания", path)
    except StaleElementReferenceException:
        with allure.step("Ссылка на элемент устарела или стала недействительной"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Ссылка на элемент устарела или стала недействительной", path)
    except ElementClickInterceptedException:
        with allure.step("Попытка клика на элемент прервана другим элементом"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Попытка клика на элемент прервана другим элементом", path)
    except ElementNotInteractableException:
        with allure.step("Элемент не доступен для взаимодействия"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не доступен для взаимодействия", path)

    if sleep is True:
        time.sleep(5)
    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.implicitly_wait(5)


def send_keys_by_xpath(driver, path, text, sleep=None, scrn=None):
    try:
        driver.implicitly_wait(5)
        # Попытка найти элемент по идентификатору
        element = find_element_by_xpath(elements_path.get(path), driver)
        # Делать что-то с элементом, если он найден
        element.send_keys(text)
    except NoSuchElementException:
        with allure.step("Элемент не найден на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не найден на экране", path)
    except ElementNotVisibleException:
        with allure.step("Элемент невидим на экране"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент невидим на экране", path)
    except ElementNotSelectableException:
        with allure.step("Элемент не может быть выбран"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не может быть выбран", path)
    except TimeoutException:
        with allure.step("Превышено время ожидания"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Превышено время ожидания", path)
    except StaleElementReferenceException:
        with allure.step("Ссылка на элемент устарела или стала недействительной"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Ссылка на элемент устарела или стала недействительной", path)
    except ElementClickInterceptedException:
        with allure.step("Попытка клика на элемент прервана другим элементом"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Попытка клика на элемент прервана другим элементом", path)
    except ElementNotInteractableException:
        with allure.step("Элемент не доступен для взаимодействия"):
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Элемент не доступен для взаимодействия", path)

    if sleep is True:
        time.sleep(5)
    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.implicitly_wait(5)


def click_by_ac(driver, id, activity, scrn=None):
    driver.implicitly_wait(10)
    btn = find_elements_by_accessibility_id(elements.get(id), driver)
    btn.click()
    x = driver.wait_activity(list_activity.get(activity), 10)

    if not x:
        print('not in' + activity)

    time.sleep(5)

    if scrn is True:
        driver.save_screenshot(directory + activity + F_EXT)

    driver.implicitly_wait(10)


def screenshot(driver, sleep=None):
    if sleep is True:
        time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def swipe(driver, sleep=None, scrn=None):
    driver.swipe(100, 600, 100, 1400)

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def back(driver, sleep=None, scrn=None):
    driver.back()

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


def confirm_allert(driver, sleep=None, scrn=None):
    driver.switch_to_alert().accept()

    if sleep is True:
        time.sleep(5)

    if scrn is True:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
