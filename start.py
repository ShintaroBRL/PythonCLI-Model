#installed modules
from pyfiglet import Figlet
from clint.textui import colored
from progressbar import *
import argparse
import signal

#system modules
import time
import sys
import os

#Metas
__author__ = "Juliano Lira Florentino"
__description__ = "Programa desenvolvido para tals"

#Configs
os.system('cls' if os.name == 'nt' else 'clear')    #Clear screen on start
parser = argparse.ArgumentParser()                  # Initialize parser
 
#Args configs
parser.add_argument("--output", help = "Show Output")
parser.add_argument("--input", help = "Show input", type=int, required=True)
args = parser.parse_args()

#Print welcome
print colored.yellow(Figlet(font='slant').renderText('Model'))
print colored.yellow("author: "+__author__)
print colored.yellow("Description: "+__description__+"\n")

#Functions
def onFinish():
    print colored.yellow("Processamento finalizado")

def onStart():
    print colored.yellow("Processamento iniciado")

def onRun(index):
    time.sleep(0.5)
    print "Processamento Run"+str(index)

def Progress(max,callback,callstart,callrun):
    callstart()
    widgets=[
        RotatingMarker(),
        ' [', Timer(), '] ',
        Bar(),
        ' (', ETA(),')',
    ]
    for i in progressbar(range(max), widgets=widgets, redirect_stdout=True):
        callrun(i)
    callback()

def keyboardInterruptHandler(signal, frame):
    exit(0)
signal.signal(signal.SIGINT, keyboardInterruptHandler)

Progress(100,onFinish,onStart,onRun)