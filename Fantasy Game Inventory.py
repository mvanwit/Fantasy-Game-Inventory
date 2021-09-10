#Fantasy Game Inventory.py

exampleInv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
emptyInv = {}

def displayInventory(someInv):
    print('Inventory:')

    totalItems = 0
    for k, v in someInv.items():

        print(str(v) + ' ' + k)
        totalItems += v

    print('Total number of items: ' + str(totalItems))

displayInventory(exampleInv)


## List to Dictionary Function - Dragon Loot !
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(someInv, someLoot):

    for item in someLoot:
        if item in someInv.keys():
            someInv[item] += 1 #Increment quantity if item already exist in inv
        else: 
            someInv.setdefault(item, 1) #Create item in inv if doesnt already exist

    print('Updated ', end='')
    displayInventory(someInv)
