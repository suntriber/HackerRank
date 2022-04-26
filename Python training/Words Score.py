"""
https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=true
"""

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score+=1
    return score


if __name__ == "__main__":
    print(f'4 --> {score_words("hacker book".split(" "))}')
    print(f'4 --> {score_words("programming is awesome".split(" "))}')