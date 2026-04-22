## <font style="color:#7E45E8;">面向过程语言和面向对象语言的区别</font>
面向过程语言和面向对象语言是两种主流的编程范式，也可以理解是两种思维、两种思想、两种模式、两种逻辑。

**<font style="color:#DF2A3F;">面向过程</font>**：当事件比较简单的时候，利用面向过程，注重的是事件的具体的步骤/过程，注重的是过程中的具体的行为，以函数为最小单位，**<font style="color:#DF2A3F;">考虑怎么做</font>**。关注的是功能与任务的实现过程。开发者需要关注的是解决问题的步骤和过程，以及如何通过函数和数据结构的设计来优化流程。它通常提供了丰富的结构化控制语句，比如循环和条件分支，使得程序员可以编写出流程清晰的代码。在面向过程语言中，程序员需要手动控制程序的执行流程，包括数据的传递、处理等各个方面，因此需要具备较高的编程能力和经验。一些典型的面向过程语言包括C、Fortran等。适合解决计算导向和行为导向的问题，特别是那些功能明确、逻辑简单的程序。在性能要求极高或资源受限的场景下，面向过程语言仍然是不可或缺的工具。

**<font style="color:#DF2A3F;">面向对象</font>**：**<font style="color:#DF2A3F;">注重找“参与者”</font>**，谁的数据谁处理，将功能封装进对象，强调具备了功能的对象，以类/对象为最小单位，**<font style="color:#DF2A3F;">考虑谁来做</font>**。关注的是对象的状态和行为。它将构成问题事务分解成各个对象，每个对象都有其属性和方法，通过对象的交互来实现功能。能够更好地实现模块化、封装、继承等面向对象编程特性。适合建模复杂的系统和交互操作。它提供了更好的结构和可维护性，使得开发者能够更清晰地描述问题域，并通过对象的交互来实现功能。

通过一个经典案例来解释面向过程与面向对象的区别——人把大象装入冰箱。（伪代码展示）

+ **<font style="color:#DF2A3F;">面向过程</font>**	

函数1：

```java
打开冰箱( ) {
    人站在冰箱前，打开冰箱;
    冰箱开到30度角的时候，冰箱的灯打开了;
    ......
}
```

函数2：

```java
储存大象( ) {
    大象先迈左腿，再迈右腿；
    考虑冰箱能不能装下；
    ......
}
```

函数3：

```java
关闭冰箱( ) { 
    人站在冰箱前，关闭冰箱；
    冰箱开到30度角的时候，冰箱的灯关闭了;
    ......
}
```

+ **<font style="color:#DF2A3F;">面向对象</font>**

参与者1：

```java
人 {
    打开(冰箱) {
        冰箱.打开();
    }
    存储(大象){
        大象.进入();
    }
 	关闭(冰箱){
        冰箱.关闭();
	}
}
```

参与者2：

```java
冰箱{
    打开(){ 
        冰箱开到30度角的时候，冰箱的灯打开了;
    }
 	关闭(){
        冰箱开到30度角的时候，冰箱的灯关闭了;
    }
}

```

参与者3：

```java
大象{
    进入(冰箱){
    	大象先迈左腿，再迈右腿；
    }
}
```

<font style="color:black;">面向过程关注的是事件的处理过程，一般以函数为最小单位，思考第一步、第二步、第三步……怎么做，事件较简单时，可以考虑用面向过程思维来处理。</font>

<font style="color:black;">面向对象关注的是事件的参与者，将参与者的行为（方法）、特性（属性）封装到对象中，以对象和类为最小处理单位宏观把控参与者，事件较复杂时，可以考虑用面向对象思维来处理。</font>

<font style="color:black;">面向对象的参与者在具体完成某个行为的时候，内部的细节处理还是面向过程的思维，所以</font>**<font style="color:#DF2A3F;">面向对象和面向过程相辅相成，并不是独立的</font>**<font style="color:black;">。</font>

## <font style="color:#7E45E8;">Java跨平台原理的解释</font>
<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736124485636-b9a042fd-a2b2-4190-aae7-4bc3dede837c.png" width="1496" title="" crop="0,0,1,1" id="Nf2I5" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">什么是Java语言？</font>
Java是一种高级编程语言，由Sun Microsystems（现为Oracle Corporation）于1995年推出。Java以“一次编写，到处运行”的理念著称，特点是跨平台、简单易学、安全可靠、具有良好的可扩展性和可移植性，在Web应用程序、移动应用程序、企业应用程序、大数据处理和人工智能等领域广泛应用。Java可以在多种系统上运行，包括Windows、Linux和macOS等操作系统，使得Java成为世界上最流行的编程语言之一。

## <font style="color:#7E45E8;">Java语言有哪些主要特点？</font>
<font style="background-color:rgb(253, 253, 254);">Java语言以其简单易学、面向对象、跨平台性、垃圾回收机制、多线程、安全性、高性能、丰富的类库和API以及函数式编程支持等特点，在软件开发领域得到了广泛应用和认可。</font>

1. 简单易学：语法简单，上手容易，<font style="background-color:rgb(253, 253, 254);">没有C++中容易混淆的概念，例如头文件、指针、结构、单元、运算符重载和虚拟基础类等</font>；
2. 面向对象：封装，继承，多态，<font style="background-color:rgb(253, 253, 254);">符合人类的思维习惯，</font>可以让程序设计更加模块化、易维护；
3. <font style="background-color:rgb(253, 253, 254);">跨平台性：</font>Java 虚拟机实现平台无关性，<font style="background-color:rgb(253, 253, 254);">一次编译，处处运行，Java编写的程序可以在任何安装了Java虚拟机（JVM）的计算机上正确运行</font>；
4. 支持多线程：<font style="background-color:rgb(253, 253, 254);">允许多个任务同时执行，实际上是处理器在不同线程之间快速切换造成的错觉</font>；
5. 编译与解释并存：<font style="background-color:rgb(253, 253, 254);">把程序编译为称作字节码，字节码在JVM上解释执行</font>；
6. <font style="background-color:rgb(253, 253, 254);">垃圾回收机制</font><font style="background-color:rgb(253, 253, 254);">：垃圾回收机制（Garbage Collection，GC），能够自动回收程序不再使用的内存空间</font>
7. 可靠性：具备异常处理和自动内存管理机制；
8. 安全性：<font style="background-color:rgb(253, 253, 254);">通过提供安全管理器和安全策略等机制</font>；
9. 高性能：解释性语言，字节码，运行在JVM上，通过 JIT编译器技术的优化，具有较高的执行效率；
10. <font style="background-color:rgb(253, 253, 254);">丰富的类库和API：Java标准库提供了大量的类库和API，涵盖了网络通信、文件处理、数据库连接等各个方面，使得Java编程更加高效、快速和方便。</font>
11. <font style="background-color:rgb(253, 253, 254);">函数式编程支持：Java 8及以后的版本增加了对函数式编程的支持（如Lambda表达式），使得程序员能够以更简洁的方式编写代码。</font>
12. 广泛应用：Java<font style="background-color:rgb(253, 253, 254);">在Web开发、移动应用开发（特别是Android平台）、企业级应用、大数据处理及人工智能等领域均有广泛应用，展现了其强大的生命力和灵活性。</font>

## <font style="color:#7E45E8;">Java的安全性体现在哪几个方面？</font>
<font style="background-color:rgb(253, 253, 254);">（一）跨平台安全性</font>

<font style="background-color:rgb(253, 253, 254);">Java程序的运行不依赖于特定的操作系统或硬件平台，而是通过Java虚拟机（JVM）实现跨平台运行。JVM作为中间层，可以屏蔽底层平台的差异性和潜在的安全漏洞，从而保护Java程序免受底层平台安全问题的影响。</font>

<font style="background-color:rgb(253, 253, 254);">（二）面向对象安全性</font>

<font style="background-color:rgb(253, 253, 254);">Java是一种纯面向对象的语言，通过封装、继承和多态等特性来组织代码。封装特性使得Java能够隐藏对象的内部状态，只通过公共的接口与外界交互，从而减少了外部对内部状态的直接访问，提高了数据的安全性。</font>

<font style="background-color:rgb(253, 253, 254);">（三）严格的安全机制</font>

1. <font style="background-color:rgb(253, 253, 254);">无指针运算：Java中不直接支持指针操作，而是通过引用（reference）来访问对象。这种机制避免了指针的野指针、越界等问题，提高了内存级的安全性。（有指针：c，go等）</font>
2. <font style="background-color:rgb(253, 253, 254);">数组边界检查</font><font style="background-color:rgb(253, 253, 254);">：Java在数组访问时会进行边界检查，防止数组越界访问，从而避免了C/C++中常见的缓存溢出等安全漏洞。</font>
3. <font style="background-color:rgb(253, 253, 254);">强制类型转换</font><font style="background-color:rgb(253, 253, 254);">：Java要求在进行类型转换时必须进行显式转换，如果转换类型不兼容，会抛出</font>`<font style="background-color:rgb(253, 253, 254);">ClassCastException</font>`<font style="background-color:rgb(253, 253, 254);">，这有助于在编译时或运行时发现潜在的错误。</font>
4. <font style="background-color:rgb(253, 253, 254);">安全管理器（SecurityManager）：Java提供了一个安全管理器，用于限制Java程序对系统资源的访问权限，如文件访问、网络访问等。通过配置安全管理器，可以进一步增强Java程序的安全性。要启用安全管理器，你需要在程序启动时通过</font>`<font style="background-color:rgb(253, 253, 254);">System.setSecurityManager(SecurityManager s)</font>`<font style="background-color:rgb(253, 253, 254);">方法设置一个安全管理器实例。一旦设置了安全管理器，JVM在执行受保护的操作之前就会自动调用相应的方法进行权限检查。</font>

<font style="background-color:rgb(253, 253, 254);">安全管理器的主要方法包括（但不限于）：</font>

+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">checkPropertyAccess(String key)</font>`<font style="background-color:rgb(253, 253, 254);">: 检查对系统属性的访问。</font>
+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">checkRead(String file)</font>`<font style="background-color:rgb(253, 253, 254);">: 检查对文件的读取权限。</font>
+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">checkWrite(String file)</font>`<font style="background-color:rgb(253, 253, 254);">: 检查对文件的写入权限。</font>
+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">checkExecute(String file)</font>`<font style="background-color:rgb(253, 253, 254);">: 检查对文件的执行权限。</font>
+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">checkConnect(String host, int port)</font>`<font style="background-color:rgb(253, 253, 254);">: 检查对网络连接的权限。</font>
+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">checkCreateClassLoader()</font>`<font style="background-color:rgb(253, 253, 254);">: 检查创建类加载器的权限。</font>

<font style="background-color:rgb(253, 253, 254);">（四）字节码验证与沙盒环境</font>

<font style="background-color:rgb(253, 253, 254);">Java编译器将源代码编译成字节码，字节码验证器（</font><font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Java字节码验证器位于JVM的内部</font><font style="background-color:rgb(253, 253, 254);">）在运行时验证字节码的完整性，确保执行的代码是安全的。同时，Java程序在受限的沙盒环境中运行，这限制了它们对系统资源的访问，防止程序执行未经授权的操作，如访问文件系统或网络。在沙盒环境中，Java程序只能访问被明确允许的资源，并且其执行行为也受到严格的监控和限制。例如，一个Java程序可能被限制为只能读取特定目录下的文件，或者只能与特定的网络地址进行通信。这些限制是通过配置安全管理器（SecurityManager）和相应的安全策略来实现的。</font><font style="color:#2A4200;background-color:rgb(253, 253, 254);">[沙盒（Sandbox），计算机专业术语，在计算机安全领域中是一种安全机制，具体指为运行中的程序提供的隔离环境。]</font>

## <font style="color:#7E45E8;">Java的开发环境主要包括哪些？</font>
Java的开发环境主要包括以下几个关键组件：

1. **JDK（Java Development Kit）**：
    - JDK是Java开发环境的核心组件，包含了Java编译器（javac）、Java运行时环境（JRE）、Java开发工具（如调试器、性能监视器等）以及Java标准库（API）。
    - JDK是Java程序员开发Java应用程序所必需的软件包，提供了编写、编译、调试和运行Java程序所需的一切工具和库。
2. **JRE（Java Runtime Environment）**：
    - JRE是运行Java程序所必需的环境，包含了Java虚拟机（JVM）、Java平台核心类库和支持文件。
    - 当用户想要执行Java程序时，需要安装JRE。JRE负责将Java字节码翻译成机器语言并执行。
    - 某些情况下，JDK安装目录下可能没有显式的jre文件夹，但这并不意味着JRE未安装。JDK 9及以上版本开始，模块化的引入使得JRE的组件不再像以往那样以文件夹的形式显式存在，而是通过模块系统来管理。
3. **IDE（Integrated Development Environment，集成开发环境）**：
    - IDE是一种集成开发环境，提供了代码编辑器、编译器、调试器、版本控制、自动化构建、测试等功能，极大地提高了开发效率。
    - 比较流行的Java IDE有Eclipse、IntelliJ IDEA、NetBeans等。这些IDE通常具有友好的用户界面、丰富的插件生态系统以及强大的代码提示和调试功能。
4. **构建工具**：
    - 构建工具用于自动化地构建和打包Java代码，简化了项目管理和部署过程。
    - 比较流行的Java构建工具有Maven和Gradle等。这些工具支持依赖管理、项目构建、打包和发布等功能。
5. **版本控制系统**：
    - 版本控制系统是一种管理源代码修改历史记录的工具，可以跟踪源代码修改并协同开发。
    - 比较流行的版本控制系统有Git、SVN等。这些工具帮助开发者管理代码版本、协作开发以及解决代码冲突等问题。
6. **测试工具**：
    - 测试工具用于对Java应用程序进行单元测试、集成测试、性能测试等，确保代码的质量和稳定性。
    - JUnit是最为流行的Java单元测试框架之一，此外还有其他测试框架和工具如TestNG、Selenium等。
7. **应用服务器**：
    - Java应用服务器是一种运行Java应用程序的Web服务器，支持Java EE规范，提供了丰富的企业级服务。
    - 比较流行的Java应用服务器有Tomcat、Jetty、JBoss（WildFly）、WebLogic等。这些服务器支持Servlet、JSP、EJB等技术，并提供了负载均衡、事务管理、安全性等企业级功能。

综上所述，Java的开发环境是一个包含多个组件的复杂系统，这些组件共同支持Java应用程序的开发、测试、部署和运行。在选择和开发Java开发环境时，开发者需要根据自己的需求和项目特点来合理配置和使用这些组件。

## <font style="color:#7E45E8;">什么是Java虚拟机？</font>
Java虚拟机（Java Virtual Machine，JVM）是Java程序执行的环境，Java程序编译成的.class文件可以在JVM上运行并执行。JVM是Java软件发挥跨平台优势的关键。

Java程序员将原始Java代码编写后，用Java编译器编译成字节码（即.class文件），这些字节码不是在特定的计算机体系结构上运行的机器代码，而是在JVM上解释执行的。这样，Java程序可以在任何装有JVM的计算机上运行，不需要针对不同的计算机架构编写不同的程序。

JVM是一个抽象的计算机，<font style="background-color:rgb(253, 253, 254);">在实际的计算机上通过软件模拟来实现。它是Java语言的运行环境，它有自己的指令集和内存模型，使得Java程序能够在不同的操作系统和硬件平台上运行而无需修改</font>。它负责将字节码解释成为计算机可以理解的指令并执行，同时管理程序的内存以及进行垃圾回收等操作，确保Java程序运行的安全和高效。JVM还提供了多种调优和监控功能，以便开发人员可以更好地优化Java程序的性能。

## <font style="color:#7E45E8;">JDK、JRE、JVM、JIT四者的关系</font>
```java
JAVAEE
  |
JAVA SE
  |
  +-- JDK (开发工具包)
  |     |
  |     +-- JRE (运行时环境)
  |     |     |
  |     |     +-- JVM (Java虚拟机)
  |     |
  |     +-- 工具包 (javac, java等)
  |
  +-- JRE (运行时环境)
        |
        +-- JVM (Java虚拟机)
              |
              +-- JIT (即时编译器)
```

1. **<font style="background-color:rgb(253, 253, 254);">JVM（Java虚拟机）</font>**<font style="background-color:rgb(253, 253, 254);">：</font>
    - <font style="background-color:rgb(253, 253, 254);">JVM是Java class运行的虚拟机，它提供了Java程序执行的环境。JVM负责加载、执行和卸载Java类，管理内存和垃圾回收等。</font>**<font style="background-color:rgb(253, 253, 254);"> </font>**
2. **<font style="background-color:rgb(253, 253, 254);">JRE（Java运行时环境）</font>**<font style="background-color:rgb(253, 253, 254);">：</font>
    - <font style="background-color:rgb(253, 253, 254);">JRE是Java程序运行所必须的环境，它包含了JVM和Java平台核心类库等运行时组件。JRE使得Java程序能够在没有JDK的计算机上运行。</font>
3. **<font style="background-color:rgb(253, 253, 254);">JDK（Java开发工具包）</font>**<font style="background-color:rgb(253, 253, 254);">：</font>
    - <font style="background-color:rgb(253, 253, 254);">JDK是JRE的扩展，它除了包含JRE之外，还提供了开发工具包，如Java编译器（javac）、Java运行工具（java）、Java调试器（jdb）等。JDK主要用于Java程序的开发和调试。</font>
4. **<font style="background-color:rgb(253, 253, 254);">JIT（即时编译器）</font>**<font style="background-color:rgb(253, 253, 254);">：</font>
    - <font style="background-color:rgb(253, 253, 254);">JIT是JVM的一个重要组成部分</font>
    - <font style="background-color:rgb(253, 253, 254);">JIT编译器能够针对热点代码（即被频繁调用的代码段）进行优化。通过即时编译，JIT可以将这些热点字节码转换为与当前硬件平台紧密相关的机器代码，从而充分利用处理器的指令集和缓存等特性，提高程序的运行速度</font>
    - <font style="background-color:rgb(253, 253, 254);">在没有JIT编译器的情况下，JVM通常使用解释器来逐条解释执行字节码。这种解释执行的方式虽然灵活，但性能较低。JIT编译器的引入，可以减少解释器的使用频率，从而降低解释执行的开销。</font>

## <font style="color:#7E45E8;">JDK和JRE有什么区别？</font>
JDK（Java Development Kit）和 JRE（Java Runtime Environment）是Java的开发工具包和运行环境。

JDK包括JRE，同时也包含编译器（javac）、调试器（jdb）、java文档工具（javadoc）等工具。JDK是开发和编译Java程序所必需的工具，也可以运行Java程序。

JRE是Java程序的运行环境，包括Java虚拟机（JVM）、Java核心类库和其他各种支持文件。如果仅仅想运行Java程序，那么只需要安装JRE即可。

因此，JDK适合进行Java应用程序的开发，而JRE适合于运行Java应用程序。

<img src="https://cdn.nlark.com/yuque/0/2025/png/47623520/1736061457190-46232672-51a1-457d-8341-e9ffc5678fa2.png?x-oss-process=image%2Fformat%2Cwebp" width="712" title="" crop="0,0,1,1" id="NFUPS" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">Java有哪几种注释？</font>
Java中的注释主要有三种形式，这三种注释形式在Java编程中都有其特定的用途和场景，合理使用注释可以提高代码的可读性和可维护性：

1. **单行注释**：
    - 使用双斜杠（//）开头，仅在该行有效。
    - 适用于对少量代码或特定代码行进行简单说明。
    - 示例：`// 这是一个单行注释`
2. **多行注释**：
    - 使用/* 开始，以 */结束，可以跨越多行。
    - 适用于对一大段代码或复杂逻辑进行详细解释。
    - 示例：`/* 这是一个多行注释，它可以跨越多行 */`
3. **文档注释**：
    - 使用/** 开始，以 */结束，通常出现在类、方法、字段等的声明前面。
    - 用于生成代码文档，如API文档，这种注释可以被工具（如Javadoc）提取并生成相应的文档。
    - 文档注释可以包含特定的标签，如@param用于描述方法参数，@return用于描述返回值，@throws用于描述可能抛出的异常等。
    - 示例：`/** * 这是一个文档注释示例 * 它通常包含有关类、方法或字段的详细信息 */`

```java
/**
 * @author zss 
 * @version 1.0
 */
public class Demo {
    /**
     * @param age
     * @return
     * @throws Exception
     */
    public int testmethod(int age) throws Exception {
        int num = 10;
        if(num == 1){
            throw new Exception();
        }
        return 10;
    }
}

```

生成API示例：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736144689813-639f110f-52ca-4528-afba-4b946f63123e.png" width="696.8" title="" crop="0,0,1,1" id="u649950f4" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736144765134-512519a7-b50d-4b15-98a3-5fb5d8ca5e8f.png" width="504.8" title="" crop="0,0,1,1" id="ue591217f" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">Java中的关键字有哪些？</font>
Java关键字一共有53个，其中包括48个关键字、2个保留字和3个特殊直接量。具体来说：

+ 48个关键字

访问修饰符：`public`、`protected`、`private`

类、接口、抽象类和实现接口、继承类、实例化对象：`class`、`interface`、`abstract`、`implements`、`extends`、`new`

包相关：`import`、`package`

数据类型：`byte`、`char`、`boolean`、`short`、`int`、`float`、`long`、`double`、`void`

条件循环：`if`、`else`、`while`、`for`、`switch`、`case`、`default`、`do`、`break`、`continue`、`return`、`instanceof`

修饰方法、类、属性和变量：`static`、`super`、`final`、`this`、`native`、`strictfp`、`synchronized`、`transient`、`volatile`

错误处理：`catch`、`try`、`finally`、`throw`、`throws`

其他：`enum`、`assert`

+ 2个保留字

`const`、`goto`（这两个保留字在Java中目前没有实际用途，但可能在未来的Java版本中被用作关键字）

+ 3个特殊直接量

`null`、`true`、`false`

## <font style="color:#7E45E8;">成员变量与局部变量的区别？</font>
<font style="color:black;">由于变量声明的位置不同，可以将变量分为成员变量和局部变量。</font>

**<font style="color:#E4495B;">成员变量</font>**<font style="color:black;">位于类中、方法之外的变量，即属性。</font>

**<font style="color:#E4495B;">局部变量</font>**<font style="color:black;">位于类中、并处于方法中或代码块中的变量。</font>

<font style="color:black;">成员变量和局部变</font><font style="color:black;">量有如下</font><font style="color:black;">6</font><font style="color:black;">个区别。</font>

+ <font style="color:black;">声明位置不同。</font>

<font style="color:black;">成员变量：类中、方法之外。</font>

<font style="color:black;">局部变量：类中、方法中/代码块中。</font>

+ <font style="color:black;">作用范围不同。</font>

<font style="color:black;">成员变量：整个类中。</font>

<font style="color:black;">局部变量：当前的方法</font><font style="color:black;">/</font><font style="color:black;">当前的代码块。</font>

+ <font style="color:black;">是否有默认值。</font>

<font style="color:black;">成员变量：如果属性没有赋值，有默认初始值。</font>

<font style="color:black;">局部变量：无默认值。</font>

| 数组类型 | 默认初始值 |
| :---: | :---: |
| byte类型 | 0 |
| short类型 | 0 |
| int类型 | 0 |
| long类型 | 0 |
| float类型 | 0.0 |
| double类型 | 0.0 |
| char类型 | '\u0000' |
| boolean类型 | false |
| 引用数据类型 | null |


+ <font style="color:black;">是否需要初始化。</font>

<font style="color:black;">成员变量：不需要初始化，有默认初始值。</font>

<font style="color:black;">局部变量：必须进行初始化，否则报错。</font>

+ <font style="color:black;">在内存中的位置。</font>

<font style="color:black;">成员变量：在堆内存中。</font>

<font style="color:black;">局部变量：在栈内存中。</font>

+ <font style="color:black;">作用时间不同。</font>

<font style="color:black;">成员变量：从对象的创建阶段开始，到消亡之前结束。</font>

<font style="color:black;">局部变量：当前方法或代码块执行结束，局部变量就会消失。</font>

## <font style="color:#7E45E8;">静态变量有什么作用？</font>
<font style="color:black;">在Java编程语言中，静态变量（也称为类变量）是定义在类内部、方法外部的变量，并使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">static</font>`<font style="color:black;">关键字进行修饰。静态变量与类的实例（对象）无关，而是属于类本身。这意味着，无论创建了多少个类的实例，静态变量在内存中只会有一个副本，并且由所有实例共享。</font>

<font style="color:black;">以下是Java中静态变量的主要作用：</font>

1. <font style="color:black;">共享数据</font><font style="color:black;">：</font>
    - <font style="color:black;">静态变量允许类的所有实例共享同一个数据值。例如，你可以使用静态变量来跟踪类的实例数量，或者存储与类本身相关的配置信息。</font>
2. <font style="color:black;">访问便利性</font><font style="color:black;">：</font>
    - <font style="color:black;">静态变量可以通过类名直接访问，而无需创建类的实例。这提供了在不需要对象上下文的情况下访问数据的便利性。</font>
3. <font style="color:black;">实现常量</font><font style="color:black;">：</font>
    - <font style="color:black;">静态变量通常用于定义常量，即其值在程序执行期间不会改变的变量。这些常量通常使用大写字母和下划线命名（例如，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">MAX_VALUE</font>`<font style="color:black;">），并通过</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">public static final</font>`<font style="color:black;">进行修饰，以表示它们是公开的、静态的且不可变的。</font>
4. <font style="color:black;">节省内存</font><font style="color:black;">：</font>
    - <font style="color:black;">由于静态变量在内存中只有一个副本，并且被类的所有实例共享，因此它们可以节省内存空间。这对于需要大量实例且每个实例都需要访问相同数据的类来说尤其有用。</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736146939378-b75f613f-fb9d-47d0-9bc0-662dcb20b534.png" width="1104.8" title="" crop="0,0,1,1" id="u4409413c" class="ne-image" style="font-size: 16px">



## <font style="color:#7E45E8;">静态方法和实例方法有何不同？</font>
<font style="color:black;">在Java中，静态方法（Static Method）和实例方法（Instance Method）是两种重要的方法类型，它们在定义、调用方式、访问权限、内存管理等方面存在显著差异。以下是对这两种方法的详细比较：</font>

<font style="color:black;">一、定义与声明</font>

+ <font style="color:black;">静态方法</font><font style="color:black;">：使用static关键字修饰的方法。它属于类本身，而不是类的实例（对象）。静态方法可以在不创建类实例的情况下通过类名直接调用。</font>
+ <font style="color:black;">实例方法</font><font style="color:black;">：没有使用static关键字修饰的方法。它属于类的实例，必须通过类的对象（实例）来调用。</font>

<font style="color:black;">二、调用方式</font>

+ <font style="color:black;">静态方法</font><font style="color:black;">：可以直接通过类名调用，无需创建类的实例。例如：</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ClassName.staticMethod();</font>`
+ <font style="color:black;">实例方法</font><font style="color:black;">：必须通过类的对象（实例）来调用。例如：首先创建对象</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ClassName obj = new ClassName();</font>`<font style="color:black;">，然后通过对象调用方法</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">obj.instanceMethod();</font>`

<font style="color:black;">三、访问权限与成员</font>

+ <font style="color:black;">静态方法</font><font style="color:black;">：只能访问静态变量和静态方法，不能直接访问实例变量和实例方法。如果需要访问实例变量或方法，必须通过对象引用。</font>
+ <font style="color:black;">实例方法</font><font style="color:black;">：可以访问实例变量和实例方法，也可以访问静态变量和静态方法。</font>

<font style="color:black;">四、内存管理与生命周期</font>

+ <font style="color:black;">静态方法</font><font style="color:black;">：在类加载时被加载到内存中，属于类的共享部分。不会为每个对象单独创建静态方法的副本。静态方法的生命周期与类相同，类加载时静态方法也随之加载，类卸载时静态方法也随之卸载。</font>
+ <font style="color:black;">实例方法</font><font style="color:black;">：在每个对象中都有一个副本，属于对象的非共享部分。每个对象都可以有不同的状态（实例变量的值），因此实例方法可以根据对象的状态进行不同的操作。</font>

<font style="color:black;">五、适用场景与特性</font>

+ <font style="color:black;">静态方法</font><font style="color:black;">：适用于工具类或不依赖于对象状态的方法，例如数学运算、字符串处理等。静态方法是线程安全的，因为它们属于类而不是类的实例。多个线程可以同时调用同一个静态方法而不会产生冲突。静态方法不能被重写（Override），但可以被隐藏（Hide）。</font>
+ <font style="color:black;">实例方法：适用于需要依赖于对象状态的方法，例如处理对象属性或行为的方法。实例方法可以访问和修改对象的内部状态。</font>

## <font style="color:#7E45E8;">静态方法为什么不能调用非静态成员?</font>
+ <font style="color:black;">静态成员（变量和方法）属于类本身，它们在类加载时被初始化，并且在整个程序运行期间都保持其状态（直到类被卸载）。静态成员不依赖于任何特定的类实例。</font>
+ <font style="color:black;">非静态成员（实例变量和实例方法）属于类的实例（对象）。每个对象都有自己的一套非静态成员，这些成员的状态是独立的，并且依赖于对象的生命周期。非静态成员必须在对象被创建后才能被访问或修改。</font>

## <font style="color:#7E45E8;">静态变量和实例变量的区别？ </font>
静态变量前要加static关键字，而实例变量前则不加。

实例变量属于某个对象的属性，必须创建了实例对象，其中的实例变量才会被分配空间，才能使用这个实例变量。

静态变量属于类，也称为类变量，只要程序加载了类的字节码，不用创建任何实例对象，静态变量就会被分配空间，静态变量可以直接使用类名来引用。

## <font style="color:#7E45E8;">是否可以从一个static方法内部发出对非static方法的调用？ </font>
不可以，因为非static方法是要与对象关联在一起的，必须创建一个对象后，才可以在该对象上进行方法调用，而static方法调用时不需要创建对象，可以直接调用。也就是说，当一个static方法被调用时，可能还没有创建任何实例对象。

## <font style="color:#7E45E8;">字符型常量和字符串常量的区别?</font>
<font style="color:black;">在Java中，字符型常量和字符串常量是两种不同的数据类型，它们之间存在显著的区别。以下是对这两者的详细比较：</font>

<font style="color:black;">一、定义方式不同</font>

+ <font style="color:black;">字符型常量：字符型常量是由单个字符组成的，用单引号括起来。例如：'A'、'b'、'1'等。</font>
+ <font style="color:black;">字符串常量：字符串常量是由多个字符组成的，用双引号括起来。例如："Hello"、 "World"等。</font>

<font style="color:black;">二、数据类型不同</font>

+ <font style="color:black;">字符型常量：字符型常量属于char类型，在内存中占用2个字节，用于存储单个字符。</font>
+ <font style="color:black;">字符串常量：字符串常量属于String类型，在内存中以字符数组的形式存在，可以存储任意数量的字符。</font>

<font style="color:black;">三、长度不同</font>

+ <font style="color:black;">字符型常量：只能包含一个字符。</font>
+ <font style="color:black;">字符串常量：可以包含零个或多个字符。</font>

<font style="color:black;">四、内存表示不同</font>

+ <font style="color:black;">字符型常量：在内存中占用固定的2个字节，用于存储字符的Unicode编码值。</font>
+ <font style="color:black;">字符串常量：在内存中以字符数组的形式存在，每个字符都有一个对应的Unicode编码值，并且字符串常量还包含一些额外的信息，如长度、哈希码等。</font>

<font style="color:black;">五、操作方法不同</font>

+ <font style="color:black;">字符型常量：可以进行一些基本的字符操作，如比较（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">==</font>`<font style="color:black;">运算符）、转换大小写（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Character</font>`<font style="color:black;">类中的方法）等。</font>
+ <font style="color:black;">字符串常量：可以进行更复杂的字符串操作，如连接（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">+</font>`<font style="color:black;">运算符或</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">StringBuilder</font>`<font style="color:black;">类）、截取（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">substring</font>`<font style="color:black;">方法）、替换（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">replace</font>`<font style="color:black;">方法）等。此外，字符串常量还可以使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">String</font>`<font style="color:black;">类中的大量方法来进行各种操作，如比较（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">equals</font>`<font style="color:black;">方法）、查找（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">indexOf</font>`<font style="color:black;">方法）、分割（使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">split</font>`<font style="color:black;">方法）等。</font>

<font style="color:black;">六、示例代码</font>

<font style="color:black;">以下是一些示例代码，用于展示字符型常量和字符串常量的使用：</font>

```java
// 字符型常量
char c = 'A';
System.out.println(c); // 输出: A

// 字符串常量
String str = "Hello";
System.out.println(str); // 输出: Hello

// 字符型常量操作
char c1 = 'a';
char c2 = 'A';
System.out.println(c1 == c2); // 输出: false（因为字符比较是区分大小写的）

// 字符串常量操作
String str1 = "Hello";
String str2 = "World";
String result = str1 + " " + str2;
System.out.println(result); // 输出: Hello World
```

## <font style="color:#7E45E8;">自增自减运算符</font>
自增运算符：

无论这个变量是否参与到运算中去，只要用++运算符，这个变量本身就加1操作

只是说如果变量参与到运算中去的话，对运算结果是产生影响：

看++在前还是在后，如果++在后：先运算，后加1；如果++在前，先加1，后运算

自减运算符：

无论这个变量是否参与到运算中去，只要用--运算符，这个变量本身就减1操作

只是说如果变量参与到运算中去的话，对运算结果是产生影响：

看--在前还是在后，如果--在后：先运算，后减1； 如果--在前，先减1，后运算

代码展示：

```java
public class TestOpe04{
    public static void main(String[] args){
        int a = 5;
        a++;//理解为：相当于  a=a+1 操作  
        System.out.println(a);//6
        
        a = 5;
        ++a;//理解为：相当于  a=a+1 操作  
        System.out.println(a); //6
        
        //总结：++单独使用的时候，无论放在前还是后，都是加1操作
        
        //将++参与到运算中：
        //规则：看++在前还是在后，如果++在后：先运算，后加1   如果++在前，先加1，后运算
        a = 5;
        int m = a++ + 7;//先运算  m=a+7  再加1：  a = a+1 
        System.out.println(m);//12
        System.out.println(a);//6
        
        a = 5;
        int n = ++a + 7;//先加1  a=a+1  再运算：  n = a+7 
        System.out.println(n);//13
        System.out.println(a);//6
    }
}
```

## <font style="color:#7E45E8;">移位运算符（用最有效率的方法算出4乘以8等于几?）</font>
+ <<   左移 

3<<2 = 12

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736148913008-68f08552-b63f-4dc8-b82c-539bc0d65711.png" width="433.6" title="" crop="0,0,1,1" id="ud126d1e6" class="ne-image" style="font-size: 16px">

面试题： 4乘以8最快的方式：  4<<3 

+ >> 有符号右移

6>>2 = 1

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736148955825-70ef59bf-77f8-44b9-be0f-dffda01dcf38.png" width="415.2" title="" crop="0,0,1,1" id="uad4b41e4" class="ne-image" style="font-size: 16px">

+ >>> 无符号右移

6>>>2  = 1

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736148984957-c6147fb8-1557-4948-a1ce-c0fa1399f02a.png" width="423.2" title="" crop="0,0,1,1" id="u75f1e3a9" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">各种运算符的优先级问题</font>
程序中经常使用一些复杂的表达式，复杂表达式中往往掺杂使用了多种运算符，这些运算符参与运算的先后顺序也不同。

| <font style="color:black;">优 先 级</font> | <font style="color:black;">运 算 符</font> | <font style="color:black;">描 </font><font style="color:black;">   </font><font style="color:black;">述</font> | <font style="color:black;">结 合 性</font> |
| :---: | --- | --- | :---: |
| <font style="color:black;">1</font> | <font style="color:black;">()</font> | <font style="color:black;">括号运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">2</font> | <font style="color:black;">!</font><font style="color:black;">、</font><font style="color:black;">+</font><font style="color:black;">（正号）、</font><font style="color:black;">−</font><font style="color:black;">（负号）</font> | <font style="color:black;">一元运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">2</font> | <font style="color:black;">～</font> | <font style="color:black;">位运算符</font> | <font style="color:black;">由右至左</font> |
| 2 | ++、− − | 自增与自减运算符 | 由右至左 |
| <font style="color:black;">3</font> | <font style="color:black;">*</font><font style="color:black;">、</font><font style="color:black;">/</font><font style="color:black;">、</font><font style="color:black;">%</font> | <font style="color:black;">算术运算符</font> | <font style="color:black;">由左至右</font> |
| 4 | +、− | 算术运算符 | 由左至右 |
| <font style="color:black;">5</font> | <font style="color:black;"><<</font><font style="color:black;">、</font><font style="color:black;">>></font> | <font style="color:black;">位左移、右移运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">6</font> | <font style="color:black;">></font><font style="color:black;">、</font><font style="color:black;">>=</font><font style="color:black;">、</font><font style="color:black;"><</font><font style="color:black;">、</font><font style="color:black;"><=</font> | <font style="color:black;">关系运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">7</font> | <font style="color:black;">==</font><font style="color:black;">、</font><font style="color:black;">!=</font> | <font style="color:black;">关系运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">8</font> | <font style="color:black;">&</font> | <font style="color:black;">位运算符、逻辑运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">9</font> | <font style="color:black;">^</font> | <font style="color:black;">位运算符、逻辑运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">10</font> | <font style="color:black;">|</font> | <font style="color:black;">位运算符、逻辑运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">11</font> | <font style="color:black;">&&</font> | <font style="color:black;">短路与运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">12</font> | <font style="color:black;">||</font> | <font style="color:black;">短路或运算符</font> | <font style="color:black;">由左至右</font> |
| <font style="color:black;">13</font> | <font style="color:black;">? :</font> | <font style="color:black;">条件运算符</font> | <font style="color:black;">由右至左</font> |
| <font style="color:black;">14</font> | <font style="color:black;">=</font><font style="color:black;">、</font><font style="color:black;">+=</font><font style="color:black;">、</font><font style="color:black;">−=</font><font style="color:black;">、</font><font style="color:black;">*=</font><font style="color:black;">、</font><font style="color:black;">/=</font><font style="color:black;">、</font><font style="color:black;">%=</font> | <font style="color:black;">赋值运算符、扩展赋值运算符</font> | <font style="color:black;">由右至左</font> |


<font style="color:black;">代码展示：</font>

```java
  5<6 | 'A'>'a' && 12* 6<= 45 + 23 && !true		// 优先计算!true
= 5<6 | 'A'>'a' && 12*6 <= 45+23 && false		// 优先计算*、+
= 5<6 | 'A'>'a' && 72 <= 68 && false     		// 优先计算<、>、<=
= true | false && false && false         		// 优先计算 |
= true && false && false                     	// 都是&&运算，由左到右计算即可
= false && false                             	// 计算&&运算
= false                                     	// 得到最终结果
```

<font style="color:black;">	优先级别不用一一记忆，一般在实际开发中很难用到像示例代码一样复杂的表达式，因为对开发者而言可读性太差了。如果真的想表示非常复杂的逻辑，用括号“()”来实现优先运算即可，遵照数学中“有括号先算括号里的”原则，简单方便可读性强。</font>

## <font style="color:#7E45E8;">java中有哪些流程控制语句？</font>
<font style="color:black;">一、条件语句</font>

1. <font style="color:black;">if语句</font><font style="color:black;">：</font>
    - <font style="color:black;">用于基于某个条件执行代码块。如果条件为真（true），则执行代码块。</font>
2. <font style="color:black;">if-else语句</font><font style="color:black;">：</font>
    - <font style="color:black;">用于基于条件执行一个代码块，如果条件为假（false），则执行另一个代码块。</font>
3. <font style="color:black;">if-else if-else语句</font><font style="color:black;">：</font>
    - <font style="color:black;">用于基于多个条件执行不同的代码块。如果某个条件为真，则执行与该条件对应的代码块；如果所有条件都不为真，则执行最后的else代码块（如果存在）。</font>

<font style="color:black;">二、选择语句</font>

1. <font style="color:black;">switch语句</font><font style="color:black;">：</font>
    - <font style="color:black;">用于基于不同的条件（通常是变量的值）执行不同的代码块。每个条件对应一个case标签，当变量的值与某个case标签匹配时，执行该case下的代码块。default标签是可选的，用于处理所有case都不匹配的情况。</font>

<font style="color:black;">三、循环语句</font>

1. <font style="color:black;">while循环</font><font style="color:black;">：</font>
    - <font style="color:black;">用于重复执行一段代码，直到给定的条件不再满足（即条件变为false）。</font>
2. <font style="color:black;">do-while循环</font><font style="color:black;">：</font>
    - <font style="color:black;">类似于while循环，但不同之处在于它至少会执行一次代码块，然后再检查条件。如果条件为真，则继续执行代码块。</font>
3. <font style="color:black;">for循环</font><font style="color:black;">：</font>
    - <font style="color:black;">用于重复执行一段代码指定的次数。它由初始化、条件和后续操作三个部分组成。在每次迭代之前，都会检查条件是否为真；如果为真，则执行代码块，并更新后续操作中的变量。</font>
4. <font style="color:black;">foreach循环（增强的for循环）</font><font style="color:black;">：</font>
    - <font style="color:black;">用于遍历数组或集合中的每个元素。它不需要知道集合的大小，而是自动处理元素的索引和迭代。</font>

## <font style="color:#7E45E8;">continue、break 和 return 的区别是什么？</font>
<font style="color:black;">在Java中，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">continue</font>`<font style="color:black;">、</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">break</font>`<font style="color:black;"> 和 </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return</font>`<font style="color:black;"> 是三个用于控制程序流程的关键字，它们各自有不同的用途和行为。</font>

<font style="color:black;">1. </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">continue</font>`

+ <font style="color:black;">用途</font><font style="color:black;">：用于跳过当前循环迭代中的剩余代码，并立即开始下一次迭代。</font>
+ <font style="color:black;">适用场景</font><font style="color:black;">：主要用在循环结构中（</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">for</font>`<font style="color:black;">、</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">while</font>`<font style="color:black;">、</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">do-while</font>`<font style="color:black;">）。</font>
+ <font style="color:black;">行为</font><font style="color:black;">：当执行到</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">continue</font>`<font style="color:black;">语句时，循环中</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">continue</font>`<font style="color:black;">之后的代码将不会执行，而是直接跳到循环的下一个迭代。</font>
+ <font style="color:black;">注意</font><font style="color:black;">：</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">continue</font>`<font style="color:black;">不能用于非循环结构中，否则会引发编译错误。</font>

<font style="color:black;">2. </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">break</font>`

+ <font style="color:black;">用途</font><font style="color:black;">：用于立即退出当前循环或</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">switch</font>`<font style="color:black;">语句。</font>
+ <font style="color:black;">适用场景</font><font style="color:black;">：可以用在循环结构（</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">for</font>`<font style="color:black;">、</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">while</font>`<font style="color:black;">、</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">do-while</font>`<font style="color:black;">）和</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">switch</font>`<font style="color:black;">语句中。</font>
+ <font style="color:black;">行为</font><font style="color:black;">：当执行到</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">break</font>`<font style="color:black;">语句时，会立即跳出当前的循环或</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">switch</font>`<font style="color:black;">语句，并继续执行之后的代码（如果有的话）。</font>
+ <font style="color:black;">注意</font><font style="color:black;">：</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">break</font>`<font style="color:black;">通常与某种条件判断一起使用，以避免无限循环。</font>

<font style="color:black;">3. </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return</font>`

+ <font style="color:black;">用途</font><font style="color:black;">：用于结束当前方法的执行，并将控制权返回给方法的调用者。</font>
+ <font style="color:black;">适用场景</font><font style="color:black;">：可以用在任何方法体中（包括构造方法）。</font>
+ <font style="color:black;">行为</font><font style="color:black;">：当执行到</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return</font>`<font style="color:black;">语句时，会立即结束当前方法的执行，并可选地返回一个值给方法的调用者（如果方法的返回类型不是</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">void</font>`<font style="color:black;">）。</font>
+ <font style="color:black;">注意：</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return</font>`<font style="color:black;">语句可以出现在方法的任何位置（除了静态初始化块、实例初始化块或构造方法中的某些受限情况）。在</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">void</font>`<font style="color:black;">方法中，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return</font>`<font style="color:black;">语句不需要返回值。</font>

## <font style="color:#7E45E8;">在JAVA中如何跳出当前的多重嵌套循环？ </font>
在Java中，要想跳出多重循环，可以在外面的循环语句前定义一个标签，然后在里层循环体的代码中使用带有标签的break 语句，即可跳出外层循环。例如，

```java
public class NestedLoopBreak {
    public static void main(String[] args) {
        outerLoop: // 这是一个标签，命名为outerLoop
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                System.out.println("i = " + i + ", j = " + j);
                if (i == 2 && j == 3) {
                    break outerLoop; // 跳出到outerLoop标签指定的循环
                }
            }
        }
        System.out.println("跳出循环后");
    }
}
```

## <font style="color:#7E45E8;">说说&和&&的区别</font>
&&逻辑与运算符，当运算符两边的表达式的结果都为true时，整个运算结果才为true，否则，只要有一方为false，则结果为false。

&&具有短路的功能，即如果第一个表达式为false，则不再计算第二个表达式。

&是位运算符，&表示按位与操作，当&操作符两边的表达式是boolean类型时，也可以作为逻辑与，但是两边的表达式都会参与运算。

&位运算符展示：

如：6&3 = 2

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736151251500-3f1d596c-5d94-403e-9e8b-ce28a0e09a9b.png" width="413.6" title="" crop="0,0,1,1" id="ua2966d4e" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">switch语句能否作用在byte、long及String上?</font>
在switch（expr）中，expr只能是int、byte、short、char、String、枚举类型。

expr只能是一个整数表达式或者枚举常量，整数表达式可以是int基本类型或Integer包装类型，由于byte,short,char都可以隐含转换为int，所以，这些类型以及这些类型的包装类型也是可以的。显然，long和String类型都不符合switch的语法规定，并且不能被隐式转换成int类型，所以，它们不能作用于swtich语句中。 在JDK7.0中对switch做了功能加强，可以接受String类型。

## <font style="color:#7E45E8;">short s1 = 1; s1 = s1 + 1;语法与 short s1 = 1; s1 += 1;语法，哪种是正确的？</font>
对于short s1 = 1; s1 = s1 + 1; 由于s1+1运算时会自动提升表达式的类型，所以结果是int型，再赋值给short类型s1时，编译器将报告需要强制转换类型的错误，可修改为s1 =(short)(s1 + 1)

对于short s1 = 1; s1 += 1;由于 += 是java语言规定的运算符，java编译器会对它进行特殊处理，因此可以正确编译。 

## <font style="color:#7E45E8;">char型变量中能不能存储一个中文汉字?为什么?</font>
char型变量是用来存储Unicode编码的字符的，Unicode编码字符集中包含了汉字，所以，char型变量中可以存储汉字，占用两个字节。 

## <font style="color:#7E45E8;">用最有效率的方法算出2乘以8等於几? </font>
2 << 3

因为将一个数左移n位，就相当于乘以了2的n次方，那么，一个数乘以8只要将其左移3位即可，而位运算CPU直接支持的，效率最高，所以，2乘以8等於几的最效率的方法是2 << 3。

## <font style="color:#7E45E8;">String是最基本的数据类型吗? </font>
基本数据类型包括byte、int、char、long、float、double、boolean和short。 

Java.lang.String类属于引用数据类型。

## <font style="color:#7E45E8;">String s="Hello"; s=s+" world!";执行后原始的String对象中的内容变了吗?</font>
没有，因为String被设计成不可变(immutable)类，所以它的所有对象都是不可变对象。s原先指向一个String对象，内容是 "Hello"，+操作后s不指向原来那个对象了，而指向了另一个String对象，内容为"Hello world!"，原来那个对象还存在于内存之中，只是s这个引用变量不再指向它了。

## <font style="color:#7E45E8;">String s = new String("xyz");创建了几个String Object? </font>
两个或一个。

"xyz"对应一个对象，这个对象放在字符串常量池中，常量"xyz"不管出现多少遍，都是常量池中的那一个。

new String每写一遍，就创建一个新的对象，它依据常量"xyz"对象的内容来创建一个新String对象。如果以前就用过"xyz"，这句代表就不会创建"xyz"自己了，直接从常量池拿。

## <font style="color:#7E45E8;">String相关内存</font>
+ <font style="color:#7E45E8;">String s = new String("xyz");创建了几个String Object? </font>

**<font style="color:rgb(15, 17, 21);">情况1：第一次执行这行代码（"xyz"不在常量池中）</font>**

<font style="color:rgb(15, 17, 21);">String s = new String("xyz");</font>

<font style="color:rgb(15, 17, 21);">会创建 2个 String对象：</font>

    1. <font style="color:rgb(15, 17, 21);">"xyz"</font><font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">- 字符串常量，存入字符串常量池</font>
    2. <font style="color:rgb(15, 17, 21);">new String("xyz") - 在堆中新建的String对象</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1758599467151-a5b248c9-0804-4b2d-aa41-b7be35cc374b.png" width="338.4" title="" crop="0,0,1,1" id="uff4cd046" class="ne-image">

**<font style="color:rgb(15, 17, 21);">情况2："xyz"已经在常量池中存在时</font>**

```java
// 之前已经有代码使用了"xyz"
String temp = "xyz";      // 第一次，创建常量池中的"xyz"
// ... 其他代码 ...
String s = new String("xyz");  // 只创建1个新对象
```

<font style="color:rgb(15, 17, 21);">只创建 1个 String对象：</font>

    - <font style="color:rgb(15, 17, 21);">堆中的新String对象（引用常量池中已存在的"xyz"）</font>
+ <font style="color:#7E45E8;">下面这条语句一共创建了多少个对象：String s="a"+"b"+"c"+"d";</font>

javac编译可以对字符串常量直接相加的表达式进行优化（编译期优化），不必要等到运行期去进行加法运算处理，而是在编译时去掉其中的加号，直接将其编译成一个这些常量相连的结果。上述代码被编译器在编译时优化后，相当于直接定义了一个 "abcd" 的字符串，所以只创建了一个String对象。

+ <font style="color:#7E45E8;">下面代码底层是如何实现的？</font>

```java
String s1 = "a";
String s2 = s1 + "b";// 运行时字符串拼接
String s3 = "a" + "b";
System.out.println(s2 == "ab");//false
System.out.println(s3 == "ab");//true 
```

编译后字节码分析：

```java
String s1 = "a";
String s2 = new StringBuilder().append(s1).append("b").toString();
```

步骤解析：

```java
// 步骤分解：
StringBuilder sb = new StringBuilder();  // 1. 创建StringBuilder对象
sb.append(s1);                           // 2. StringBuilder内部操作
sb.append("b");                          // 3. StringBuilder内部操作  
String s2 = sb.toString();               // 4. 创建新的String对象
```

内存：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1758599721550-d46a4dff-dc77-488d-9a39-d5eb39277f3a.png" width="300.8" title="" crop="0,0,1,1" id="u6150133d" class="ne-image">





## <font style="color:#7E45E8;">说明String 、StringBuilder及StringBuffer的区别。</font>
都可以储存和操作字符串，String类表示内容不可改变的字符串，而StringBuffer和StringBuilder类都表示内容可以被修改的字符串。

StringBuilder是线程不安全的，运行效率高，如果一个字符串变量是在方法里面定义，这种情况只可能有一个线程访问它，不存在不安全的因素了，则用StringBuilder。StringBuffer是线程安全的，如果要在类里面定义成员变量，并且这个类的实例对象会在多线程环境下使用，那么最好用StringBuffer。

## <font style="color:#7E45E8;">如何把一段逗号分割的字符串转换成一个数组?</font>
+ 方式1：使用String的split方法分割

```java
String str="aa,bb,cc,dd";
String[] strArr = str.split(",");
for (String s : strArr) {
    System.out.println(s);
}
```

+ 方式2：使用StringTokenizer字符串分隔解析类 
    - 构造器StringTokenizer(String str, String delim) ：构造一个用来解析str的StringTokenizer对象，并提供一个指定的分隔符。
    - boolean hasMoreTokens() ：返回是否还有分隔符。
    - String nextToken() ：返回从当前位置到下一个分隔符的字符串。

```java
StringTokenizer st = new StringTokenizer(str,",");
while(st.hasMoreTokens()){
    String s = st.nextToken();
    System.out.println(s);
}
```

## <font style="color:#7E45E8;">下面这条语句一共创建了多少个对象：String s="a"+"b"+"c"+"d";</font>
javac编译可以对字符串常量直接相加的表达式进行优化（编译期优化），不必要等到运行期去进行加法运算处理，而是在编译时去掉其中的加号，直接将其编译成一个这些常量相连的结果。上述代码被编译器在编译时优化后，相当于直接定义了一个 "abcd" 的字符串，所以只创建了一个String对象。

验证：

```java
String s1 = "a";
String s2 = s1 + "b";
String s3 = "a" + "b";
System.out.println(s2 == "ab");//false
System.out.println(s3 == "ab");//true 
```

## <font style="color:#7E45E8;">final关键字的作用</font>
+ final修饰变量

使用final关键字修饰一个基本数据类型的变量时，其值不可以变；修饰引用数据类型变量时，是指地址不能变，地址所指向的对象中的内容还是可以改变的。

```java
public class Student {
    int id;
    String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
}

```

```java
public class Demo {
    public static void main(String[] args) {
        final int NUM = 10;
        // NUM = 20;报错
        final Student s = new Student(1001,"feifei");
        // s = new Student(2002,"lulu");报错
        s.id = 9008;
        System.out.println(s.id);
    }
}
```

+ final修饰方法
    - **<font style="color:rgb(15, 17, 21);">作用</font>**<font style="color:rgb(15, 17, 21);">：防止子类重写（override）该方法。</font>
    - **<font style="color:rgb(15, 17, 21);">使用场景</font>**<font style="color:rgb(15, 17, 21);">：认为该方法实现已经完美，不希望被子类修改。</font>

```java
class Parent {
    // final方法，不能被子类重写
    public final void show() {
        System.out.println("这是父类的最终实现");
    }
    
    public void normalMethod() {
        System.out.println("普通方法可以重写");
    }
}

class Child extends Parent {
    // ❌ 编译错误：不能重写final方法
    // @Override
    // public void show() { }
    
    // ✅ 允许：重写普通方法
    @Override
    public void normalMethod() {
        System.out.println("子类重写了普通方法");
    }
}
```

+ final修饰类、
    - **<font style="color:rgb(15, 17, 21);">作用</font>**<font style="color:rgb(15, 17, 21);">：阻止类被继承。</font>
    - **<font style="color:rgb(15, 17, 21);">使用场景</font>**<font style="color:rgb(15, 17, 21);">：认为该类功能已经完整，不需要扩展，或者出于安全考虑不希望被继承。</font>

```java
// final类，不能被继承
final class StringUtils {
    public static boolean isEmpty(String str) {
        return str == null || str.length() == 0;
    }
}

// ❌ 编译错误：不能继承final类
// class MyStringUtils extends StringUtils { }
```

## <font style="color:#7E45E8;">使用final关键字修饰一个变量时，是引用不能变，还是引用的对象不能变？ </font>
使用final关键字修饰一个变量时，是指引用变量不能变，引用变量所指向的对象中的内容还是可以改变的。

```java
public class Student {
    int id;
    String name;

    public Student(int id, String name) {
        this.id = id;
        this.name = name;
    }
}

```

```java
public class Demo {
    public static void main(String[] args) {
        final int NUM = 10;
        // NUM = 20;报错
        final Student s = new Student(1001,"feifei");
        // s = new Student(2002,"lulu");报错
        s.id = 9008;
        System.out.println(s.id);
    }
}
```

## <font style="color:#7E45E8;">"=="和equals方法究竟有什么区别？</font>
==操作符专门用来比较两个变量的值是否相等，也就是用于比较变量所对应的内存中所存储的数值是否相同，要比较两个基本类型的数据或两个引用变量是否相等，只能用==操作符。

如果一个变量指向的数据是对象类型的，那么，这时候涉及了两块内存，对象本身占用一块内存（堆内存），变量也占用一块内存，例如Objet obj = new Object();变量obj是一个内存，new Object()是另一个内存，此时，变量obj所对应的内存中存储的数值就是对象占用的那块内存的首地址。对于指向对象类型的变量，如果要比较两个变量是否指向同一个对象，即要看这两个变量所对应的内存中的数值是否相等，这时候就需要用==操作符进行比较。

equals方法是用于比较两个独立对象的内容是否相同，它比较的两个对象是独立的。例如，对于下面的代码：

```java
String a=new String("foo");
String b=new String("foo");
```

两条new语句创建了两个对象，然后用a,b这两个变量分别指向了其中一个对象，这是两个不同的对象，它们的首地址是不同的，即a和b中存储的数值是不相同的，所以，表达式a==b将返回false，而这两个对象中的内容是相同的，所以，表达式a.equals(b)将返回true。

字符串的比较基本上都是使用equals方法。

如果一个类没有自己定义equals方法，那么它将继承Object类的equals方法，Object类的equals方法的实现代码如下：

```java
boolean equals(Object o){
    return this==o;
}
```

这说明，如果一个类没有自己定义equals方法，它默认的equals方法（从Object 类继承的）就是使用==操作符，也是在比较两个变量指向的对象是否是同一对象，这时候使用equals和使用==会得到同样的结果，如果比较的是两个独立的对象则总返回false。如果你编写的类希望能够比较该类创建的两个实例对象的内容是否相同，那么你必须覆盖equals方法，由你自己写代码来决定在什么情况即可认为两个对象的内容是相同的。

## <font style="color:#7E45E8;">hashCode方法的作用？</font>
一般来讲，equals这个方法是给用户调用的，如果你想判断2个对象是否相等，你可以重写equals方法，然后在代码中调用，就可以判断他们是否相等了。简单来讲，equals方法主要是用来判断从表面上看或者从内容上看，2个对象是不是相等。

hashcode方法一般用户不会去调用，比如在HashMap中，由于key是不可以重复的，在判断key是不是重复的时候就判断了hashcode这个方法，而且也用到了equals方法。和equals不同就在于他返回的是int型的，比较起来不直观。我们一般在覆盖equals的同时也要覆盖hashcode，让他们的逻辑一致。

## <font style="color:#7E45E8;">基本类型和包装类型的区别？</font>
<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Java中的基本类型（Primitive Types）和包装类型（Wrapper Classes）之间存在多个关键区别，这些区别主要体现在以下方面：</font>

<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">一、包含内容与性质</font>

+ 基本类型：只包含数据本身，不包含任何方法或操作。它们不是对象，因此没有对象的特性，如继承和多态。
+ 包装类型：不仅包含数据，还包含了一系列的方法（如类型转换、比较等）和属性，是对基本类型数据的封装。包装类型是对象，具有对象的所有特性，如继承自Object类的功能（如toString()、equals()等）。

二、声明方式与存储位置

+ 基本类型：直接声明变量并赋值，不需要使用new关键字。它们直接将值保存在栈内存中，访问速度较快。
+ 包装类型：需要使用new关键字在堆内存中分配内存空间，或者使用自动装箱（JDK 5及以上版本支持）来创建对象。包装类型将对象放在堆内存中，通过栈中的引用来调用它们，访问速度相对较慢，并且需要考虑垃圾回收等额外开销。

三、初始值

+ 基本类型：在声明时如果没有显式赋值，则会被赋予一个默认值。例如，int的默认值为0，boolean的默认值为false。
+ 包装类型：在声明时如果没有显式赋值，则默认值为null，因为它们是引用类型。

四、使用方式

+ 基本类型：直接用于数值计算、位运算等场景，效率较高。但由于它们不是对象，因此不能在需要对象的场合（如集合中）直接使用。
+ 包装类型：主要用于需要对象的地方，如集合（List、Map等）中只能存储对象，因此基本类型需要通过包装类来转换为对象才能存储在集合中。此外，包装类型还提供了丰富的操作方法和常量。

五、泛型适用性

+ 基本类型：不能直接用于泛型，因为泛型在编译时会进行类型擦除，而基本类型没有对应的类型信息可以擦除。
+ 包装类型：可以用作泛型的类型参数，因为它们是对象类型，具有类型信息。例如，可以使用List<Integer>来存储整数对象。

六、内存占用与性能

+ 基本类型：通常占用较少的内存空间，因为它们只存储数据本身。
+ 包装类型：由于它们是对象，因此需要额外的内存来存储对象头和引用等信息。这可能导致在大量使用包装类型时增加内存开销。此外，自动装箱和拆箱操作也会消耗一定的性能。

综上所述，Java中的基本类型和包装类型在包含内容、性质、声明方式、存储位置、初始值、使用方式、泛型适用性、内存占用与性能等方面都存在明显的区别。在开发中，应根据具体需求选择合适的类型以提高代码的可读性、可维护性和性能。

## <font style="color:#7E45E8;">包装类型的缓存机制了解么？</font>
Java包装类型的缓存机制是Java中一个重要的性能优化手段。以下是对Java包装类型缓存机制的详细解释：

一、缓存机制概述

Java中的包装类（Wrapper Class）是为了将基本数据类型转换为对象而存在的。包装类都位于java.lang包中，使用时无需显式导入。包装类型缓存机制指的是，在某些情况下，Java会对一定范围内的包装类对象进行缓存，以减少对象的创建和销毁，从而提高性能和节省内存空间。

二、缓存机制的实现

包装类型的缓存机制是通过静态成员变量来实现的。在Integer、Long、Short、Byte、Character这五个包装类中，定义了一个静态数组cache[]，用于缓存常用的数值对象。当使用valueOf()方法创建包装类对象时，会先检查该值是否在缓存范围内。如果是，则直接返回缓存中的对象；否则，创建一个新的对象并可能放入缓存中（注意，对于超出缓存范围的新对象，有的包装类并不会将其放入缓存，这取决于具体的实现）。

三、各包装类的缓存范围

1. Integer：默认缓存了-128到127之间的整数。这个范围是根据实际应用中整型数据的常用范围来设定的，能够覆盖大多数常用情况。
2. Long：默认缓存了-128到127之间的长整数。
3. Short：默认缓存了-128到127之间的短整数。
4. Byte：默认缓存了-128到127之间的字节。由于byte的值范围本身就是-128到127，所以所有的Byte对象都使用缓存。
5. Character：默认缓存了0到127之间的字符。这是因为ASCII字符集只定义了128个字符，而Unicode字符集的前128个字符与ASCII字符集完全相同。
6. Boolean：只缓存了true和false两个对象。

需要注意的是，浮点数类型的包装类（Float和Double）并没有实现缓存机制，主要是因为浮点数的表示范围非常大，且使用场景多样，缓存效果并不明显。

以Integer为案例，在创建Integer对象的时候，底层会调用valueOf方法：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736219079723-111b9af6-d33a-4fa5-b2aa-a705af91a26a.png" width="1051" title="" crop="0,0,1,1" id="u0effe3cd" class="ne-image" style="font-size: 16px">

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736219044109-2555877d-dd52-4eac-9d2b-e147d549b5ba.png" width="1220" title="" crop="0,0,1,1" id="u6be36ed0" class="ne-image" style="font-size: 16px">

查看源码：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736235140722-419bbc6a-cd5b-4b7f-9515-1779f299d511.png" width="1497" title="" crop="0,0,1,1" id="u613af40a" class="ne-image" style="font-size: 16px">

延伸面试题：

```java
public class Demo {
    public static void main(String[] args) {
        Integer i1 = 12;
        Integer i2 = 12;
        System.out.println(i1 == i2);// 结果是什么

        Integer i3 = 1200;
        Integer i4 = 1200;
        System.out.println(i3 == i4);// 结果是什么
    }
}
```

## <font style="color:#7E45E8;">说明Integer与int的区别。</font>
int是java提供的8种原始数据类型之一。Java为每个原始类型提供了封装类，Integer是java为int提供的封装类。引用类型和原始类型具有不同的特征和用法，它们包括：大小、速度、存储结构及缺省值。

int存放在内存栈上，占用4个字节，存取速度快；Integer对象存放在内存堆上，占用更多的内存空间，存取速度慢；

int的默认值为0，而Integer的默认值为null，即Integer可以区分出未赋值和值为0的区别，int则无法表达出未赋值的情况。

Integer提供了多个与整数相关的操作方法，例如，将一个字符串转换成整数，Integer中还定义了表示整数的最大值和最小值的常量。

int一般用在数值计算中，Integer则用在类型转换或者向集合中存取数值时。

## <font style="color:#7E45E8;">自动装箱与拆箱了解吗？原理是什么？</font>
Java中的自动装箱与拆箱是Java 5引入的一项特性，它允许Java编译器在需要时自动地将基本数据类型转换为对应的包装类类型（自动装箱），或者将包装类类型转换为对应的基本数据类型（自动拆箱）。这一特性极大地简化了代码编写，提高了代码的可读性和可维护性。

1. 自动装箱的原理：
    - 当需要将一个基本数据类型（如int、char等）赋值给一个对应的包装类类型（如Integer、Character等）的变量时，Java编译器会自动调用该包装类的valueOf()方法，将基本数据类型转换为包装类对象。例如，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Integer i = 100;</font>` 这行代码实际上会被编译器转换为 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Integer i = Integer.valueOf(100);</font>`。
2. 自动拆箱的原理：
    - 当需要将一个包装类类型的变量赋值给一个基本数据类型（或其对应的包装类类型的变量参与基本数据类型的运算或比较）时，Java编译器会自动调用该包装类的xxxValue()方法（如intValue()、charValue()等），将包装类对象转换为对应的基本数据类型。例如，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">int j = i;</font>` 这行代码（假设i是一个Integer类型的变量）实际上会被编译器转换为 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">int j = i.intValue();</font>`。

## <font style="color:#7E45E8;">Math.round(11.5)等于多少? Math.round(-11.5)等于多少?</font>
Math类中提供了三个与取整有关的方法：ceil、floor、round —— ceil方法表示向上取整，floor表示向下取整，round方法表示“四舍五入”，代码展示：

```java
public class Demo {
    public static void main(String[] args) {

        System.out.println(Math.floor(4.6));//4.0
        System.out.println(Math.ceil(4.1));//5.0
        System.out.println(Math.round(4.6));//5
        System.out.println(Math.round(11.5));//12
        System.out.println(Math.round(-11.6));//-12
        System.out.println(Math.round(-11.5));//-11
    }
}
```

`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Math.round()</font>` 方法遵循的是“银行家舍入”（Bankers' rounding）规则的一个变种，但更具体地说，它是向零方向舍入（round half to even的变种，但在这里主要体现为向零舍入，因为Java的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Math.round()</font>`不总是遵循严格的“向偶数舍入”规则，特别是在处理负数时）。这意味着：

+ 对于正数，如果小数部分恰好是0.5，则结果会舍入到最近的偶数整数。
+ 对于负数，如果小数部分恰好是-0.5（即，原数是-X.5的形式），则结果会向下舍入（即，向更小的负数或零的方向），这实际上等同于向零方向舍入。

因此：

+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Math.round(-11.5)</font>` 结果为 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">-11</font>`，因为-11.5的小数部分是-0.5，根据向零方向舍入的规则，它舍入到-11。
+ `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Math.round(-11.6)</font>` 结果为 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">-12</font>`，因为-11.6的小数部分是-0.6，它小于-0.5的阈值，所以整数部分-11需要减1，变为-12。

## <font style="color:#7E45E8;">double类型数字运算精度问题？</font>
```java
public class Demo {
    public static void main(String[] args) {
        System.out.println(0.4-0.3);//0.10000000000000003
        System.out.println(2.0-1.1);//0.8999999999999999
        System.out.println(new BigDecimal("0.4").subtract(new BigDecimal("0.3")));//0.1
        System.out.printf("%.1f\n",0.4-0.3);//0.1
        System.out.println(new BigDecimal("2.0").subtract(new BigDecimal("1.1")));//0.9
        System.out.printf("%.1f\n", 2.0-1.1);//0.9
    }
}
```

## <font style="color:#7E45E8;">超过 long 整型的数据应该如何表示？</font>
1. 使用`BigInteger`类：  
`BigInteger`是`java.math`包中的一个类，它提供了任意精度的整数运算。你可以使用`BigInteger`来表示和操作非常大的整数。

```java
BigInteger bigInt = new BigInteger("123456789012345678901234567890");
System.out.println(bigInt);//123456789012345678901234567890
```

2. 使用`BigDecimal`类（如果涉及小数）：  
如果你需要表示非常大的小数，可以使用`BigDecimal`类。它也是`java.math`包中的一个类，提供了任意精度的浮点数（实际上是定点数）运算。

```java
BigDecimal bigDecimal = new BigDecimal("12345678901234567890.1234567890");
System.out.println(bigDecimal);//12345678901234567890.1234567890
```

## <font style="color:#7E45E8;">判断奇数偶数是否严谨，考虑到了所有情况？</font>
<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">考虑以下情况是否能判断一个数是否是奇数？</font>

```java
public static boolean isOdd(int i){ 
     return i % 2 == 1; 
}
```

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">以上没考虑负数的问题，应该改为</font>

```java
public static boolean isOdd(int i){
    return i % 2 != 0;
}
```

## <font style="color:#7E45E8;">什么是可变参数？</font>
<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">在Java中，可变参数（Varargs）是一种语法特性，它允许一个方法接受不定数量的参数。这种特性极大地提升了方法的灵活性和可扩展性。</font>

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">可变参数通过在参数类型后面添加省略号（...）来实现。这意味着在调用方法时，可以传入不同数量的参数，而不需要为每种情况分别定义方法。可变参数在方法内部实际上是被当作数组来处理的。</font>

代码展示：

```java
public class TestArray12{
        /*
        1.可变参数：作用提供了一个方法，参数的个数是可变的 ,解决了部分方法的重载问题
        int...num
        double...num
        boolean...num
        
        
        2.可变参数在JDK1.5之后加入的新特性
        3.方法的内部对可变参数的处理跟数组是一样
        4.可变参数和其他数据一起作为形参的时候，可变参数一定要放在最后
        5.我们自己在写代码的时候，建议不要使用可变参数。
        */
    public static void main(String[] args){
                //method01(10);
                //method01();
                //method01(20,30,40);
                method01(30,40,50,60,70);
                //method01(new int[]{11,22,33,44});
        }
        public static void method01(int num2,int...num){
                System.out.println("-----1");
                for(int i:num){
                        System.out.print(i+"\t");
                }
                System.out.println();
                
                System.out.println(num2);
        }
}
```

## <font style="color:#7E45E8;">面向对象的三大特征有哪些方面？</font>
+ 封装：把客观事物封装成抽象的类，封装可以隐藏实现细节，使得代码模块化
+ 继承：继承是指可以使用现有类的所有功能，并在无需重新编写原来的类的情况下对这些功能进行扩展。创建的新类称为“子类”或“派生类”。被继承的类称为“基类”、“父类”或“超类”。目的也是为了代码重用。
+ 多态：包括覆盖（重写）和重载，重写，是指子类重新定义父类的方法。重载，多个方法同名不同参（参数个数、参数类型等）。

## <font style="color:#7E45E8;">请说出作用域public，private，protected，default的区别</font>
说明：如果在修饰的元素上面没有写任何访问修饰符，则表示default。

| 作用域 | 当前类 | 同一package | 子孙类 | 其他package |
| --- | --- | --- | --- | --- |
| public | √ | √ | √ | √ |
| protected | √ | √ | √ | × |
| default | √ | √ | × | × |
| private | √ | × | × | × |


## <font style="color:#7E45E8;">Overload和Override的区别? </font>
重载（Overload）：在同一个类中，当方法名相同，形参列表不同的时候  多个方法构成了重载。

重写（Override）：在不同的类中，子类对父类提供的方法不满意的时候，要对父类的方法进行重写。

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736326232240-8f0764d8-86e2-4a4e-a1c4-8aaa3ca8fd38.png" width="962.4" title="" crop="0,0,1,1" id="ud521ab44" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">构造方法有哪些特点？是否可被重载?</font>
+ Java 中的构造方法（也称为构造函数）具有以下特点：
    1. 与类同名：构造方法的名称必须与类名完全相同，包括大小写。
    2. 无返回类型：构造方法没有返回类型，包括 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">void</font>` 也不写。
    3. 用于初始化对象：构造方法的主要作用是初始化新创建的对象的状态。通过调用构造方法，可以为新对象分配内存并设置其初始状态。
    4. 默认构造方法：如果类中没有显式定义任何构造方法，编译器会提供一个默认的无参构造方法。但是，如果类中定义了至少一个构造方法，编译器就不会再提供默认构造方法。
    5. 可以访问修饰符：构造方法可以有访问修饰符，如 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">public</font>`、`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">private</font>`、`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">protected</font>` 或默认（包访问权限）。这决定了谁可以创建该类的对象。
    6. 可以抛出异常：构造方法可以声明它可能抛出的异常，使用 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">throws</font>` 关键字。
    7. 可以在构造方法内部调用其他构造方法：通过使用 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this()</font>` 语法，可以在一个构造方法内部调用同一个类的另一个构造方法。但必须是构造方法的第一条语句。
    8. 不能被继承：构造方法不是类成员，不能被子类继承。但是子类可以通过调用父类的构造方法来初始化父类的部分。
+ 构造方法是否可被重载？

是的，构造方法可以被重载。在 Java 中，方法重载是指同一个类中有多个方法名相同但参数列表不同的方法。构造方法也可以遵循这一规则。通过定义多个构造方法，每个方法具有不同的参数列表（包括参数的数量、类型或顺序），可以创建不同类型的初始化方式。

## <font style="color:#7E45E8;">this和super的区别</font>
+ 相同点
    1. 实例相关性：`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`都与实例有关，它们都不能出现在`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">static</font>`方法中和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">static</font>`代码块中（类初始化器）。
    2. 构造方法调用：`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`都可以用于调用构造方法，且当通过`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`或`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`调用构造方法时，它们必须位于构造方法的第一行。同一个构造方法内部`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`或`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`不能同时出现。
+ 不同点
    1. 实例表示：
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`：代表本类的当前实例，可以通过`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`访问本类中的成员（`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`可以单独使用）。
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`：用于访问从父类继承的、可见的成员，所以`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`不能表示父类实例，不能单独使用。
    2. 构造方法调用：
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`：用于调用本类内部的其它重载的构造方法。
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`：用于调用父类的构造方法。
    3. 成员访问：
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this.</font>`：可以访问本类中以及父类中继承的、可见的成员（方法和属性（字段））。
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super.</font>`：只能访问从父类中继承的、可见的成员（方法和字段（属性））。
    4. 使用方式：
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`关键字可以单独使用，比如直接输出`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`或当作返回值。
        * `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`关键字不可以单独使用，必须通过`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super(参数)</font>`或`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super.</font>`形式使用。

## <font style="color:#7E45E8;">什么是向上转型和向下转型？</font>
+ 向上转型（Upcasting）

向上转型是指将子类对象转换为父类类型。这是一个隐式的转换过程，不需要进行任何特殊的操作，编译器会自动进行类型转换。向上转型的语法很简单，直接将子类对象赋值给父类类型的引用即可。例如：

```java
class Animal {}
class Dog extends Animal {}

Animal myAnimal = new Dog(); // 向上转型，将Dog对象赋值给Animal类型的引用
```

向上转型的目的是为了提高代码的灵活性和重用性。通过向上转型，可以使用父类类型的引用来调用子类对象的方法，而这些方法是在父类中定义或由子类重写的。这样，就可以在不知道具体子类类型的情况下，编写出能够处理多种子类对象的通用代码。

+ 向下转型（Downcasting）

向下转型是指将父类对象转换为子类类型。这是一个显式的转换过程，需要使用强制类型转换操作符来完成。向下转型的语法是在需要转型的对象前面加上要转换到的子类类型，并用括号括起来。例如：

```java
class Animal {}
class Dog extends Animal {}

Animal myAnimal = new Dog(); // 向上转型
Dog myDog = (Dog) myAnimal; // 向下转型，将Animal类型的引用强制转换为Dog类型
```

需要注意的是，向下转型只能在向上转型的基础上进行，即只能将已经向上转型后的对象再次向下转型回原来的子类类型。否则，如果将一个没有向上转型的对象进行向下转型，会在运行时抛出`<font style="color:rgb(5, 7, 59);">ClassCastException</font>`异常。为了避免这种异常的发生，可以使用`<font style="color:rgb(5, 7, 59);">instanceof</font>`运算符来判断对象是否属于指定的类型，然后再进行向下转型。

例如：

```java
if (myAnimal instanceof Dog) {
    Dog myDog = (Dog) myAnimal; // 安全地向下转型
} else {
    // 处理不是Dog类型的myAnimal对象
}
```

向下转型的目的是为了调用子类特有的方法或访问子类特有的属性。在多态的场景下，通过父类引用调用方法时，执行的是子类重写后的方法，这带来了代码的灵活性和可维护性等诸多好处。然而，多态也存在一定的局限性，即当通过父类引用指向子类对象时，我们只能直接访问父类中定义的属性和方法，无法直接访问子类特有的属性和方法。而向下转型就为我们提供了一种途径，使得在特定情况下，我们可以突破这个限制，从而能够充分利用子类所特有的功能。

## <font style="color:#7E45E8;">abstract class和interface有什么区别? 	</font>
+ 抽象类

抽象类：使用abstract修饰；不能实例化；含有抽象方法的类是抽象类；抽象类可以含有抽象方法，也可以不包含抽象方法，抽象类中可以有具体的方法；如果一个子类实现了父类（抽象类）的所有抽象方法，那么该子类可以不必是抽象类，否则就是抽象类；

+ 接口

接口：接口使用interface修饰；接口不能被实例化；一个类只能继承一个类，但是可以实现多个接口；

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">在</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">jdk8</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">之前，</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">interface</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">之中可以定义变量和方法，变量必须是</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">public</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">、</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">static</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">、</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">final</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">的，方法必须是</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">public</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">、</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">abstract</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">的。</font>

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">JDK8</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">及以后，允许我们在接口中定义</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">static</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">方法和</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">default</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">方法。</font>

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">如果一个</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">实现类实现</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">了两个</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">接口，两个接口中</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">有同名的</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">静态方法</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">，</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">不会产生错误，因为</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">jdk8</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">只能通过接口类调用接口中的静态方法，所以对编译器来说是可以区分的</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">，</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">接口中的静态方法可以在接口默认方法中调用，实现类的方法可以调用，但是不能通过实现类名及实现类对象来调用</font><font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">。</font>

<font style="color:rgb(51,51,51);background-color:rgb(255,255,255);">如果两个接口中定义了一模一样的默认方法，并且一个实现类同时实现了这两个接口，那么必须在实现类中重写默认方法，否则编译失败。</font>

<font style="color:rgb(0,0,0);">接口更多的是在系统架构设计方法发挥作用，主要用于定义模块之间的通信契约。而抽象类在代码实现方面发挥作用，可以实现代码的重用</font><font style="color:rgb(0,0,0);">。</font>

## <font style="color:#7E45E8;">abstract的方法是否可同时是final、static、native或者synchronized的? </font>
+ final修饰方法表示方法不能被子类重写，但是抽象方法需要被子类重写，所以肯定不能在一起使用。
+ abstract的method 不可以是static的，因为抽象的方法是要被子类实现的，而static与子类扯不上关系！
+ native方法表示该方法要用另外一种依赖平台的编程语言实现的，不存在着被子类实现的问题，所以它也不能是抽象的，不能与abstract混用。
+ abstract是抽象的，而synchronized是同步的，相对于线程讲的；abstract只是声明没有实现，既然没有实现就谈不上同步了，所以不能放到一块使用。当然如果其子类实现了这个方法在子类是可以同步的。

## <font style="color:#7E45E8;">深拷贝和浅拷贝区别了解吗？什么是引用拷贝？</font>
（一）引用拷贝

当我们想复制一个对象时，最自然的操作就是：直接赋值给另一个变量。如下代码：

```java
public class Person {
    int age;
    public Person(int age) {
        this.age = age;
    }
}

class Test{
    public static void main(String[] args) {
        Person p1 = new Person(18);
        Person p2 = p1;
        p2.age = 20;

        System.out.println(p1 == p2);// true
        System.out.println(p1.age);// 20
        System.out.println(p2.age);// 20
    }
}
```

这种做法只复制了对象的地址，两个变量指向了同一个对象。任意一个变量操作了对象的属性，都会影响到另一个变量。这种对同一个对象的操作，算不上真正意义的复制，所以引用拷贝算不上对象拷贝。

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736493846779-b557ede6-451c-4a00-9f83-340a68f66ba7.png" width="280.8" title="" crop="0,0,1,1" id="u5f0898d0" class="ne-image" style="font-size: 16px">

对象拷贝，一般说的就是浅拷贝和深拷贝。

（二）浅拷贝

浅拷贝的实现，类实现Cloneable接口：

```java
public class Person implements Cloneable{// 实现Cloneable接口，
    int age;
    public Person(int age) {
        this.age = age;
    }

    // 重写Object的clone方法，修改修饰符为public，返回值为Person，方法体：
    @Override
    public Person clone() throws CloneNotSupportedException {
        return (Person)super.clone();
    }
}

class Test{
    public static void main(String[] args) throws CloneNotSupportedException {
        Person p1 = new Person(18);
        Person p2 = p1.clone();
        p2.age = 20;

        System.out.println(p1 == p2);// false
        System.out.println(p1.age);// 18
        System.out.println(p2.age);// 20
    }
}
```

发现两个变量指向的是不同的对象：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736495178507-eb473928-6b15-4bc5-8c64-9e5015469320.png" width="276" title="" crop="0,0,1,1" id="u580780b5" class="ne-image" style="font-size: 16px">

各自改变属性，也不会影响到另一个对象。但是还是存在问题的，如果拷贝的对象中有属性是引用数据类型，浅拷贝会直接复制内部对象的引用地址，也就是说拷贝对象和原对象的属性共用同一个对象。

如下代码：

```java
public class Person implements Cloneable{// 实现Cloneable接口，
    int age;
    int[] arr = new int[]{11,22,33};// 属性为引用数据类型
    public Person(int age) {
        this.age = age;
    }

    // 重写Object的clone方法，修改修饰符为public，返回值为Person，方法体：
    @Override
    public Person clone() throws CloneNotSupportedException {
        return (Person)super.clone();
    }
}
```

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736495307454-948554ba-f79c-4538-b27e-0665f9ab3b34.png" width="336" title="" crop="0,0,1,1" id="u67ed401e" class="ne-image" style="font-size: 16px">

如果对其中一个引用类型的属性操作，那么会影响另一个对象的属性。

所以：浅拷贝会在堆上创建一个新的对象，不过，如果原对象内部的属性是引用类型的话，浅拷贝会直接复制内部对象的引用地址，也就是说拷贝对象和原对象的属性共用同一个对象。

（三）深拷贝

深拷贝会完全复制整个对象，包括这个对象所包含的内部对象。

实现，修改克隆方法：

```java
public class Person implements Cloneable{// 实现Cloneable接口，
    int age;
    int[] arr = new int[]{11,22,33};// 属性为引用数据类型
    public Person(int age) {
        this.age = age;
    }

    // 重写Object的clone方法，修改修饰符为public，返回值为Person，方法体：
    @Override
    public Person clone() throws CloneNotSupportedException {
        Person p = (Person)super.clone();
        p.arr.clone();
        return p;
    }
}
```

克隆对象以后，再对对象的属性也进行克隆，实现深拷贝。

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736495670107-6be99695-a509-43ee-b745-7e70a08518ca.png" width="275.2" title="" crop="0,0,1,1" id="ucf829015" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">Object 类的常见方法有哪些？</font>
1. clone()
    - 作用：创建并返回一个对象的拷贝。
    - 特点：clone方法是浅拷贝，对象内属性引用的对象只会拷贝引用地址，而不会将引用的对象重新分配内存。相对应的深拷贝则会连引用的对象也重新创建。
    - 注意事项：使用clone方法时，必须实现Cloneable接口，否则会抛出CloneNotSupportedException异常。重写clone方法时，需要调用super.clone()方法以获取原始对象的副本。
2. equals(Object obj)
    - 作用：比较两个对象是否相等。
    - 默认行为：在Object类中，equals方法使用==运算符来比较两个对象的引用是否相同，即判断两个对象是否是同一个对象。
    - 重写规范：子类通常会重写equals方法，以添加判断内容是否相等的功能。重写时需要遵循自反性、对称性、传递性和一致性等约束。
3. finalize()
    - 作用：当垃圾回收器确定不存在对该对象的更多引用时，会调用此方法，在对象被垃圾回收之前执行一些清理操作或资源释放。
    - 代码展示：

```java
public class MyResource {
    // 假设这是一个需要清理的资源，比如文件句柄、数据库连接等
    private boolean isOpen = true;

    // 模拟打开资源
    public void open() {
        isOpen = true;
        System.out.println("Resource opened.");
    }

    // 模拟关闭资源
    public void close() {
        isOpen = false;
        System.out.println("Resource closed.");
    }

    // 重写 finalize 方法以在垃圾回收时尝试关闭资源
    @Override
    protected void finalize() throws Throwable {
        try {
            if (isOpen) {
                System.out.println("Finalizing: Closing resource in finalize().");
                close();
            }
        } finally {
            super.finalize(); // 调用父类的 finalize 方法（虽然通常不推荐这样做）
        }
    }
}
```

```java
public class FinalizeExample {
    public static void main(String[] args) {
        MyResource resource = new MyResource();
        resource.open();

        // 显式地将 resource 设置为 null，以便它可能更快地被垃圾回收（但这并不保证）
        resource = null;

        // 强制垃圾回收（仅供演示，实际应用中不应这样做）
        System.gc();

        // 等待一段时间，以便垃圾回收线程有机会运行（这仍然是一个不可靠的方法）
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // 请注意，即使我们调用了 System.gc()，也不能保证 finalize() 会立即执行
        // 因为垃圾回收是由 JVM 在后台异步执行的
    }
}
```

结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736496898344-adeb2e13-0857-4e40-ab19-756c12117b53.png" width="667.2" title="" crop="0,0,1,1" id="ube11dc88" class="ne-image" style="font-size: 16px">

4. getClass()
    - 作用：获取对象的运行时类的Class对象。
    - 应用场景：这是反射的三种方式之一（类名.class、对象.getClass()、Class.forName("全类名")）。通过getClass方法，可以获取到对象的运行时类型信息，进而进行反射操作。
5. hashCode()
    - 作用：生成一个代表对象的哈希码（散列码），这是一个32位的整数。这个哈希码可以作为对象的唯一标识符，在哈希表等数据结构中用于快速定位对象。
6. toString()
    - 作用：返回对象的字符串表示形式。
    - 默认行为：在Object类中，toString方法返回类名+“@”+十六进制的hashCode值。
    - 重写建议：建议所有子类都重写toString方法，以提供更有意义的字符串表示形式。
7. wait()
    - 作用：让当前线程进入等待状态，直到其他线程调用此对象的notify()方法或notifyAll()方法将其唤醒。
    - 注意事项：wait方法只能在当前线程获取到对象的锁监视器之后才能调用，否则会抛出IllegalMonitorStateException异常。调用wait方法时，线程会释放锁监视器。
8. notify()
    - 作用：唤醒在此对象监视器上等待的一个线程。
    - 注意事项：notify方法只能被作为此对象监视器的所有者的线程来调用。一次只能有一个线程被唤醒，选择是任意性的。
9. notifyAll()
    - 作用：唤醒在此对象监视器上等待的所有线程。
    - 注意事项：与notify方法类似，notifyAll方法也只能被作为此对象监视器的所有者的线程来调用。

## <font style="color:#7E45E8;">hashCode() 有什么用？和equals()方法有什么关系？</font>
1. 等价性要求：如果两个对象根据 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">equals()</font>` 方法判断为相等，那么它们的 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hashCode()</font>` 方法返回值也必须相同。这是为了确保在使用基于哈希的集合时，能够正确处理相等的对象，避免出现错误的插入和删除操作。
2. 非必然关系：反过来，如果两个对象的 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hashCode()</font>` 返回值相同，并不意味着这两个对象一定相等。这种情况被称为哈希冲突，不同的对象可能有相同的哈希码。但是，如果两个对象的 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hashCode()</font>` 返回不同的值，那么这两个对象一定不相等。
3. 重写规范：鉴于 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hashCode()</font>` 和 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">equals()</font>` 方法之间的紧密关系，如果重写了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">equals()</font>` 方法，通常也需要重写 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hashCode()</font>` 方法，以保持这两个方法的一致性。



（一）HashSet集合：

+ 代码展示：

```java
public class Test {
        public static void main(String[] args) {
                HashSet<Integer> set=new HashSet<Integer>();
                
                set.add(12);
                set.add(1);
                set.add(23);
                set.add(18);
                set.add(12);
                set.add(16);

                System.out.println(set.size());
                
        }
}
```

+ 数组存放数据的特点：

无序，唯一

+ 数组存放数据的优点：

查询，删除，增加效率高

+ 数组存放数据的缺点：

无序

+ 原理展示：

<img src="https://cdn.nlark.com/yuque/0/2024/png/39281619/1727339605450-eb9874ef-8d60-4879-b2bb-541d7a52b024.png" width="747.2" title="" crop="0,0,1,1" id="ub034a34a" class="ne-image" style="font-size: 16px">

+ 在HashSet中放入自定义的Student数据:

如果想要放入Student数据，也具备上面的无序，唯一的特点，必须做的事：

在Student中重写hashCode()和equals()---直接用快捷键生成即可！

```java
import java.util.Objects;

public class Student {
    private String name;
    private int age;
    private double height;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public double getHeight() {
        return height;
    }
    public void setHeight(double height) {
        this.height = height;
    }
    public Student(String name, int age, double height) {
        super();
        this.name = name;
        this.age = age;
        this.height = height;
    }
    @Override
    public String toString() {
        return "Student [name=" + name + ", age=" + age + ", height=" + height + "]";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return age == student.age && Double.compare(height, student.height) == 0 && Objects.equals(name, student.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age, height);
    }
}
```

```java
import java.util.HashSet;
public class Test3 {
        public static void main(String[] args) {
                HashSet<Student> set=new HashSet<Student>();
                set.add(new Student("lili", 19, 170.4));
                set.add(new Student("lulu", 21, 170.4));
                set.add(new Student("lili", 19, 170.4));
                set.add(new Student("feifei", 24, 140.4));
                System.out.println(set);
                System.out.println(set.size());
        }
}
```

（二）HashMap集合：

```java
public class Test {
    public static void main(String[] args) {

        Map<String,Integer> map=new HashMap<String,Integer>();
        map.put("nana",12304534);
        map.put("lili",34556778);
        map.put("nana",66923433);
        map.put("feifei",345456567);
    }
}
```

+ 原理：

<font style="color:#080808;background-color:#ffffff;">HashMap中的key是按照哈希表的结构处理数据的，如果是个自定义的引用数据类型作为key，必须重写hashCode和equals方法！</font>

<img src="https://cdn.nlark.com/yuque/0/2024/png/39281619/1731135119118-1e4c895a-06a3-40f5-a145-d68c1183cd53.png" width="1407" title="" crop="0,0,1,1" id="NSPMy" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">关于super.getClass()方法调用结果。</font>
下面程序的输出结果是多少？

```java
package com.wm.test14;
import java.util.Date;
public class Main extends Date {
    public void test(){
        System.out.println(this.getClass().getName());
        System.out.println(super.getClass().getName());
        System.out.println(getClass().getSuperclass().getName());
    }
    public static void main(String[] args) {
        new Main().test();
    }
}
```

<font style="color:rgb(0,0,0);">结果：</font>

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736497576891-c63d618f-c0f2-4ef0-a313-9907aaaf8663.png" width="462.4" title="" crop="0,0,1,1" id="u03a3978a" class="ne-image" style="font-size: 16px">

+ <font style="color:rgb(0,0,0);">值得注意的是，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">getClass()</font>`<font style="color:rgb(0,0,0);"> 方法并不属于从父类继承的方法，而是所有对象从 </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Object</font>`<font style="color:rgb(0,0,0);"> 类继承而来的。</font>
+ <font style="color:rgb(0,0,0);">在这个特定的场景中，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super.getClass()</font>`<font style="color:rgb(0,0,0);"> </font><font style="color:rgb(0,0,0);">实际上与</font><font style="color:rgb(0,0,0);"> </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this.getClass()</font>`<font style="color:rgb(0,0,0);"> </font><font style="color:rgb(0,0,0);">调用的是同一个方法，因为</font><font style="color:rgb(0,0,0);"> </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">getClass()</font>`<font style="color:rgb(0,0,0);"> </font><font style="color:rgb(0,0,0);">方法定义在</font><font style="color:rgb(0,0,0);"> </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Object</font>`<font style="color:rgb(0,0,0);"> </font><font style="color:rgb(0,0,0);">类中，并被所有类继承。</font>
+ <font style="color:rgb(0,0,0);">不论使用</font><font style="color:rgb(0,0,0);"> </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">this</font>`<font style="color:rgb(0,0,0);"> </font><font style="color:rgb(0,0,0);">还是</font><font style="color:rgb(0,0,0);"> </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super</font>`<font style="color:rgb(0,0,0);"> </font><font style="color:rgb(0,0,0);">调用</font><font style="color:rgb(0,0,0);"> </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">getClass()</font>`<font style="color:rgb(0,0,0);">，返回的都是当前对象的运行时类对象。</font>
+ <font style="color:rgb(0,0,0);">因此，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">super.getClass().getName()</font>`<font style="color:rgb(0,0,0);"> 同样会输出 </font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Main</font>`<font style="color:rgb(0,0,0);"> 类的完全限定名。</font>

## <font style="color:#7E45E8;">什么是singleton？如何实现？写出代码。</font>
<font style="color:rgb(15, 17, 21);">单例模式是一种创建型设计模式，它确保一个类只有一个实例，并提供一个全局访问点来获取这个实例。</font>

<font style="color:rgb(0,0,0);">经典实现方式：</font>

<font style="color:rgb(0,0,0);">（一）饿汉式</font>

```java
public class Singleton {
    // 在类加载时就完成实例化
    private static Singleton INSTANCE = new Singleton();

    // 私有构造函数，防止外部实例化
    private Singleton() {}

    // 提供全局访问点
    public static Singleton getInstance() {
        return INSTANCE;
    }

    public static void main(String[] args) {
        Singleton s1 = getInstance();
        Singleton s2 = getInstance();
        System.out.println(s1 == s2);// true
    }
}
```

<font style="color:rgb(15, 17, 21);">优点：</font>

+ <font style="color:rgb(15, 17, 21);">实现简单</font><font style="color:rgb(15, 17, 21);">，代码简洁。</font>
+ <font style="color:rgb(15, 17, 21);">线程安全</font><font style="color:rgb(15, 17, 21);">：由于实例在类加载时创建，JVM 保证了线程安全。</font>

<font style="color:rgb(15, 17, 21);">缺点：</font>

+ <font style="color:rgb(15, 17, 21);">可能造成资源浪费：如果这个实例从头到尾都没被使用过，或者实例的创建过程非常耗费资源，那么这种提前创建的方式就不太合适。</font>

<font style="color:rgb(0,0,0);">（二） </font><font style="color:rgb(0,0,0);">懒汉式</font>

**<font style="color:rgb(15, 17, 21);">a) 非线程安全版本：</font>**

```java
public class Singleton {
    // 静态实例变量，初始为null
    private static Singleton instance;

    // 私有构造函数，防止外部实例化
    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

<font style="color:rgb(15, 17, 21);">缺点：在多线程环境下，如果多个线程同时进入 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">if (instance == null)</font>`<font style="color:rgb(15, 17, 21);"> 判断，可能会创建多个实例，违反单例原则。</font>

**<font style="color:rgb(15, 17, 21);">b) 线程安全版本（使用 synchronized）：</font>**

```java
public class Singleton {
    // 静态实例变量，初始为null
    private static Singleton instance;

    // 私有构造函数，防止外部实例化
    private Singleton() {}

    public static synchronized  Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

**<font style="color:rgb(15, 17, 21);">  </font>**<font style="color:rgb(15, 17, 21);">优点：线程安全。</font>  
<font style="color:rgb(15, 17, 21);">	缺点：每次调用 </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">getInstance()</font>`<font style="color:rgb(15, 17, 21);"> 都需要进行同步，性能有开销。实际上只有第一次创建实例时需要同步。</font>

<font style="color:rgb(0,0,0);">（三）</font><font style="color:rgb(15, 17, 21);">双重检查锁（Double-Checked Locking，DCL）</font>

```java
public class DCLSingleton {
    // 使用 volatile 关键字禁止指令重排序，确保可见性
    private static volatile DCLSingleton instance;

    private DCLSingleton() {}

    public static DCLSingleton getInstance() {
        // 第一次检查：如果实例已存在，直接返回，避免不必要的同步
        if (instance == null) {
            // 同步代码块
            synchronized (DCLSingleton.class) {
                // 第二次检查：进入同步块后再次检查，确保只有一个线程创建实例
                if (instance == null) {
                    instance = new DCLSingleton();
                }
            }
        }
        return instance;
    }
}
```

**<font style="color:rgb(15, 17, 21);">关键点：</font>**

+ **<font style="color:rgb(15, 17, 21);">第一次检查 (</font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">if (instance == null)</font>**`**<font style="color:rgb(15, 17, 21);">)</font>**<font style="color:rgb(15, 17, 21);">: 避免绝大多数不必要的同步，提高性能。</font>
+ **<font style="color:rgb(15, 17, 21);">同步块 (</font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">synchronized</font>**`**<font style="color:rgb(15, 17, 21);">)</font>**<font style="color:rgb(15, 17, 21);">: 保证只有一个线程进入创建实例的代码。</font>
+ **<font style="color:rgb(15, 17, 21);">第二次检查 (</font>**`**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">if (instance == null)</font>**`**<font style="color:rgb(15, 17, 21);">)</font>**<font style="color:rgb(15, 17, 21);">: 防止在等待锁的线程进入同步块后重复创建实例。</font>
+ `**<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">volatile</font>**`**<font style="color:rgb(15, 17, 21);"> </font>****<font style="color:rgb(15, 17, 21);">关键字</font>**<font style="color:rgb(15, 17, 21);">：至关重要。它防止了指令重排序，确保</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">instance = new DCLSingleton();</font>`<font style="color:rgb(15, 17, 21);"> </font><font style="color:rgb(15, 17, 21);">这行代码的执行顺序是：1. 分配内存空间，2. 初始化对象，3. 将引用指向内存地址。如果没有</font><font style="color:rgb(15, 17, 21);"> </font>`<font style="color:rgb(15, 17, 21);background-color:rgb(235, 238, 242);">volatile</font>`<font style="color:rgb(15, 17, 21);">，可能发生重排序（1->3->2），导致另一个线程拿到一个未完全初始化的对象。</font>

**<font style="color:rgb(15, 17, 21);">优点</font>**<font style="color:rgb(15, 17, 21);">：线程安全，延迟加载，且相比同步方法性能更高。  
</font>**<font style="color:rgb(15, 17, 21);">缺点</font>**<font style="color:rgb(15, 17, 21);">：代码稍复杂。</font>



## <font style="color:#7E45E8;">Java中如何定义枚举？</font>
Enum一般用来表示一组相同类型的常量，如性别、日期、月份、颜色等。对这些属性用常量的好处是不仅可以保证单例，且比较时候可以用”==”来替换equals，是一种好的习惯。JDK1.5之前没有Enum这个类型，那时候一般用接口常量来替代。

代码展示：自定义枚举类：

```java
public class Season {
    //属性：
    private final String seasonName ;//季节名字
    private final String seasonDesc ;//季节描述
    //利用构造器对属性进行赋值操作：
    //构造器私有化，外界不能调用这个构造器，只能Season内部自己调用
    private Season(String seasonName,String seasonDesc){
        this.seasonName = seasonName;
        this.seasonDesc = seasonDesc;
    }

    //提供枚举类的有限的  确定的对象：
    public static final Season SPRING = new Season("春天","春暖花开");
    public static final Season SUMMER = new Season("夏天","烈日炎炎");
    public static final Season AUTUMN = new Season("秋天","硕果累累");
    public static final Season WINTER = new Season("冬天","冰天雪地");


    @Override
    public String toString() {
        return "Season{" +
                "seasonName='" + seasonName + '\'' +
                ", seasonDesc='" + seasonDesc + '\'' +
                '}';
    }
}

```

```java
public class Test {
    public static void main(String[] args) {
        // 创建季节对象：
        // Season s = new Season(); 错误

        // 只能使用内部定义的对象：
        Season autumn = Season.AUTUMN;
        System.out.println(autumn);
    }
}

```

	JDK1.5以后使用enum关键字创建枚举类：

<img src="https://cdn.nlark.com/yuque/0/2024/png/39281619/1729671249173-62f1783d-1d89-4853-bd96-c543fda6ba9c.png" width="1409" title="" crop="0,0,1,1" id="EZtkQ" class="ne-image" style="font-size: 16px">

变为下面的枚举类：

```java
public enum Season {
    //提供枚举类的有限的  确定的对象：
    SPRING("春天","春暖花开"),
    SUMMER("夏天","烈日炎炎"),
    AUTUMN("秋天","硕果累累"),
    WINTER("冬天","冰天雪地");
    //属性：
    private final String seasonName ;//季节名字
    private final String seasonDesc ;//季节描述
    //利用构造器对属性进行赋值操作：
    //构造器私有化，外界不能调用这个构造器，只能Season内部自己调用
    private Season(String seasonName,String seasonDesc){
        this.seasonName = seasonName;
        this.seasonDesc = seasonDesc;
    }
    @Override
    public String toString() {
        return "Season{" +
                "seasonName='" + seasonName + '\'' +
                ", seasonDesc='" + seasonDesc + '\'' +
                '}';
    }
}

```

## <font style="color:#7E45E8;">定义类，类中有哪些组成部分？</font>
类的组成：属性，方法，构造器，代码块（普通块，静态块，构造块，同步块），内部类

其中代码块的分类：普通块，构造块，静态块，同步块（多线程）

+ 普通块：可以限制局部变量的作用范围

```java
public class Test {
    //方法
    public void a(){
        System.out.println("-----a");
        {
            //普通块限制了局部变量的作用范围
            System.out.println("这是普通块");
            System.out.println("----000000");
            int num = 10;
            System.out.println(num);
        }
        //System.out.println(num);
        //if(){}
        //while(){}
    }
   
}
```

+ 构造块：构造块是定义在类体内，但在任何方法之外、构造方法之外的代码块。每次创建对象时执行，用于实例变量的初始化。

```java
public class Test {

    private int x;

    // 构造块
    {
        System.out.println("Instance initializer block");
        x = 10;
    }

    public Test() {
        System.out.println("Constructor Test()");
    }

    public Test(int x) {
        System.out.println("Constructor Test(int x)");
        this.x = x;
    }

    public static void main(String[] args) {
        Test obj1 = new Test();
        System.out.println(obj1.x);
        Test obj2 = new Test(20);
        System.out.println(obj2.x);
    }

}

```

代码结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736818611781-d70552df-d5bd-4966-9a01-cba7f748e0d6.png" width="758" title="" crop="0,0,1,1" id="u1edbf98c" class="ne-image" style="font-size: 16px">

+ 静态代码块：静态代码块是定义在类体内，但在任何方法之外、构造方法之外的，并使用`static`关键字修饰的代码块。类加载时执行一次，用于静态变量的初始化以及只需执行一次的初始化逻辑。

```java
public class Test {

    private static int y;

    // 静态代码块
    static {
        System.out.println("Static initializer block");
        y = 20;
    }

    public Test() {
        System.out.println("Constructor Test()");
    }

    public static void main(String[] args) {
        System.out.println("Main method");
        Test obj1 = new Test();
        Test obj2 = new Test();
    }

}
```

运行结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1736818911700-5994ac60-fbd7-4e33-937a-6d4d7195fdff.png" width="564" title="" crop="0,0,1,1" id="ub705d79b" class="ne-image" style="font-size: 16px">



## <font style="color:#7E45E8;"> 说说内部类是什么</font>
<font style="color:rgb(0,0,0);">内部类的分类：</font>

<font style="color:rgb(0,0,0);">一、成员内部类（普通内部类）</font>

    - <font style="color:rgb(0,0,0);">定义</font><font style="color:rgb(0,0,0);">：定义在外部类中的非静态类。</font>

<font style="color:rgb(0,0,0);">二、静态内部类（静态嵌套类）</font>

    - <font style="color:rgb(0,0,0);">定义</font><font style="color:rgb(0,0,0);">：定义在外部类中的静态类。</font>

<font style="color:rgb(0,0,0);">三、局部内部类（方法内部类）</font>

    - <font style="color:rgb(0,0,0);">定义</font><font style="color:rgb(0,0,0);">：定义在外部类的方法中的类。</font>

<font style="color:rgb(0,0,0);">四、匿名内部类</font>

    - <font style="color:rgb(0,0,0);">定义：没有名字的内部类。</font>

分别讲解：

（一）<font style="color:rgb(0,0,0);">成员内部类</font>、静态内部类、<font style="color:rgb(0,0,0);">局部内部类</font>

+ <font style="color:rgb(0,0,0);">内部类就是在一个类的内部定义的类</font>
+ <font style="color:rgb(0,0,0);">内部类可以定义在外部类的方法外面（成员内部类），也可以定义在外部类的方法体中（局部内部类）</font>
+ <font style="color:rgb(0,0,0);">静态内部类中只能访问外部类中被static修饰的内容</font>
+ <font style="color:rgb(0,0,0);">内部类创建对象的方式特殊</font>
+ <font style="color:rgb(0,0,0);">在方法体外面定义的内部类的访问类型可以是public、protected、默认的，private等4种类型</font>
+ <font style="color:rgb(0,0,0);">在方法内部定义的内部类前面不能有访问类型修饰符</font>

```java
/**
 * 成员内部类:
 *      里面属性，方法，构造器等
 *      修饰符：private，default，protect，public，final,abstract
 */
public class TestOuter {
    //属性：
    int age;
    static int height;


    // 成员内部类：
    public class D{
        String name;
        static int num;
        public void method(){
            System.out.println(age);
            System.out.println(height);
            System.out.println(num);
        }
    }
    // 静态成员内部类：
    static class E{
        public void method(){
            // System.out.println(age); 报错，不能访问非静态内容
            System.out.println(height);
        }
    }

    //方法：
    public void a(){
        System.out.println("这是a方法");
        {
            System.out.println("这是一个普通块");
            class B{
            }
        }
        class A{
        }
    }

}
class Demo{
    public static void main(String[] args) {
        // 创建内部类的对象：
        TestOuter t = new TestOuter();
        TestOuter.D d = t.new D();
    }
}

```

（二）匿名内部类

<font style="color:rgb(0,0,0);">在Java中，匿名内部类（Anonymous Inner Class）是一种没有名称的内部类。它允许你在声明和实例化一个类的时候，直接定义和创建它的实例。匿名内部类通常用于简化代码，特别是在需要创建一个类的实例并且该类只需要临时使用一次的时候。</font>

```java
public interface MyInterface {
    void a();
}
```

```java
public class TestOuter {
    //1. 如果类B在整个项目中只使用一次，那么就没有必要单独创建一个B类，使用内部类就可以了
    public MyInterface method1(){
        class B implements MyInterface{
            @Override
            public void a() {
                System.out.println("B类中重写a方法");
            }
        }
        return new B();
    }
    public MyInterface method2(){
        //2.匿名内部类（一种没有名称的内部类）
        return new MyInterface(){
            @Override
            public void a() {
                System.out.println("匿名内部类中重写a方法");
            }
        };
    }
    public void teat(){
        MyInterface com = new MyInterface(){
            @Override
            public void a() {
                System.out.println("匿名内部类中重写a方法");
            }
        };
        com.a();
    }

    public MyInterface method() {
        // Lambda表达式替代匿名内部类
        return () -> System.out.println("匿名内部类中重写a方法");
    }
}
```

## <font style="color:#7E45E8;">内部类可以引用包含类的成员吗？有没有什么限制？ </font>
完全可以。如果不是静态内部类，那没有什么限制！

如果你把静态嵌套类当作内部类的一种特例，那在这种情况下不可以访问外部类的普通成员变量，而只能访问外部类中的静态成员。

## <font style="color:#7E45E8;">什么是匿名内部类？如何实现？</font>
答案如4.2中匿名内部类所示。

## <font style="color:#7E45E8;">什么是Throwable？</font>
在Java中，`Throwable`是所有错误（errors）和异常（exceptions）的超类。它定义了在Java程序中用于表示和处理错误情况的通用机制。`Throwable`类及其子类被用来表示程序中出现的异常情况，从而允许程序能够采取适当的措施来处理这些异常，而不是简单地崩溃。



<img src="https://cdn.nlark.com/yuque/0/2024/png/39281619/1727322965793-a17cf5e8-9224-4ab4-be4c-c7b983007290.png" width="1139" title="" crop="0,0,1,1" id="Pb7Xy" class="ne-image" style="font-size: 16px">



## <font style="color:#7E45E8;">error和exception有什么区别? </font>
Throwable类派生了两个子类，分别是Exception和Error类。Error类及其子类用来描述Java运行系统中的内部错误以及资源耗尽的错误，比如说内存溢出，这类错误比较严重，基本上很难恢复。Exception类称为非致命性错误，表示程序存在设计或实现问题，可以通过捕捉处理使程序继续执行。

`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Throwable</font>`类有两个主要的子类：

1. `**<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Error</font>**`：
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Error</font>`类表示那些通常是由JVM（Java虚拟机）本身抛出的严重问题，这些问题通常被认为是系统级的错误，应用程序通常无法处理这些错误。例如，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">OutOfMemoryError</font>`和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">StackOverflowError</font>`都是`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Error</font>`的子类。
    - 大多数情况下，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Error</font>`不应该被捕获或处理，因为它们指示的是程序或JVM本身存在的问题，而不是程序逻辑中的错误。
2. `**<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Exception</font>**`：
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Exception</font>`类表示那些程序在运行时可能遇到的异常条件，这些条件通常是可以通过适当的错误处理机制来恢复的。例如，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">NullPointerException</font>`、`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ArrayIndexOutOfBoundsException</font>`和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">IOException</font>`都是`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Exception</font>`的子类。
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Exception</font>`类进一步分为两类：已检查异常（checked exceptions）和未检查异常（unchecked exceptions）。
        * 已检查异常：在编译时就被检查的异常，必须在方法签名中声明，或者在代码中显式地捕获和处理。例如，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">IOException</font>`和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">SQLException</font>`。
        * 未检查异常：在编译时不被检查的异常，通常是由于编程错误引起的，如`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">NullPointerException</font>`和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ArrayIndexOutOfBoundsException</font>`。这些异常不需要在方法签名中声明，也不强制要求捕获和处理。

## <font style="color:#7E45E8;">运行时异常与一般检查异常有何异同？ </font>
异常表示程序运行过程中可能出现的非正常状态，Exception类根据错误发生的原因分为：RuntimeException异常和RuntimeException之外的异常。

运行时异常表示虚拟机的通常操作中可能遇到的异常，是一种常见运行错误。java编译器不要求必须声明抛出未被捕获的运行时异常，如NullPointerException，ClassCastException，IndexOutOfBoundsException等。

非运行时异常也叫一般异常，java编译器要求方法必须声明抛出可能发生的非运行时异常，常见的一般异常包括如SocketException，SQLException，IOException，ClassNotFoundException，NoSuchMethodException等。

（一）运行时异常

```java
public class Test5 {
    //这是一个main方法，是程序的入口：
    public static void main(String[] args) {
        //运行时异常：
        int[] arr = {1,2,3};
        System.out.println(arr.length);
        /*int[] arr2 = null;
        System.out.println(arr2.length);*/
        System.out.println(arr[10]);
    }
}
```

（二）检查异常

```java
public class Test6 {
    //这是一个main方法，是程序的入口：
    public static void main(String[] args) {
        //检查异常：
        try {
            try {
                Class.forName("com.wm.test01.Test").newInstance();
            } catch (InstantiationException e) {
                e.printStackTrace();
            } catch (IllegalAccessException e) {
                e.printStackTrace();
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

## <font style="color:#7E45E8;">try {}里有一个return语句，那么finally {}里的code会不会被执行?</font>
return和finally执行顺序是：先执行finally最后执行return。

<font style="color:rgb(0,0,0);">      请看下面程序代码的运行结果： </font>

```java
public class Test {
    public static void main(String[] args){
        System.out.println(Test.test());;
    }
    static int test(){
        int x = 1;
        try{
            return x;
        }finally{
            x = 5;
        }
    }
}
```

<font style="color:rgb(0,0,0);">执行结果为：1</font>

<font style="color:rgb(0,0,0);">下面是代码的逐步解释：</font>

    1. <font style="color:rgb(0,0,0);">方法</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">test</font>`<font style="color:rgb(0,0,0);">被调用。</font>
    2. <font style="color:rgb(0,0,0);">局部变量</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">x</font>`<font style="color:rgb(0,0,0);">被初始化为1。</font>
    3. `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`<font style="color:rgb(0,0,0);">块被执行，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return x;</font>`<font style="color:rgb(0,0,0);">语句准备返回</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">x</font>`<font style="color:rgb(0,0,0);">的值（此时为1）。</font>
    4. <font style="color:rgb(0,0,0);">在返回值被实际传递给调用者之前，控制流转移到</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`<font style="color:rgb(0,0,0);">块。</font>
    5. `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`<font style="color:rgb(0,0,0);">块执行，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">x</font>`<font style="color:rgb(0,0,0);">的值被修改为5。但这不会影响已经确定的返回值。</font>
    6. <font style="color:rgb(0,0,0);">方法结束，返回值为1。</font>

<font style="color:rgb(0,0,0);"></font>

<font style="color:rgb(0,0,0);">请看下面程序代码的运行结果： </font>

```java
public class Test {
    public static void main(String[] args){
        System.out.println(Test.test());;
    }
    static int test(){
        try{
            return 1 ;
        }finally{
            return 2 ;
        }
    }
}
```

<font style="color:rgb(0,0,0);">返回的结果是2。</font>

<font style="color:rgb(0,0,0);">这里是代码的逐步解释：</font>

    1. `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">main</font>`<font style="color:rgb(0,0,0);">方法调用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Test.test()</font>`<font style="color:rgb(0,0,0);">。</font>
    2. `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">test</font>`<font style="color:rgb(0,0,0);">方法开始执行，进入</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`<font style="color:rgb(0,0,0);">块。</font>
    3. <font style="color:rgb(0,0,0);">在</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`<font style="color:rgb(0,0,0);">块中，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return 1;</font>`<font style="color:rgb(0,0,0);">语句被执行。但是，这里的返回值并没有立即被传递给调用者，因为</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`<font style="color:rgb(0,0,0);">块还没有执行。</font>
    4. <font style="color:rgb(0,0,0);">由于</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`<font style="color:rgb(0,0,0);">块正常结束（没有抛出异常），控制流转移到</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`<font style="color:rgb(0,0,0);">块。</font>
    5. <font style="color:rgb(0,0,0);">在</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`<font style="color:rgb(0,0,0);">块中，</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">return 2;</font>`<font style="color:rgb(0,0,0);">语句被执行。这个返回值将覆盖</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`<font style="color:rgb(0,0,0);">块中的返回值。</font>
    6. `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`<font style="color:rgb(0,0,0);">块执行完毕后，方法结束，返回值为2。</font>

## <font style="color:#7E45E8;">final, finally, finalize的区别。 </font>
	final 用于声明属性，方法和类，分别表示属性不可变，方法不可覆盖，类不可继承。 内部类要访问局部变量，局部变量必须定义成final类型。

finally是异常处理语句结构的一部分，表示总是执行。 

finalize是Object类的一个方法，当垃圾回收器确定不存在对该对象的更多引用时，会调用此方法，在对象被垃圾回收之前执行一些清理操作或资源释放。

## <font style="color:#7E45E8;">Java中的异常处理机制的简单原理和应用。 </font>
异常是指java程序运行时（非编译）所发生的非正常情况或错误，与现实生活中的事件很相似，现实生活中的事件可以包含事件发生的时间、地点、人物、情节等信息，可以用一个对象来表示，Java使用面向对象的方式来处理异常，它把程序中发生的每个异常也都分别封装到一个对象来表示的，该对象中包含有异常的信息。

Java对异常进行了分类，不同类型的异常分别用不同的Java类表示，所有异常的根类为java.lang.Throwable，Throwable下面又派生了两个子类：Error和Exception，Error 表示应用程序本身无法克服和恢复的一种严重问题，程序只有死的份了，例如，说内存溢出和线程死锁等系统问题。Exception表示程序还能够克服和恢复的问题，其中又分为系统异常和普通异常，系统异常是软件本身缺陷所导致的问题，也就是软件开发人员考虑不周所导致的问题，软件使用者无法克服和恢复这种问题，但在这种问题下还可以让软件系统继续运行或者让软件死掉，例如，数组脚本越界（ArrayIndexOutOfBoundsException），空指针异常（NullPointerException）、类转换异常（ClassCastException）；普通异常是运行环境的变化或异常所导致的问题，是用户能够克服的问题，例如，网络断线，硬盘空间不够，发生这样的异常后，程序不应该死掉。

java为系统异常和普通异常提供了不同的解决方案，编译器强制普通异常必须try..catch处理或用throws声明继续抛给上层调用方法处理，所以普通异常也称为checked异常，而系统异常可以处理也可以不处理，所以，编译器不强制用try..catch处理或用throws声明，所以系统异常也称为unchecked异常。

## <font style="color:#7E45E8;">Java的异常处理关键字：throws,throw,try,catch,finally分别代表什么意义？ </font>
Java的异常处理是通过5个关键词来实现的：try、catch、throw、throws和finally。一般情况下是用try来执行一段程序，如果出现异常，系统会抛出（throws）一个异常，这时候你可以通过它的类型来捕捉（catch）它，或最后（finally）由缺省处理器来处理。用try来指定一块预防所有"异常"的程序。紧跟在try程序后面，应包含一个catch子句来指定你想要捕捉的"异常"的类型。throw语句用来明确地抛出一个"异常"。throws用来标明一个成员函数可能抛出的各种"异常"。Finally为确保一段代码不管发生什么"异常"都被执行一段代码。

## <font style="color:#7E45E8;">throw和throws的区别?</font>
（1）位置不同：

throw：方法内部

throws: 方法的签名处，方法的声明处

（2）内容不同：

throw+异常对象（检查异常，运行时异常）

throws+异常的类型（可以多个类型，用，拼接）

（3）作用不同：

throw：异常出现的源头，制造异常。

throws:在方法的声明处，告诉方法的调用者，这个方法中可能会出现我声明的这些异常。然后调用者对这个异常进行处理：

要么自己处理要么再继续向外抛出异常

代码展示：

```java
public class Test7 {
    //这是一个main方法，是程序的入口：
    public static void main(String[] args) throws Exception {
        //实现一个功能：两个数相除，当除数为0的时候，程序出现异常。
        /*try {
            devide();
        } catch (Exception e) {
            e.printStackTrace();
        }*/
        devide();
    }
    public static void devide() throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("请录入第一个数：");
        int num1 = sc.nextInt();
        System.out.println("请录入第二个数：");
        int num2 = sc.nextInt();
        if(num2 == 0 ){//除数为0 ，制造异常。
            //制造运行时异常：
            /*throw new RuntimeException();*/
            //制造检查异常：
            /*try {
                throw new Exception();
            } catch (Exception e) {
                e.printStackTrace();
            }*/
            throw new Exception();
        }else{
            System.out.println("商："+num1/num2);
        }
    }
}
```

## <font style="color:#7E45E8;">finally 中的代码一定会执行吗？</font>
【1】什么代码会放在finally中呢？

关闭数据库资源，关闭IO流资源，关闭socket资源。

【2】有一句话代码很厉害，它可以让finally中代码不执行!

System.exit(0);//终止当前的虚拟机执行

## <font style="color:#7E45E8;">如何使用try-with-resources代替try-catch-finally？</font>
在Java中，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-with-resources</font>`语句是一种更简洁、更安全的方式来管理资源，它自动处理实现了`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">AutoCloseable</font>`接口（或其子接口`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Closeable</font>`）的资源的关闭操作。这种方式可以替代传统的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-catch-finally</font>`结构，使得代码更加简洁且易于维护。

`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-with-resources</font>`语句确保每个资源在语句结束时自动关闭，无论是正常结束还是异常结束。它通过在`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`关键字后面使用一对圆括号来声明一个或多个资源。

以下是一个使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-with-resources</font>`的示例，以及一个等效的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-catch-finally</font>`结构作为对比：

+ 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-with-resources</font>`

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesExample {
    public static void main(String[] args) {
        String filePath = "example.txt";
        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        // 注意：这里不需要显式地关闭BufferedReader，因为try-with-resources会自动处理
    }
}
```

+ 等效的`try-catch-finally`结构

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryCatchFinallyExample {
    public static void main(String[] args) {
        String filePath = "example.txt";
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(filePath));
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

在`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-with-resources</font>`示例中，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">BufferedReader</font>`在`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`语句的圆括号中声明，并且当`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try</font>`块结束时（无论是正常结束还是异常结束），它都会被自动关闭。这使得代码更加简洁，并且减少了忘记关闭资源的风险。

相比之下，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-catch-finally</font>`示例需要手动关闭资源，并且在`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`块中处理关闭操作可能抛出的异常。这增加了代码的复杂性，并且如果忘记在`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">finally</font>`块中关闭资源，可能会导致资源泄露。

因此，当使用实现了`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">AutoCloseable</font>`接口的资源时，推荐使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">try-with-resources</font>`语句来简化资源管理。

## <font style="color:#7E45E8;">ArrayList和Vector的区别</font>
ArrayList和Vector都是Java集合框架中提供的动态数组实现类，它们都实现了List接口，具有动态调整大小的能力，允许存储重复元素，并且元素保持插入顺序。然而，它们在以下几个方面存在一些关键的区别：

一、初始容量和扩容方式

+ ArrayList：其缺省初始容量为10（该值在Java 8及后续版本中可能有所不同，但通常默认为10）。当容器大小增加到容量大小时，容器容量会自动增加50%（即变为原来的1.5倍）。
+ Vector：其初始容量缺省也为10（但可以在创建Vector对象时指定初始容量）。当容量不足时，容器容量会以原来容量的2倍自动扩展。

二、线程安全性

+ ArrayList：是非线程安全的。在多线程环境下，如果需要对ArrayList进行并发访问或修改，必须手动实现同步操作，例如使用synchronized关键字或Collections.synchronizedList方法将其包装成同步的List。
+ Vector：是线程安全的。Vector类中的大部分方法都使用了synchronized关键字进行同步，以确保在多线程环境下对容器的操作是安全的。因此，在多线程环境中，Vector比ArrayList更适合使用。

三、性能

+ 由于ArrayList是非线程安全的，它在单线程环境下的性能通常比Vector更好。ArrayList没有同步开销，因此在执行添加、删除、查找等操作时速度更快。
+ 而Vector由于支持同步操作，具有额外的同步开销，因此在多线程环境下的性能相对较低。然而，在多线程环境中，Vector的线程安全性使其成为了一个更可靠的选择。

四、使用场景

+ ArrayList：适用于单线程环境或不需要考虑线程安全性的场景。在这些场景中，ArrayList提供了高性能的动态数组实现。
+ Vector：适用于多线程环境或需要保证容器同步性的场景。在这些场景中，Vector的线程安全性使其成为了一个更合适的选择。

## <font style="color:#7E45E8;">HashMap和Hashtable的区别</font>
HashMap是Hashtable的轻量级实现（非线程安全的实现），都实现了了Map接口。

Hashtable和HashMap采用的hash/rehash算法都大概一样，所以性能不会有很大的差异。

其主要区别：

    - 空键值：HashMap允许空（null）键值（key）,即允许将null作为一个entry的key或者value，而Hashtable不允许。
    - 同步性：Hashtable的方法是同步的，而HashMap不是，在只有一个线程访问的情况下，效率要高于Hashtable。 

## <font style="color:#7E45E8;">List和Map区别?</font>
List是存储单列数据的集合，Map是存储键和值这样的双列数据的集合；

List中存储的数据是有顺序的，允许重复，取值按照索引号来取；Map中存储的数据是没有顺序的，其键是不能重复的，它的值是可以有重复的，取值按照对应的键名来取。

## <font style="color:#7E45E8;">List、Map、Set三个接口存取元素时，各有什么特点？ </font>
首先，List与Set具有相似性，它们都是单列元素的集合，所以，它们有一个功共同的父接口，叫Collection。Set里面不允许有重复的元素，所谓重复，即不能有两个相等（equals方法为真）的对象。Set取元素时，只能以Iterator接口取得所有的元素，再逐一遍历各个元素。（如：HashSet的遍历，可以利用迭代器，也可以使用for-each循环，但是不可以使用普通for循环遍历）

List表示有先后顺序的集合，当多次调用add(Object e)方法时，每次加入的对象按先来后到的顺序排序。也可以插队，即调用add(int index,Object e)方法。一个对象可以被反复存储进List中。List除了可以以Iterator接口取得所有的元素，再逐一遍历各个元素之外，还可以调用get(index i)来明确说明取第几个。

Map与List和Set不同，它是双列的集合，其中有put方法，put(obj key,obj value)，每次存储时，要存储一对key/value，不能存储重复的key，这个重复的规则也是按equals比较相等。取则可以根据key获得相应的value，即get(Object key)。另外可以获得所有的key的集合，还可以获得所有的value集合，还可以获得key和value组合成的Map.Entry对象的集合。

## <font style="color:#7E45E8;">说出ArrayList,Vector, LinkedList存储性能和特性 </font>
同步性：ArrayList，LinkedList是不同步的，而Vector是同步的，由于使用了synchronized方法（线程安全），性能上较ArrayList差。

数据增长：从内部实现机制来讲ArrayList和Vector都是使用Object的数组形式来存储的。当你向这两种类型中增加元素的时候，如果元素的数目超出了内部数组目前的长度它们都需要扩展内部数组的长度，Vector缺省情况下自动增长原来一倍的数组长度，ArrayList是原来的50%（即变为原来的1.5倍）。

检索、插入、删除对象的效率：ArrayList和Vector中，从指定的位置（用index）检索一个对象，或在集合的末尾插入、删除一个对象的时间是一样的, 但是在集合的其他位置增加或移除元素花费时间长，由于要涉及数组元素移动等内存操作。

LinkedList使用双向链表实现存储，按序号索引数据需要进行前向或后向遍历，但是插入数据时只需要记录本项的前后项即可，所以插入速度较快。在插入、删除集合中任何位置的元素所花费的时间都是一样的，但它在索引一个元素的时候比较慢。

## <font style="color:#7E45E8;">LinkedList 为什么不能实现RandomAccess接口？</font>
`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">LinkedList</font>` 不能实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">RandomAccess</font>` 接口的原因，主要在于其底层数据结构的特性。

`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">RandomAccess</font>` 是一个标记接口，在 Java 集合框架中用来表明实现该接口的类支持高效的随机访问，即可以通过索引快速访问元素。然而，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">LinkedList</font>` 是基于链表的数据结构，链表是一种线性数据结构，其元素存储在节点中，每个节点包含一个数据部分和一个指向下一个节点的引用。由于链表的节点在内存中不一定是连续的，因此无法通过索引直接访问特定位置的元素。相反，访问链表中的元素通常需要通过遍历节点来实现，这导致访问时间复杂度为 O(n)，其中 n 是链表中元素的数量。

相比之下，实现了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">RandomAccess</font>` 接口的类（如 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ArrayList</font>`）通常具有基于数组的数据结构，数组元素在内存中是连续的，因此可以通过索引直接访问特定位置的元素，访问时间复杂度为 O(1)。

因此，由于 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">LinkedList</font>` 的底层数据结构不支持高效的随机访问，它不能实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">RandomAccess</font>` 接口。在实际应用中，当需要频繁地通过索引访问元素时，应该选择实现了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">RandomAccess</font>` 接口的集合类（如 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ArrayList</font>`）。而在需要频繁插入和删除操作的场景下，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">LinkedList</font>` 会更为高效。

## <font style="color:#7E45E8;">Comparable 和 Comparator 的区别</font>
`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 和 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 都是 Java 中用于定义对象比较规则的接口，但它们在使用方式和应用场景上存在显著的区别。

一、定义与位置

1. Comparable：
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 是一个位于 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">java.lang</font>` 包中的接口。
    - 它被称为“内比较器”，因为实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口的类具有自身比较的能力。
2. Comparator：
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 是一个位于 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">java.util</font>` 包中的接口。
    - 它被称为“外比较器”，因为它允许开发者为不支持排序的类（即没有实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口的类）定义比较规则。

二、实现方式

1. Comparable：
    - 实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口的类需要重写 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">compareTo(T o)</font>` 方法。
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">compareTo</font>` 方法定义了对象之间的自然排序规则。
    - 实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口的类的对象可以用作有序集合（如 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">TreeSet</font>`）或有序映射（如 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">TreeMap</font>`）中的元素，而不需要指定比较器。
2. Comparator：
    - 实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 接口的类需要重写 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">compare(T o1, T o2)</font>` 方法。
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">compare</font>` 方法定义了对象之间的比较逻辑，这种逻辑可以不同于 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口中定义的自然排序规则。
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 接口提供了一种更灵活、更定制化的排序机制。

三、应用场景

1. Comparable：
    - 适用于类本身具有自然排序规则的情况。
    - 例如，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">String</font>` 类和 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Integer</font>` 类都实现了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口，因此它们可以按照字典序和数字大小进行自然排序。
2. Comparator：
    - 适用于需要对对象进行多种排序规则的情况。
    - 例如，对于 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Person</font>` 类，我们可以定义一个根据年龄排序的 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 和一个根据姓名排序的 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>`。
    - `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 还常用于对集合或数组进行排序时，当集合或数组中的元素类型没有实现 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口，或者需要按照不同于自然排序规则的方式排序时。

四、优先级

+ 当一个类同时实现了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 接口和提供了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 比较器时，通常 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 的比较规则会覆盖 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 的自然排序规则。
+ 这意味着在使用排序方法（如 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Collections.sort()</font>` 或 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Arrays.sort()</font>`）时，如果指定了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>`，则会按照 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 的规则进行排序；否则，会按照 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 的自然排序规则进行排序。

五、示例代码

以下是一个简单的示例代码，展示了 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>` 和 `<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>` 的使用：

```java
import java.util.*;

class Person implements Comparable<Person> {
    private String name;
    private int age;

    // 构造函数、getter 和 setter 方法省略

    @Override
    public int compareTo(Person p) {
        int temp = this.age - p.age;
        return temp == 0 ? this.name.compareTo(p.name) : temp;
    }
}

class PersonComparator implements Comparator<Person> {
    @Override
    public int compare(Person p1, Person p2) {
        int temp = p1.getName().compareTo(p2.getName());
        return temp == 0 ? p1.getAge() - p2.getAge() : temp;
    }
}

public class Main {
    public static void main(String[] args) {
        List<Person> people = new ArrayList<>();
        // 添加一些 Person 对象到列表中（省略）

        // 使用自然排序（根据年龄和姓名）
        Collections.sort(people);//它会使用集合中元素的默认比较器，即元素必须实现Comparable接口

        // 使用自定义比较器排序（根据姓名和年龄）
        Collections.sort(people, new PersonComparator());
    }
}
```

在这个示例中，`Person` 类实现了 `Comparable` 接口，定义了按照年龄和姓名的自然排序规则。同时，我们还定义了一个 `PersonComparator` 类，实现了 `Comparator` 接口，定义了按照姓名和年龄的比较规则。在 `main` 方法中，我们展示了如何使用这两种排序规则对 `Person` 对象列表进行排序。

## <font style="color:#7E45E8;">介绍Collection框架的结构</font>
```java
Collection
    ├List
        │├LinkedList
        │├ArrayList
        │└Vector
        │ └Stack
    └Set
        ├HashSet
        └TreeSet
    Map
        ├Hashtable
        │└Properties
        ├HashMap
        └WeakHashMap
```

Collection是最基本的集合接口，一个Collection代表一组Object。 

## <font style="color:#7E45E8;">Collection框架中实现比较要实现什么接口?</font>
要排序的类实现Comparable接口或者通过其它实现Comparator接口的比较器来排序。

Compaable接口通过compareTo()方法进行比较；Comparator接口通过compare()方法进行比较。

一般排序使用Collections工具类的sort()方法对集合进行排序。

Collections.sort(实现了Comparable接口的类的集合);//<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">它会使用集合中元素的默认比较器，即元素必须实现Comparable接口</font>

Collections.sort(集合，外部比较器);

## <font style="color:#7E45E8;">Collection 和 Collections的区别?</font>
Collection是集合类的上级接口，子接口主要有Set 和List。 

Collections是针对集合类的一个帮助类，提供一系列静态方法实现对各种集合的搜索、排序、线程安全化等操作。 



## <font style="color:#7E45E8;">Iterable接口有什么作用？</font>
<img src="https://cdn.nlark.com/yuque/0/2026/png/39281619/1772434023197-c3a59431-dc1a-4ec1-91f0-d9a0acf5d39e.png" width="1331.2" title="" crop="0,0,1,1" id="u946e1b8d" class="ne-image">

在Java中，Iterable接口扮演着至关重要的角色。它是Java集合框架中的一个核心接口，定义了一种通用的迭代方式，使得实现了该接口的集合类可以方便地遍历其元素。以下是Iterable接口的主要作用：

1. 提供统一的迭代方式：  
Iterable接口为集合提供了一种统一的遍历方式。通过实现Iterable接口，集合类可以支持for-each循环语法，从而简化了遍历集合的代码。for-each循环会隐式地调用集合的iterator()方法来获取迭代器，并使用迭代器进行遍历操作。
2. 支持for-each循环：  
实现了Iterable接口的集合类可以直接使用for-each循环进行遍历，而无需手动创建迭代器。这使得代码更加简洁和易读。
3. 增强代码的可读性和可维护性：  
使用for-each循环遍历集合时，代码更加直观和易于理解。此外，由于for-each循环隐藏了迭代器的细节，因此减少了出错的可能性，提高了代码的可维护性。
4. 支持并发操作（在JDK 8及之后）：  
在JDK 8及之后的版本中，Iterable接口增加了lambda迭代的forEach方法以及获取Spliterator可分割迭代器的方法。这使得集合类在遍历元素时，可以支持并发操作，提高了遍历效率。
5. 作为集合框架的基础：  
Iterable接口是Java集合框架中所有集合类型的基本接口之一。许多容器类都实现了Iterable接口，以便它们可以被迭代。这确保了集合框架的一致性和互操作性。
6. 与Iterator接口协同工作：  
Iterable接口通过其iterator()方法返回一个实现了Iterator接口的对象。Iterator接口定义了遍历集合中所有元素的方法，如hasNext()、next()和remove()等。Iterable接口和Iterator接口共同为集合的遍历提供了完整的解决方案。

综上所述，Iterable接口在Java集合框架中扮演着非常重要的角色。它提供了一种通用的迭代方式，使得容器类可以方便地遍历其元素，并支持并发操作。同时，它也增强了代码的可读性和可维护性，是Java集合框架中不可或缺的一部分。

## <font style="color:#7E45E8;">Iterator迭代器的作用？</font>
在Java中，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Iterator</font>`（迭代器）是一个用于遍历集合（如List、Set等）元素的接口。它提供了一种统一的方法来访问集合中的每一个元素，而无需了解集合的内部结构。`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Iterator</font>`接口属于Java集合框架（Java Collections Framework）的一部分，该框架提供了一套设计良好的支持对大量对象进行高效操作（如搜索、排序、遍历等）的类和接口。

`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Iterator</font>`接口主要包含以下几个方法：

1. `**<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">boolean hasNext()</font>**`：
    - 如果仍有元素可以迭代，则返回`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">true</font>`。
2. `**<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">E next()</font>**`：
    - 返回迭代的下一个元素。
    - 在调用此方法之前，必须先调用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hasNext()</font>`方法以确保有元素可以返回。
    - 如果在调用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">next()</font>`时没有更多的元素可供迭代，则会抛出`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">NoSuchElementException</font>`。
3. `**<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">void remove()</font>**`：
    - 从迭代器指向的集合中移除迭代器最后一次返回的元素（可选操作）。
    - 如果调用此方法之前未调用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">next()</font>`方法，或者已经调用了太多次的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">next()</font>`方法，则抛出`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">IllegalStateException</font>`。
    - 如果迭代器不支持移除操作，则调用此方法将抛出`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">UnsupportedOperationException</font>`。

`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Iterator</font>`接口的使用通常遵循以下步骤：

1. 通过集合的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">iterator()</font>`方法获取该集合的迭代器实例。
2. 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hasNext()</font>`方法检查是否还有元素可以迭代。
3. 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">next()</font>`方法获取当前迭代的元素。
4. 如果需要，可以使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">remove()</font>`方法从集合中移除元素（注意：这通常是在遍历过程中进行某些条件判断后执行的操作）。

使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Iterator</font>`遍历集合的好处之一是它提供了一种统一的方式来遍历不同类型的集合，而无需关心集合的具体实现。此外，`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Iterator</font>`还允许在遍历过程中安全地移除元素（如果迭代器支持此操作）。然而，需要注意的是，使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Iterator</font>`遍历集合时，不能通过集合的方法来修改集合（除了通过迭代器自身的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">remove()</font>`方法），否则可能会抛出`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ConcurrentModificationException</font>`异常。

## <font style="color:#7E45E8;">TreeSet如何排序？</font>
TreeSet是依靠TreeMap来实现的，TreeSet是一个有序集合，元素按照升序排列，默认是按照自然顺序排列，也就是说TreeSet中的对象元素需要实现Comparable接口。 

如果类没有实现Comparable接口，可以在创建TreeSet对象时传递一个比较器来实现排序。

TreeSet类中跟HashSet类一样也没有get()方法来获取列表中的元素，所以也只能通过迭代器方法来获取。两个相等的元素无法同时放到集合中。

```java
public class Student implements Comparable<Student> {
    private int age;
    private String name;
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Student(int age, String name) {
        this.age = age;
        this.name = name;
    }
    @Override
    public String toString() {
        return "Student{" +
                "age=" + age +
                ", name='" + name + '\'' +
                '}';
    }
    @Override
    public int compareTo(Student o) {
        return this.getAge()-o.getAge();
    }
}
```

```java
public class Test03 {
    //这是main方法，程序的入口
    public static void main(String[] args) {
        //创建一个TreeSet:
        TreeSet<Student> ts = new TreeSet<>();
        ts.add(new Student(10,"elili"));
        ts.add(new Student(8,"blili"));
        ts.add(new Student(4,"alili"));
        ts.add(new Student(9,"elili"));
        ts.add(new Student(10,"flili"));
        ts.add(new Student(1,"dlili"));
        System.out.println(ts.size());
        System.out.println(ts);
    }
}
```

## <font style="color:#7E45E8;">HashMap 和 TreeMap 区别</font>
HashMap和TreeMap是Java集合框架中的两种不同实现，它们提供了不同的特性和用途。以下是它们之间的主要区别：

一、内部实现

+ HashMap：基于哈希表的数据结构实现。它使用键的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">hashCode()</font>`方法来确定键值对在哈希表中的位置。如果发生哈希冲突（即不同的键具有相同的哈希值），则使用链表（在JDK 8之前）或红黑树（在JDK 8及之后）来解决冲突。
+ TreeMap：基于红黑树（一种自平衡的二叉搜索树）实现。它根据键的自然顺序（如果键实现了`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparable</font>`接口）或通过提供的`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Comparator</font>`来组织键值对。

二、元素排序

+ HashMap：不保证元素的顺序。元素的排列顺序会随着键值对的添加、删除或更新而变化。
+ TreeMap：保证元素按照键的排序顺序（自然顺序或自定义比较器顺序）进行存储和遍历。

三、线程安全性

+ HashMap：不是线程安全的。如果在多线程环境中使用，需要外部同步或使用线程安全的集合类（如`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">ConcurrentHashMap</font>`）。
+ TreeMap：同样不是线程安全的。多线程访问时也需要适当的同步措施。

四、性能

+ HashMap：提供了快速的查找、插入和删除操作。在平均情况下，这些操作的时间复杂度为O(1)。然而，在最坏情况下（哈希冲突很多时），性能可能会下降到O(n)。
+ TreeMap：查找、插入和删除操作的时间复杂度为O(log n)，因为底层实现是红黑树。

五、键值对的存储限制

+ HashMap：允许使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">null</font>`作为键和值。但是，每个HashMap只能有一个`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">null</font>`键，因为键是唯一的。
+ TreeMap：不允许使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">null</font>`作为键，否则会抛出`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">NullPointerException</font>`。但是，可以使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">null</font>`作为值。

六、适用场景

+ HashMap：适用于需要快速查找、插入和删除操作，且不关心元素顺序的场景。
+ TreeMap：适用于需要有序存储和遍历键值对的场景，可以根据键进行排序操作。

综上所述，HashMap和TreeMap各有其独特的特性和适用场景。在选择使用哪种集合时，应根据具体需求来决定。

## <font style="color:#7E45E8;">HashMap 的底层实现</font>
HashMap是Java中一种非常常用的基于哈希表的数据结构，允许以O(1)的时间复杂度进行元素的插入、查找和删除。它通过“键-值”对的方式存储数据，底层实现主要依赖于数组、链表（在JDK 1.8之后还引入了红黑树）以及哈希函数。以下是HashMap底层实现的详细解析：

一、哈希函数与哈希值

每个键都会通过哈希函数计算出一个哈希值，这个哈希值用于决定数据在数组中的存储位置。哈希函数的主要目的是将数据均匀地分布在不同的桶（bucket）中，从而减少哈希碰撞（即两个不同的键映射到同一个桶中的情况）。

二、数组

HashMap的底层是一个数组，每个数组元素可以看作是一个桶，用于存放链表或红黑树（在JDK 1.8及之后版本中）。当新元素插入HashMap时，它首先根据哈希值找到数组中的某个位置（桶）。如果该位置为空，则直接插入；如果该位置已经存在元素（发生碰撞），则通过链表或红黑树解决冲突。

三、链表与红黑树

1. 链表：在JDK 1.8之前的版本中，链表是解决哈希冲突的唯一方式。当发生哈希碰撞时，HashMap会将相同哈希值的元素以链表的形式存储在同一个桶中。
2. 红黑树：在JDK 1.8及之后的版本中，当链表长度超过一定阈值（默认是8）时，且当前数组长度大于64时，链表会转换为红黑树。红黑树的引入是为了降低在链表较长时搜索的时间复杂度，从O(n)降低到O(log n)，查询效率提升了。

四、负载因子与扩容

1. 负载因子：HashMap有一个重要的参数叫负载因子（load factor），它决定了当数组中元素数量超过数组容量的多大比例时会触发扩容操作。默认的负载因子是0.75。也就是说，当HashMap的元素数量达到数组容量的75%时，HashMap会自动进行扩容操作。
2. 扩容：扩容时，HashMap会重新分配一个更大的数组（通常是原来的2倍），并将原来的元素重新映射到新的数组中。这个过程叫做rehashing，比较耗时，因为要重新计算每个元素的哈希值并将其放入新的桶中。

五、插入逻辑

1. 检查数组是否为空：如果数组为空，调用resize()方法进行扩容。
2. 找到数组中的桶位置：通过哈希值定位存储桶。如果该位置为空，则直接插入。
3. 处理哈希碰撞：如果该位置已经有元素，则检查是否是相同的键。如果是，则覆盖旧值；如果不是，则遍历链表或红黑树来寻找插入点。
4. 树化：如果链表长度超过阈值，且当前数组长度大于64，则将链表转换为红黑树。
5. 扩容检查：如果元素数量超过阈值（即负载因子与当前容量的乘积），则进行扩容。

综上所述，HashMap的底层实现通过结合数组、链表（以及红黑树在JDK 1.8及之后版本中）和哈希函数等数据结构及算法，实现了高效的存储和查询机制。

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1737102605541-0188e48f-cef8-4f0f-9237-9a9ac3770873.png" width="1025.6" title="" crop="0,0,1,1" id="ud1ec13d1" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">HashMap有哪几种遍历方式？</font>
HashMap的遍历方式多种多样，根据JDK版本的不同以及具体实现方式的不同，可以归纳为以下几种主要方式：

一、迭代器（Iterator）方式遍历

1. 遍历entrySet：
    - 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.entrySet().iterator()</font>`获取迭代器，然后通过`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">while</font>`循环和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">iterator.next()</font>`方法逐个访问键值对。
    - 这种方式性能较好，因为entrySet包含了所有的键值对，且避免了二次取值。
2. 遍历keySet：
    - 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.keySet().iterator()</font>`获取迭代器，然后通过`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">while</font>`循环和`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">iterator.next()</font>`方法逐个访问键，再通过`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.get(key)</font>`获取对应的值。
    - 这种方式性能稍差，因为需要二次取值。

二、For Each方式遍历

1. 遍历entrySet：
    - 使用增强for循环（for-each）直接遍历`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.entrySet()</font>`，这种方式代码简洁，易于阅读。
    - 同样是性能较好的一种方式。
2. 遍历keySet：
    - 使用增强for循环遍历`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.keySet()</font>`，然后通过`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.get(key)</font>`获取对应的值。
    - 这种方式同样存在二次取值的问题，性能稍差。
3. 遍历values：
    - 使用增强for循环遍历`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.values()</font>`，这种方式只能获取到值，无法直接获取到键。
    - 如果只需要遍历值，这种方式是合适的。

三、Lambda表达式遍历（JDK 1.8+）

1. 直接遍历：
    - 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.forEach((key, value) -> { /* 操作 */ })</font>`方法，通过Lambda表达式直接遍历键值对。
    - 这种方式代码简洁，且利用了Java 8引入的函数式编程特性。
2. 遍历entrySet：
    - 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.entrySet().forEach(entry -> { /* 操作entry.getKey()和entry.getValue() */ })</font>`方法，通过Lambda表达式遍历entrySet。
    - 这种方式与直接遍历类似，但更明确地表示了遍历的是entrySet。
3. 遍历keySet：
    - 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.keySet().forEach(key -> { /* 操作map.get(key) */ })</font>`方法，通过Lambda表达式遍历keySet。
    - 这种方式同样存在二次取值的问题，但代码仍然保持了简洁性。

四、Streams API遍历（JDK 1.8+）

1. 单线程遍历：
    - 使用`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">map.entrySet().stream().forEach(entry -> { /* 操作entry.getKey()和entry.getValue() */ })</font>`方法，通过Streams API进行遍历。
    - 这种方式利用了Java 8引入的Streams API，提供了更丰富的操作选项，如过滤、映射、排序等。
2. 多线程遍历（不常见）：
    - 虽然理论上可以使用Streams API的并行流（parallelStream）进行多线程遍历，但在HashMap的上下文中，由于HashMap本身不是线程安全的，因此多线程遍历通常不是推荐的做法。

五、性能分析

+ 一般来说，entrySet的遍历方式性能较好，因为它避免了二次取值，且能够同时获取键和值。
+ keySet的遍历方式性能稍差，因为需要二次取值。
+ values的遍历方式只适用于只需要遍历值的情况。
+ Lambda表达式和Streams API的遍历方式在性能上通常与对应的迭代器或for-each遍历方式相近，但提供了更简洁的代码和更丰富的操作选项。

综上所述，HashMap的遍历方式多种多样，根据具体需求和JDK版本的不同，可以选择最适合的遍历方式。在大多数情况下，推荐使用entrySet的遍历方式，因为它性能较好且能够同时获取键和值。



## <font style="color:#7E45E8;">ConcurrentHashMap了解吗？</font>
**<font style="color:#DF2A3F;">整体架构:</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1739102301979-03b7c083-2aeb-40db-90bf-40f6e5468445.png" width="1071" title="" crop="0,0,1,1" id="u1499f0b9" class="ne-image" style="font-size: 16px">

+ 底层是由数组+单向链表+ 红黑树组成
+ 当初始化一个ConcurrentHahMap的时候,底层默认会初始化一个长度为16的数组
+ 因为底层是哈希表结构,必然会存在哈希冲突的问题,采用链式寻址的方式来解决哈希表冲突问题
+ 当哈希冲突比较多的时候,会造成链表长度较长的问题,这样就会增加查询复杂度,所以JDK1.8后引入了红黑树的机制,当数组长度大于64,并且链表的长度大于8的时候,单向链表就会转成红黑树.
+ 如果元素数量减少,一旦长度小于等于6,红黑树会退化成为单向链表.

**<font style="color:#DF2A3F;">基本功能</font>**

+ ConcurrentHahMap本质上还是一个HashMap,因此功能与HashMap是一样的,但是ConcurrentHahMap在HashMap的基础上,提供了并发安全的实现,如何实现?主要是通过对Node节点去加锁来保证数据更新的安全性:

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1739102957299-de26d1a2-30e3-42cd-9265-5533361e783c.png" width="1570" title="" crop="0,0,1,1" id="uf7aba8aa" class="ne-image" style="font-size: 16px">

**<font style="color:#DF2A3F;">性能优化</font>**

+ **<font style="color:#000000;">JDK1.7之前,它采用的是Segment锁,分段锁,锁的范围更大,所以性能上会更低(JDK1.7最多16把锁)</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1739103687964-68550163-3bf0-4df6-973a-3645744e012e.png" width="671" title="" crop="0,0,1,1" id="u1af37497" class="ne-image" style="font-size: 16px">

+ **<font style="color:#000000;">在JDK1.8后,锁的粒度更细,一个桶是一把锁(一个桶代表一个索引位置,包括后面的链表或者红黑树),数据放数组时候,用的是CAS,数据放链表或者红黑树的时候,用的是synchronized</font>**

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1739103865990-f34636c5-3152-4171-9938-8ad9fe1cb0f2.png" width="740" title="" crop="0,0,1,1" id="ud6db2976" class="ne-image" style="font-size: 16px">

+ 引入红黑树机制后,降低了数据查询的时间复杂度,红黑树的时间复杂度是O(logn)
+ 当数组的长度不够的时候,底层需要对数组进行扩容,在扩容的方式上,引入了多线程并发扩容的实现.就是多个线程对原始数组进行分片分片后,每个线程负责一个分片的数据迁移,从而整体提升扩容过程中数据迁移的效率

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1739104420255-fd1767f2-ccaf-4e41-a97c-63f8bd4937a4.png" width="1045" title="" crop="0,0,1,1" id="u853e7e47" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">WeakHashMap类了解吗？</font>
<font style="color:#000000;background-color:rgb(253, 253, 254);">Java 中的 </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> 是一个特殊的哈希映射实现，它允许键值对中的键为弱引用（weak references）。这意味着，当垃圾回收器运行时，如果一个键除了作为 </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> 中的键之外，没有其他强引用，那么该键可以被回收。一旦键被回收，相应的值也会自动从映射中移除。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">以下是一些关于</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">的关键点：</font>

1. **<font style="color:#000000;background-color:rgb(253, 253, 254);">弱引用键</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - `<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">使用弱引用存储键。这意味着键对象可以被垃圾回收器回收，如果它们没有其他强引用。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">与之相对的是</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">HashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">，它使用强引用存储键和值，因此键和值在</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">HashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">中不会被垃圾回收器自动回收，除非显式地从映射中移除。</font>
2. **<font style="color:#000000;background-color:rgb(253, 253, 254);">自动清理</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">当垃圾回收器回收一个键时，相应的条目会自动从</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">中移除。这种机制不需要手动干预。</font>
3. **<font style="color:#000000;background-color:rgb(253, 253, 254);">迭代行为</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">在迭代</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">时，如果遇到已经被回收的键，这些条目不会出现在迭代结果中。因此，迭代过程可能看不到所有最初插入的条目。</font>
4. **<font style="color:#000000;background-color:rgb(253, 253, 254);">线程安全</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - `<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">不是线程安全的。如果在多线程环境中使用，需要额外的同步机制。</font>
5. **<font style="color:#000000;background-color:rgb(253, 253, 254);">使用场景</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - `<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">常用于缓存实现，其中缓存条目可以自动失效，当它们不再被其他地方使用时。这样可以避免内存泄漏，因为不再需要的对象可以被垃圾回收器回收。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">以下是一个简单的示例，展示了 </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> 的基本用法：</font>

```java
import java.util.WeakHashMap;
import java.util.Map;

public class WeakHashMapExample {
    public static void main(String[] args) {
        Map<String, String> weakMap = new WeakHashMap<>();
        
        // 创建一些字符串对象作为键
        String key1 = new String("Key1");
        String key2 = new String("Key2");
        
        // 将键值对添加到映射中
        weakMap.put(key1, "Value1");
        weakMap.put(key2, "Value2");
        
        // 输出映射内容
        System.out.println("Initial Map: " + weakMap);
        
        // 将 key1 设置为 null，以移除其强引用
        key1 = null;
        
        // 触发垃圾回收（请求 JVM 进行垃圾回收，但不保证一定会执行）
        System.gc();
        
        // 等待一会儿，让垃圾回收器有机会运行
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        // 输出映射内容（key1 对应的条目应该已经被移除）
        System.out.println("Map after GC: " + weakMap);
    }
}
```

<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">在这个示例中，当</font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">key1</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">被设置为</font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">null</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">并且垃圾回收器运行后，</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">key1</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">对应的条目将从</font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">中移除。因此，输出将显示</font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">key2</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">及其对应的值仍然存在，但</font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">key1</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> </font><font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">及其值已经被移除。</font>

<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">需要注意的是，垃圾回收的行为是不确定的，因此在实际代码中，不应该依赖 </font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">System.gc()</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> 的调用或特定的垃圾回收行为。这个例子只是为了演示 </font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">WeakHashMap</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"> 的工作原理。</font>

## <font style="color:#7E45E8;">几种常见集合的源码分析</font>
ArrayList

LinkedList

HashMap

...

## <font style="color:#7E45E8;">其它集合：</font>
[https://www.mashibing.com/course/81](https://www.mashibing.com/course/81)

## <font style="color:#7E45E8;">java中有几种类型的流？这些流分别继承自哪些抽象类？ </font>
字节流，字符流。字节流继承于InputStream,OutputStream，字符流继承于Reader,Writer。在java.io包中还有许多其他的流，主要是为了提高性能和使用方便。 

<img src="https://cdn.nlark.com/yuque/0/2024/png/39281619/1727402840622-efbf66de-5469-442b-97d7-238cdc731286.png" width="1186.4" title="" crop="0,0,1,1" id="ue43a58e7" class="ne-image" style="font-size: 16px">

继承关系：

```java
InputStream
    ├── FileInputStream
    ├── BufferedInputStream
    ├── DataInputStream
    └── ...

OutputStream
    ├── FileOutputStream
    ├── BufferedOutputStream
    ├── DataOutputStream
    └── ...

Reader
    ├── FileReader
    ├── BufferedReader
    ├── InputStreamReader
    └── ...

Writer
    ├── FileWriter
    ├── BufferedWriter
    ├── OutputStreamWriter
    └── ...
```

IO流的体系结构：

<img src="https://cdn.nlark.com/yuque/0/2024/png/39281619/1727402855677-c1bfc6e8-fb0a-4c64-8d8e-3d92a2cb51a8.png" width="956" title="" crop="0,0,1,1" id="u7cb96700" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">字节流与字符流的区别。</font>
<font style="color:#000000;background-color:rgb(253, 253, 254);">Java中的字节流与字符流是用于处理输入和输出的两种不同的流，它们之间存在显著的区别。以下是对这两者的详细比较：</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">一、数据表示与处理单位</font>

1. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字节流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">以字节（8位二进制数）为单位处理数据。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">不关心数据的具体编码和字符集。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">适用于处理任何类型的数据，包括非文本数据（如图像、音频等）。</font>
2. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字符流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">以字符为单位处理数据。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">使用特定的字符集进行编码和解码。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">通常用于处理文本数据。在Java中，字符流默认使用UTF-16编码。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">二、编码方式</font>

1. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字节流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">以字节的形式直接读写数据，不处理字符编码。</font>
2. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字符流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">以字符的形式读写数据，会根据指定的字符编码将字符转换为字节进行处理。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">在Java中，字符流是用于处理文本数据的抽象，它们提供了读取和写入字符序列的方法。然而，在计算机内部，所有的数据最终都是以字节的形式存储和传输的。因此，当字符流需要读取或写入文本数据时，它必须在字符和字节之间进行转换。</font>
        1. <font style="color:#000000;background-color:rgb(253, 253, 254);">字符到字节的转换</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：  
</font><font style="color:#000000;background-color:rgb(253, 253, 254);">当你使用字符流写入文本数据时（例如，通过</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Writer</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">的子类），字符流会将你提供的字符序列转换为字节序列。这个转换过程涉及到字符编码，即将字符映射到特定的字节序列上。Java允许你选择不同的字符编码（如UTF-8、ISO-8859-1等），但如果不指定，它将使用默认的字符编码（通常是UTF-16）。</font>
        2. <font style="color:#000000;background-color:rgb(253, 253, 254);">字节到字符的转换：  
</font><font style="color:#000000;background-color:rgb(253, 253, 254);">相反地，当你使用字符流读取文本数据时（例如，通过</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Reader</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">的子类），字符流会从数据源中读取字节序列，并将它们转换回字符序列。这个过程同样涉及到字符解码，即将字节序列映射回它们对应的字符上。同样地，你可以指定使用的字符编码，如果不指定，它将使用默认的字符编码。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">三、处理效率</font>

1. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字节流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">通常比字符流更快，因为它们直接操作字节，不需要进行编码和解码。</font>
2. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字符流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">在进行I/O操作时需要进行编码和解码，这可能会引入额外的性能开销。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">四、使用场景</font>

1. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字节流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">适用于处理二进制数据，如文件的复制、网络传输等。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">当需要处理二进制数据或者对性能要求较高时，应使用字节流。</font>
2. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字符流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">适用于处理文本数据，如文件的读写、文本的处理等。</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">当需要处理文本数据，尤其是在处理多语言文本或者需要考虑字符编码问题时，应使用字符流。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">五、类层次结构</font>

1. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字节流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">顶层抽象类是</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">InputStream</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">和</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">OutputStream</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">。</font>
2. **<font style="color:#000000;background-color:rgb(253, 253, 254);">字符流</font>**<font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">顶层抽象类是</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Reader</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">和</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Writer</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">六、转换关系</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">在Java中，可以使用</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">InputStreamReader</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">和</font><font style="color:#000000;background-color:rgb(253, 253, 254);"> </font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">OutputStreamWriter</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);"> </font><font style="color:#000000;background-color:rgb(253, 253, 254);">这两个类来在字节流和字符流之间进行转换。这使得在处理文本数据时，即使底层使用的是字节流，也可以通过这两个类方便地将其转换为字符流进行处理。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">综上所述，Java中的字节流与字符流在数据表示、编码方式、处理效率、使用场景以及类层次结构等方面都存在显著的区别。选择使用哪种流取决于具体的应用场景和数据类型。</font>

## <font style="color:#7E45E8;">什么是java序列化和反序列化，如何实现？请解释Serializable接口的作用。  项目中哪些功能使用到了？</font>
<font style="color:#000000;background-color:rgb(253, 253, 254);">（一）Java序列化和反序列化</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">Java序列化和反序列化是软件开发中的重要概念，特别是在数据存储、网络通信和远程调用等场景中。</font>

+ <font style="color:#000000;background-color:rgb(253, 253, 254);">序列化</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：是指将数据结构或对象转换为可以存储或传输的格式的过程。在Java中，通过序列化可以将对象转换为字节流，以便将其保存到文件、数据库或通过网络发送到其他系统。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">反序列化</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：是序列化过程的逆过程，即将存储或传输的数据格式恢复为原始数据结构或对象的过程。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">（二）实现方式</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">在Java中，序列化和反序列化通常通过实现</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口来实现。以下是具体步骤：</font>

1. <font style="color:#000000;background-color:rgb(253, 253, 254);">实现Serializable接口</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：一个类必须实现</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口才能使其对象序列化。这个接口是一个标记接口，没有任何方法需要实现，只是起到标记作用。当一个类实现了</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口时，就表示该类的实例是可以被序列化的。</font>
2. <font style="color:#000000;background-color:rgb(253, 253, 254);">使用ObjectOutputStream和ObjectInputStream</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">序列化</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：使用</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">ObjectOutputStream</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">的</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">writeObject()</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">方法将对象写入输出流，完成序列化。例如：</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("output.txt")); oos.writeObject(objectToSerialize);</font>`
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">反序列化</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：使用</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">ObjectInputStream</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">的</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">readObject()</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">方法从输入流中读取字节序列，反序列化为对象。例如：</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">ObjectInputStream ois = new ObjectInputStream(new FileInputStream("input.txt")); Object deserializedObject = ois.readObject();</font>`

<font style="color:#000000;background-color:rgb(253, 253, 254);">（三）Serializable接口的作用</font>

`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口在Java序列化和反序列化中起到了关键作用：</font>

1. <font style="color:#000000;background-color:rgb(253, 253, 254);">标记作用</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：通过实现</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口，可以告知JVM该对象是可以被序列化的。</font>
2. <font style="color:#000000;background-color:rgb(253, 253, 254);">提供序列化规范</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：Java要求序列化的对象必须遵循特定的协议和规范，而</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口则是Java定义的接口之一，其中定义了序列化和反序列化所需遵循的规范。</font>
3. <font style="color:#000000;background-color:rgb(253, 253, 254);">支持自定义序列化</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：实现</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口的类可以利用</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">transient</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">和</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">static</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">等关键字来控制其内部字段的序列化方式。此外，还可以通过重写</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">writeObject</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">和</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">readObject</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">方法来实现自定义的序列化和反序列化过程。</font>
4. <font style="color:#000000;background-color:rgb(253, 253, 254);">版本控制</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口提供了</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">serialVersionUID</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">属性，它可以保持类定义的稳定性，即使在类发生变化时也能保证反序列化成功。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">（四）项目中的应用场景</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">在项目中，序列化和反序列化通常用于以下场景：</font>

1. <font style="color:#000000;background-color:rgb(253, 253, 254);">数据存储</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：在将对象信息存储到文件或数据库中时，需要先将其序列化。当需要读取这些数据时，则需要反序列化。</font>
2. <font style="color:#000000;background-color:rgb(253, 253, 254);">网络通信</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：在通过网络发送数据时，数据通常需要先序列化为字符串或字节流格式，以便在接收方能够正确解析和恢复原始数据。</font>
3. <font style="color:#000000;background-color:rgb(253, 253, 254);">远程调用</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：在分布式系统中，客户端与服务器之间的通信经常需要序列化和反序列化操作，以便在不同的系统之间传递对象和数据。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">综上所述，Java的序列化和反序列化是实现对象持久化和网络传输的重要手段，而</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">Serializable</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口则为此提供了标准和规范。在项目中合理利用这些技术和接口，可以大大提高数据处理的效率和灵活性。</font>

## <font style="color:#7E45E8;">如果有些字段不想进行序列化怎么办？</font>
<font style="color:#000000;background-color:rgb(253, 253, 254);">使用</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">transient</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">关键字</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">这是最简单和直接的方法。只需在不想被序列化的字段前加上</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">transient</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">关键字。被</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">transient</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">修饰的字段在序列化时会被忽略，其值不会被保存到序列化后的数据中。在反序列化时，这些字段的值会被设置为该字段类型的默认值（如</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">null</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">、</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">0</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">、</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">false</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">等）。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">例如：</font>

```java
import java.io.Serializable;

public class User implements Serializable {
    private String username;
    private transient String password; // 不想被序列化的字段

    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    // 其他方法和字段...
}
```

<font style="color:#000000;background-color:rgb(253, 253, 254);">在这个例子中，</font>`<font style="color:#000000;">password</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">字段被标记为</font>`<font style="color:#000000;">transient</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">，因此在序列化</font>`<font style="color:#000000;">User</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">对象时，</font>`<font style="color:#000000;">password</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">字段的值不会被包含在内。</font>

## <font style="color:#7E45E8;">什么是泛型？</font>
<font style="color:#000000;background-color:rgb(253, 253, 254);">在Java中，泛型（Generics）是一种在编译时期进行类型检查的机制，它允许在类、接口和方法中定义类型参数（Type Parameters）。这些类型参数在代码实际运行时会被具体的类型（也称为实际类型参数或实际类型参数化类型）所替代。泛型的主要目的是提高代码的重用性、可读性和安全性。</font>

+ <font style="color:#000000;background-color:rgb(253, 253, 254);">泛型的好处</font>
    1. <font style="color:#000000;background-color:rgb(253, 253, 254);">类型安全</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：  
</font><font style="color:#000000;background-color:rgb(253, 253, 254);">泛型可以在编译时期检查类型错误，从而避免在运行时出现</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">ClassCastException</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">等异常。</font>
    2. <font style="color:#000000;background-color:rgb(253, 253, 254);">消除强制类型转换</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：  
</font><font style="color:#000000;background-color:rgb(253, 253, 254);">使用泛型后，编译器会自动进行类型转换，从而减少了代码中的显式类型转换。</font>
    3. <font style="color:#000000;background-color:rgb(253, 253, 254);">提高代码重用性</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：  
</font><font style="color:#000000;background-color:rgb(253, 253, 254);">通过定义泛型类、接口和方法，可以编写更加通用的代码，适用于多种数据类型。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">泛型的基本用法</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">泛型类</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">泛型接口</font>
    - <font style="color:#000000;background-color:rgb(253, 253, 254);">泛型方法</font>

## <font style="color:#7E45E8;">什么是泛型类、泛型接口、泛型方法？</font>
**（一）泛型类**

<font style="color:#000000;background-color:rgb(253, 253, 254);">在这个例子中，</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">GenericTest</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">类是一个泛型类，它有一个类型参数</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">E</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">。你可以使用</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">GenericTest<String></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">、</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">GenericTest<Integer></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">等来创建不同类型的</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">GenericTest</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">对象。</font>

```java
/**
 * GenericTes就是一个普通的类
 * GenericTest<E> 就是一个泛型类
 * <>里面就是一个参数类型，但是这个类型是什么呢？这个类型现在是不确定的，相当于一个占位
 * 但是现在确定的是这个类型一定是一个引用数据类型，而不是基本数据类型
 */
public class GenericTest<E> {
    int age;
    String name;
    E sex;
    public void a(E n){
    }
    public void b(E[] m){
    }
}
class Test{
    //这是main方法，程序的入口
    public static void main(String[] args) {
        //GenericTest进行实例化：
        //(1)实例化的时候不指定泛型：如果实例化的时候不明确的指定类的泛型，那么认为此泛型为Object类型
        GenericTest gt1 = new GenericTest();
        gt1.a("abc");
        gt1.a(17);
        gt1.a(9.8);
        gt1.b(new String[]{"a","b","c"});
        //（2）实例化的时候指定泛型：---》推荐方式
        GenericTest<String> gt2 = new GenericTest<>();
        gt2.sex = "男";
        gt2.a("abc");
        gt2.b(new String[]{"a","b","c"});
        
    }
}
```

**（二）泛型接口**

```java
public interface Pair<K, V> {
    K getKey();
    V getValue();
}
```

`<font style="color:#000000;background-color:rgb(253, 253, 254);">Pair</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">接口有两个类型参数</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">K</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">和</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">V</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">，分别代表键和值的类型。</font>

**（三）泛型方法**

```java
/**
 * 1.什么是泛型方法：
 * 不是带泛型的方法就是泛型方法
 * 泛型方法有要求：这个方法的泛型的参数类型要和当前的类的泛型无关
 * 换个角度：
 * 泛型方法对应的那个泛型参数类型 和  当前所在的这个类 是否是泛型类，泛型是啥  无关
 * 2.泛型方法定义的时候，前面要加上<T>
 *     原因：如果不加的话，会把T当做一种数据类型，然而代码中没有T类型那么就会报错
 * 3.T的类型是在调用方法的时候确定的
 * 4.泛型方法可否是静态方法？可以是静态方法
 */
public class TestGeneric<E> {
    //不是泛型方法 （不能是静态方法）
    public static void a(E e){
    }
    //是泛型方法
    public <T>  void b(T t){
    }
}
class Demo{
    //这是main方法，程序的入口
    public static void main(String[] args) {
        TestGeneric<String> tg = new TestGeneric<>();
        tg.a("abc");
        tg.b("abc");
        tg.b(19);
        tg.b(true);
    }
}
```

## <font style="color:#7E45E8;">泛型有哪些通配符？</font>
<font style="color:#000000;background-color:rgb(253, 253, 254);">在Java泛型中，通配符（Wildcard）是一种特殊的语法，它允许在不具体指定类型的情况下进行更灵活的代码编写。Java泛型通配符主要有以下几种：</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">1. 无界通配符（Unbounded Wildcards）</font>

+ <font style="color:#000000;background-color:rgb(253, 253, 254);">表示方法</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：使用</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">?</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">来表示。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">意义</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：无界通配符表示可以接受任何类型。它适用于我们不关心具体类型的场合。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">示例</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>

```java
public void printList(List<?> list) {
    for (Object obj : list) {
        System.out.println(obj);
    }
}
```

<font style="color:#000000;background-color:rgb(253, 253, 254);">在这个例子中，</font>`<font style="color:rgb(6, 7, 31);">printList</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">方法可以接收任何类型的</font>`<font style="color:rgb(6, 7, 31);">List</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">，如</font>`<font style="color:rgb(6, 7, 31);">List<String></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">或</font>`<font style="color:rgb(6, 7, 31);">List<Integer></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">，并打印其中的元素。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">2. 上界通配符（Upper Bounded Wildcards）</font>

+ <font style="color:#000000;background-color:rgb(253, 253, 254);">表示方法</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：使用</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"><? extends T></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">来表示。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">意义</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：上界通配符表示接受类型为T及其子类的泛型类型。它适用于需要读取数据而不需要修改数据的场景。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">示例</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>

```java
public void acceptNumbers(List<? extends Number> list) {
    for (Number number : list) {
        System.out.println(number);
    }
}
```

<font style="color:#000000;background-color:rgb(253, 253, 254);">在这个例子中，</font>`<font style="color:rgb(6, 7, 31);">acceptNumbers</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">方法可以接收</font>`<font style="color:rgb(6, 7, 31);">List<Integer></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">、</font>`<font style="color:rgb(6, 7, 31);">List<Double></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">等，因为它们都是</font>`<font style="color:rgb(6, 7, 31);">Number</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">的子类。</font>

<font style="color:#000000;background-color:rgb(253, 253, 254);">3. 下界通配符（Lower Bounded Wildcards）</font>

+ <font style="color:#000000;background-color:rgb(253, 253, 254);">表示方法</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：使用</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);"><? super T></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">来表示。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">意义</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：下界通配符表示接受类型为T及其父类的泛型类型。它适用于需要向集合中添加数据的场景。</font>
+ <font style="color:#000000;background-color:rgb(253, 253, 254);">示例</font><font style="color:#000000;background-color:rgb(253, 253, 254);">：</font>

```java
public void addNumbers(List<? super Integer> list) {
    list.add(10);
}
```

<font style="color:#000000;background-color:rgb(253, 253, 254);">在这个例子中，</font>`<font style="color:rgb(6, 7, 31);">addNumbers</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">方法可以接收</font>`<font style="color:rgb(6, 7, 31);">List<Object></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">、</font>`<font style="color:rgb(6, 7, 31);">List<Number></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">或</font>`<font style="color:rgb(6, 7, 31);">List<Integer></font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">，并允许向其添加</font>`<font style="color:rgb(6, 7, 31);">Integer</font>`<font style="color:#000000;background-color:rgb(253, 253, 254);">类型的数据。</font>

## <font style="color:#7E45E8;">什么是反射？有什么优缺点？</font>
+ 什么是反射

JAVA反射机制是在运行状态中，对于任意一个类，都能够知道这个类的所有属性和方法；对于任意一个对象，都能够调用它的任意方法和属性；这种动态获取信息以及动态调用对象方法的功能称为java语言的反射机制。

在编译后产生字节码文件的时候，类加载器子系统通过二进制字节流，负责从文件系统加载class文件。

在执行程序（java.exe）时候，将字节码文件读入JVM中--->这个过程叫做类的加载。然后在内存中对应创建一个java.lang.Class对象-->这个对象会被放入字节码信息中,这个Class对象,就对应加载那个字节码信息,这个对象将被作为程序访问方法区中的这个类的各种数据的外部接口。

所以：我们可以通过这个对象看到类的结构，这个对象就好像是一面镜子，透过镜子看到类的各种信息，我们形象的称之为反射.这种“看透”class的能力（the ability of the program to examine itself）被称为introspection（内省、内观、反省）。Reflection和introspection是常被并提的两个术语。

说明：在运行期间，如果我们要产生某个类的对象，Java虚拟机(JVM)会检查该类型的Class对象是否已被加载。如果没有被加载，JVM会根据类的名称找到.class文件并加载它。一旦某个类型的Class对象已被加载到内存，就可以用它来产生该类型的所有对象。

+ Java反射的优点
    1. 灵活性高：反射允许程序在运行时动态地加载类、调用方法、访问属性，而不需要在编译时就确定下来。这对于开发一些需要动态加载插件或模块的系统特别有用。
    2. 框架开发利器：许多框架（如Spring）都大量使用了反射。它们需要在运行时根据配置文件或注解来实例化对象、调用方法，反射是实现这一功能的关键。
    3. 测试方便：在单元测试中，有时需要访问类的私有属性或方法来进行测试。通过反射，可以轻松做到这一点，而不需要修改原有的代码。
+ Java反射的缺点
    1. 性能开销大：反射涉及到类型解析、方法查找等操作，这些都比直接调用要慢得多。特别是在高频调用的场景下，性能问题会更加明显。因此，在性能要求较高的场景中应谨慎使用反射。
    2. 安全性问题：反射可以绕过Java的访问控制机制，访问类的私有属性和方法。这可能会破坏封装性，导致代码的安全性降低。因此，在使用反射时应确保代码的安全性。
    3. 代码可读性差：反射的代码通常比较难读懂，因为它涉及到很多字符串操作，如类名、方法名等。这些字符串很容易出错，而且不易维护。过度使用反射可能会使代码变得复杂和难以阅读。
    4. 破坏封装性：反射可以访问类的私有成员，这在一定程度上破坏了面向对象的封装原则。如果滥用反射，可能会导致代码结构变得混乱不堪。

## <font style="color:#7E45E8;">Class类了解吗？</font>
<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1740037832234-b93b389b-f63e-4134-bdb5-c8366c969d20.png" width="1426.4" title="" crop="0,0,1,1" id="uaf13231a" class="ne-image" style="font-size: 16px">

在Java中，`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class</font>`类是一个非常重要的内置类，它提供了关于类和接口的运行时信息，并且可以用来进行反射操作。反射是一种强大的机制，允许程序在运行时检查和操作类、接口、字段和方法等。

以下是一些关于`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class</font>`类的关键点和用法示例：

+ 获取`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Class</font>`对象
    - 通过类名获取：

```java
Class<?> clazz = MyClass.class;
```

    - 通过对象实例获取：<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">	</font>

```java
MyClass obj = new MyClass();
Class<?> clazz = obj.getClass();
```

    - 通过`Class.forName`方法获取（需要处理`ClassNotFoundException`）：

```java
try {
    Class<?> clazz = Class.forName("com.example.MyClass");
} catch (ClassNotFoundException e) {
    e.printStackTrace();
}
```

+ <font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">使用</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">Class</font>`<font style="color:rgb(5, 7, 59);background-color:rgb(253, 253, 254);">对象</font>

<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">一旦你获得了</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class</font>`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">对象，你可以进行以下操作：</font>

    - 获取类的名称：

```java
String className = clazz.getName(); // 完全限定名
String simpleName = clazz.getSimpleName(); // 简单类名
```

    - 创建类的实例（需要处理`InstantiationException`和`IllegalAccessException`）：

```java
try {
    Object instance = clazz.newInstance(); // 仅适用于有默认构造函数的类
    // 或者使用更灵活的Constructor类
    Constructor<?> constructor = clazz.getConstructor();
    Object instance = constructor.newInstance();
} catch (Exception e) {
    e.printStackTrace();
}
```

    - 获取类的构造函数：

```java
Constructor<?>[] constructors = clazz.getConstructors();
for (Constructor<?> constructor : constructors) {
    System.out.println(constructor);
}
```

    - 获取类的方法：

```java
Method[] methods = clazz.getDeclaredMethods();
for (Method method : methods) {
    System.out.println(method.getName());
}
```

    - 获取类的字段：

```java
Field[] fields = clazz.getDeclaredFields();
for (Field field : fields) {
    System.out.println(field.getName());
}
```

    - 获取类的父类和接口：

```java
Class<?> superclass = clazz.getSuperclass();
Class<?>[] interfaces = clazz.getInterfaces();
```

## <font style="color:#7E45E8;">Field类了解吗？</font>
在Java中，反射（Reflection）是一种强大的工具，允许程序在运行时检查和操作自身的结构（如类、方法、字段等），而不需要在编译时知道这些信息。`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field</font>`类是Java反射API的一部分，用于表示类、接口或注解类型的字段（成员变量）。

以下是一些关于`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field</font>`类的关键点和用法示例：

（一）关键方法

    1. 获取字段（Field）
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class.getField(String name)</font>`: 获取公共字段。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class.getDeclaredField(String name)</font>`: 获取所有字段（包括私有字段）。
    2. 字段操作
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field.get(Object obj)</font>`: 获取指定对象上此字段的值。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field.set(Object obj, Object value)</font>`: 将指定对象上此字段的值设为指定的新值。
    3. 字段信息
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field.getName()</font>`: 获取字段的名称。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field.getType()</font>`: 获取字段的`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class</font>`对象，表示字段的声明类型。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field.isAccessible()</font>`: 检查该字段是否可以在没有`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">java.lang.access.AccessControlException</font>`的情况下被访问。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Field.setAccessible(boolean flag)</font>`: 设置字段的访问权限。

（二）使用示例

假设我们有一个简单的类`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Person</font>`：

```java
public class Person {
    private String name;
    public int age;

    public Person() {}

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
}
```

我们可以通过反射来获取和操作`<font style="color:rgb(6, 7, 31);">Person</font>`类的字段：

```java
import java.lang.reflect.Field;

public class ReflectionExample {
    public static void main(String[] args) {
        try {
            // 创建Person对象
            Person person = new Person("Alice", 30);

            // 获取公共字段age
            Field ageField = Person.class.getField("age");
            System.out.println("Public Field: " + ageField.getName() + " = " + ageField.get(person));

            // 获取私有字段name
            Field nameField = Person.class.getDeclaredField("name");
            // 设置私有字段的访问权限
            nameField.setAccessible(true);
            System.out.println("Private Field: " + nameField.getName() + " = " + nameField.get(person));

            // 修改私有字段的值
            nameField.set(person, "Bob");
            System.out.println("Modified Private Field: " + nameField.getName() + " = " + nameField.get(person));

        } catch (NoSuchFieldException | IllegalAccessException e) {
            e.printStackTrace();
        }
    }
}
```

输出结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1740213181467-5111ec7d-9dc2-43b3-b25c-2a29e6ec0748.png" width="249.6" title="" crop="0,0,1,1" id="ub7d65522" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">Method类了解吗？</font>
在Java反射API中，`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method</font>`类用于表示类、接口（从Java 8开始，接口也可以有默认方法和静态方法）或注解类型中的方法。通过反射，你可以在运行时检查方法的详细信息（如方法名、参数类型、返回类型等），并动态地调用对象的方法。

以下是一些关于`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method</font>`类的关键点和用法示例：

（一）关键方法

    1. 获取方法（Method）
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class.getMethod(String name, Class<?>... parameterTypes)</font>`: 获取公共方法，该方法名称和参数类型与指定参数匹配。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Class.getDeclaredMethod(String name, Class<?>... parameterTypes)</font>`: 获取类中声明的特定方法，该方法可以是公共的、受保护的、默认的（包级私有）或私有的。
    2. 方法调用
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method.invoke(Object obj, Object... args)</font>`: 在指定对象上调用此方法，传递指定的参数。如果方法是静态的，则`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">obj</font>`参数应为`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">null</font>`。
    3. 方法信息
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method.getName()</font>`: 获取方法的名称。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method.getReturnType()</font>`: 获取方法的返回类型。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method.getParameterTypes()</font>`: 获取方法的参数类型数组。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method.getParameterCount()</font>`: 获取方法的参数个数。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method.isAccessible()</font>`: 检查该方法是否可以在没有`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">java.lang.IllegalAccessException</font>`的情况下被访问。
    - `<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Method.setAccessible(boolean flag)</font>`: 设置方法的访问权限。

（二）使用示例

假设我们有一个简单的类`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">Calculator</font>`，它包含一些数学运算方法：

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    private int multiply(int a, int b) {
        return a * b;
    }
}
```

我们可以通过反射来调用这些方法：

```java
import java.lang.reflect.Method;

public class ReflectionMethodExample {
    public static void main(String[] args) {
        try {
            // 创建Calculator对象
            Calculator calculator = new Calculator();

            // 获取并调用公共方法add
            Method addMethod = Calculator.class.getMethod("add", int.class, int.class);
            int resultAdd = (int) addMethod.invoke(calculator, 5, 3);
            System.out.println("add(5, 3) = " + resultAdd);

            // 获取并调用私有方法multiply
            Method multiplyMethod = Calculator.class.getDeclaredMethod("multiply", int.class, int.class);
            // 设置私有方法的访问权限
            multiplyMethod.setAccessible(true);
            int resultMultiply = (int) multiplyMethod.invoke(calculator, 5, 3);
            System.out.println("multiply(5, 3) = " + resultMultiply);

        } catch (NoSuchMethodException | IllegalAccessException | InvocationTargetException e) {
            e.printStackTrace();
        }
    }
}
```

输出结果：

<img src="https://cdn.nlark.com/yuque/0/2025/png/39281619/1740213639848-5b792a20-07df-4176-ae98-ceee37e7dfae.png" width="151.2" title="" crop="0,0,1,1" id="ua658e128" class="ne-image" style="font-size: 16px">

## <font style="color:#7E45E8;">什么是注解？解析方式有哪几种？</font>
JDK5.0新增注解（Annotation），也叫元数据。

注解其实就是代码里的<font style="color:#DF2A3F;">特殊标记</font>，这些标记可以在编译,类加载,运行时被读取,并执行相应的处理。<font style="color:#DF2A3F;">通过使用注解,程序员可以在不改变原有逻辑的情况下，在源文件中嵌入一些补充信息。</font>代码分析工具、开发工具和部署工具可以通过这些补充信息进行验证或者进行部署。

使用注解时要在其前面增加@符号,并把该注解当成一个<font style="color:#DF2A3F;">修饰符</font>使用。用于修饰它支持的程序元素。

Annotation 可以像修饰符一样被使用，可用于修饰包，类，构造器,方法，成员变量,参数，局部变量的声明，这些信息被保存在Annotation的"name=value"对中。在JavaSE中，注解的使用目的比较简单，例如标记过时的功能，忽略警告等。在JavaEE/ArIdroid中注解占据了更重要的角色，例如用来配置应用程序的任何切面，<font style="color:#DF2A3F;">代替</font>JavaEE旧版中所遗留的繁冗代码和XML<font style="color:#DF2A3F;">配置</font>等。未来的开发模式都是基于注解的，JPA(java的持久化API)是基于注解的，Spring2.5以. E都是基于注解的，Hibernate3.x以后也是基于注解的，现在的Struts2有一部分也是基于注解的了，注解是一种趋势，一定程度上可以说 ：<font style="color:#DF2A3F;">框架=注解+反射+设计模式</font>。

## <font style="color:#7E45E8;">如何解析注解？</font>
（一）步骤指南

    1. 定义注解：  
首先，你需要定义一个注解。注解是通过`<font style="color:rgb(6, 7, 31);background-color:rgb(253, 253, 254);">@interface</font>`关键字声明的，并且可以包含元素（类似于类的字段），这些元素可以有默认值。
    2. 应用注解：  
将定义的注解应用到类、方法、字段或参数上。
    3. 解析注解：  
使用Java反射API在运行时读取注解的值。

（二）示例代码

定义注解

```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

// 定义一个注解，保留策略为RUNTIME，以便在运行时可以通过反射访问
@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {
    String value(); // 注解的元素
}
```

应用注解

```java
// 将注解应用到类上
@MyAnnotation(value = "This is a class annotation")
public class AnnotatedClass {
    
    // 将注解应用到方法上
    @MyAnnotation(value = "This is a method annotation")
    public void annotatedMethod() {
        // 方法体
    }
}
```

解析注解

```java
import java.lang.annotation.Annotation;
import java.lang.reflect.Method;

public class AnnotationParser {
    public static void main(String[] args) {
        try {
            // 获取AnnotatedClass类的Class对象
            Class<?> clazz = Class.forName("com.example.AnnotatedClass");
            
            // 检查类上是否有MyAnnotation注解
            if (clazz.isAnnotationPresent(MyAnnotation.class)) {
                MyAnnotation classAnnotation = clazz.getAnnotation(MyAnnotation.class);
                System.out.println("Class annotation value: " + classAnnotation.value());
            }
            
            // 获取类的方法数组
            Method[] methods = clazz.getDeclaredMethods();
            
            // 遍历方法，检查每个方法上是否有MyAnnotation注解
            for (Method method : methods) {
                if (method.isAnnotationPresent(MyAnnotation.class)) {
                    MyAnnotation methodAnnotation = method.getAnnotation(MyAnnotation.class);
                    System.out.println("Method " + method.getName() + " annotation value: " + methodAnnotation.value());
                }
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```


