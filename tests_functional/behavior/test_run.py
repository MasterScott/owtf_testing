import sys

from hamcrest import *

from owtf_testing.utils.owtf import OWTFTestCase
import owtf


class OWTFRunTest(OWTFTestCase):
    def test_run_no_param(self):
        """Run OWTF without any parameter."""
        sys.argv = ['owtf.py', ]
        with self.assertRaises(SystemExit) as cm:
            owtf.main(sys.argv)
        # Check that OWTF exited properly exit(0).
        self.assertEqual(cm.exception.code, 0, 'OWTF did not exit properly')
        # Check that Web UI has started.
        assert_that(str(self.mock_log_warn.call_args_list), contains_string('Web UI URL'))
        # Check that Web UI has properly started.
        assert_that(str(self.mock_log_info.call_args_list), contains_string('Press Ctrl+C'))