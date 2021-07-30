"""
A lib to test the few HTTPBin request and response services
"""

import requests
from requests import HTTPError


class HTTPBinService:
    """This class representing all details needed to perform CRUD"""
    def __init__(self):
        self._base_url = 'http://httpbin.org/'

    def test_get_http_req_base64(self, encoded_text):
        """
        GET request on http base64 bin encoder API
        :param encoded_text: encoded input binary data
        :return: decoded readable text
        """
        url = self._base_url + '/base64/' + encoded_text
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPError(f' Failed to decode encoded text:  {encoded_text}')
        return response.text

    def test_get_http_cookies(self, name, value):
        """
        GET the http cookies API response
        :param name:
        :param value: integer value to be passed
        :return: json response
        """
        url = self._base_url + '/cookies/set/' + name + '/' + str(value)
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPError(f' Failed to retrieve the cookies list for:  {name,value}')
        return response.json()


    def test_post_http_deleyed_respose(self, delay):
        """
        POST the value for the delay in response
        :param delay: delay response time in seconds
        :return: elapsed time including execution time and delay
        """
        url = self._base_url + '/delay/' + str(delay)
        response = requests.post(url)
        if response.status_code != 200:
            raise HTTPError(f' Post response failed for delay ' + delay)
        return response.elapsed.total_seconds()

    def test_put_http_deleyed_respose(self, delay):
        """
        PUT(MODIFY) the value for the delay in response
        :param delay: delay response time in seconds
        :return: elapsed time including execution time and delay
        """
        url = self._base_url + '/delay/' + str(delay)
        response = requests.put(url)
        if response.status_code != 200:
            raise HTTPError(f' Post response failed for delay ' + delay)
        return response.elapsed.total_seconds()


    def test_post_http_anything(self):
        """
        POST request on http anything
        :return: json response
        """
        url = self._base_url + '/anything'
        payload = {
            "company": "Irdeto",
            "job": "Automation"
        }
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            raise HTTPError(f' Post http payload failed  ')
        return response.json()

    def test_delete_http_anything(self):
        """
        DELETE the resource from the server for http anything
        :return: 200 status code with with no content
        """
        url = self._base_url + '/anything'
        response = requests.delete(url)
        if response.status_code != 200:
            raise HTTPError(f' Delete response failed ')
        return response.status_code
