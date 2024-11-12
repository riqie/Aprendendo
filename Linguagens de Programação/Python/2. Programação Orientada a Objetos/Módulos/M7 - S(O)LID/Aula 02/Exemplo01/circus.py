class Circus:
    def show(self, type):
        if type == 1:
            self.showJuggler()
        if type == 2:
            self.showClown()
        
    def showJuggler(self):
        print('Juggler presenting his show.')

    def showClown(self):
        print('Clown presenting his show.')
