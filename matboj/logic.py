from collections import defaultdict

from .models import Competition, Match, Person


INITIAL_SCORE = 1000


def new_score(score, other_score, result):
    diff = (other_score - score) / 4.0
    diff += result*100
    diff += abs(0.1*diff)
    return int(score + diff)


def final_score(person_scores):
    mini = float("inf")
    sumi = 0
    for c in person_scores:
        mini = int(min(mini, person_scores[c]))
        sumi += person_scores[c]
    return (sumi-mini)//2


def calculate_scores():
    res = defaultdict(lambda: defaultdict(lambda: INITIAL_SCORE))
    for m in Match.objects.order_by('time'):
        sw = res[m.winner][m.competition.name]
        sl = res[m.loser][m.competition.name]
        res[m.winner][m.competition.name] = new_score(sw, sl, +1)
        res[m.loser][m.competition.name] = new_score(sl, sw, -1)
    for c in Competition.objects.all():
        for p in Person.objects.all():
            res[p][c.name]
    return res


def calculate_table():
    scores = calculate_scores()
    for p in scores:
        scores[p].update({
            'name': p.name,
            'total': final_score(scores[p]),
        })
    table = [scores[p] for p in scores]
    table = sorted(table, key=(lambda x: x['total']), reverse=True)
    return table
