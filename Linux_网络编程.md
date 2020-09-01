[TOC]



## Socket建立

服务端建立连接包括：socket、bind、listen、accept

客户端包括：socket、connect

[https://www.zhihu.com/search?type=content&q=accept%E5%87%BD%E6%95%B0](https://www.zhihu.com/search?type=content&q=accept函数)

从socket层面看三次握手

![](https://picb.zhimg.com/v2-3c0b414214728dbe8877e5d2b1b7028c_b.jpg)

当客户端调用connect时，触发了连接请求，向服务器发送了SYN J包，这时connect进入阻塞状态；服务器监听到连接请求，即收到SYN J包，调用accept函数接收请求向客户端发送SYN K ，ACK J+1，这时accept进入阻塞状态；客户端收到服务器的SYN K ，ACK J+1之后，这时connect返回，并对SYN K进行确认；服务器收到ACK K+1时，accept返回，至此三次握手完毕，连接建立。**所以三次握手是在accept之后阻塞完成之后完成的**

### socket()函数

int socket(int domain, int type, int protocol);

socket()用于创建一个socket的套接字，它唯一标识一个socket。后续的操作都有用到这个套接字，把它作为参数，通过它来进行一些读写操作。

socket()的参数：

domain：即协议域，又称为协议族（family）。常用的协议族有，AF_INET、AF_INET6、AF_LOCAL...

type：指定socket类型。常用的socket类型有，SOCK_STREAM、SOCK_DGRAM、SOCK_RAW、SOCK_PACKET等等

protocol：指定协议。常用的协议有，IPPROTO_TCP、IPPTOTO_UDP、IPPROTO_SCTP、IPPROTO_TIPC等。当protocol为0时，会自动选择type类型对应的默认协议。

使用：int server_socket = socket(PF_INET, SOCK_STREAM, 0);---返回socket套接字

### bind()函数

int bind(int sockfd, const struct sockaddr *addr, socklen_t addrlen);

bind()函数把一个地址族中的特定地址赋给socket。例如对应AF_INET、AF_INET6就是把一个ipv4或ipv6地址和端口号组合赋给socket。

bind()的参数：

sockfd：即socket套接字，它是通过socket()函数创建了，唯一标识一个socket.

addr：一个const struct sockaddr *指针，指向要绑定给sockfd的协议地址。

addrlen：对应的是地址的长度。

使用：bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr))---返回0即表示成功

### listen()、connect()

如果作为一个服务器，在调用socket()、bind()之后就会调用listen()来监听这个socket，如果客户端这时调用connect()发出连接请求，服务器端就会接收到这个请求。

服务器：int listen(int sockfd, int backlog);

客户端：int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen);

listen函数的第一个参数即为要监听的socket套接字，第二个参数为相应socket可以排队的最大连接个数。

connect函数的第一个参数即为客户端的socket套接字，第二参数为服务器的socket地址，第三个参数为socket地址的长度。

### accept

int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);

accept函数的第一个参数为服务器的socket描述字，第二个参数为指向struct sockaddr *的指针，用于返回客户端的协议地址，第三个参数为协议地址的长度。

accept函数返回的是已连接的socket套接字。

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

**Socket通信也是网络通信的重要方式，本质上也是两个进程之间的通信，并且还是在不同主机上，因为本地进程通信可以通过Pid表示，但是不同主机就不行了，所以只能通过五元组来标示**

## IO多路复用的三种模型

https://blog.csdn.net/Eunice_fan1207/article/details/99674021

https://blog.csdn.net/shenya1314/article/details/73691088



### 数据传输过程

网卡收到了数据以后，会触发中断，向CPU发送中断信号，然后网卡通过中断程序去处理数据（主要是将网络数据放到创建的socket对象的接收缓冲区，重新唤醒进程，将进程加入工作队列中）

操作系统如何知道数据应该放哪个socket中？

答：由于数据包包含了ip和端口，而一个socket也对应一个端口，所以系统可以通过端口找到对应的socket

### 如何同时监听多个socket

#### select

```cpp
int select(
    int max_fd, //最大监听描述符数量
    fd_set *readset,  //注册了可读事件的描述符列表
    fd_set *writeset, //注册了可写事件的描述符列表
    fd_set *exceptset, //注册了异常事件的描述符列表
    struct timeval *timeout //超时时间
)              
```

##### 代码流程

```cpp
listenfd = socket(AF_INET, SOCK_STREAM, 0); //第一步，创建socket
bind(listenfd,(sockaddr *)&seraddr,sizeof(seraddr));  //第二步，绑定端口
listen(listenfd,LISTENQ);  //第三步，监听端口
int nready=select(maxfd+1,&rset,nullptr,nullptr,NULL);  //第四步，阻塞等待事件发生
```

![](https://img-blog.csdn.net/20131007164314234?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvbGluZ2Zlbmd0ZW5nZmVp/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

select在用户态创建新的socket后，需要将

将一个进程加入到每个socket的等待列表中，如果有一个socket接收到了数据，那么就会使得这个进程从所有socket的等待列表中去掉，唤醒进程，这个进程知道了这么多socket中有一个接收到了数据，那么就遍历一遍socket列表。以上是调用select的时候没有任何socket有数据的情况，而其实调用select的时候，内核会遍历一遍socket列表，如果有一个以上的socket接收区有数据，那么直接返回，不会阻塞，这也是为什么select会返回大于1

##### 缺点

- 每次调用select都要将进程加入到所有socket的等待列表，每一次唤醒还要从每个中移除。这里涉及了两次遍历，而且还需要将socket数组传给内核，所以规定了select的最大监听数量默认值是**1024**个
- 进程被唤醒以后还需要进行一次遍历查看哪些socket接收到了数据
- select需要从内核中复制大量的fd有关数据结构，这里就会有不小的时间开销
- select是水平触发模式，所以当一个事件没有对socket完成一个完整的IO操作，select也会去读取数据

#### poll

poll相比于select来说是使用链表保存文件描述符，所以摆脱了1024的限制。

#### epoll

**epoll是一种I/O事件通知机制，是linux 内核实现IO多路复用的一个实现。**

https://zhuanlan.zhihu.com/p/64746509

select低效的原因是将维护等待队列和阻塞进程合二为一，epoll做的就是将这两步分开，先用epoll_ctl维护等待队列（**是一个链表**），再调用epoll_wait阻塞进程。**空间换时间**

最大可监听的数量可以查看：**cat /proc/sys/fs/file-max**

**流程**

1. 当某个进程调用**epoll_create**方法时，内核会在cache中创建一个eventpoll对象，这是一个结构体

   ```c
   struct eventpoll{
       ....
       /*红黑树的根节点，这颗树中存储着所有添加到epoll中的需要监控的事件*/
       struct rb_root  rbr;
       /*双链表中则存放着将要通过epoll_wait返回给用户的满足条件的事件*/
       struct list_head rdlist;
       ....
   }
   ```

   主要储存了就绪队列和红黑树。

   红黑树和双向链表的节点类型：

   ```c
   struct epitem{
       struct rb_node  rbn;//红黑树节点
       struct list_head    rdllink;//双向链表节点
       struct epoll_filefd  ffd;  //事件句柄信息
       struct eventpoll *ep;    //指向其所属的eventpoll对象
       struct epoll_event event; //期待发生的事件类型
   }
   ```

   

2. 创建epoll对象后，可以用**epoll_ctl**添加或删除所要监听的socket，将用户态的event拷贝到内核态，也就是插入红黑树。

   具体实现是：https://blog.csdn.net/Mr_H9527/article/details/99745659

   首先要删除或者添加socket文件描述符的是调用epoll_ctl函数，该函数底层是调用了sys_epoll_ctl函数，这个函数接受的参数：

   ```c++
   sys_epoll_ctl(int epfd, int op, int fd, struct epoll_event __user *event)
   ```

   op代表操作类型是删除还是修改还是插入；fd是文件描述符。

   像插入操作的的过程如下：

   - epoll底层调用了ep_insert方法去插入，而这个方法是调用了ep_rbtree_insert方法去插入。
   - 这个方法首先用了个while循环查找到可以插入的位置
   - 然后进行插入，最后调用维护红黑树平衡的方法。
   - 然后**向内核注册回调函数**，如果有中断触发，那么就调用这个中断服务程序，向就绪链表插入fd，唤醒wait的进程

3. 当socket收到数据后，中断程序会给eventpoll的“就绪列表”添加socket引用，这个就绪列表中储存的是接收到数据的socket。

4. 当进程执行到epoll_wait之后，系统会将这个进程放到eventpoll的等待队列中阻塞进程。

   ```c
   int epoll_wait(int epfd， struct epoll_event *events， int maxevents， int timeout);
   ```

   在epoll_wait主要是调用了ep_poll，在ep_poll里直接判断就绪链表有无数据，有数据就返回，没有数据就sleep，等到timeout时间到后即使链表没数据也返回。当有数据时，还需要将内核就绪事件拷贝到传入参数的events中的用户空间，就绪链表中的数据一旦拷贝就没有了，所以这里要区分LT和ET，如果是LT有可能会将后续的重新放入就绪链表。

   events: 用来记录被触发的events，数组，其大小应该和maxevents一致，events和maxevents两个参数描述一个由用户分配的struct epoll event数组。也就是比如触发了EPOLLIN事件后就会触发回调函数。

   ```c++
   typedef union epoll_data {
   void *ptr;
   int fd;
   uint32_t u32;
   uint64_t u64;
   } epoll_data_t;
   
   struct epoll_event {
   uint32_t events; /* Epoll events */
   epoll_data_t data; /* User data variable */
   };
   
   ```

   

5. socket接受数据后一边修改就绪列表，一边也会唤醒eventpoll里面的阻塞进程，由于这些被唤醒的进程可以通过就绪列表知道哪些socket收到数据了，所以不需要遍历列表。

### 水平触发和边缘触发

https://zhuanlan.zhihu.com/p/107995399

- 水平触发就是只要socket中有数据，就会触发返回数据给epoll_wait()阻塞的进程
- 边缘触发是等到socket有数据写入的事件发生，才会去触发返回数据给阻塞的进程

### epoll的优势

- 相比与select，没有fd限制，可监听大量的socket
- 不会随着FD数量的增加导致效率线性下降。如果监听的所有fd中只有部分是很活跃的，那么select和poll必须每次去循环所有fd，而epoll只储存有数据接受的socket，而不是所有的fd
- 有两种触发模式，水平触发和边缘触发，像边缘触发只有socket缓冲区中新接受了触发epollwait，可以有效减少触发的次数，提高效率。

### **epoll相关事件**

综上，当监测的fd数量较小，且各个fd都很活跃的情况下，建议使用select和poll；当监听的fd数量较多，且单位时间仅部分fd活跃的情况下，使用epoll会明显提升性能。

### epoll的缺点

   epoll将等待队列和就绪队列维护在内核，所以每次添加文件描述符都需要进行一个系统调用，系统调用的开销比较大，对于大量的短链接存在可能就会比较低效。

### 数据结构

      1. 就绪列表储存socket的引用，所以需要是一个**能快速删除**和插入的数据结构。epoll采用了双向链表的数据结构。
      2. 内核cache在epoll_create时创建红黑树，储存了监听的socket。

## NIO和BIO

在IO多路复用技术出现之前，解决多链接的方式主要就是NIO和BIO

### BIO(同步阻塞)

- 服务端采用单线程，当accept一个请求后，在recv或send调用阻塞时，将无法accept其他请求（必须等上一个请求处recv或send完），`无法处理并发`

```cpp
// 伪代码描述
while(1) {
  // accept阻塞
  client_fd = accept(listen_fd)
  fds.append(client_fd)
  for (fd in fds) {
    // recv阻塞（会影响上面的accept）
    if (recv(fd)) {
      // logic
    }
  }  
}
```

- 服务器端采用多线程，当accept一个请求后，开启线程进行recv，可以完成并发处理，但随着请求数增加需要增加系统线程，`大量的线程占用很大的内存空间，并且线程切换会带来很大的开销，10000个线程真正发生读写事件的线程数不会超过20%，每次accept都开一个线程也是一种资源浪费`

```cpp
// 伪代码描述
while(1) {
  // accept阻塞
  client_fd = accept(listen_fd)
  // 开启线程read数据（fd增多导致线程数增多）
  new Thread func() {
    // recv阻塞（多线程不影响上面的accept）
    if (recv(fd)) {
      // logic
    }
  }  
}
```

### NIO同步非阻塞

- 服务器端当accept一个请求后，加入fds集合，每次轮询一遍fds集合recv(非阻塞)数据（这个动作是主动发生的，而不是通过事件回调导致的），没有数据则立即返回错误，`每次轮询所有fd（包括没有发生读写事件的fd）会很浪费cpu`

```cpp
setNonblocking(listen_fd)
// 伪代码描述
while(1) {
  // accept非阻塞（cpu一直忙轮询）
  client_fd = accept(listen_fd)
  if (client_fd != null) {
    // 有人连接
    fds.append(client_fd)
  } else {
    // 无人连接
  }  
  for (fd in fds) {
    // recv非阻塞
    setNonblocking(client_fd)
    // recv 为非阻塞命令
    if (len = recv(fd) && len > 0) {
      // 有读写数据
      // logic
    } else {
       无读写数据
    }
  }  
}
```

