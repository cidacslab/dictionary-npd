#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/juancaio/Documents/juan/dictionary_npd/")

from app import app as application
