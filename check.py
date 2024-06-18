import os
import subprocess

def install_apache():
    try:
        # Update package list
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)

        # Install Apache 2
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'apache2'], check=True)

        # Modify the Apache configuration to change the port to 8081
        apache_ports_file = '/etc/apache2/ports.conf'
        apache_default_file = '/etc/apache2/sites-available/000-default.conf'

        # Update ports.conf
        with open(apache_ports_file, 'r') as file:
            data = file.readlines()
        with open(apache_ports_file, 'w') as file:
            for line in data:
                if 'Listen 80' in line:
                    file.write('Listen 8081\n')
                else:
                    file.write(line)

        # Update 000-default.conf
        with open(apache_default_file, 'r') as file:
            data = file.readlines()
        with open(apache_default_file, 'w') as file:
            for line in data:
                if '<VirtualHost *:80>' in line:
                    file.write('<VirtualHost *:8081>\n')
                else:
                    file.write(line)

        # Restart Apache service to apply changes
        subprocess.run(['sudo', 'systemctl', 'restart', 'apache2'], check=True)

        print('Apache installed and configured on port 8081 successfully.')

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    install_apache()