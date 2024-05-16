# user_limit.pp
file { '/etc/security/limits.conf':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => @("EOF")
*       soft    nofile  4096
*       hard    nofile  8192
| EOF
}

file_line { 'pam_limits_common_session':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^session required pam_limits.so',
}

file_line { 'pam_limits_common_session_noninteractive':
  path  => '/etc/pam.d/common-session-noninteractive',
  line  => 'session required pam_limits.so',
  match => '^session required pam_limits.so',
}

file { '/etc/sysctl.conf':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => @("EOF")
fs.file-max = 100000
| EOF
}

exec { 'sysctl -p':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
  subscribe   => File['/etc/sysctl.conf'],
}

