#!/usr/bin/python3

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    cur_session_time_label = None
    this_week_time_label = None
    total_time_label = None

    game_widget = None
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
        self.game_widget = GameWidget()
        self.game_widget.return_button.connect("clicked", self.on_return_main_page)

        self.stack.add_named(self.main_widget, "main_widget")

        self.add_page(self.game_widget, "game_widget", "Start Game")

    def on_change_page(self, button, page_id: str):
        self.stack.set_visible_child_name(page_id)

        if page_id == "game_widget":
            self.game_widget.start_game()

    def on_return_main_page(self, button):
        self.stack.set_visible_child_name("main_widget")


class GameWidget(Gtk.Box):
    buttons_box = None
    check_word_button = None
    next_word_button = None

    pronounce_label = None
    source_word_label = None
    target_word_entry = None
    correct_answer_label = None

    return_button = None
    correct_answers_count_label = None
    top_panel = None

    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)

        self.top_panel = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.game_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.game_box.set_border_width(100)

        self.init_top_panel()
        self.init_game_box()

        self.pack_start(self.top_panel, False, False, 0)
        self.pack_start(self.game_box, True, True, 0)

    def init_game_box(self):
        self.source_word_label = Gtk.Label(label="Source word")
        self.pronounce_label = Gtk.Label(label="sɔːs wɝd")
        self.target_word_entry = Gtk.Entry()
        self.buttons_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.check_word_button = Gtk.Button(label="Check")
        self.next_word_button = Gtk.Button(label="Next")
        self.correct_answer_label = Gtk.Label(label="Answer is correct! / Answer is wrong! The correct aswer is:")
        self.buttons_box.pack_start(self.check_word_button, True, False, 12)
        self.buttons_box.pack_start(self.next_word_button, True, False, 12)

        self.game_box.pack_start(self.source_word_label, False, False, 6)
        self.game_box.pack_start(self.pronounce_label, False, False, 6)
        self.game_box.pack_start(self.target_word_entry, False, False, 6)
        self.game_box.pack_start(self.correct_answer_label, False, False, 6)
        self.game_box.pack_start(self.buttons_box, False, False, 6)

        self.next_word_button.set_sensitive(False)
        self.correct_answer_label.hide()

    def init_top_panel(self):
        self.return_button = Gtk.Button("Return to main")
        self.correct_answers_count_label = Gtk.Label("Correct answers: 0 / 0 (0 %)")

        self.top_panel.pack_start(self.return_button, False, False, 12)
        self.top_panel.pack_end(self.correct_answers_count_label, False, False, 12)
    def start_game(self):
        self.correct_answer_label.hide()
        self.correct_answers_count_label.set_text("Correct answers: 0 / 0 (0 %)")


class MainWidget(Gtk.Box):
    def __init__(self):
        super().__init__(orientation=Gtk.Orientation.VERTICAL)

        self.buttons_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_center_widget(self.buttons_box)

    def add_button(self, button: Gtk.Button):
        self.buttons_box.pack_start(button, False, False, 6)
