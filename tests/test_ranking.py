from rankedleague.rankedleague.domain import Team, Result, LeaguePoints

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
    assert result.loser() is None

def test_result_negative_score():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    try: 
        result = Result(team1, -1, team2, 2)
        assert False, "Expected ValueError for negative score"
    except ValueError as e:
        assert str(e) == "Scores must be non-negative"


def test_league_points_equality():
    team1 = Team("Lions")
    lp1 = LeaguePoints(team1, 3)
    lp2 = LeaguePoints(team1, 3)
    lp3 = LeaguePoints(team1, 0)
    assert lp1 == lp2

def test_league_points_inequality():
    team1 = Team("Lions")   
    lp1 = LeaguePoints(team1, 3)
    lp2 = LeaguePoints(team1, 0)    
    assert lp1 != lp2  

def test_league_points_not_the_same_as_result():
    team1 = Team("Lions")
    lp1 = LeaguePoints(team1, 3)
    team2 = Team("Grouches")
    result = Result(team1, 3, team2, 1)
    assert lp1 != result

def test_result_league_points_home_win():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    result = Result(team1, 3, team2, 1)
    team1_expected_points = LeaguePoints(team1, 3)
    team2_expected_points = LeaguePoints(team2, 0)

    league_points = LeaguePoints.calculate_for_result(result)
    assert team1_expected_points in league_points
    assert team2_expected_points in league_points

def test_result_league_points_away_win():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    result = Result(team1, 1, team2, 4)
    team1_expected_points = LeaguePoints(team1, 0)
    team2_expected_points = LeaguePoints(team2, 3)

    league_points = LeaguePoints.calculate_for_result(result)
    assert team1_expected_points in league_points
    assert team2_expected_points in league_points

def test_result_league_points_draw():
    team1 = Team("Lions")
    team2 = Team("Grouches")
    result = Result(team1, 2, team2, 2)
    team1_expected_points = LeaguePoints(team1, 1)
    team2_expected_points = LeaguePoints(team2, 1)

    league_points = LeaguePoints.calculate_for_result(result)
    assert team1_expected_points in league_points
    assert team2_expected_points in league_points

