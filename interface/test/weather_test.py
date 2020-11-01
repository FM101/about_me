# -*- coding: UTF-8 -*-
#import allure

from unittest import TestCase
from library.httpclient import HttpClient


#@allure.feature('Test Weather api')
class Weather(TestCase):
    """Weather api test cases"""
    
    def setUp(self):
#        super(self).setUp()
        self.host = 'http://www.weather.com.cn'
        self.ep_path = '/data/cityinfo'
        self.client = HttpClient()
        
#    @allure.story('Test of shenzhen')
    def test_1(self):
        city_code = '101280601'
        exp_city = "18:00"
        self._test(city_code, exp_city)

    def test_2(self):
        city_code = '101010100'
        exp_city = "18:00"
        self._test(city_code, exp_city)

    def _test(self, city_code, exp_city):
        url = self.host + self.ep_path + '/' + city_code + '.html'
        print(url)
        response = self.client.get(url=url)
        print(response.content)
        act_city = response.json()['weatherinfo']['ptime']
        print(act_city)
        #print('Expect city = %s, while actual city = %s' % (exp_city, act_city))
#        self.assertEqual(exp_city, act_city, 'Expect city = {exp_city}, while actual city = {act_city}')
        self.assertEqual(exp_city, act_city)