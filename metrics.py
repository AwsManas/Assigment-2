def MSE(predictions, labels):
    differences = [(x - y) ** 2 for x, y in zip(predictions, labels)]
    return sum(differences) / len(differences)

  
def MAE(predictions, labels):
    differences = [abs(x - y) for x, y in zip(predictions, labels)]
    return sum(differences) / len(differences)


def RMSE(predictions, labels):
    differences = [(x - y) ** 2 for x, y in zip(predictions, labels)]
    return (sum(differences) ** 0.5) / len(differences)
  