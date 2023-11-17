pets = {
    'Ice': {
        'Name': 'Ice',
        'Kind': 'Cat',
        'Owner': 'Railey',
        'Age': '7',
        'Size': 'Medium-sized'
    },
    'Terry': {
        'Name': 'Terry',
        'Kind': 'Dog',
        'Owner': 'Dyan',
        'Age': '2',
        'Size': 'Small-sized'
    },
    'Octonami': {
        'Name': 'Octonami',
        'Kind': 'Octopus',
        'Owner': 'Nami',
        'Age': '4',
        'Size': 'Large-sized'
    }

    }
for pet, pet_info in pets.items():
    print("\nPet: " + pet)
    name = pet_info['Name']
    kind = pet_info['Kind']
    owner = pet_info['Owner']
    age = pet_info['Age']
    size = pet_info['Size']
    print("\tName: " + name)
    print("\tKind: " + kind)
    print("\tOwner: " + owner)
    print("\tAge: " + age)
    print("\tSize: " + size)