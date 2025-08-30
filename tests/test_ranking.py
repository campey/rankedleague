from rankedleague.rankedleague.domain import Team

def test_team_init():
    team = Team("Lions")
    assert team.name == "Lions"
    assert repr(team) == "Team(Lions)"

def test_team_equality():
    team1 = Team("Lions")
    team2 = Team("Lions")
    team3 = Team("Grouches")
    
    assert team1 == team2
    assert team1 != team3
    assert team1 != "NotATeam"

def test_team_hash():
    team1 = Team("Lions")
    team2 = Team("Lions")
    team3 = Team("Grouches")
    
    team_set = {team1, team3}
    assert team2 in team_set
    assert len(team_set) == 2

