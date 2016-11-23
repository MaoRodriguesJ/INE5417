import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def show_hourtable_dialog(self):
        hourtable_dialog = builder.get_object("create_hourtable_dialog")
        hourtable_dialog.show_all()

    def show_event_dialog(self):
        event_dialog = builder.get_object("create_event_dialog")
        event_dialog.show_all()

    def show_date_dialog(self):
        date_dialog = builder.get_object("create_date_dialog")
        date_dialog.show_all()

    def close_popup(self):
        self.hide()
        return True


if __name__ == '__main__':
    builder = Gtk.Builder()
    builder.add_from_file("mato.glade")
    builder.connect_signals(Handler)

    main_window = builder.get_object("main_window")

    main_window.show_all()

    Gtk.main()
