import numpy as np
import pandas as pd
import sklearn
import wandb

def dummy_function():
    """A simple function to test the workflow."""
    data = np.array([1, 2, 3, 4, 5])
    df = pd.DataFrame({'Values': data})
    print("Dummy DataFrame:")
    print(df)
    print("Scikit-learn version:", sklearn.__version__)
    print("Weights & Biases version:", wandb.__version__)

if __name__ == "__main__":
    dummy_function()