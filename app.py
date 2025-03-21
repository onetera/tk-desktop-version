# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import sys
import sgtk
import traceback

class Version(sgtk.platform.Application):
    """
    The app entry point. This class is responsible for intializing and tearing down
    the application, handle menu registration etc.
    """

    def init_app(self):
        """
        Called as the application is being initialized
        """
        try:
            tk_multi_version = self.import_module("tk_multi_version")
            # register command
            cb = lambda: tk_multi_version.show_dialog(self)
            menu_caption = "Version"
            self.engine.register_command(menu_caption, cb)
        except Exception:
            traceback.print_exc()

    def destroy_app(self):
        """
        Tear down the app
        """
        self.log_debug("Destroying tk-multi-version")
