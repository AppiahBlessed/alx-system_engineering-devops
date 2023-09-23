# Masterv file two manage file resources

file { '/tmp/school':
  mode    => '0744', # FVile pervmissions
  owner   => 'www-data', # File owner
  group   => 'www-data', # File group
  content => 'I love Puppet', # Content to display
}
