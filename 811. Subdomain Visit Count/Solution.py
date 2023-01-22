# https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for i in cpdomains:
            rep, domain = i.split()
            rep = int(rep)
            domain = domain.split('.')
            for j in range(len(domain)):
                subdomain = '.'.join(domain[j:])
                d[subdomain] += rep
        for x, i in d.items():
            yield f'{i} {x}'