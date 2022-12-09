people = []

person = {'first_name': 'Railey', 'last_name': 'Inductivo', 'age': '17', 'city': 'Dubai'}
people.append(person)

person2 = {'first_name': 'Dyan', 'last_name': 'Inductivo', 'age': '15', 'city': 'Dubai'}
people.append(person2)

person3 = {'first_name': 'Rami', 'last_name': 'Soriano', 'age': '6', 'city': 'Sharjah'}
people.append(person3)

for person in people:
    print(person["first_name"],person["last_name"], "is", person["age"], "years old and lives in", person["city"] + ".")