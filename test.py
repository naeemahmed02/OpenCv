import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window(title="Hello World")
window.show()
Gtk.main()
