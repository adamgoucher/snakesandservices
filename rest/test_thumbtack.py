import py
import pytest
import requests
from bs4 import BeautifulSoup

key = "994124a9812d7a63972e89fc2145b9bc"
secret = "d8761d47cb245888"

url = "http://api.flickr.com/services/rest/"

class TestPhotoSearch(object):
    def setup_method(self, method):
        self.payload = {
            # required for everything
            "method": "flickr.photos.search",
            # required for this method
            "api_key": key
        }
        
    def test_thumbtack(self):
        self.payload["text"] = "thumbtack" 
        print(self.payload)
        r = requests.get(url, params=self.payload)
        print(r)
        print(r.text)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, features="xml")
            if soup.rsp['stat'] == 'ok':
                assert(soup.photos["total"] > 0)
            else:
                pytest.fail(msg = 'Did not get OK from Flickr')
        else:
            pytest.fail(msg = 'Did not get OK from server')

    @py.test.mark.yesterday
    def test_thumbtack_from_yesterday(self):
        self.payload["text"] = "cat"
        self.payload["min_upload_date"] = "2012-04-23 00:00:01"
        # print(self.payload)
        r = requests.get(url, params=self.payload)
        # print(r)
        # print(r.text)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, features="xml")
            if soup.rsp['stat'] == 'ok':
                assert(soup.photos["total"] > 0)
            else:
                pytest.fail(msg = 'Did not get OK from Flickr')
        else:
            pytest.fail(msg = 'Did not get OK from server')