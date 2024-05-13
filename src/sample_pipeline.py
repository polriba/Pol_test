# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
""" Sample Iris Pipeline """
import seaborn as sns
import pandas as pd


def iris_pipeline():
    """ Loads the Iris dataset """
    iris = sns.load_dataset('iris')

    # Transform the data to pandas DataFrame
    data = pd.DataFrame(iris)
    
    # Return the count of different species in the dataset
    print(data["species"].value_counts())
    return (data["species"].value_counts())


if __name__ == '__main__':
    iris_pipeline()
# -


