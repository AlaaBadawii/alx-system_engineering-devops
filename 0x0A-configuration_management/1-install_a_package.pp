package { 'pip3':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  creates => '/usr/local/lib/python3.*/dist-packages/Flask-2.1.0.dist-info',
  require => Package['python3-pip'],
}

