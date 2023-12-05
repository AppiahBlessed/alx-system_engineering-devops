markdown
Copy code
# SSH Key Generation with Puppet

This Puppet module facilitates the generation and management of SSH key pairs for secure authentication. It includes a script for creating an RSA key pair with specific parameters, and an example Puppet manifest for deploying SSH configurations.

## Prerequisites

- Puppet installed on the system where you want to generate and manage SSH keys.
- Basic knowledge of Puppet manifests.

## SSH Key Generation

1. **Clone this repository to your Puppet module path:**

   ```bash
   git clone https://github.com/yourusername/puppet-ssh-keygen.git
Modify the script parameters (optional):

Edit the ssh-keygen.sh script if you need to customize key generation parameters.

Run the script:

bash
Copy code
bash ssh-keygen.sh
Follow the on-screen instructions to generate your SSH key pair.

Apply the Puppet configuration:

bash
Copy code
puppet apply --modulepath=/path/to/puppet/modules /path/to/puppet/manifests/site.pp
Replace /path/to/puppet/modules and /path/to/puppet/manifests/site.pp with your actual Puppet module and manifest paths.

Puppet Manifest
The included Puppet manifest (site.pp) demonstrates how to deploy SSH configurations, including host-specific settings and global options.

Contributing
If you encounter issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

License
This Puppet module is licensed under the MIT License - see the LICENSE file for details.
