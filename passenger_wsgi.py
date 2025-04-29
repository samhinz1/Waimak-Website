import sys, os

# This path will need to be updated with your actual cPanel username and Python version
INTERP = os.path.expanduser("/home/waimsezc/virtualenv/waimak/3.9/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

from app import app as application 