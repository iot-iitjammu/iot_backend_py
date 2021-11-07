class Periods:
    DailyGroup   = "daily"
    WeeklyGroup  = "weekly"
    MonthlyGroup = "monthly"
    YearlyGroup  = "yearly"

    @classmethod
    def get_all_periods(cls):
        return [Periods.DailyGroup, Periods.WeeklyGroup, Periods.MonthlyGroup, Periods.YearlyGroup]