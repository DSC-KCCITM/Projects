class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)


class Movie_MP4(Video):
    type = "MP4"

def addRecommendation(gender):
    if gender=='Male':
        movie = Movie_MP4(r"C:\Users\Jitender kumar\Desktop\Intel HackFury2\Video\1.mp4")
        movie.play()

    else:
        movie = Movie_MP4(r"C:\Users\Jitender kumar\Desktop\Intel HackFury2\Video\2.mp4")
        movie.play()