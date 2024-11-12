from circus import Circus
from juggler import Juggler
from clown import Clown

myCircus = Circus()
myJuggler = Juggler()
myClown = Clown()

myCircus.present(myJuggler)
myCircus.present(myClown)