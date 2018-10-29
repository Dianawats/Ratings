class Scores:
    def __init__(self):
        self.scores = []

    def all_scores(self):
        for score in self.scores:
            return score

    # def return_one_score(self, username):
    #     my_score = [score for score in self.scores if user['username'] == username]