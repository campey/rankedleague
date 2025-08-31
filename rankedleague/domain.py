class Team:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
    
    def __repr__(self):
        return f"Team({self.name})"
    

class Result:
    def __init__(self, team1: Team, score1: int, team2: Team, score2: int):
        self.team1 = team1
        self.score1 = score1
        self.team2 = team2
        self.score2 = score2

    def __repr__(self):
        return f"Result({self.team1} {self.score1}, {self.team2} {self.score2})"
    
    def winner(self):
        if self.score1 > self.score2:
            return self.team1
        elif self.score2 > self.score1:
            return self.team2
        else:
            return None