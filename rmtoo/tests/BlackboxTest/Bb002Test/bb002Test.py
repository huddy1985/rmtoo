'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Blackbox rmtoo test
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''

import os
import time

from rmtoo.lib.RmtooMain import main
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, \
    compare_results, cleanup_std_log, delete_result_is_dir, check_file_results

mdir_orig = "tests/blackbox-test/bb002-test"
mdir = "tests/BlackboxTest/Bb002Test"

class TestBB002:

    def test_pos_001(self):
        "BB Hotspot in the middle of the graph 2"

        # This is needed, because the prios use localtime
        os.environ['TZ'] = 'Europe/Berlin'
        time.tzset()

        def myexit(n):
            pass

        os.environ["basedir"] = mdir_orig
        os.environ["rbasedir"] = mdir
        mout, merr = prepare_result_is_dir()
        main(["-j", "file://" + mdir + "/input/Config.json"],
             mout, merr, exitfun=myexit)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
