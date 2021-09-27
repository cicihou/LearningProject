class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for email in emails:
            email, domain = email.split('@')
            email = email.split('+')[0]
            email = ''.join(email.split('.'))
            res.append('@'.join([email, domain]))
        return len(set(res))
