#coding=utf8
from googleapiclient.discovery import build
import sys
reload(sys)
sys.setdefaultencoding('utf8')

__author__ = 'fychiu'
my_api_key = 'YOUR DEVELOPER KEY'
my_cse_key = 'YOUR CSE KEY (cx)'

def search(q, api_key, cse_key, **kwargs):
    service = build('customsearch', 'v1', developerKey=api_key)
    res = service.cse().list(q=q, cx=cse_key, **kwargs).execute()
    return res

'''
# Example:

# By experiments, the sort attribute is ineffective....
# More attributes: https://developers.google.com/custom-search/json-api/v1/reference/cse/list

res = search(q='Google API', my_api_key, my_cse_key, sort='sort by date')

for item in res['items']:
    print item['link']
'''
