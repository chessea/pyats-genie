# Example
# -------
#
#   subsections

from pyats import aetest

# subsections exists within CommonSetup
class ScriptCommonSetup(aetest.CommonSetup):

    # define subsections by applying @subsection decorator
    @aetest.subsection
    def common_setup_subsections(self):
        pass
    @aetest.subsection
    def common_setup_subsections2(self):
        pass

# -------------------------------------------

# subsections exists within CommonCleanup
class ScriptCommonCleanup(aetest.CommonCleanup):

    # define subsections by applying @subsection decorator
    @aetest.subsection
    def common_cleanup_subsections(self):
        pass


if __name__ == '__main__':
    aetest.main()