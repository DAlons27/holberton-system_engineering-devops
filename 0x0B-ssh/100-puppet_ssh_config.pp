IntelliJ IDEAPyCharmRubyMine   
# Configurate SSH to connect to a server without typing a password.

file_line { 'identity_file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	IdentityFile ~/.ssh/school',
}

file_line { 'password_no':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}