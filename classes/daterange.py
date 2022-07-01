import datetime as dt


class Daterange:

    def __init__(self, start, end=dt.datetime.now(), resolution=1):
        if start > end:
            start, end = end, start
        self.start = start
        self.end = end
        self.resolution = resolution
        if resolution < 1:
            raise ValueError("resolution can't be negative or null")

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        max_index = (self.end - self.start).total_seconds()

        if self.index >= max_index:
            raise StopIteration

        date = self.start + dt.timedelta(seconds=self.index)
        self.index += self.resolution
        return date

    def __contains__(self, other):
        return self.start <= other < self.end

    def __repr__(self):
        second = 'second'
        if self.resolution > 1:
            second = 'seconds'
        return f"Daterange({self.start}, {self.end}, {self.resolution} {second})"

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end and self.resolution == other.resolution

    def to_list(self):
        return [date for date in self]

    def split(self, interval=1, new_resolution=1):
        interval = dt.timedelta(seconds=interval)
        dateranges = [Daterange(date, date + interval, new_resolution) for date in
                      Daterange(self.start, self.end, self.resolution) if date != self.end]
        return dateranges
