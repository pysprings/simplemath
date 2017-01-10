# -*- coding: utf-8 -*-
# Copyright 2016 Tim Flink, Richard Doell
# License: Apache 2.0 <https://spdx.org/licenses/Apache-2.0>
# See the LICENSE file for more details on Licensing

class SimpleMath(object):

    def __init__(self, start_value=0):
        self.total = start_value

    def increment(self):
        self.total += 1
