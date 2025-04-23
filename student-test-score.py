import numpy as np

scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])


print("Avg per student:", scores.mean(axis=1))


print("Avg per subject:", scores.mean(axis=0))

print("Top student index:", scores.sum(axis=1).argmax())

scores[:, 2] += 5
print("Updated scores:\n", scores)
