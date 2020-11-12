#installed modules
from pyfiglet import Figlet
from clint.textui import colored, puts
import argparse

#system modules
import sys
import os

#Configs
os.system('cls' if os.name == 'nt' else 'clear')
sys.path.insert(0, os.path.abspath('..'))

print colored.yellow(Figlet(font='slant').renderText('Login Flood'))