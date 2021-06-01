# from collections import defaultdict
from english_words import english_words_set
mapper = {'2': 'a', '22': 'b', '222': 'c', '3': 'd', '33': 'e', '333': 'f', '4': 'g', '44': 'h', '444': 'i', '5': 'j', '55': 'k', '555': 'l', '6': 'm',
          '66': 'n', '666': 'o', '7': 'p', '77': 'q', '777': 'r', '7777': 's', '8': 't', '88': 'u', '888': 'v', '9': 'w', '99': 'x', '999': 'y', '9999': 'z', '0': ' '}


def generateAllSentences(start: int, end: int, nums: str, lst: list):
    if(start == end):
        return list(set(lst))
    for i in range(len(lst)):
        tmp = lst[i]
        if(start >= 2 and nums[start-1] == nums[start] and nums[start-2] == nums[start]):
            if(tmp[-1] == mapper[nums[start-1]+nums[start]]):
                lst += [tmp[:-1]+mapper[nums[start-2]+nums[start-1]+nums[start]]]
            if(tmp[-1] == mapper[nums[start]] and tmp[-2] == mapper[nums[start]]):
                lst += [tmp[:-2]+mapper[nums[start-2]+nums[start-1]+nums[start]]]
        if(start >= 1 and nums[start] == nums[start-1]):
            if(tmp[-1] == mapper[nums[start]]):
                lst += [tmp[:-1]+mapper[nums[start-1]+nums[start]]]
        lst[i] += mapper[nums[start]]
    generateAllSentences(start+1, end, nums, lst)


def numberToSentence(nums: str):
    start = 0
    end = len(nums)
    lst = ['']
    generateAllSentences(start, end, nums, lst)
    possibleSents = list(set(lst))
    d = dict()
    maxscore = 0
    for s in possibleSents:
        score = 0
        for w in s.split():
            if(w in english_words_set):
                score += 1
        try:
            d[score].append(s)
        except KeyError:
            d.update({score: [s]})
        if(score > maxscore):
            maxscore = score

    print(d[maxscore])
    print("max score is ", maxscore)


numberToSentence(str(input('enter a number pad format: ')))
