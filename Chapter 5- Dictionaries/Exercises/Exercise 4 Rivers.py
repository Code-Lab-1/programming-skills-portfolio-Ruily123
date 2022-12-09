major_rivers = {"Yangtze": "China", "Ganges": "India", "Yenisei": "Russia"}

for rivers, country in major_rivers.items():
    print("The " + rivers + " River runs through " + country + ".")

print("\nThe major rivers included in the dictionary are:")
for mrivers in major_rivers.keys():
    print(mrivers)

print("\nThe countries included in the dictionary are:")
for country in major_rivers.values():
    print(country)