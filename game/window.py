#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application, **kwargs):
        super().__init__(
            application=application,
            **kwargs
        )

        self.set_size_request(800, 600)
        self.show_all()
