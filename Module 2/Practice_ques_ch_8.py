years_list = [year for year in range(2006, 2006 + 6)]
print(years_list)

print(f"Age 3 in year: {years_list[3]}")

print(f"Oldest in year: {years_list[len(years_list)-1]}")



surprise = ["Groucho", "Chico", "Harpo"]
surprise[2] = surprise[2].lower()
print(surprise)

surprise[2] = surprise[2][::-1]
print(surprise)

surprise[2] = surprise[2].capitalize()
print(surprise)
