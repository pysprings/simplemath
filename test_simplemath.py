# -*- coding: utf-8 -*-
# Copyright 2016 Tim Flink, Richard Doell
# License: Apache 2.0 <https://spdx.org/licenses/Apache-2.0>
# See the LICENSE file for more details on Licensing

import unittest

import simplemath

class TestSimpleMath(unittest.TestCase):

    def test_increment(self):
        test_simplemath = simplemath.SimpleMath(0)
        test_simplemath.increment()

        self.assertEqual(test_simplemath.total, 1)


if __name__ == '__main__':
    unittest.main()
