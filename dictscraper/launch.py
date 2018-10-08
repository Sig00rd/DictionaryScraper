import sys

from app import App

app = App()
print(sys.argv[1:])
app.set_arguments(sys.argv[1:])
app.run()
