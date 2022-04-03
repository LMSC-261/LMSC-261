areaCodes = {"Boston": 617, "New York": 212}
# Delete an element with the key "New York"
del areaCodes["New York"]
print(areaCodes)
# Delete all elements in the dictionary
areaCodes.clear()
print(areaCodes)
areaCodes["Boston"] = 617
#Check if an element exist in dicionary
if "Boston" in areaCodes:
  # Delete an element with the key "Boston"
  del areaCodes["Boston"]
print(areaCodes)