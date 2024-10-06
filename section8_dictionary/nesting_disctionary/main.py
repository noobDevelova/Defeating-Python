starting_dictionary = {
    "a": 9,
    "b": 8,
    "c": [1,2,3,4,5,6],
    "d": {
        1: 2,
        3: 4
    },
    "f": [
        {
            "name": 'Randi'
        }
    ]
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

print(starting_dictionary["f"][0]['name'])