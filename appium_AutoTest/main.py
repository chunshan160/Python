__author__ = '小翟'

import pytest
import time
from Common.conf_dir import htmlreports_dir


curTime = time.strftime("%Y-%m-%d_%H-%M-%S")
pytest.main(["-m", "smoke",
             "-s", "-q",
             "--alluredir", htmlreports_dir + "/APP_AutoTest_Reports_{0}.xml".format(curTime)])

