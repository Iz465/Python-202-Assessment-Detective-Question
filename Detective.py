Room = {
 "Ball": 0.5,
 "Dining": 0.9,
 "Kitchen": 0.1,
 "Master Bedroom": 0.3,
 "Bathroom": 0.3
}
Tool = {
  "Dagger": 0.4,
  "Revolver": 0.7,
  "Lead Pipe": 0.1,
  "Hammer": 0.8
}
Situation = {
  "Situation 1. Name: John": Room["Bathroom"] + Tool["Lead Pipe"],
  "Situation 2. Name: Cathy": Room["Dining"] + Tool["Revolver"],
  "Situation 3. Name: Cathy": Room["Dining"] + Tool["Dagger"],
  "Situation 4. Name: Samuel": Room["Master Bedroom"] + Tool["Revolver"],
  "Situation 5. Name: John": Room["Kitchen"] + Tool["Dagger"],
  "Situation 6. Name: Cathy": Room["Master Bedroom"] + Tool["Hammer"] 
}


Situation_List = sorted(Situation.items(),key = lambda index: index[1],reverse=True) # Sorted adds the dictionary into a list and sorts it from highest value to lowest.
# The items() command lets the list values be shown. the key function lets you choose what you want to base the sorting on. I am choosing it to be based on index 1, which is the value of each situation.


print("\nBelow are the scenarios from most likely to least likely to have commited the murder.\n")
for specificSituation, value in Situation_List:
  print(f"{specificSituation}. Value: {value}")
print()  