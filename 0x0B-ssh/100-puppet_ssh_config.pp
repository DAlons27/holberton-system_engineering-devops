# Configurate SSH to connect to a server without typing a password.

file_line { 'Declare identity file':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school'
}

file_line { 'Turn off passwd authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no'
}