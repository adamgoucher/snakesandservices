import pytest
from suds.client import Client

import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

application_id = "0E100A06A5C6822E953B7F954C568BA6437FA918"

class TestBingSearch(object):
    def setup_method(self, method):
        self.client = Client('http://api.bing.net/search.wsdl?AppID=%s&Version=2.2' % application_id)
        self.SearchRequest = self.client.factory.create('SearchRequest').parameters
        # print(self.SearchRequest)
        self.SearchRequest["AppId"]= application_id
    
    def test_thumbtack(self):
        self.SearchRequest["Query"] = "thumbtack"
        
        adult = self.client.factory.create('AdultOption')
        adult = "Strict"
        self.SearchRequest["Adult"] = adult
        
        source_types = self.client.factory.create('ArrayOfSourceType')
        source_types.SourceType.append("Web")
        self.SearchRequest["Sources"] = source_types
        # print(self.SearchRequest)
        SearchResponse = self.client.service.Search(self.SearchRequest)
        # print(SearchResponse)
        assert(SearchResponse.Web.Total > 0)