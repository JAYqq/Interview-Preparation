# AOP基础知识

AOP是面向切面编程，关于切面要理解下面几个点：

1. `Joint point`（连接点）：表示在程序中明确定义的点，典型的包括方法调用，对类成员的访问以及异常处理程序块的执行等等，它自身还可以嵌套其它 joint point。
2. `Pointcut`（切点）：表示**一组 joint point**，这些 joint point 或是通过逻辑关系组合起来，或是通过通配、正则表达式等方式集中起来，它定义了相应的 Advice 将要发生的地方。
3. `Advice`（增强）：Advice 定义了在 `Pointcut` 里面定义的程序点具体要做的操作，它通过 before、after 和 around 来区别是在每个 joint point 之前、之后还是代替执行的代码
4. `Aspect`（切面）： Aspect 声明类似于 Java 中的类声明，在 Aspect 中会**包含着一些 Pointcut 以及相应的 Advice**。
5. `Target`（目标对象）：织入 `Advice` 的目标对象.。
6. `Weaving`（织入）：将 `Aspect` 和其他对象连接起来, 并创建 `Advice`d object 的过程

下面有一个更加形象的说明：https://zhuanlan.zhihu.com/p/37497663

# AOP的深入理解

## 动态代理

看完上面链接的文章，对AOP差不多有了大概的印象，关于AOP不得不涉及动态代理，Spring中的动态代理默认使用jdk动态代理，除了jdk还有cglib动态代理。

### jdk动态代理

先读文章：http://scwmason.cn/2020/10/13/Java%E5%8F%8D%E5%B0%84%E2%80%94%E2%80%94%E5%8A%A8%E6%80%81%E4%BB%A3%E7%90%86/

文章中的最优版例子就是jdk动态代理的写法，其中执行了**Proxy.newProxyInstance** 之后发生的事情，才是jdk动态代理的精髓。

继续读文章：https://segmentfault.com/a/1190000021821314

之后主要调用了 **ProxyGenerator.generateProxyClass**方法：

```java
byte[] proxyClassFile = ProxyGenerator.generateProxyClass(
                proxyName, interfaces, accessFlags);
```

返回值为字节数组，这个方法**生成了代理对象，并将二进制数据写入了class文件**。

文章中生成的class文件我们可以看到：

```java
public final class UserService extends Proxy implements com.example.demo.jdk_dynamic_proxy.service.UserService{}
```

是这样的，因此**jdk动态代理只能代理实现接口的类**。

### Cglib代理

可以实现任意可以被继承的类的代理（final修饰的类或方法是无法被继承的）

#### 原理

利用ASM开源包，对代理对象类的class文件加载进来，通过修改其字节码生成子类来处理。

就像是我们手写静态代理的时候，手动给被代理类实现一个proxy然后进行增强，但是Cglib是把这个过程实现了动态代理，并且是在字节码层面。

在JVM中程序执行不一定非要写java代码，只要能生成java字节码，jvm并不关系字节码的来源，因此ASM就可以通过cglib生成字节码。

先读文章：https://zhuanlan.zhihu.com/p/35144462

#### 创建代理类的步骤

1. 生成代理类的二进制字节码文件
2. 加载二进制字节码，生成Class对象( 例如使用Class.forName()方法 )
3. 通过反射机制获得实例构造，并创建代理类对象（这一步类似http://scwmason.cn/2020/10/13/Java%E5%8F%8D%E5%B0%84%E2%80%94%E2%80%94%E5%8A%A8%E6%80%81%E4%BB%A3%E7%90%86/  这里开头获取构造器然后反射的过程）

### jdk 代理和Cglib代理的对比

1. jdk动态代理针对实现接口的类，cglib针对任何可以被继承的类
2. jdk是利用拦截器 InvocationHandler 加上反射机制生成的一个代理类，在调用具体方法前调用InvokeHandler来处理；Cglib是通过修改字节码生成子类实现代理。
3. spring中默认是使用jdk动态代理，但是遇到没实现接口的类还是使用cglib，这样才会效率最大化。
4. 效率上随着jdk版本的升级，在调用次数较少的情况下jdk代理的效率高于cglib，而较多的情况下两者差距也不明显，具体还是以实践为主。

## Spring中使用AOP

先读文章：https://www.cnblogs.com/wanghq1994/p/12187186.html、https://segmentfault.com/a/1190000021821314

### 相关注解

- @Pointcut

  **定义一个切点**，里面的表达式一般表示切点切入的方法范围

- @Before

  类似的还有after、AfterThrowing等等，**定义一个增强**，表示在切点之前或者之后或者抛异常后等等情况具体怎么做。

- @Aspect

  定义一个切面类。切面包含了上面的切点和增强

- @EnableAspectJAutoProxy(proxyTargetClass = false)

  开启切面编程，false表示默认jdk动态代理，而true表示采用cglib动态代理，一般不强制使用。

  

还有很多相关注解，不过以上这三类就已经构成了一组常规的切面。