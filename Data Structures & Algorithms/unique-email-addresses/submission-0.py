class Solution:
    def helper(self, email):
        res = []
        seen = False
        i = 0

        while i < len(email):
            if email[i] == "+":
                while email[i] != "@":
                    i += 1
                seen = True
            if email[i] != ".":
                res.append(email[i])
            if seen and email[i] == ".":
                res.append(email[i])
            i += 1
        print("".join(res))
        return "".join(res)
    def numUniqueEmails(self, emails: List[str]) -> int:
        emails_set = set()

        for email in emails:
            formatted_email = self.helper(email)

            if formatted_email not in emails_set:
                emails_set.add(formatted_email)
        print(emails_set)
        return len(emails_set)

"""
+ = skip everything up until the @ aka where the domain name beings
. = ignore and don't include it in the final email


create a set to store the emails and check to see if they are in the set already


iterate through the array:
    call a helper
    check to see if the email is already in the set
        if not then we add it to the set

return the length of the set
"""
        