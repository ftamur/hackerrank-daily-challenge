def minion_game(string):
    # your code goes here

    score_kevin = 0
    score_stuart = 0
    string_len = len(string)

    for i in range(len(s)):
        if s[i] in "AEIOU":
            score_kevin += string_len - i
        else:
            score_stuart += string_len - i
            
    if score_stuart > score_kevin: print("Stuart", score_stuart)
    elif score_stuart < score_kevin: print("Kevin", score_kevin)
    else: print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)