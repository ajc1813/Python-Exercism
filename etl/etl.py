def transform(legacy_data):
    data = {}
    for key,value in legacy_data.items():
        for elt in value:
            elt=elt.lower()
            data.update({elt: key})
    return data
            
