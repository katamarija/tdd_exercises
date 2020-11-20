class VacationPlanner:

    BUDGET_CATEGORIES = ["lodging", "transportation", "food"]

    def __init__(self, departing=None, arriving=None, budget_limit=0):
        self.departing = departing
        self.arriving = arriving
        self.budget_limit = budget_limit

        self.budget = {}
        self._update_budget()

    @property
    def arriving_city(self):
        return self.arriving and self.arriving.split(",")[0]

    @property
    def arriving_state(self):
        return self.arriving and self.arriving.split(",")[1].strip()

    @property
    def departing_city(self):
        return self.departing and self.departing.split(",")[0]

    @property
    def departing_state(self):
        return self.departing and self.departing.split(",")[1].strip()

    def _update_budget(self):
        portion = self.budget_limit / 3

        for category in self.BUDGET_CATEGORIES:
            self.budget[category] = portion
