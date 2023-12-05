# Thiss is a puppet manifest that re-configures an ssh config file

file { "~/.ssh/school":
  ensure  => present,
  content => @("EOF"),
# Global settig
# Host settings
  Host myserver
    HostName 3.94.185.128
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
EOF
}
