0x0D. Web stack debugging #0

1. This project's main task is to identify a solution to a particular problem
2. Docker container was used with Apache2 running on it
3. The solution was to confirm that the DocumentRoot was pointing to the default html page that displayes anytime we run the apache2 (using curl)
4. We then wrote the string "Hello Holberton" to the index.html file
5. Restart the apache2 and exit.

After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains Hello Holberton. Paste the command(s) you used to fix the issue in your answer file.
