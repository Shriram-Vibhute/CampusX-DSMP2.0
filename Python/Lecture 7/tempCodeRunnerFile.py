dt = {'c': [3], 'b': [12, 10], 'a': [19, 4]}

# Sorting keys
dt_keys = sorted(dt.keys())
new_dt = {key: dt[key] for key in dt_keys}

# sorting values
for key, value in new_dt.items():
    # Sorting Values
    new_dt[key].sort()

print(new_dt)