import random
import matplotlib.pyplot as plt

meta = [2, 3, 3] + [4] * 3 + [5] * 4 + [6] * 5 + [7] * 6 + [8] * 5 + [9] * 4 + [10, 10, 10, 11, 11, 12]

prob = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

for _ in range(50):
	prob[random.choice(meta)] += 1


plt.bar(range(len(prob)), prob.values(), align='center')
plt.xticks(range(len(prob)), prob.keys())

plt.show()