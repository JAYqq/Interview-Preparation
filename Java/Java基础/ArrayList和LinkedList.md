## 数据结构

ArrayList是数组结构，LinkedList是双向链表结构

双向链表是因为LinkedList内部有一个node方法根据index去查询节点，因此可以判断index和链表size的比较选择从后往前还是从前往后，这边又可以节省一部分时间。

## 随机访问

```java
public class LinkedList<E>
    extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
//---------------
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable
```

ArrayList比LinkedList多继承了一个RandomAccess，这个接口只是一个标注接口，没有实际方法，它说明了：

1. ArrayList支持随机访问，LinkedList不支持
2. ArrayList的for循环比Iterator循环更加高效

## 使用场景

### 添加数据

ArrayList每次添加会去执行ensureCapacityInternal 检查数组是否需要扩容，而LinkedList是创建新节点并连接。

### 删除数据

ArrayList由于数组结构限制，需要移动数据位置；LinkedList只是删除节点后修改指针。

### 修改数据

修改数据本质上也是先查询数据后修改，根据索引查询ArrayList的效率比较高（随机访问），查找指定值时看似都需要循环遍历查找，两者效率差不多，但是实际考虑到CPU缓存变量的问题，数组作为连续存储的结构可以整块被缓存进缓存块，可以更快速的去CPU缓存中查找，而链表结构分散存储，所以只能去内存中查询，速度就不如数组了。

### 查询数据

如修改数据

因此总结下面的：

ArrayList适合频繁查询和获取数据，LinkedList适合频繁删除和增加数据

## 扩容机制

ArrayList每次add的时候都会检测容量大小，如果需要扩容，就会开辟新空间为原来的 **1.5倍**；LinkedList由于链表结构，所以不需要扩容，受内存大小限制。





