def get_country_city(country, city, population=None):
    if population:
        res = f"{city},{country} - population {population}"
    else:
        res = f"{city},{country}"

    return res
