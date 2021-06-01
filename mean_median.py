# M0_C5 - Mean, Median

def mean(scores):
    scores_valid = []
    for score in scores:    
        if score >= 0 and score <= 100:
            scores_valid.append(score)
    tests = len(scores_valid)
    total = sum(scores_valid)
    if len(scores_valid) == 0:
        return -1
    else:
        return int(total/tests)

def median(scores):
    scores_valid = []
    for score in scores:    
        if score >= 0 and score <= 100:
            scores_valid.append(score)
    tests = len(scores_valid)
    if len(scores_valid) == 0:
        return -1
    else:
        if tests % 2 == 0:
            return int((scores_valid[tests//2-1] + scores_valid[tests//2])/2)
        else:
            return int(scores_valid[tests//2])

if __name__ == '__main__':
    scores = input("Input list of test scores, space-separated: ")
    scores_list = [int(i) for i in scores.split()]

    mean = mean(scores_list)
    median = median(scores_list)

    print(f"Mean: {mean}")
    print(f"Median: {median}")
