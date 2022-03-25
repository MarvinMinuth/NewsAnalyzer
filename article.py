from datetime import date


class Article:
    def __init__(self, title, year, month, day, medium):
        self.title = title
        self.medium = medium
        self.date = date(year, month, day)

