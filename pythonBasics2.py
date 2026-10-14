capitals = ["Montgomery", "Juneau", "Phoenix"]
capitals.append("Sacramento")
capitals.insert(3, "LittleRock")
capitals.remove("Juneau")
population = [200000, 32000, 1600000]
capitals[2] = "Little Rock"
capitals.sort(reverse=True)
print(capitals.pop())
print(capitals)
print(min(population))
print(len(capitals))
