import random
import string
from difflib import SequenceMatcher
import matplotlib.pyplot as plt


goal = "charles darwin was always seasick"
length_of_goal = len(goal)
simulations = 10  # Number of simulations to run
generations_needed = []

def get_random_string(length):
    letters = string.ascii_lowercase + " "
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

for simulation in range(simulations):
    generation = 0
    default_str = get_random_string(length_of_goal)
    similarity = int(SequenceMatcher(None, default_str, goal).ratio() * 100)
    while similarity < 100:
        temp_str = default_str
        new_letter = random.choice(string.ascii_lowercase + " ")
        random_index = random.randint(0, len(default_str) - 1)
        temp_str = default_str[:random_index] + new_letter + default_str[random_index + 1:]
        new_sim = int(SequenceMatcher(None, temp_str, goal).ratio() * 100)

        if new_sim > similarity:
            default_str = temp_str
            similarity = new_sim
            generation += 1
            print("#"+str(generation)+" "+str(similarity) + "%"+" "+default_str)

            
    generations_needed.append(generation)

    
    
# Plotting results
plt.figure(figsize=(10, 5))
plt.hist(generations_needed, bins=30, color='blue', alpha=0.7)
plt.title('Distribution of Generations Needed')
plt.xlabel('Generations Needed')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

average_generations = sum(generations_needed) / len(generations_needed)
print(f"Average generations needed: {average_generations:.2f}")