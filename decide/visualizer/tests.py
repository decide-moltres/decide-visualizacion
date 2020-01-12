from django.test import TestCase

# Create your tests here.

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()


class TestDarkMode(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_darkmode_fire(self):
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('switch-mode-dark').click()

    def tearDown(self):
        self.driver.quit


class TestLightMode(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_lightmode_fire(self):
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('switch-mode-dark').click()
        self.driver.find_element_by_id('switch-mode-light').click()

    def tearDown(self):
        self.driver.quit

class TestExportPDF(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('save').click()

    def tearDown(self):
        self.driver.quit

class TestExportPNG1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('graf1').click()

    def tearDown(self):
        self.driver.quit

class TestExportPNG2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('graf2').click()

    def tearDown(self):
        self.driver.quit

class TestContactUs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_contactUs_fire(self):
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('contact').click()

    def tearDown(self):
        self.driver.quit

class TestBackContactUs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_backContactUs_fire(self):
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('contact').click()
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/visualizer/contactUs/")
        self.driver.find_element_by_id('back').click()

    def tearDown(self):
        self.driver.quit

class TestSendEmail(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_sendEmail_fire(self):
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("visualizacion")
        self.driver.find_element_by_id('id_password').send_keys("visualizacion")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('contact').click()
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/visualizer/contactUs/")
        self.driver.find_element_by_id('correoEz').click()

    def tearDown(self):
        self.driver.quit
        
class TestLanguge(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_language_fire(self):
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/admin/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("practica")
        self.driver.find_element_by_id('id_password').send_keys("practica")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_xpath('//button[normalize-space()="Export this votation to PDF"]')
        select = Select(self.driver.find_element_by_id('language'))
        select.select_by_value('es')
        self.driver.find_element_by_id('go').click()
        self.driver.find_element_by_xpath('//button[normalize-space()="Exportar esta votación a PDF"]')

class TestExcel(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_excel_fire(self):
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("practica")
        self.driver.find_element_by_id('id_password').send_keys("practica")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("http://https://decide-moltres-visualizacion.herokuapp.com/visualizer/4/")
        self.driver.find_element_by_id('excel').click()








