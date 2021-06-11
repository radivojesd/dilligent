from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Dilligent(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # testing search bar, entering desired word and searching items via "ENTER" key

    def test_searchBar(self):
        driver = self.driver
        driver.get("https://www.etsy.com/")
        time.sleep(10)
        search_bar = driver.find_element_by_id("global-enhancements-search-query")
        search_bar.click()
        time.sleep(5)
        search_bar.send_keys("shoes")
        time.sleep(3)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(5)


    # testing filters and checkbutton free shipping

    def test_checkButton(self):
        driver = self.driver
        driver.get("https://www.etsy.com/")
        time.sleep(10)
        driver.find_element_by_xpath("//img[@src='https://i.etsystatic.com/17095327/r/il/879610/2016510847/il_300x300.2016510847_kn0j.jpg']").click()
        time.sleep(5)
        driver.get(driver.current_url)
        time.sleep(3)
        driver.refresh
        time.sleep(5)
        driver.find_element_by_xpath("//span[contains(.,'All Filters')]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//label[@for='special-offers-free-shipping'][contains(.,'FREE shipping')]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[contains(@aria-label,'Apply')]").click()
        time.sleep(5)

    # testing log in option, now sometimes when i open the site and click sign in,
    # requires only email but sometimes requires email and password

    def test_LogIn(self):
        driver = self.driver
        driver.get("https://www.etsy.com/")
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(.,'Sign in')]").click()
        time.sleep(5)
        email = driver.find_element_by_id("join_neu_email_field")
        time.sleep(3)
        email.send_keys("r.mihajlovicc@gmail.com")
        time.sleep(3)
        driver.find_element_by_name("submit_attempt").click()
        time.sleep(3)
        password = driver.find_element_by_id("join_neu_password_field")
        time.sleep(3)
        password.send_keys("12345")
        time.sleep(3)
        driver.find_element_by_name("submit_attempt").click()
        time.sleep(5)


    # testing browsing throung top nav categories and drop down menus

    def test_categories(self):
        driver = self.driver
        driver.get("https://www.etsy.com/")
        time.sleep(10)
        action = ActionChains(driver)
        home_living = driver.find_element_by_id("catnav-primary-link-891")
        action.move_to_element(home_living).perform()
        time.sleep(5)
        pet_supplies = driver.find_element_by_xpath("//span[@id='side-nav-category-link-4440']")
        action.move_to_element(pet_supplies).perform()
        time.sleep(5)
        toys = driver.find_element_by_partial_link_text("Entert")
        action.move_to_element(toys).perform()
        time.sleep(5)


    def test_register(self):
        driver = self.driver
        driver.get("https://www.etsy.com/")
        time.sleep(10)
        action = ActionChains(driver)
        driver.find_element_by_xpath("//button[contains(.,'Sign in')]").click()
        email = driver.find_element_by_id("join_neu_email_field")
        time.sleep(3)
        email.send_keys("raleparkour@gmail.com")
        time.sleep(5)
        driver.find_element_by_name("submit_attempt").click()
        time.sleep(5)
        first_name = driver.find_element_by_id("join_neu_first_name_field")
        time.sleep(5)
        first_name.send_keys("Marko")
        time.sleep(5)
        password = driver.find_element_by_id("join_neu_password_field")
        time.sleep(5)
        password.send_keys("03071995senscw")
        time.sleep(5)
        driver.find_element_by_name("submit_attempt").click()
        time.sleep(5)









    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
