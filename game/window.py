#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    cur_session_time_label = None
    this_week_time_label = None
    total_time_label = None

    main_widget = None

    def __init__(self, application, **kwargs):
        super().__init__(
            application=application,
            **kwargs
        )

        self.set_size_request(800, 600)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.times_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.stack = Gtk.Stack()
        self.stack.set_border_width(18)
        self.box.pack_start(self.times_box, False, False, 12)
        self.box.pack_start(self.stack, False, False, 12)

        self.init_times()
        self.init_widgets()

        self.add(self.box)

        self.show_all()

    def add_page(self, widget: Gtk.Widget, page_id: str, name: str):
        self.stack.add_named(widget, page_id)

        widget_button = Gtk.Button(label=name)
        widget_button.connect("clicked", self.on_change_page, page_id)
        self.main_widget.add_button(widget_button)

    def init_times(self):
        self.cur_session_time_label = Gtk.Label("Current time: 00:00:00")
        self.this_week_time_label = Gtk.Label("This week: 00:00:00")
        self.total_time_label = Gtk.Label("Total: 00:00:00")

        self.times_box.pack_start(self.cur_session_time_label, True, True, 12)
        self.times_box.pack_start(self.this_week_time_label, True, True, 12)
        self.times_box.pack_start(self.total_time_label, True, True, 12)

    def init_widgets(self):
        self.main_widget = MainWidget()

        self.stack.add_named(self.main_widget, "main_widget")

    def on_change_page(self, button, page_id: str):
        self.stack.set_visible_child_name(page_id)


class MainWidget(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        self.buttons_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_center_widget(self.buttons_box)

    def add_button(self, button: Gtk.Button):
        self.buttons_box.pack_start(button, False, False, 6)
