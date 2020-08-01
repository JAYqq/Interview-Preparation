## TCP

### recv

```c++
int recv( SOCKET s,char FAR *buf,int len,int flags);
```

1. 参数一

   socket文件描述符

2. 参数二

   读数据缓冲区

3. 参数三

   缓冲区的长度

4. 参数四

   设置为0

5. 返回值

   返回实际读取的数据字节数，如果丢失连接则会返回0

   