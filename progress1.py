from time import sleep
from progressbar import progressbar
from progress.spinner import MoonSpinner
from progress.bar import Bar
from progress.bar import ChargingBar
from tqdm import tqdm
from tqdm import tnrange
from alive_progress import alive_bar

def ault():
	with alive_bar(100) as bar:
		for i in range(100):
			sleep(0.03)
			bar()
			
ault()

def bub():
	with alive_bar(100, bar ='bubbles', spinner ='notes2') as bar:
		for i in range(100):
			sleep(0.03)
			bar()

bub()

# def progress2():
# 	for i in progressbar(range(100)):
# 		sleep(0.02)

# progress2()

def spinner():
	with MoonSpinner('Loading...') as spinner:
		for i in range(100):
			sleep(0.02)
			spinner.next()
spinner()

def modd():
	with Bar('Downloading',fill='$', suffix='%(percent).1f%% - %(eta)ds') as bar:
		for i in range(100):
			sleep(0.02)
			bar.next()

modd()

def tq():
	for i in tqdm(range(100)):
		sleep(0.02)

tq()

def tq2():
	for i in tnrange(3, desc='datadw'):
		for j in tnrange(100, desc="dataiw"):
			sleep(0.02)

tq2()

def charging():
	with ChargingBar('Charging') as bar:
		for i in range(100):
			sleep(0.02)
			bar.next()
charging()
