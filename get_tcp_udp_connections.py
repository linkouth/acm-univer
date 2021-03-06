import psutil

connections = psutil.net_connections()
print('{0}'.format('Имя', width = 4, fill = ' '), end = ' ')
print('{0}'.format('Локальный адрес', width = 25, fill = ' '), end = '  ')
print('{0}'.format('Внешний адрес', width = 20, fill = ' '), end = '    ')
print('{0}'.format('Состояние', width = 11, fill = ' '))
for connection in connections:
  fd, family, stream_type, laddr, raddr, status, pid = (connection)
  if len(raddr) == 0:
    continue
  if stream_type == 1:
    stream_name = 'TCP'
  else:
    stream_name = 'UDP'
  print('{0}'.format(stream_name, width = 4, fill = ' '), end = ' ')
  local_ip, local_port = laddr
  print('{0}'.format(local_ip), end = ':')
  print('{0}'.format(local_port), end = ' ')
  remote_ip, remote_port = raddr
  print('{0}'.format(remote_ip, width = 15, fill = ' ', align = '<'), end = ':')
  print('{0}'.format(remote_port, width = 5, fill = ' '), end = ' ')
  print('{0}'.format(status, width = 11))
