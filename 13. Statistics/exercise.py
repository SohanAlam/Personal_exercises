x, n = 0.0, 0

for number_of_steps in data.steps:
    x += number_of_steps

n = len(data.steps)

mean = x / n
mean