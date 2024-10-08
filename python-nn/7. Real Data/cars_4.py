inputs = [0.2, 1.0, 1.4, 1.6, 2.0, 2.2, 2.7, 2.8, 3.2,
    3.3, 3.5, 3.7, 4.0, 4.4, 5.0, 5.2]
targets = [230, 555, 815, 860, 1140, 1085, 1200, 1330, 1290,
    870, 1545, 1480, 1750, 1845, 1790, 1955]

w = 0.1
b = 0.3
epochs = 400
learning_rate = 0.05

def predict(i):
    return w * i + b

# train the network
for epoch in range(epochs):
    preds = [predict(i) for i in inputs]
    cost = sum([(p - t) ** 2 for p, t in zip(preds, targets)])/len(targets)
    print(f"w:{w:.2f}, b:{b:.2f}, c:{cost:.2f}")

    errors_d = [2 * (p - t) for p, t in zip(preds, targets)]
    weigth_d = [e * i for e, i in zip(errors_d, inputs)]
    bias_d = [e * 1 for e in errors_d]

    w -= learning_rate * sum(weigth_d) / len(weigth_d)
    b -= learning_rate * sum(bias_d) / len(bias_d)

# Notice that the cost is not nearing zero.
# But what does that tell us?
# Nothing really. More interesting is to see how the cost evolves.
# At the end, you see that the cost does not change much.
# That means that the network cannot improve much, even if we traiin it more.
# So why don't we take the weight and bias and plot a regresssion line to see how we are doing?
