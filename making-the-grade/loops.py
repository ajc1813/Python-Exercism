"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    r_scores = []
    while student_scores:
        r_scores.append(round(student_scores.pop()))
    return r_scores
        
def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    c=0
    for scor in student_scores:
        if scor<=40:
            c+=1
    return c

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    t_scores=[]
    for scor in student_scores:
        if scor>=threshold:
            t_scores.append(scor)
    return t_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    l_scores=[]
    r=round((highest-40)/4)
    for scor in range(41,highest,r):
        if scor in range(41,40+r):
            l_scores.append(41)
        elif scor in range(41+r,40+(2*r)):
            l_scores.append(41+r)
        elif scor in range(41+(2*r),40+(3*r)):
            l_scores.append(41+(2*r))
        else:
            l_scores.append(41+(3*r))
    return l_scores


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    l=[]
    for index,scor in enumerate(student_scores):
        name=student_names[index]
        l.append(f"{index+1}. {name}: {scor}")
    return l
            


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    p_score=[]
    for info in student_info:
        if info[1]==100:
            p_score=info
            break
    return p_score
