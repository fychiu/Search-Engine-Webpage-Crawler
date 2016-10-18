#coding=utf8

# The file is copied from https://xyang.me/using-bing-search-api-in-python/

import urllib
import requests
from requests.auth import HTTPBasicAuth

# Bing API key
API_KEY = "YOUR API KEY"

def bing_api(query, source_type = "Web", top = 10, format = 'json'):
    """Returns the decoded json response content

    :param query: query for search
    :param source_type: type for seacrh result
    :param top: number of search result
    :param format: format of search result
    """
    # set search url
    query = '%27' + urllib.quote(query) + '%27'
    # web result only base url
    base_url = 'https://api.datamarket.azure.com/Bing/SearchWeb/' + source_type
    url = base_url + '?Query=' + query + '&$top=' + str(top) + '&$format=' + format

    # create credential for authentication
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
    # create auth object
    auth = HTTPBasicAuth(API_KEY, API_KEY)
    # set headers
    headers = {'User-Agent': user_agent}

    # get response from search url
    response_data = requests.get(url, headers=headers, auth = auth)
    # decode json response content
    json_result = response_data.json()

    return json_result

'''
# Example:

res = bing_api(q='Bing API')['d']['results']

for re in res:
    print re[“Description”], re[“Title”], re[“Url”], re[“__metadata”], re[“DisplayUrl”], re[“ID”]

'''
