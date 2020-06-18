1. char (*p) [] 、char \*p[]、char (\*p)()的区别？

   由于[]的优先级高于\*，所以char(*p)[]是指向一个数组的指针，char \*p[]指的是一个存放指针的数组。

   char(\*p)()指的是返回值是char指针的一个方法

2. 手写int atoi(char *str)

   https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/

   ```c
   int strToInt(char* str){
       /*
       1.基本逻辑就是先判断空格，去除；然后判断©️，记录到flag
       2.往后找数字，换算成一个整数
       这里最重要的是整数溢出的判断，因为这边的数值范围是-2^31~2^31-1，也就是[-2147483648，2147483647]，所以我们在进行ans=ans*10+r之前，需要判断一下这一层的ans是否已经溢出整数的范围，
       两种情况：
       1.ans>INT_MAX/10，也就是ans>214748364，那么一定溢出了
       2.ans==INT_MAX/10 && r>7，也就是214748364这一部分是一样的，需要比较个位，所以只要大于7，
       就是溢出了。
   
       */
       int ans=0;
       int flag=1;
       int r;
       while(*str==' ') str++;
       if(*str=='-') flag = -1;
       if(*str=='+' || *str=='-') str++; 
       while(*str>='0' && *str<='9')
       {
           r=*str-'0';
           if(ans>INT_MAX/10 || ans==INT_MAX/10 && r>7) return flag==1?INT_MAX:INT_MIN;
           ans=ans*10+r;
           str++;
       }
       return ans*flag;
   }
   ```

3. 指针和引用的区别

   - 指针是一个变量，而引用只是别名，所以指针本身后开辟栈空间储存，而引用本身不占空间
   - 指针可以有多级指针，但是引用只能一级
   - 指针可以的是空指针，而引用不能指向空
   - 指针的值在初始化完后可以重新指向，而引用不能重新指向新对象

4. C和C++的区别

   https://www.zhihu.com/question/28834538/answer/100698972

   C++是面向对象的语言，而C是面向过程的。C++几乎是C的超集，C++比C多了很多的语法概念，就像RALL，rall是资源初始化的概念，资源的使用至少有三个阶段，也就是资源的获取，使用，释放。但是这个释放经常被忘记，C++不像java，python可以自己释放资源，而是需要程序员手动释放。所以RALL就是C++将资源获取的过程封装成一个类，通过构造函数获取资源，析构函数释放资源，这也是正好利用了C++的特性。

   https://zhuanlan.zhihu.com/p/34660259（RALL原理介绍）

