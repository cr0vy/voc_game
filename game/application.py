#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gio, Gtk
import signal

from .window import MainWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(
            application_id="com.github.cr0vy.voc_game"
        )

        self.window = None

    def do_activate(self):
        if not self.window:
            self.window = MainWindow(application=self)
        
        self.window.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        action = Gio.SimpleAction.new("quit")
        action.connect("activate", lambda *x: self.quit())
        self.add_action(action)
        self.add_accelerator("<Primary>q", "app.quit")
