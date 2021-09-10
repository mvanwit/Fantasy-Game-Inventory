#Fantasy Game Inventory.py

exampleInv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(someInv):
    print('Inventory:')

    totalItems = 0
    for k, v in someInv.items():

        print(str(v) + ' ' + k)
        totalItems += v

    print('Total number of items: ' + str(totalItems))

displayInventory(exampleInv)