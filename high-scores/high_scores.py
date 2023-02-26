#class HighScores:
    #def __init__(self, scores):
        #pass

#In the test, it is given self.assertEqual(HighScores(scores).scores, expected), self.assertEqual(HighScores(scores).latest(), expected), self.assertEqual(HighScores(scores).personal_best(), expected),self.assertEqual(HighScores(scores).personal_top_three(), expected)
#HighScores is the class. So HighScores(scores).scores means that scores is an class instance
#In HighScores(scores).latest()/ HighScores(scores).personal_best()/ HighScores(scores).personal_top_three(), brackets indicate that latest, personal_best and personal_top_three are instance methods
#So the class HighScores has a class instance 'scores' and instance methods latest, personal_best and personal_top_three

class HighScores:
    
    def __init__(self, scores):
        self.scores=scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[0:3]