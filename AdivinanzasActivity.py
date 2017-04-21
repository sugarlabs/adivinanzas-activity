from gettext import gettext as _

import sys
import gtk
import pygame

import sugar.activity.activity
from sugar.graphics.toolbarbox import ToolbarBox
from sugar.activity.widgets import ActivityToolbarButton
from sugar.graphics.toolbutton import ToolButton
from sugar.activity.widgets import StopButton


sys.path.append('..')  # Import sugargame package from top directory.
import sugargame.canvas

class JuegoAdivinanzas:

    def jugar(self):
        import adivinanzas

class AdivinanzasActivity(sugar.activity.activity.Activity):
    def __init__(self, handle):
        super(AdivinanzasActivity, self).__init__(handle)

        self.paused = False

        # Create the game instance.
        self.game = JuegoAdivinanzas() 

        # Build the activity toolbar.
        self.build_toolbar()

        # Build the Pygame canvas.
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)

        # Note that set_canvas implicitly calls read_file when
        # resuming from the Journal.
        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()

        # Start the game running (self.game.run is called when the
        # activity constructor returns).
        self._pygamecanvas.run_pygame(self.game.jugar)

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        # Blank space (separator) and Stop button at the end:

        separator = gtk.SeparatorToolItem()
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
