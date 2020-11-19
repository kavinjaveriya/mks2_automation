import os
import subprocess as sp
print("-------Welcome to my program----------")
def docker():
    
    status = sp.getstatusoutput('docker --version')
    print(status[0])
    print(status[1])
    if status[0] != 0 :
        print("Hello sir DOCKER is not installed on your machine")
        ch = input('''
        press y/n for installing or not installing respectivly - ''')
        if ch == y :
            os.system('yum install yum-utils -y')
            os.system('yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo')
            os.system('yum install docker-ce --nobest -y')
        else :
            print("Try again,Thank you!!!")
    else :
        print("----------DOCKER----------")
        print("(1. Docker daemon status/start/stop services")
        print("(2. Show docker container")
        print("(3. Show docker images")
        print("(4. Search images on docker hub")
        print("(5. Download docker image from docker hub")
        print("(6. Run a docker container")
        print("(7. Stop a docker container")
        print("(8. Delete a docker container")
        print("(9. Delete a docker image")
        choice =int(input("\nEnter your choice - "))
    if choice == 1 :
        output = int(input('''
        press 1 for status
        press 2 for start
        press 3 for stop - '''))
        if output == 1: os.system('systemctl status docker')
        elif output == 2: os.system('systemctl start docker')
        elif output == 3: os.system('systemctl stop docker')
        else: print('Enter a wrong choice')
       
    elif choice == 2 :
        output =int(input('''
        press 1 for all running container
        press 2 for all container - '''))
        if output == 1: os.system('docker ps')
        elif output == 2: os.system('docker ps -a')
        else: print('Enter a wrong choice')
    elif choice == 3: os.system('docker images')
    elif choice == 4:
        image = input('image name - ')
        os.system('docker search {}'.format(image))
    elif choice == 5:
        image = input('image name - ')
        os.system('docker pull {}'.format(image))
    elif choice == 6:
        image = input('image name - ')
        name = input('conatainer name - ')
        os.system('docker run -dit --name {} {} &'.format(name,image))
    elif choice == 7:
        name = rnput('conatainer name - ')
        os.system('docker stop {}'.format(name))
    elif choice == 8:
        name = input('container name - ')
        os.system('docker rm -f {}'.format(name))
    elif choice == 9:
        image = input('image name - ')
        os.system('docker rmi {}'.format(name))
docker()

