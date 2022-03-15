"""
https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
"""

def minion_game(string):

    k = sum(len(string)-i for i in range(len(string)) if string[i] in 'AEIOU')
    s = int(len(string)*(len(string) + 1) / 2 - k)

    if k == s:print('Draw')
    else:print(f'Kevin {k}' if k>s else f'Stuart {s}')


if __name__ == '__main__':
    minion_game("BANANA")
