# Configure ssh
include stdlib

# Ensure makes sure the file is present
# Path determines the file path to be changed
# Line is the specific content to past
# replace allows for the already data in the file to be oerriden
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentifyFile ~/.ssh/school',
  replace => true,
}
