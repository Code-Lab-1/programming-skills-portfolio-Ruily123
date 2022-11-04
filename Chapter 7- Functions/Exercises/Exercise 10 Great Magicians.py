def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = "The Great " + magician
        great_magicians.append(great_magician)

    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['Railey', 'Dyan', 'Rami', 'Nami']
show_magicians(magicians)
print(" ")
make_great(magicians)
show_magicians(magicians)

