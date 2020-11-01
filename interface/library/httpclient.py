# -*- coding: UTF-8 -*-
import requests
import urllib3


class HttpClient:
    """Generic Http Client class"""
    
    def __init__(self, disable_ssl_vertify=False, timeout=60):
        """Initialize nethod"""
        
        self.client = requests.session()
        self.disable_ssl_vertify = disable_ssl_vertify
        self.timeout = timeout
        if self.disable_ssl_vertify:
            urllib3.disable_warnings(urlib3.exceptions.InsecrueRequestWarning)

    def get(self, url, headers=None, json=None, params=None, *args, **kwargs):
        """Http Get method"""    
        
        if headers is None:
            headers = {}
            
        if self.disable_ssl_vertify:
            response = self.client.get(url,headers=headers, data=data, json=json, params=params, 
                                       vertify=False, timeout=self.timeout, *args, **kwargs)
        else:
            response = self.client.get(url,headers=headers, json=json, params=params,
                                       timeout=self.timeout, *args, **kwargs) 
        
        response.encoding = 'utf-8'
        print('{response.json()}')

        return response        