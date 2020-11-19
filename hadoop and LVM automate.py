import os
import subprocess as sp 

def dnconfig():
    mnip=input("Enter the ip address of your master node:")
    dirdn= input("Enter a directory name for the data  node : ")
    s1="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{}</value>
</property>
</configuration>""".format(dirdn)
    
    s2="""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{}:9001</value>
</property>
</configuration>""".format(mnip)

    
    fh=open("/etc/hadoop/hdfs-site.xml",'a')
    fh.write(s1)
    fh.close()

    fh=open("/etc/hadoop/core-site.xml",'a')
    fh.write(s2)
    fh.close()

    os.system("mkdir /{}".format(dirdn))

    print("\n")
    input("Press enter to continue")
    return dirdn


def dnshare(d):
    os.system("tput setaf 3")
    print("The format for specifying size is as follows :")
    print("\n\n")
    os.system("tput setaf 7")
    print("<size><x> : where x has to be B for bytes , K for Kilobytes , M for Megabytes and G for Gigabytes")
    print("\n")
    sz=input("Enter the size of storage you want to share")
    v=sp.getstatusoutput("pvcreate /dev/sdb ; vgcreate myvg /dev/sdb ; lvcreate --size {} --name storage myvg ; udevadm settle ; mkfs.ext4 /dev/myvg/storage ;mount /dev/myvg/storage /{} ;".format(sz,d))
    if v[0]==0:
        print("\n")
        print("Intial storage has been successfully allocated !!!")
    else:
        print("FAILED!!!")


    print("\n")
    input("Press enter to continue")


def dnservice():
    print("\nFor starting data node service press y and for stopping data node service press n\n\n")
    ch=input()
    if ch=='y':
        v=sp.getstatusoutput("hadoop-daemon.sh start datanode")
        if v[0]==0:
            print("DATA NODE Service has been successfully started !!!")
        else:
            print("FAILED!!!")
    elif ch=='n':
        v=sp.getstatusoutput("hadoop-daemon.sh stop datanode")
        if v[0]==0:
            print("DATA NODE Service has been successfully stopped !!!")
        else:
            print("FAILED !!!")

    print("\n")
    input("Press enter to continue")
    


def dnflex():
    print("\n Press e for increasing the storage capacity ")
    ch=input()
    
    if ch=='e':
        sz=input("Enter the size or amount to be increased")
        v=sp.getstatusoutput("lvextend --size +{} /dev/myvg/storage ; resize2fs /dev/myvg/storage ;".format(sz))
        if v[0]==0 :
            print("\n\nStorage has been successfully increased !!!")
        else:
            print("Failed")

    print("\n")
    input("Press enter to continue")


        

while True :
    os.system("tput setaf  6")
    print("********    HERE IS AUTOMATION FOR YOU     *********".center(100))
    print("\n\n")
    os.system("tput setaf 2")
    print("********   The following is the menu for YOU !!!    *********".center(100))
    print("\n\n")

    os.system("tput setaf 3")
    print("\n")
    print("Press 1 : To configure system as DATA NODE")
    print("\n")
    print("Press 2 : To provide some  storage of data node")
    print("\n")
    print("Press 3 : To start or stop  datanode  service { for thi option1 has to be selected first }")
    print("\n")
    print("Press 4 : To flexibly increase storage on the fly ")
    print("\n")
    print("Press 5 : To exit from the menu")
    print("\n\n\n")
    os.system("tput setaf 7")


    ch=input("Enter your choice : ")
    print("\n\n")

    if ch=='5':
        os.system("tput setaf 2")
        print("****** THANK YOU FOR USING AUTOMATION !!! ******")
        os.system("tput setaf 7")
        print("\n")
        exit()
    elif ch=='1':
       drdn = dnconfig()
       os.system("clear")
    elif ch=='2':
        dnshare(drdn)
        os.system("clear")
    elif ch=='3':
        dnservice()
        os.system("clear")
    elif ch=='4':
        dnflex()
        os.system("clear")









