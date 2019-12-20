import requests
from bs4 import *
import logging
import json

class FetchNews():

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        

    def make_request(self):
        
        logging.info(' Making HTTP Request to Indiatimes.com > Briefs Section')
        resp = requests.get('https://timesofindia.indiatimes.com/briefs')
        if(resp.status_code==200):
            logging.info(' Request sucessful with status code {}'.format(resp.status_code))
            self.parse(resp)
        else:
            logging.info( 'Request unsucessful')
            

    def parse(self,resp):

        soup = BeautifulSoup(resp.text, 'lxml')
        briefs = soup.findAll('div',{'class':'brief_box'})
        logging.info(' {} Briefs found.'.format(len(briefs)))
        sections = set([i.text.replace('/n','') for i in soup.findAll('span',{'class':'subsection_card'})])
        logging.info(' {} Sections Found.'.format(len(sections)))
        news_feed = {k:[] for k in sections}
        for brief in briefs:
            
            brief_sec = brief.find('span',{'class':'subsection_card'})
            if(brief_sec):
                feed = dict()
                feed['Title'] = brief.find('img').get('alt')
                feed['Link'] = 'https://timesofindia.indiatimes.com' + brief.find('a').get('href')
                feed['Content'] = brief.find('p').text
                feed['Image URL'] = brief.find('img').get('onerror').replace('this.src=','').replace("'","").replace(';','')
                    
                
                news_feed[brief_sec.text].append(feed)
        
        news_feed = json.dumps(news_feed,indent = 4,ensure_ascii = False)
        
        with open('news_feed.json', 'w') as f:
            json.dump(news_feed,f)
        
        
        
if __name__=='__main__':

    obj = FetchNews()
    obj.make_request()
        
              
