# Executes the kill command

exec { 'pkill':
  command  => 'pkill killmenow', # The specific command to execute
  provider => 'shell',
}

