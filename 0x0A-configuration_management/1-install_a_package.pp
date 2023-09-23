# Installs Flask version 2.1.0 from pip3

package { 'flask':
  ensure   => '2.1.0', # Specifies version
  provider => 'pip3', # Specifies source
}
