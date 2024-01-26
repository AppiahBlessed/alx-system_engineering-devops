The user root is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the root user, as if you fat finger a command and for example run rm -rf /, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

For the containers that you are given in this project as well as the checker, everything is run under the root user, which has the ability to run anything as another user.

Requirements:

write a Bash script that accepts one argument
the script should run the whoami command under the user passed as an argument
make sure to try your script by passing different users
Example:

root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#




2. Requirements:

nginx must be running as nginx user
nginx must be listening on all active IPs on port 8080
You cannot use apt-get remove
Write a Bash script that configures the container to fit the above requirements

a. We change the nginx.conf file to let the user point to "nginx" rather
b. We changed the /sites-available/default configuration file too, to allow port 8080, changed from port 80. The server now listens on port 8080
c. Change the permission of the nginx.conf file
d. Stopped all running process
e. Run the nginx server but this time using the "nginx" user instead of "root"
