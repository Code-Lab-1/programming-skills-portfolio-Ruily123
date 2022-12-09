def city_country(city, country):
    full_name = "\"" + city + ", " + country + "\""
    return full_name

pair = city_country('Manila', 'Philippines')
print(pair)
pair = city_country('New Delhi', 'India')
print(pair)
pair = city_country('Dubai', 'UAE')
print(pair)
