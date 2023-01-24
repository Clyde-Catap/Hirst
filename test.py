
resources = {
    "water": -300,
    "milk": 200,
    "coffee": 100,
}

for g in resources:
    print(resources[f"{g}"])
    if resources["water"] <= 0:
        print("dddd")

for g in resources:
    if resources[g] <= 0:
        print("not enough resources")