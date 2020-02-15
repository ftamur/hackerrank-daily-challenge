if __name__ == '__main__':

    score_name = dict()
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())

        scores.add(score);

        if score in score_name.keys():
            score_name[score].append(name)
        else:
            score_name[score] = [name]

    for name in sorted(score_name[sorted(list(set(scores)))[1]]):
        print(name)
 
