from sys import exit
from os import mkdir
from os import chdir

def stop():
	exit()

def file_name(name, text):
	file_make = name
	file = open(name, f"a")
	file.write(text)
	file.close()

def main():
	file_path = input(f"путь к файлу:\n")
	chdir(file_path)
	mkdir(f"files")
	chdir(f"files")
	file_name_main = input(f"Назови файл:\nесли хотите выйти напишите: выход\n")
	if file_name_main == f"выход":
		stop()
	while True:
		a = input(f"")
		if a == f"выход":
			stop()
		file_name(file_name_main, f"{a}\n")

if __name__ == f"__main__":
	main()