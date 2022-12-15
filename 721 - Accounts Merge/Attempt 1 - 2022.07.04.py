class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        https://leetcode.com/problems/accounts-merge/

        Given a list of accounts where each element accounts[i] is a list of strings, where the first element
        accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

        Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is
        some common email to both accounts. Note that even if two accounts have the same name, they may belong to
        different people as people could have the same name. A person can have any number of accounts initially,
        but all of their accounts definitely have the same name.

        After merging the accounts, return the accounts in the following format: the first element of each account is
        the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in
        any order.


        Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com",
        "john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
        Output: [["John",
        "john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John",
        "johnnybravo@mail.com"]]
        Explanation: The first and second John's are the same person as they have the common
        email "johnsmith@mail.com". The third John and Mary are different people as none of their email addresses are
        used by other accounts. We could return these lists in any order, for example the answer [['Mary',
        'mary@mail.com'], ['John', 'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com',
        'johnsmith@mail.com']] would still be accepted. Example 2:

        Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co",
        "Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co",
        "Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
        Output: [["Ethan","Ethan0@m.co",
        "Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co",
        "Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co",
        "Fern1@m.co","Fern5@m.co"]]

        Constraints:

        1 <= accounts.length <= 1000
        2 <= accounts[i].length <= 10
        1 <= accounts[i][j].length <= 30
        accounts[i][0] consists of English letters.
        accounts[i][j] (for j > 0) is a valid email.

        Plan:

        1. Make a merge_two_func helper function, which will take two lists with the same name, and return the merged
        combination.
        2. Create a detect_duplicate_user helper function, which will take two lists with the same name,
        and if a duplicate email is detected, returns True. Otherwise, returns False.
        3. Construct a dictionary which will contain a list of lists that holds all the accounts of people with the
        same name.
        4. Loop through all the keys and call detect_duplicate_user. If duplicates are found, then call the
        merge_two_func helper function, and then repeat the detect_duplicate_user until there are no remaining
        accounts to be merged.
        5. Sort and return the final list of merged accounts.
        6. Time: O(n^2), Space: O(n)
        '''

        names = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                names[email] = name

        comps, seen, ans, i = defaultdict(list), set(), [], 0

        def dfs(node, i):
            comps[i].append(node)
            seen.add(node)
            for neib in graph[node]:
                if neib not in seen: dfs(neib, i)

        for email in graph:
            if email not in seen:
                dfs(email, i)
                i += 1

        return [[names[val[0]]] + sorted(val) for _, val in comps.items()]

        # 1: Create an array which will track visited accounts (initialized to False).
        # 2: Create a dictionary (keys: email address, values: group indexes where that email is found) that will
        # contain the locations of all unique emails.
        # 3: Create an array which will return the final answer.
        # 4: Loop through accounts, extract the individual email addresses, and fill up the dictionary.
        # 5: Traverse...
        #
        # from collections import defaultdict
        # visited_accounts = [False] * len(accounts)
        # emails_accounts_map = defaultdict(list)
        # res = []
        # # Build up the graph.
        # for i, account in enumerate(accounts):
        #     for j in range(1, len(account)):
        #         email = account[j]
        #         emails_accounts_map[email].append(i)
        #
        # # DFS code for traversing accounts.
        # def dfs(i, emails):
        #     if visited_accounts[i]:
        #         return
        #     visited_accounts[i] = True
        #     for j in range(1, len(accounts[i])):
        #         email = accounts[i][j]
        #         emails.add(email)
        #         for neighbor in emails_accounts_map[email]:
        #             dfs(neighbor, emails)
        #
        # # Perform DFS for accounts and add to results.
        # for i, account in enumerate(accounts):
        #     if visited_accounts[i]:
        #         continue
        #     name, emails = account[0], set()
        #     dfs(i, emails)
        #     res.append([name] + sorted(emails))
        # return res