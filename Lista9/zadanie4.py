import numpy as np
import matplotlib.pyplot as plt

langs = ["Python", "C", "C++", "Java", "C#", "Visual Basic", "JS", "SQL", "Assembly", "PHP"]
rank = [16.36, 16.26, 12.91, 12.21, 5.73, 4.64, 2.87, 2.50, 1.60, 1.39]

y_pos = np.arange(len(langs))

plt.bar(y_pos, rank, align="center", alpha=0.5)
plt.xticks(y_pos, langs)
plt.xlabel("Języki")
plt.ylabel("Popularność(%)")
plt.title("Popularność różnych języków programowania.")

plt.show()