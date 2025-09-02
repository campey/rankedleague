from typing import List

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

    def loser(self):  # todo: refactor to remove duplication with winner()
        if self.score1 < self.score2:
            return self.team1
        elif self.score2 < self.score1:
            return self.team2
        else:
            return None


class ResultsFile:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.results = self._read_results()

    def __iter__(self):
        return self.results.__iter__()

    def _read_results(self) -> List[Result]:
        results = []
        with open(self.filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    team1_part, team2_part = line.split(',')
                    if not team1_part or not team2_part:
                        raise ValueError(f"Invalid line: {line}")
                    team1_name, score1_str = team1_part.rsplit(' ', 1)
                    if not team1_name or not score1_str:
                        raise ValueError(f"Invalid line: {line}")
                    team2_name, score2_str = team2_part.rsplit(' ', 1)
                    if not team2_name or not score2_str:
                        raise ValueError(f"Invalid line: {line}")
                    try:
                        score1 = int(score1_str.strip())
                        score2 = int(score2_str.strip())
                    except ValueError:
                        raise ValueError(f"Invalid score: {score1_str} or {score2_str}")
                    team1 = Team(team1_name.strip())
                    team2 = Team(team2_name.strip())
                    result = Result(team1, score1, team2, score2)
                    results.append(result)
        return results


class LeaguePoints:
    def __init__(self, team: Team, points: int):
        self.team = team
        self.points = points

    def __eq__(self, value):
        if not isinstance(value, LeaguePoints):
            return False
        return self.team == value.team and self.points == value.points

    def calculate_for_result(result: Result) -> tuple['LeaguePoints', 'LeaguePoints']:
        winner = result.winner()
        if winner:
            return (LeaguePoints(winner, 3), LeaguePoints(result.loser(), 0))
        else:
            return (LeaguePoints(result.team1, 1), LeaguePoints(result.team2, 1))


class LeagueTable:
    def __init__(self):
        self.standings: List[LeaguePoints] = []

    def points_for_team(self, team: Team) -> LeaguePoints | None:
        for lp in self.standings:
            if lp.team == team:
                return lp
        return None

    def update_with_result(self, result: Result):
        league_points = LeaguePoints.calculate_for_result(result)
        for lp in league_points:
            existing = self.points_for_team(lp.team)
            if existing:
                existing.points += lp.points
            else:
                self.standings.append(lp)
        self.standings.sort(key=lambda lp: (-lp.points, lp.team.name))  # Sort by points desc, then name asc

    def write_to_file(league_table: 'LeagueTable', filepath: str):
        with open(filepath, 'w') as file:
            for idx, lp in enumerate(league_table.standings):
                point_unit = "pt" if lp.points == 1 else "pts"
                file.write(f"{idx + 1}. {lp.team.name}, {lp.points} {point_unit}\n")

