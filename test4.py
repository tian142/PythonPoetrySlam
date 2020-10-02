hats = {
    "snapback": 10,
    "beanie": 5,
    "baseballcap": 3
}

hats.update({"weird top hat": 1})
hats['snapback'] = hats.get("snapback", 0) + 1
del hats['weird top hat']

print(hats)
