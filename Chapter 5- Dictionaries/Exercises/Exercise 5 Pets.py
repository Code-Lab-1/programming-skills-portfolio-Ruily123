pets = []
Ice = {"name of animal": "Ice", "kind of animal": "cat", "owner": "Railey", "age": "7", "size": "medium-sized"}
pets.append(Ice)

Terry = {"name of animal": "Terry", "kind of animal": "dog", "owner": "Dyan", "age": "2", "size": "medium-sized"}
pets.append(Terry)

Bunbun = {"name of animal": "Bunbun", "kind of animal": "bunny", "owner": "Nami", "age": "5", "size": "small-sized"}
pets.append(Bunbun)

Hammy = {"name of animal": "Hammy", "kind of animal": "hamster", "owner": "Rami", "age": "4", "size": "small-sized"}
pets.append(Hammy)

for pet in pets:
    print("\n" + pet["name of animal"], "is a", pet["kind of animal"], "owned by", pet["owner"] + ".",
    pet["name of animal"], "is", pet["age"], "years old", "and is a", pet["size"], pet["kind of animal"] + ".")