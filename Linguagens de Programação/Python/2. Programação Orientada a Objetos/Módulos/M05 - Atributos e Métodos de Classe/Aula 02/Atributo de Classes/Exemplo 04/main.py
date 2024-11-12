from store import Store

store1 = Store('Caragua Beach')
store2 = Store('Ubatuba Beach')

store1.showAddress()
store2.showAddress()

print(store1.sell())
print(store2.sell())

store1.setTax(3.4)

print(store1.sell())

