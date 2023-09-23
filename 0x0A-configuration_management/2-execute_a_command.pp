# Executes the kill command

exec { 'killmenow':
  command  => 'pkill killmenow', # The specific command to execute
  prvoider => 'shell',
  onlyif   => 'pgrep killmenow', # Condition for only if the prvocess is running
}

