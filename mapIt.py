import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    print(address)
else:
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
