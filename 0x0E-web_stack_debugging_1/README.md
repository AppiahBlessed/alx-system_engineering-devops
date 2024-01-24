0. Nginx likes port 80
mandatory
Score: 0.0% (Checks completed: 0.0%)
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.

Requirements:

Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
Write a Bash script that configures a server to the above requirements


-------------------------------------------------------------------------
You can then execute the script to apply the changes:

bash
Copy code
./your_script.sh
This script assumes that your Nginx configuration file is located at /etc/nginx/sites-available/default and that your system uses systemctl for managing services. If your setup is different, adjust the script accordingly.
(Chatgpt)
-------------------------------------------------------------------------

This script comfigures the nginx server to listen on port 80
