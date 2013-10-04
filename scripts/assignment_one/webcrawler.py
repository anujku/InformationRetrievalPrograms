# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:42:53 2013
 
@author: anuj
"""
 
import urlparse
import urllib2
from time import sleep
import time
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup
from reppy.cache import RobotsCache

# Webcrawler.py class is used for crawling urls starting 
# with a single seed. 
# It uses these libraries : 
# 1. Beautifulsoup : to parse the html content
# 2. reppy : to parse robot.txt file
# 3. urllib2 : to request the contents of a url
# 4. urlparse : to parse the url
# 5. time : to find the time for crawl

class webcrawler:
    
    # set the url, limit, sleeptime and agent for crawler
    def __init__(self, url, limit, sleeptime, agent):
        self.url = url
        self.limit = limit
        self.sleeptime = sleeptime
        self.agent = agent
     
    
    # remove duplicates from the list if any
    def remove_duplicates(self, l):
        return list(set(l))
          
    # crawl the url with the seed      
    def crawl(self): 
        
        # to maintain a list of urls to be craw   
        urls = [self.url] 
        
        # to maintain a list of visited urls
        visited = [self.url] 
        
        # initialize the RobotCache from reppy
        robots = RobotsCache()
        robots_url = urljoin(self.url, '/robots.txt')
        
        # fetch robot url for the instance of RobotCache
        r = robots.fetch(robots_url)
        
        # loop until visited urls < limit 
        while len(urls) > 0 and len(visited) < self.limit:
            try:
                # use opener from urllib2 to request webpages 
                opener = urllib2.build_opener()
                
                # add agent to as a header to the opener
                opener.addheaders = [{'User-agent', self.agent}]
                urllib2.install_opener(opener)
                
                # get the html for the url
                htmltext = urllib2.urlopen(urls[0]).read()
        
            except:
                # print url causing exception
                print urls[0]
            soup = BeautifulSoup(htmltext)
             
            # pop out the url fetched 
            urls.pop(0)
           
            # find all anchor tags from the html page 
            for tag in soup.findAll('a', href=True):
                
                # parse the anchor tag to fetch url from it
                tag['href'] = urlparse.urljoin(self.url , tag['href'])                
                newurl = tag['href'];
                
                # check if the url obtained is not a visited list
                if self.url in newurl and newurl not in visited:
                    urls.append(newurl)
                    
                    # if visited urls > limit break the loop
                    if(len(visited) >= self.limit):
                        break
                    # if the url is allowed for the agent by the robot 
                    # parser then add the url in visited urls list 
                    elif(r.allowed(newurl, self.agent)):
                        visited = self.remove_duplicates(visited)
                        visited.append(newurl)    
 
            # sleep for the given sleep time before making next request            
            sleep(self.sleeptime) 
        
        # return the list of visited urls    
        return visited
    
    
if __name__ == '__main__':
    # seed website for crawl
    seed = 'http://www.ccs.neu.edu'
    # limit the links to find
    limit = 100
    # wait between each request to the url
    sleeptime = 5     
    # agent for requesting connection
    agent = 'htdig'
    # initialize the crawler with seed, limit, sleeptime and agent
    crawler = webcrawler(seed, limit, sleeptime, agent)
    # note the start time to start crawl 
    start_time = time.time()
    # find the crawled urls using crawl()
    urls = crawler.crawl()
    # print the time to crawl the urls
    print  time.time() - start_time, " seconds to crawl " + seed
    # print the urls found
    for url in urls:
        print url    
        
