class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}

        def add_domain_count(domain, count):
            count = int(count)
            if domain in dic:
                dic[domain] += count
            else:
                dic[domain] = count

        for domains in cpdomains:
            count, domain = domains.split(' ')
            sub = domain.split('.')
            for i in range(len(sub)):
                add_domain_count('.'.join(sub[i:]), count)

        res = []
        for k, v in dic.items():
            res.append(f'{v} {k}')
        return res
