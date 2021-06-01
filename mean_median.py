# M0_C5 - Mean, Median
import math

def mean(scores):
    scores_valid = []
    for score in scores:    
        if score >= 0 and score <= 100:
            scores_valid.append(score)
    tests = len(scores_valid)
    test_scores = sum(scores_valid)
    if len(scores_valid) == 0:
        mean = -1
    else:
        mean = math.floor(test_scores/tests)
    return mean

def median(scores):
    scores_valid = []
    for score in scores:    
        if score >= 0 and score <= 100:
            scores_valid.append(score)
    tests = len(scores_valid)
    if len(scores_valid) == 0:
        median = -1
    else:
        if tests % 2 == 0:
            median = math.floor( (scores_valid[int(tests/2-1)] + scores_valid[int(tests/2)])/2 )
        else:
            median = math.floor( scores_valid[math.ceil(tests/2)-1] )
    return median

if __name__ == '__main__':
    scores = input("Input list of test scores, space-separated: ")
    scores_list = [int(i) for i in scores.split()]

    mean = mean(scores_list)
    median = median(scores_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
