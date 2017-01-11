# -*- coding: utf-8 -*-
# Copyright 2016 Tim Flink, Richard Doell
# License: Apache 2.0 <https://spdx.org/licenses/Apache-2.0>
# See the LICENSE file for more details on Licensing


class SimpleMath(object):
    """SimpleMath is pretty much an implementation of an integer for the
    purpose of learning how to use git and contribute to an existing project

    :ivar int total: the internal value of the SimpleMath "integer"
    """

    def __init__(self, start_value=0):
        """Create a SimpleMath object

        :param int start_value:  the value to initialize our object to
        :throws ValueError: if start_value is not an integer
        """

        self.total = 1

    def increment(self):
        """ increment the total by 1"""
        pass
