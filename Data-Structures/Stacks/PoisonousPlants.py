class Plant:
    def __init__(self, pesticide, days):
        self.pesticide = pesticide
        self.days = days
        
# Complete the poisonousPlants function below.
def poisonousPlants(plant):
    stack = []
    maxDaysAlive = 0
    for pesticide in plant:
        daysAlive = 0
        while stack and pesticide <= stack[-1].pesticide:
            daysAlive = max(daysAlive, stack.pop().days)
             
        if not stack:
            daysAlive = 0
        else:
            daysAlive += 1
             
        maxDaysAlive = max(maxDaysAlive, daysAlive)
         
        stack.append(Plant(pesticide, daysAlive))
     
    print(maxDaysAlive)
    return maxDaysAlive
