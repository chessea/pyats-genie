# Example
# -------
#
#   two example testcase

# import the aetest module
from pyats import aetest

# define a simple testcase by inheriting aetest.Testcase
# this testcase's uid is defaulted to "SimpleTestcase"
class SimpleTestcase(aetest.Testcase):

    @aetest.test
    def trivial_test(self):
        assert 1 + 1 == 2

# testcases could also have its own setup/cleanups
class SlightlyMoreComplexTestcase(aetest.Testcase):

    # providing this testcase a user-defined uid
    uid = 'id_of_this_testcase'

    @aetest.setup
    def setup(self):
        self.value = 1

    @aetest.test
    def another_trivial_test(self):
        self.value += -1
        assert self.value == 0

    @aetest.cleanup
    def cleanup(self):
        del self.value


if __name__ == '__main__':
    aetest.main()