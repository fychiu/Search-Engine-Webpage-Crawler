# Search-Engine-Webpage-Crawler
The project is to search a query and then crawl the URL retrieved.

I tried a couple of ways to retrieve the URL of queries results.

1. Python Module: google

    Here is the website: http://pythonhosted.org/google/
    
    Installation: pip install google
    
    Apart from the way 2.,this is probable the easiest way to use.
    
    My setting is "pause = 4.0", which means query every 4 seconds.
    
    Even though, the delay I deemed long enough, the consequence was my IP was blocked.
    
    So, use this way carefully.
    
2. Google Search API: Custome Search Engine (CSE)

    You can set the service here: https://cse.google.com/cse/all
    
    There are lots of tutorial on the Web. Google it!
    
    The only thing is aquiring keys: Developer Key and API Key (aka cx)
    
    See more detail about cse: https://developers.google.com/custom-search/json-api/v1/reference/cse/list
    
    
    This way is what I spent most of time on.
    
    However, the limit usage of CSE API made me extremely upset.
    
    The limit is 100 per day, quite few for crawling a large amount of data.
    
    So far, I have tried various ways to utilize Google Search API.
    
    The outcomes all directed to CSE. I realized that Google wants to gain profit by it.
    
    Now, Google Search is a product.
    
    
3. Bing API

    Register in this websit: https://datamarket.azure.com/dataset/bing/search
    
    Get API key in this website: https://datamarket.azure.com/account/keys
    
    
    Then you can use my code directly without any installation.
    
    The code is from: https://xyang.me/using-bing-search-api-in-python/
    
    So, there is no installation as well.
    
    Although it does not provide lots of functions like Google CSE, it can satisfy the 
    
    need to crawl a large amount of data from the search results.
    
To sum up, way 1. and 3. are applicable to normal developer.

To avoid being blocked, we can set a random sleep time with random.uniform(X,Y).

For example, I set X = 3.0, Y = 10.0 with way 1. Then, this time I survived longer but finally got blocked....

It proved that Google do not allow webpage crawler again.

Hope you use them successfully!
