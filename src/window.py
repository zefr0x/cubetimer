# window.py
#
# Copyright 2023 Herpiko Dwi Aguno
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright
# holders shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization.

from gi.repository import Gtk
import random


@Gtk.Template(resource_path='/xyz/aguno/CubeTimer/window.ui')
class CubetimerWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'CubetimerWindow'

    ScrambleNotation = Gtk.Template.Child("ScrambleNotation")
    Timer = Gtk.Template.Child("Timer")
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scrambled = self.generate_scramble()
        print(scrambled) 
        self.ScrambleNotation.set_text(scrambled)
        print("helloooo")
       
        # Events 
        #self.Timer.connect("key-press-event", self.start_timer)
        
    def generate_scramble(self):
        moves = ["U", "U'", "U2", "D", "D'", "D2", "L", "L'", "L2", "R", "R'", "R2", "F", "F'", "F2", "B", "B'", "B2"]
        scramble = []
        for _ in range(21):
            random_move = random.choice(moves)
            scramble.append(random_move)
        return "  ".join(scramble)
        
    def start_timer(self):
        print("ok")
        


class AboutDialog(Gtk.AboutDialog):

    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = 'cubetimer'
        self.props.version = "0.1.0"
        self.props.authors = ['Herpiko Dwi Aguno']
        self.props.copyright = '2022 Herpiko Dwi Aguno'
        self.props.logo_icon_name = 'xyz.aguno.CubeTimer'
        self.props.modal = True
        self.set_transient_for(parent)
