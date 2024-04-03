# import csv

# with open ("favorites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     scratch, c, python = 0, 0, 0
#     # next(row)
#     for row in reader:
#         favorite = row["language"]
#         if favorite == "Scratch":
#             scratch += 1
#         elif favorite == "C":
#             c += 1
#         elif favorite == "Python":
#             python += 1

# print(f"Scratch: {scratch}")
# print(f"C: {c}")
# print(f"Python: {python}") 

# import csv

# with open ("favorites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     counts = {}
#     for row in reader:
#         favorite = row["language"]
#         if favorite in counts:
#             counts[favorite] += 1
#         else:
#             counts[favorite] = 1

# for favorite in counts:
#     print(f"{favorite}: {counts[favorite]}")


# import csv

# with open ("favorites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     counts = {}
#     for row in reader:
#         favorite = row["language"]
#         if favorite in counts:
#             counts[favorite] += 1
#         else:
#             counts[favorite] = 1

# def get_value(language):
#     return counts[language]

# for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
#     print(f"{favorite}: {counts[favorite]}")

# import csv

# with open ("favorites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     counts = {}
#     for row in reader:
#         favorite = row["problem"]
#         if favorite in counts:
#             counts[favorite] += 1
#         else:
#             counts[favorite] = 1

# def get_value(language):
#     return counts[language]

# for favorite in sorted(counts, key=lambda problem: counts[problem], reverse=True):
#     print(f"{favorite}: {counts[favorite]}")

import csv

with open ("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["problem"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

def get_value(language):
    return counts[language]

favorite = input("favorite: ")
if favorite in counts:
    print(f"{favorite}: {counts[favorite]}")


