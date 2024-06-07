'''
648 Replace Words
Medium
In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.
'''

'''
直接匹配就是了，在nlp中还是有点用，我直接匹配，居然击败了44%的人的时间复杂度...我还想哈希一下呢...
'''

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dictionary.sort()
        res = []
        for item in sentence.split(' '):
            flag = False
            for word in dictionary:
               if word == item[:len(word)]:
                    res.append(word)
                    flag = True
                    break  
            if not flag:
                res.append(item)
        return ' '.join(res)        