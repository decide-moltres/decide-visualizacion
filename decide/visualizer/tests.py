from django.test import TestCase

# Create your tests here.

import unittest
from selenium import webdriver

class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_signup_fire(self):
        self.driver.get("http://127.0.0.1:8000/admin/login/?next=/admin/")
        self.driver.find_element_by_id('id_username').send_keys("practica")
        self.driver.find_element_by_id('id_password').send_keys("practica")
        self.driver.find_element_by_id('login-form').click()
        self.driver.get("http://127.0.0.1:8000/visualizer/3/")

    def tearDown(self):
        self.driver.quit

if __name__ == '__main__':
    unittest.main()
