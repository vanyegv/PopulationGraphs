def get_population():
    keys = ['col','bol']
    values = [300,400]
    return keys, values

def population_by_country(data,country):
    result = list(filter(lambda item: item['Country/Territory'] == country,data))
    return result

def population_by_year(data):
    years = list(lambda key: key[0:3] for key in data[0].keys())
    #result = list(filter(lambda item: item[''.endswith('Population')] == year,data))
    return years