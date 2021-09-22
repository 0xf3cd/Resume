# Ningqi Wang

> nq.maigre@gmail.com  [LinkedIn](https://www.linkedin.com/in/ningqi-wang)  [English Ver. Resume](https://drive.google.com/file/d/1xYoTwvz8s6pVGqTGwRoXwsvuOyOlt6ME)
>



## 教育经历

* __卡内基梅隆大学__ `2020.08 - 2021.12`
  * 硕士 - *Information Networking*；GPA：3.50/4.00
  * 担任两学期（Spring 2021 & Fall 2021）的 17-681 *Java for Application Programmers* 课程助教
* __同济大学__ `2015.09 - 2020.07`
  * 本科 - 计算机科学与技术；GPA：91.37/100；专业课 GPA：93.9/100
  * **上海市优秀毕业生**
  * 在 2017、2018 年获得同济优秀学生奖学金（年级排名分别为 14/177 及 **1/164**）



## 工作经历

* __Apple__ - GPU System Software Engineer Intern `2021.05 - 2021.08`
  * 与同事合作构建了一条 **color transform pipeline**，将**虚拟化 GPU** 的图形渲染请求调度到物理 GPU 上执行
  * 开发了内部使用的 APIs，并使用 *Metal* 构建了**高性能** *GPU shaders* 以支撑 guest OS 中的视觉无障碍功能
* __Autodesk__ - Software Engineer Intern `2019.09-2020.02`
  * 将 Windows 版本的 AutoCAD（一个由数十万行 C/C++ 代码构成的项目）从 *MSVC* 迁移到 *LLVM* 平台
  * 升级内部的 *CI/CD* 平台，对由 LLVM 生成的 Windows 版本 AutoCAD builds 进行**自动化测试**
  * 开发了一些 *Clang* 插件，用以分析源代码文件的 dependency，并检测冗余代码



## 项目经历

* **云计算相关课程项目**

  * 使用 *Hadoop* 及 *Spark* 在云上构建了 *ETL* pipelines 以处理 1.4 TB 的推特推文数据 - 优化 *HBase* 的 **rowkeys** 以及 *MySQL* 中各表的 **schema 和索引**，并将处理后的数据存入其中

  * 使用 *React*，*Node.js*，*Docker*，及 *Kubernetes* 构建了一个**微服务架构**的应用，用户可以通过网页使用运行在云上的工具来处理他们的数据（包括 Jupyter Notebook，Hadoop，及 Spark） 

  * 使用 *Gofiber* 和 *Vert.x* 设计并建构了一个**高性能**、**负载均衡**、有一定**容错能力**的云服务（硬件资源有限，预算紧张，且性能要求严格），支持区块链验证请求（CPU 密集型任务）及复杂的数据库查询任务 （I/O 密集型任务）

    

* **Micro-Computer on FPGA**

  * 设计并使用 *Verilog* 实现了一个 MIPS32 CPU 及 Coprocessor 0，支持中断、异常、系统调用；CPU 带有 **cache** 和 **5-stage pipeline**（静态、动态流水线都已实现）

  * 使用 DDR2 SDRAM 作为**内存**；实现了 SD 卡的读写控制器以将 SD 卡作为**外存**

  * 构建了**以太网卡**的 adapter，并编写了相应的软件 infrastructure 以处理**以太网帧**

  * 构建了 **VGA 屏幕**的 adapter 及 buffer，以让 micro-computer 能够输出彩色图案和文字

  * 编写了一个运行在 micro-computer 上的游戏（由汇编语言编写并储存在 SD 卡上），用户可以通过运行在另一台电脑（通过网线连接到 micro-computer）上的 Python 程序控制游戏并获取游戏结果

  * 实现了一个 **bootloader** 以初始化各个外围设备并将游戏从 SD 卡加载入内存

    

* **快速分布式训练的并行算法**

  * 提出了一个**通用的同步机制**（即 LOSP，基于 *Parameter Server* 模型），在一个分布式 GPU 集群上加速神经网络的训练过程（通过使用 local compensation 及重叠计算和通信过程以减少同步过程的代价）

  * 实现了 LOSP（通过重载 *PyTorch* 在参数训练时的行为以完成）- 运行在 workers 上的状态机将控制 RPC 调用，并以此操作本地或全局的神经网络参数；也实现了其他 3 种分布式训练算法以供之后的比较

  * 编写了 Python 程序以：1. 执行自动化训练，每种神经网络架构（CNN，AlexNet，LSTM，ResNet，及 DenseNet）会在不同的集群大小（4/8/16）和各种超参数组合下进行训练；2. 记录本地模型在每一个 epoch 中的训练时间、loss 等评价数据；3. 定期地使用测试集评估全局模型的 accuracy

  * 以 Local-SGD 算法为 baseline，LOSP 达到了：1. 大部分模型**收敛时间缩短为原来的约 50%** （且达到同样甚至更好的 accuracy）；2. **更高的 GPU 利用率**（几乎没有空闲等待时间）；3. **显著降低的通信代价**（需要发送和接受的数据减少，同步过程的次数也减少）

  * 发表论文：H. Wang, Z. Qu, S. Guo, N. Wang, R. Li and W. Zhuang, ”LOSP: Overlap Synchronization Parallel With Local Compensation for Fast Distributed Training,” in IEEE Journal on Selected Areas in Communications, vol. 39, no. 8, pp. 2541-2557, Aug. 2021, doi: 10.1109/JSAC.2021.3087272.

    

* **计算机系统和基础架构项目**

  * **实时操作系统内核**：一个基本内核，支持多线程、抢占调度、上下文切换、优先级调度、互斥锁
  * **类 UNIX 文件系统**：一个简化版本的 UNIX 文件系统，带有读写缓存
  * **分布式文件系统**：使用读写锁构建的一个分布式文件系统，支持单写者和多读者
  * **动态内存分配机制**：即 **malloc** 及 **free**
  * **Linux Shell**：一个简易版本的 shell 程序，支持前后台任务切换、信号处理、I/O 重定向
  * **多线程网络代理服务器**：一个带有同步 cache 以储存 web objects
  * **无锁队列**：使用 C++ 构建了一个 CAS 无锁队列
  * **RPC 框架**：使用 *Golang* 构建的一个通用的 RPC 框架
  * **Raft 公式算法**：使用 Golang 复现该算法
  * **编译器**：一系列软件：1. 根据输入的文法动态生成 LL(1) 或 SLR(1) parser（即 parser generator）；2. 通过 parser 分析一个类 C 语言，得到 AST 后转化为中间代码；3. 对于中间代码进行**处理器无关优化**及**窥孔优化**；4. 生成可在 x86 处理器上运行的汇编代码



## 其他

* 语言：C++，C，Objective-C，Golang，Java，Scala，Python，R，JavaScript，TypeScript，Verilog，汇编语言
* 工具与技能：系统软件（CMake，Make，LLVM，GDB，perf，Valgrind）；Web 全栈（React，Nginx，Django,
  Node.js，Gofiber，Vert.x，Kafka，MySQL，NoSQL，Redis，Docker，Kubernetes）；云计算、数据科学、机器学习（Terraform，Spark，MapReduce，HBase，HDFS，pandas，NumPy，scikit-learn，PyTorch，TensorFlow）

