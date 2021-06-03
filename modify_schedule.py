import subprocess

def disable_task():
	subprocess.Popen(['schtasks.exe', '/Change', '/TN', "Test Task",
	                          '/DISABLE'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)



def main(args=None):
	disable_task()
	print("Done")


if __name__ == '__main__':
	main()