# Puppet script that configures a "nginx" web server in an ubuntu 16.04 machine

package { 'nginx':
  ensure => installed
}

file_line { 'Add redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World'
}

#file { '/usr/share/nginx/html/404.html':
#  ensure  => file,
#  path    => '/usr/share/nginx/html/404.html',
#  mode    => '0644'
#  content => 'Ceci n\'est pas une page'
#}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}