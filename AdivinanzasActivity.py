from gettext import gettext as _

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pygame

import sugar3.activity.activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton


sys.path.append('..')  # Import sugargame package from top directory.
import sugargame.canvas

class JuegoAdivinanzas:

    def jugar(self):
        import adivinanzas

class AdivinanzasActivity(sugar3.activity.activity.Activity):
    def __init__(self, handle):
        super(AdivinanzasActivity, self).__init__(handle)

        self.paused = False

        # Create the game instance.
        self.game = JuegoAdivinanzas() 

        self.game.canvas = sugargame.canvas.PygameCanvas(
                self,
                main=self.game.jugar,
                modules=[pygame.display, pygame.font])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()

        # Build the activity toolbar.
        self.build_toolbar()

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        # Blank space (separator) and Stop button at the end:

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

    def read_file(self, file_path):
        pass

    def write_file(self, file_path):
        pass
