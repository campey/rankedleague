from rankedleague.rankedleague.domain import Team, Result

def test_team_init():
    team = Team("Lions")
    assert team.name == "Lions"
    assert repr(team) == "Team(Lions)"

def test_team_equality():
    team1 = Team("Lions")
    team2 = Team("Lions")    
    assert team1 == team2
    
def test_team_inequality():
    team1 = Team("Lions")   
    team3 = Team("Grouches")
    assert team1 != team3

def test_team_not_equals_string():
    team1 = Team("Lions")
    assert team1 != "NotATeam"

def test_team_hash():
    team1 = Team("Lions")
    team2 = Team("Lions")
    team3 = Team("Grouches")
    team_set = {team1, team3}
    assert team2 in team_set
    assert len(team_set) == 2

def test_result_constructor():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    result = Result(team1, 3, team2, 1)
    assert repr(result) == "Result(Team(Lions) 3, Team(Grouches) 1)"

def test_result_home_winner():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    result = Result(team1, 3, team2, 1)
    assert result.winner() == team1

def test_result_away_winner():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    result = Result(team1, 1, team2, 4)
    assert result.winner() == team2

def test_result_draw():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    result = Result(team1, 2, team2, 2)
    assert result.winner() is None 

