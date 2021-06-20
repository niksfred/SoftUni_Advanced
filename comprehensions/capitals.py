countries = [x for x in input().split(", ")]
capitals =  [x for x in input().split(", ")]

result = {country: capital for country,capital in zip(countries, capitals)}

for country in result:
    print(f"{country} -> {result[country]}")
