from invoke import task
import subprocess
import socket

@task
def ManageGroupMembers(c, what = None, action = None):
        if what and action:
                if not action in ['ADD','REMOVE']:
                        print("Invalid action specified!")
                        return False
                print(f"Performing {action} on {what}")
                try:
                        data = socket.gethostbyname_ex(what)[2][0]
                except:
                        data = None
                if data:
                        print(f"The IP for {what} is {data}")
                        command = f"ansible-playbook /tmp/ManageGroupMembersv2.yaml -e ITEM={what} -e ACTION={action} -e IP={data}"
                        pinky = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                        (stdout, stderr) = pinky.communicate()
                        print(stdout.decode())
                        if pinky.returncode == 0:
                                print("/etc/hosts file successfully edited!")
                        else:
                                print("Could not edit /etc/hosts file!")
                command = f"ansible-playbook /tmp/ManageGroupMembersv2.yaml -e ITEM={what} -e ACTION={action} -e GROUP=lin"
                pinky = subprocess.Popen(command, shell = True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                (stdout, stderr) = pinky.communicate()
                if pinky.returncode == 0:
                        print("/etc/ansible/hosts file successfully edited!")
                else:
                        print("Could not edit /etc/ansible/hosts file!")
        else:
                print(f"I dont know what action should be performed on what!")