"""
Unit tests for the measure module.
"""

import bootcamp2023
import numpy as np
import pytest


@pytest.mark.slow
def test_calculate_distance():

    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])
    
    expected_distance = 1.0

    calculated_distance = bootcamp2023.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

