FIREWALL PROTECTION WITH ufw(Uninterrupted firewall)
----------------------------------------------------

We can install the ufw to become a firewall for all servers
or load balacers. it is install using the command "sudo apt-get install ufw"

After it has been installed, some configurations need to be made
in order to allow specified traffick coming through that server. The stages below follows how that is done
1. Opn the ufw config file normally located at /etc/default/ufw
2. Change the values for both "DEFAULT_OUTPUT_POLICY" and "DEFAULT_INPUT_POLICY" to "DROP"
3. The above stage helps us to allow only ports that have been explicitly allowd using the command below
4. Add the required ports for example, you can accept traffick from SSH, HTTP or HTTPS by using the command "sudo ufw allow {port_number}/tcp"
5. Enable the firewall with sudo ufw enable
