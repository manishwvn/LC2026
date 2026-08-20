# Last updated: 8/20/2026, 2:04:49 AM
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        host = startUrl.split("/")[2]
        
        queue = deque()
        queue.append(startUrl)
        visited = set()
        
        while queue:
            url = queue.popleft()
            if url in visited: continue
                
            visited.add(url)
            sites = htmlParser.getUrls(url)
            
            for site in sites:
                if site.split("/")[2] == host:
                    queue.append(site)
                    
        return list(visited)
        

        