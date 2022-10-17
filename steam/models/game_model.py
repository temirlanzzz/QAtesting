class GameModel:
    def __init__(self):
        pass

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPlatforms(self, platforms):
        self.platforms = platforms

    def setReleaseDate(self, release_date):
        self.release_date = release_date

    def setReviewResult(self, review_result):
        self.review_result = review_result

    def setPrice(self, price):
        self.price = price

    def __eq__(self, other):
        if isinstance(other, GameModel):
            return self.price == other.price and self.platforms == other.platforms and self.release_date == other.release_date and self.review_result == other.review_result and self.price == other.price