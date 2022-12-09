favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
for name, language in favorite_languages.items():
 print(name.title() + "'s favorite language is " +
 language.title() + ".")

print(" ")

names = ["railey", "dyan", "jen", "terry", "ice", "phil", "nami", "sarah"]
for name in names:
 if name in favorite_languages.keys():
  print(name.title() + ", thank you for responding the poll.")
 else:
  print(name.title() + ", please respond the poll.")




