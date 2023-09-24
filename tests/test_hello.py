# (c) 2017-2022 Spiros Papadimitriou <spapadim@gmail.com>
#
# This file is released under the MIT License:
#    https://opensource.org/licenses/MIT
# This software is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied.

from .hwtest.unittest import HomeworkTestCase
from .hwtest import autograde as grade


class HelloTests(HomeworkTestCase):
  @grade.score(100)
  def test(self):
    output = self.runScript("hello.py")
    self.assertEqual('Hello, world!\n', output)

