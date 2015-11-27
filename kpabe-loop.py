import subprocess


f = open('file.txt','w+')
f.write('salam') # python will convert \n to os.linesep
f.close() # you can omit in most cases as the destructor will call it


top = 30
all=""
for m in range(1,5):
        for i in range(0,top):
                        num=1
                        command0=""
                        command3=""
                        for num in range(0,i+1):
                                        if num>0:
                                                        command0=command0+"A"+str(num)+" "
                                                        command3=command3+"A"+str(num)+" and "



                        command1="kpabe-setup "+command0+"A"+str(num+1)
                        command2="kpabe-enc -k pub_key file.txt "+command0+"A"+str(num+1)
                        command3='kpabe-keygen -o doctor_priv_key pub_key master_key \"'+command3+'A'+str(num+1)+'\"'
                        command4='kpabe-dec pub_key doctor_priv_key file.txt.kpabe'

                        print(" ")
                        print(command1)
                        print(command2)
                        print(command3)
                        print(command4)
                        print (" ")

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

                        p = subprocess.Popen(command3, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        for line in p.stdout.readlines():
                                print line,
                                all=all+line
                        retval = p.wait()
                        all=all+",  "

                        p = subprocess.Popen(command4, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

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
