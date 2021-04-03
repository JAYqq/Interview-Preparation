### 垃圾回收

#### -XX:+PrintGCDetails

打印出垃圾分代回收的细节，如下：

```shell
[GC (Allocation Failure) [PSYoungGen: 86644K->480K(111616K)] 86644K->81388K(367104K), 0.1010248 secs] [Times: user=0.22 sys=0.03, real=0.11 secs] 
Heap
 PSYoungGen      total 111616K, used 13337K [0x0000000743600000, 0x0000000751000000, 0x00000007c0000000)
  eden space 95744K, 13% used [0x0000000743600000,0x000000074428e748,0x0000000749380000)
  from space 15872K, 3% used [0x0000000749380000,0x00000007493f8020,0x000000074a300000)
  to   space 15872K, 0% used [0x0000000750080000,0x0000000750080000,0x0000000751000000)
 ParOldGen       total 255488K, used 80908K [0x000000064a200000, 0x0000000659b80000, 0x0000000743600000)
  object space 255488K, 31% used [0x000000064a200000,0x000000064f103010,0x0000000659b80000)
 Metaspace       used 3098K, capacity 4496K, committed 4864K, reserved 1056768K
  class space    used 340K, capacity 388K, committed 512K, reserved 1048576K
```

用于查看各个代的使用情况。

### -XX:MaxTenuringThreshold

设置分代收集的年龄阙值，也就是年龄达到多少就会放到老生代。