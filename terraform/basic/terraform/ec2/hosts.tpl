[nginx_lb]
%{ for ip in nginx_lb ~}
${ip}
%{ endfor ~}

[mysql_server]
%{ for ip in mysql_server ~}
${ip}
%{ endfor ~}

[php_fpm_servers]
%{ for ip in php_fpm_servers ~}
${ip}
%{ endfor ~}