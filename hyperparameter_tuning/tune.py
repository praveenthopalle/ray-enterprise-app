from ray import tune

def objective(config):
    x = config["learning_rate"]
    return {"score": -(x ** 2) + 4 * x}

if __name__ == "__main__":
    analysis = tune.run(
        objective,
        config={"learning_rate": tune.grid_search([0.01, 0.1, 0.2, 0.5])}
    )
    print("Best Hyperparameters:", analysis.best_config)
