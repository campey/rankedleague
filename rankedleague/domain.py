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
        if score1 < 0 or score2 < 0:
            raise ValueError("Scores must be non-negative") 
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
        
    def loser(self): #todo: refactor to remove duplication with winner()
        if self.score1 < self.score2:
            return self.team1
        elif self.score2 < self.score1:
            return self.team2
        else:
            return None
    
    def league_points(self):
        winner = self.winner()
        if winner:
            return (LeaguePoints(winner, 3), LeaguePoints(self.loser(), 0))
        else:
            return (LeaguePoints(self.team1, 1), LeaguePoints(self.team2, 1))
            

        
class LeaguePoints:
    def __init__(self, Team: Team, points: int):
        self.team = Team
        self.points = points
    
    def __eq__(self, value):
        if not isinstance(value, LeaguePoints):
            return False
        return self.team == value.team and self.points == value.points
    