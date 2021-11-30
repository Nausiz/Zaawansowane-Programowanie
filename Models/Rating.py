class Rating:
    def __init__(self, userid: str, movieid: str, rating: int, timestamp: int):
        self.userid = userid
        self.movieid = movieid
        self.rating = rating
        self.timestamp = timestamp
