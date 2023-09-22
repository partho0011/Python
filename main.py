





import os


def checkUpdate():
	os.system("clear");
	os.system('cd..  && rm -rf Python')
	os.system("git clone 'https://github.com/partho0011/Python' && cd Python && python main.py")
	
	

def main():
	checkUpdate()
	
	print("This is a line")
	
	
main()
