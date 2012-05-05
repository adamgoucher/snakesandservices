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
        
    @pytest.mark.parametrize("term", [
        ("snail",),
        ("turtle",),
        ("urchin",),
    ])
    def test_driven_photos(self, term):
        self.payload["text"] = term

        r = requests.get(url, params=self.payload)
        if r.status_code == requests.codes.ok:
            soup = BeautifulSoup(r.text, features="xml")
            if soup.rsp['stat'] == 'ok':
                assert(soup.photos["total"] > 0)
            else:
                pytest.fail(msg = 'Did not get OK from Flickr')
        else:
            pytest.fail(msg = 'Did not get OK from server')