## map

### 基本操作

1. 初始化

   ```cpp
   map<string,int> mp
   ```

2. 赋值

   ```cpp
   //1
   map[1]="hello";
   //2
   //这里的value_type就是pair类型
   mp.insert(map<string,int>::value_type("Anna",1));
   
   ```

3. 查询

   ```cpp
   mp.count(k)   //mp中k键出现的次数
   mp.find(k)    //返回一个迭代器，如果不存在就会返回一个end迭代器
   int cur=0;
   map<string,int>::iterator it=mp.find("Anna");
   if (it!=mp.end())
     cur=it->second();
   ```

4. 删除

   ```cPP
   //1 指定删除，返回void，接收迭代器类型
   map<string,int> it=mp.find("hello");
   mp.erase(it);
   //2 返回删除数量，接受指定类型
   mp.erase("hello");
   //3 删除指定区域，接收迭代器类型
   mp.erase(it,mp.end());
   //4 循环删除注意
   for(ITER iter=mapTest.begin();iter!=mapTest.end();)
   {
     cout<<iter->first<<":"<<iter->second<<endl;
     mapTest.erase(iter++);//注意一定要++,否则iter被删除后就无法再循环了
   }
   ```
   
5. 交换

   ```cpp
   std::map<string,int> m1,m2;
   m1.swap(m2); //这样就可以将m2中的键值对和m1中交换
   ```

### 深入原理

map内部使用红黑树实现，而红黑树只是作为了一种基础模版去使用，在STL中是更加个性化的红黑树

#### 具体实现

#### 为什么使用红黑树？

说到查找问题 必然有几种备选的数据结构不乏：

- **线性结构及其变种：数组、链表、跳跃链表**
- **树形结构：BST、AVL、RB-Tree、Hash_Table、B-Tree、Splay-Tree、Treap**

当然还有一些其他我可能不知道的，但是热门的基本都在这里了，那么一一来看进行优劣势分析：

- **数组和链表** 不用多说，动态高效的插入、删除、查找都不能满足要求。
- **跳跃链表SkipList** 在Redis中和LevelDB中都有应用，并且当时是声称要替代RB-Tree，那为什么map不是使用跳跃链表来实现的呢？
- **BST和AVL** 是二叉搜索树和平衡二叉树，这两个比较容易排除，BST可能退化成为链表，那么树就相当于很高，时间无法保证，AVL作为严格平衡的二叉搜索树对平衡性要求很高，因此在插入和删除数据时会造成不断地重度调整，影响效率，有点学术派而非工程派，但是AVL是后面很多变种树的基础也很重要，但是确实不适合用在map中。
- **Hash_Table** 其实目前已经有基于哈希表的map版本了，相比红黑树查找更快，然而时间的提升也是靠消耗空间完成的，哈希表需要考虑哈希冲突和装载因子的处理，在1994年左右内存很小并且很贵，因此哈希表在当时并没有被应用于实现map，现在内存相对来说已经很大并且不再昂贵，哈希表自然也有用武之地了。
- **Splay-Tree** 伸展树也是一种变种，它是一种能够自我平衡的二叉查找树，它能在均摊O(log n)的时间内完成基于伸展（Splay）操作的插入、查找、修改和删除操作。它是由丹尼尔·斯立特（Daniel Sleator）和罗伯特·塔扬在1985年发明的。
- **Treap** 就是Tree+heap，树堆也是一种二叉搜索树，是有一个随机附加域满足堆的性质的二叉搜索树，其结构相当于以随机数据插入的二叉搜索树。其基本操作的期望时间复杂度为O(log{n})。相对于其他的平衡二叉搜索树，Treap的特点是实现简单，且能基本实现随机平衡的结构。
- **B-Tree** 这里可以认为是B树族包括B树、B+树、B*树，我们都知道B树在MySQL索引中应用广泛，构建了更矮更胖的N叉树，这种结构结点可以存储更多的值，有数据块的概念，因此应对磁盘存储很有利，事实上即使内存中使用B树也可以提高CacheHit的成功率，从而提高效率，网上有的文章提到STL之父说如果再有机会他可能会使用B树来实现一种map，也就是借助于局部性原理来提高速度。



## Vector

vector在底层和数组没有区别，都是地址连续的内存空间，但是vector能够动态分配空间，不用初始化大小。

```cpp
//alloc是SGI STL的空间配置器
template <class T,class Alloc=alloc>
class vector
{
public:
    typedef T   value_type;
    typedef value_type*  pointer;
    typedef value_type*  iterator;
    typedef value_type&  reference;
    typedef size_t   size_type;
    typedef ptrdiff_t   difference_type;

protected:
    //simple_alloc是SGI STL的空间配置器
    typedef simple_alloc<value_type,Alloc> data_allocator;
    //表示目前使用空间的头
    iterator start; 
    //表示目前使用空间的尾
    iterator finish; 
    //表示目前可用空间的尾
    iterator end_of_storage;
}
```

vector类主要有三个迭代器成员变量：

1. start
2. finish
3. end_of_storage 

vector的一些取值操作：

```cpp
//迭代器举例
iterator begin()
{
    return start;
}
iterator end()
{
    return finish;
}

reference front()
{
    return *begin();
}
reference back()
{
    return *(end() - 1);
}
```

**push_back**

- 如果end_of_storage > end 说明尾部还有空间，直接放入
- 如果没有空间的话，就扩充空间为原来的两倍（有些是素数扩充）并重新分配内存后将原数据和新数据一起放到新的内存空间，重新定义对应的迭代器对象。

这里的扩容在C++11之前reserve()是调用复制构造，但是11以后就采用了移动构造

**vector扩容的时间复杂度是多少**

O(N)

**那为什么push_back的时间复杂度为1**

摊还问题，因为多次的O(1)的操作，最后可能到需要扩容了就是，O(N)的时间平摊给每一次就是O(1)了。

## list

 非连续存储结构，具有双链表结构，每个元素维护一对前向和后向指针，因此支持前向/后向遍历。支持高效的随机插入/删除操作，但随机访问效率低下，且由于需要额外维护指针，开销也比较大。每一个结点都包括一个信息快Info、一个前驱指针Pre、一个后驱指针Post。可以不分配必须的内存大小方便的进行添加和删除操作。使用的是非连续的内存空间进行存储。
  优点：(1) 不使用连续内存完成动态操作。
        (2) 在内部方便的进行插入和删除操作
        (3) 可在两端进行push、pop
  缺点：(1) 不能进行内部的随机访问，即不支持[ ]操作符和vector.at()
        (2) 相对于verctor占用内存多

## deque

连续存储结构，即其每个元素在内存上也是连续的，类似于vector，不同之处在于，deque提供了两级数组结构， 第一级完全类似于vector，代表实际容器；另一级维护容器的首位地址。这样，deque除了具有vector的所有功能外，还支持高效的首/尾端插入/删除操作。

## string

### 切割

```cpp
string.substr(start,len)
```

## Stack

### 为什么需要分别top和pop

原因在于，假设有一个`stack<vector<int>>`，拷贝vector时需要在堆上分配内存，如果系统负载严重或资源有限（比如vector有大量元素），vector的拷贝构造函数就会抛出[std::bad_alloc](https://en.cppreference.com/w/cpp/memory/new/bad_alloc)异常。如果pop可以返回栈顶元素值，返回一定是最后执行的语句，stack在返回前已经弹出了元素，但如果拷贝返回值时抛出异常，就会导致弹出的数据丢失（从栈上移除但拷贝失败）。因此[std::stack](https://en.cppreference.com/w/cpp/container/stack)的设计者将这个操作分解为top和pop两部分，但这样的分割却造成了race condition。

这里的竞争比如多个线程同时处理这个stack，多个线程同时top了一个值并处理了两次，这是很危险的；另外如果一个线程先pop了，另一个线程准备pop的时候就会因为没有值而报错。















