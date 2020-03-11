from progress.bar import ChargingBar


class ProgressBar:
    def __init__(self, level):
        self.bar = ChargingBar('Processing', max=100)
        self.level = level

    def up(self, item: int):
        if self.level > 20:
            self.bar.next(item)

    def finish(self):
        self.bar.finish()
