# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os

from mozlog import get_proxy_logger


LOG = get_proxy_logger(component="gen_test_url")


def gen_test_url(browser, test, sysdir):
    LOG.info("writing test settings url background js, so webext can get it")

    data = """
    // this file is auto-generated by raptor, do not edit directly
    function getSettingsURL() {
      return 'http://localhost:8000/%s.json';
    }
    """ % test

    if browser == 'firefox':
        webext_background_script = (os.path.join(sysdir,
                                                 'webext',
                                                 'raptor-firefox',
                                                 'auto_gen_settings_url.js'))
    elif browser == 'chrome':
        webext_background_script = (os.path.join(sysdir,
                                                 'webext',
                                                 'raptor-chrome',
                                                 'auto_gen_settings_url.js'))
    else:
        LOG.error("invalid browser")

    file = open(webext_background_script, "w")
    file.write(data)
    file.close()

    LOG.info("finished writing test settings url into webext")