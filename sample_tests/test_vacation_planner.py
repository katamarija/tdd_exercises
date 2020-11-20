from vacation import VacationPlanner

def test_vacation_planner_can_be_configured():
    planner = VacationPlanner(departing="Detroit, MI", arriving="Lincoln, NE")

    assert planner.departing_city == "Detroit"
    assert planner.departing_state == "MI"
    assert planner.arriving_city == "Lincoln"
    assert planner.arriving_state == "NE"

def test_vacation_has_not_exceeded_budget():
    planner = VacationPlanner(budget_limit = 600)

    assert planner.budget["lodging"] == 200
    assert planner.budget["transportation"] == 200
    assert planner.budget["food"] == 200
