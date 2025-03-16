class DateUSA:
    def __init__(
        self,
        day: int,
        month: int,
        year: int
    ):
        self.day = day
        self.month = month
        self.year = year

    def format(self):
        return f"{self.month:02}/{self.day:02}/{self.year:04}"
    def isoformat(self):
        return f"{self.year:04}-{self.month:02}-{self.day:02}"

class DateEurope:
    def __init__(
        self,
        day: int,
        month: int,
        year: int
    ):
        self.day = day
        self.month = month
        self.year = year

    def format(self):
        return f"{self.day:02}/{self.month:02}/{self.year:04}"

    def isoformat(self):
        return f"{self.year:04}-{self.month:02}-{self.day:02}"
