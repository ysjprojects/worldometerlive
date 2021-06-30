import json

DATA = None

with open("livedata.json") as f:
    DATA = json.load(f)


def get_fields():
    return list(DATA.keys())

def get_categories():
    return ['world_population', 'government_and_economics', 'society_and_media', 'environment', 'food', 'water', 'energy', 'health']

def get_world_population():
    params = ['Current World Population',
            'Births this year',
            'Births today',
            'Deaths this year',
            'Deaths today',
            'Net population growth this year',
            'Net population growth today']
    
    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"World Population":result}

def get_government_and_economics():
    params = ['Public Healthcare expenditure today', 
            'Public Education expenditure today', 
            'Public Military expenditure today', 
            'Cars produced this year', 
            'Bicycles produced this year', 
            'Computers produced this year']
    
    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"Government & Economics":result}

def get_society_and_media():
    params = ['New book titles published this year', 
            'Newspapers circulated today', 
            'TV sets sold worldwide today', 
            'Cellular phones sold today', 
            'Money spent on videogames today', 
            'Internet users in the world today', 
            'Emails sent today', 
            'Blog posts written today', 
            'Tweets sent today', 
            'Google searches today']
    
    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"Society & Economics":result}

def get_environment():
    params = ['Forest loss this year (hectares)', 
            'Land lost to soil erosion this year (ha)', 
            'CO2 emissions this year (tons)', 
            'Desertification this year (hectares)', 
            'Toxic chemicals released in the environment this year (tons)']
    
    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"Society & Economics":result}


def get_food():
    params = ['Undernourished people in the world', 
            'Overweight people in the world', 
            'Obese people in the world', 
            'People who died of hunger today', 
            'Money spent for obesity related diseases in the USA today', 
            'Money spent on weight loss programs in the USA today']

    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"Food":result}

def get_water():
    params = ['Water used this year (million L)', 
            'Deaths caused by water related diseases this year', 
            'People with no access to a safe drinking water source']

    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"Water":result}

def get_energy():
    params = ['Energy used today (MWh)', 
            'Energy used today from non-renewable sources (MWh)', 
            'Energy used today from renewable sources (MWh)', 
            'Solar energy striking Earth today (MWh)', 
            'Oil pumped today (barrels)', 'Oil left (barrels)', 
            'Days to the end of oil (~42 years)', 
            'Natural Gas left (boe)', 
            'Days to the end of natural gas', 
            'Coal left (boe)', 
            'Days to the end of coal'] 

    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"Energy":result}

def get_health():
    params = ['Communicable disease deaths this year', 
            'Seasonal flu deaths this year', 
            'Deaths of children under 5 this year', 
            'Abortions this year', 
            'Deaths of mothers during birth this year', 
            'HIV/AIDS infected people', 
            'Deaths caused by HIV/AIDS this year', 
            'Deaths caused by cancer this year', 
            'Deaths caused by malaria this year', 
            'Cigarettes smoked today', 
            'Deaths caused by smoking this year', 
            'Deaths caused by alcohol this year', 
            'Suicides this year', 
            'Money spent on illegal drugs this year', 
            'Road traffic accident fatalities this year']
    
    result = {}
    for param in params:
        if param not in DATA:
            result[param] = "NA"
            continue
        result[param] = DATA[param]

    return {"Health":result}

def get_all():
    return {**get_world_population(), **get_government_and_economics(), **get_society_and_media(), **get_environment(), **get_food(), **get_water(), **get_energy(), **get_health()}





