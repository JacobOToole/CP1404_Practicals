"""
CP1404 - Jacob O'Toole
Score Menu
"""


def main():
    score = get_valid_score()
    result = calculate_result(score)
    print(result)
    print('*' * score)


def calculate_result(score):
    if score < 0 or score > 100:
        result = 'Invalid score'
    elif score >= 90:
        result = 'Excellent'
    elif score >= 50:
        result = 'Passable'
    else:
        result = 'Bad'
    return result


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score (0-100)")
        score = int(input("Score: "))
    else:
        return score


main()