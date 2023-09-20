#!/usr/bin/python3
"""This module contains unit tests for the functions and classes defined in the
Review model
"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Defines tests for Review Class"""

    def __init__(self, *args, **kwargs):
        """Initializes the test class """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Defines tests for place_id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Defines tests for user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Defines tests for text"""
        new = self.value()
        self.assertEqual(type(new.text), str)
