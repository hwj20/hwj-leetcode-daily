'''
1255. Maximum Score Words Formed by Letters
Hard
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
'''


'''
直接枚举word的话，复杂度在2^14 = 8k，感觉能过；
把单词转换成25维的向量
'''


class Solution(object):


    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        from collections import defaultdict,Counter
        
        def has_negative_values(counter):
        # 遍历 Counter 中的所有值，检查是否存在负数
            for value in counter.values():
                if value < 0:
                    return True
            return False
        def number_to_letter(number):
            # 检查输入是否在0到25的范围内
            if 0 <= number <= 25:
                # 将数字转换为相应的字母
                return chr(number + 97)
            else:
                raise ValueError("输入的数字必须在0到25之间")
        def letters_to_numbers(char):
            # 创建一个字典，将字母映射到数字
            letter_to_number = {
                'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
            }
            return letter_to_number[char]

        def subtract_counters(counter1, counter2):
            # 先进行减法运算，这不会保留负值
            result = counter1 - counter2

            # 手动处理负值
            for key in counter2:
                if key in counter1:
                    result[key] = counter1[key] - counter2[key]
                else:
                    result[key] = -counter2[key]

            return result

        word_counts = []
        for word in words:
            word_counts.append(Counter(word))
        # print(word_counts)
        ans = [0]
        # scores = defaultdict(list)
        storage = Counter()
        for i in range(len(letters)):
            # scores[letters[i]].append(score[i])
            storage[letters[i]] += 1

        # for key in scores:
        #     scores[key].sort(key=lambda x:-x)

        # print(storage)
        def dfs(now,now_count):
            if now == len(words):
                now_ans = 0
                used = storage-now_count
                # print('-'*10)
                # print(used)
                for k in used:
                    if used[k] > 0:
                        # print(k)
                        now_ans += score[letters_to_numbers(k)]*used[k]
                        # print(score[k])
                ans[0] = max(ans[0],now_ans)
                return
            # print(now_count,words[now])
            n_count = subtract_counters(now_count, word_counts[now])
            # print(n_count)
            if not has_negative_values(n_count):
                dfs(now+1,n_count)
            dfs(now+1,now_count)
        dfs(0,copy.deepcopy(storage))
        return ans[0]

            