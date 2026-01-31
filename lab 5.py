import json
from pathlib import Path

config_path = Path("config.json")
results_path = Path("results.json")

# Create config.json if it does not exist
if not config_path.exists():
    default_config = {
        "epochs": 10,
        "learning_rate": 0.001,
        "batch_size": 32,
        "model": "simple_nn"
    }
    with config_path.open("w", encoding="utf-8") as f:
        json.dump(default_config, f, indent=2)

# Load training config
with config_path.open("r", encoding="utf-8") as f:
    config = json.load(f)

# Print config values
print("Training Config:")
for k, v in config.items():
    print(k, ":", v)

# Simulate training results
results = {
    "epochs": config["epochs"],
    "learning_rate": config["learning_rate"],
    "final_loss": 0.12,
    "accuracy": 0.94
}

# Save results safely
with results_path.open("w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)
