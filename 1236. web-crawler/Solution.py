# https://leetcode.com/problems/web-crawler

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

    def getHostName(self, url):
        return url.split('/')[2]

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = self.getHostName(startUrl)
        res = set([startUrl])
        stack = set([startUrl])

        while(stack):
            currentUrl = stack.pop()
            newUrls = [i for i in htmlParser.getUrls(currentUrl) if i not in res and (self.getHostName(i) == hostname)]
            res.update(newUrls)
            stack.update(newUrls)
            

        return res