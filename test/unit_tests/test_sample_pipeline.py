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
""" Unit tests for sample_pipeline.py """

import pytest
import os
import sys
import pandas as pd

cur_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/../../src")

from sample_pipeline import iris_pipeline

def test_iris_pipeline():
    """ Test the iris_pipeline function """

    actual_result = iris_pipeline()

    expected_result = pd.Series({"species": {"setosa": 50, "versicolor": 50, "virginica": 50}})

    assert actual_result.any() == expected_result.any()
