from pessoa import Person
from interruptor import Interruptor

somebody = Person()
kitchenSwitch = Interruptor('kitchen')
roomSwitch = Interruptor('room')

somebody.turningOnTheLight(kitchenSwitch)
somebody.turningOffTheLight(kitchenSwitch)
somebody.turningOffTheLight(roomSwitch)
somebody.sleep()
