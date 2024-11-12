from artist import Artist

class Circus:
    def presentShow(self, artist: Artist):
        print('The show is starting!')
        artist.present()
        print('The audicence is applauding!')
