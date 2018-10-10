import sys

from app import App

app = App()
app.set_arguments(sys.argv[1:])
app.run()
