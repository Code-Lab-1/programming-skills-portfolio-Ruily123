cities = {
    'Dubai': {
        'Country': 'UAE',
        'Population': '3.3 million',
        'Fact': 'The tallest building in the world is located here.',
    },
    'Manila': {
        'Country': 'Philippines',
        'Population': '21.3 million',
        'Fact': 'Manila is known for its blend of fascinating colonial history.',
    },
    'New Delhi': {
        'Country': 'India',
        'Population': '32 million',
        'Fact': 'New Delhi is the location of India\'s national government.'
    }

    }
for city, city_info in cities.items():
    print("\nCity: " + city)
    country = city_info['Country']
    population = city_info['Population']
    fact = city_info['Fact']
    print("\tCountry: " + country)
    print("\tPopulation: " + population)
    print("\tFact: " + fact)
