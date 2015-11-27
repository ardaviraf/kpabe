import subprocess


f = open('file.txt','w+')
f.write('salam') # python will convert \n to os.linesep
f.close() # you can omit in most cases as the destructor will call it


top =30
all=""
for m in range(1,5):
	for i in range(0,top):
		num=1
		command1=""
		command2=""
		for num in range(0,i+1):
				if num>0:	
				command1=command1+"A"+str(num)+" "
					command2=command2+"A"+str(num)+" and "



		command1="cpabe-keygen -o peter_priv_key pub_key master_key "+command1+"A"+str(num+1)
		command2='cpabe-enc -k pub_key file.txt \"'+command2+'A'+str(num+1)+'\"'
		
		print(" ")
		print(command1)
		print(command2)
		print (" ")

		p = subprocess.Popen('cpabe-setup', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print line,
			all=all+line
		retval = p.wait()
			all=all+",  "

		p = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print line,
				all=all+line
		retval = p.wait()
			all=all+",  "

		p = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print line,
				all=all+line
		retval = p.wait()
			all=all+",  "

		p = subprocess.Popen('cpabe-dec pub_key peter_priv_key file.txt.cpabe', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

		for line in p.stdout.readlines():
		   print line,
			   all=all+line
		retval = p.wait()
			all=all+"\n"


	print(" ")
	print(" ")
	all=all+"\n"
	all=all+"------------------------"
	all=all+"\n"
	
print (all)