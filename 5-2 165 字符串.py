'''
165. Compare Version Numbers
Medium

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
'''


'''
用.分一下，然后从左到右比较就是了；想去学有限差分，抄个答案
'''


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        parts1, parts2 = version1.split("."), version2.split(".")
        i, j = len(parts1) - 1, len(parts2) - 1
        while parts1 != [] and int(parts1[i]) == 0:
            parts1.pop()
            i -= 1
        while parts2 != [] and int(parts2[j]) == 0:
            parts2.pop()
            j -= 1
        for i in range(len(min(parts1, parts2))):
            int1, int2 = int(parts1[i]), int(parts2[i])
            # print(int1,int2)
            if int1 > int2:
                return 1
            elif int1 < int2:
                return -1
        if len(parts1) > len(parts2):
            return 1
        elif len(parts2) > len(parts1):
            return -1
        return 0