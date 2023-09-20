#!/usr/bin/python3
"""This module contains unit tests for the functions and classes defined in the
state model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Defines tests for state class"""

    def __init__(self, *args, **kwargs):
        """Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """Defines tests for name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
