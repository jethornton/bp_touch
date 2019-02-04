from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.offsetButtonGroup.buttonClicked.connect(self.offsetHandleKeys)

    def offsetHandleKeys(self, button):
        char = str(button.text())
        text = self.offsetLabel.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.offsetLabel.setText(text)
