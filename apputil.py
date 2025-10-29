import pandas as pd

## Exercise 1
"""
Build python class called 'GroupEstimate' taking categorical data and corresponding 
continuous values, and determines which group a new observation falls into, and 
predicts an estimate value based on the data provided.
"""
# Part 1: Define a class 'GroupEstimate' that accepts an 'estimate' argument, which can be either "mean" or "median".

class GroupEstimate(object):
    def __init__(self, estimate):
        if estimate not in ["mean", "median"]:
            raise ValueError("Estimate must be either 'mean' or 'median'")
        self.estimate = estimate
        self.group_data = {}

# Part 2: Add a .fit(X, y) method that takes in a pandas DataFrame of categorical data 'X', and a 1-D array, 'y'. 
    """
    Combine 'X' and 'y' into single pandas DataFrame.
    Grouping all columns in 'X'.
    Compute group-level statistic depending on 'estimate' argument. 
    """
    def fit(self, X, y):
        data = X.copy()
        data['y'] = y
        grouped = data.groupby(list(X.columns))['y']
        if self.estimate == "mean":
            self.group_data = grouped.mean().to_dict()
        else:
            self.group_data = grouped.median().to_dict()

    def predict(self, X_):
        """Predict based on the learned group means/medians."""
        X_ = pd.DataFrame(X_)
        keys = [tuple(row) for row in X_.to_numpy()]
        predictions = [self.group_data.get(k, np.nan) for k in keys]

        missing_count = sum(pd.isna(predictions))
        if missing_count > 0:
            print(f"{missing_count} observation(s) belong to unseen group(s). Returning NaN for those.")

        return predictions

# Part 3: 
