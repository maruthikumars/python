capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

#Nested list in Dictionary

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"],
}


#Print Lille
print(travel_log["France"][1])

#nested list
nested_list = ['A', 'B', ['C', 'D']]
#print letter 'D'

print(nested_list[2][1])

travel_log = {
    "France" : {
        "title_visited" : ["Paris", "Lille", "Dijon"],
        "num_times_visited" : 12
    },
    "Germany" : {
        "cities_visited": ["Stuttgart", "Berlin"],
        "num_times_visited" : 5
    }
}

#Stuttgart print this

print(travel_log["Germany"]["cities_visited"][0])