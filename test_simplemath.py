# -*- coding: utf-8 -*-
# Copyright 2016 Tim Flink, Richard Doell
# License: Apache 2.0 <https://spdx.org/licenses/Apache-2.0>
# See the LICENSE file for more details on Licensing

import unittest

import simplemath

class TestSimpleMath(unittest.TestCase):

    def test_construct(self):
        """Test to make sure that we can start with any integer value"""
        test_simplemath = simplemath.SimpleMath(0)

        self.assertEqual(test_simplemath.total, 0)

    def test_string_render(self):
        """test to make sure that the string rendering works"""

        test_simplemath = simplemath.SimpleMath(2)

        self.assertEqual(str(test_simplemath), "2")

    def test_construct_integer_only(self):
        """Make sure that a ValueError is thrown if a non-integer parameter is passed as start_value"""
        pass


if __name__ == '__main__':
    unittest.main()
