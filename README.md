# Ningqi Wang

> nq.maigre@gmail.com, [LinkedIn](https://www.linkedin.com/in/ningqi-wang), [English Ver. Resume](https://drive.google.com/file/d/1xYoTwvz8s6pVGqTGwRoXwsvuOyOlt6ME)



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
  * 构建了 **color transform pipeline**，将**虚拟化 GPU** 的图形渲染请求调度到物理 GPU 上执行
  * 开发了内部使用的 APIs，并使用 *<u>Metal</u>* 构建了**高性能** *<u>GPU shaders</u>* 以支持 guest OS 中的视觉无障碍功能

* __Autodesk__ - Software Engineer Intern `2019.09-2020.02`
  * 将 Windows 版本的 AutoCAD（由数十万行 C/C++ 代码构成的项目）从 *<u>MSVC</u>* 迁移到 *<u>LLVM</u>* 平台
  * 升级内部的 *<u>CI/CD</u>* 平台，对由 LLVM 生成的 Windows 版本 AutoCAD builds 进行**自动化测试**
  * 开发了 *<u>Clang</u>* 插件，用以分析源代码文件的 dependency，并检测冗余代码



## 项目经历

* **云计算课程项目**
  * 使用 *<u>Hadoop</u>* 及 *<u>Spark</u>* 构建了 <u>*ETL* pipelines</u> 以：
    * 清洗 **1.4 TB** 的推特数据（用户间的评论、回复、点赞等互动数据）
    * 提前处理数据以得到中间结果（如提前统计推文中的某些字符串的出现次数、整合用户间的互动记录），从而加速后续计算
    * 合理使用 **RDD cache** 以减少数据通信量并加速整体计算过程
  * 推演并优化数据库的设计
    * <u>*HBase*</u>：
      * 设计 HBase 的二级索引，使得 throughput 提升了 **2531.33%**
    * <u>*MySQL*</u> ：
      * 通过拆表和优化 schema 减少了需要存储数据量和冗余度（通过 mysqldump 备份的文件大小从 16.6 GB 减小到 8.44 GB）
      * 从充分利用 MySQL 的索引、减少 join 操作次数等角度考虑，优化 SQL 查询语句
      * 分析各属性访问频次从而进行拆表、调整 MySQL 缓存配置，最终 throughput 提升为原来的 **6.595** 倍
  * 编写自动化测试脚本，获取测试结果与 reference server 返回的结果，分析并生成测试报告
  * 使用 *<u>React</u>*，*<u>Node.js</u>*，*<u>Docker</u>*，及 *<u>Kubernetes</u>* 构建了一个**微服务架构**的应用，用户可以通过网页使用运行在 Docker 容器中的各工具（包括 Jupyter Notebook，Hadoop，Spark）来分析或处理数据
  * 设计并使用 *<u>Gofiber</u>* 、 *<u>Vert.x</u>*、 *<u>Amazon Aurora</u>*、*<u>EKS</u>* 建构了**高性能**、**负载均衡**、有一定**容错能力**的云服务，支持区块链验证请求（CPU 密集型任务）及复杂的数据库查询任务 （I/O 密集型任务）
* **并行算法 - 快速分布式训练**
  * 提出了一个**通用的同步机制**（即 **LOSP**，基于 *<u>Parameter Server</u>* 模型），在一个**分布式 GPU 集群**上**加速神经网络的训练过程**（通过使用 local compensation 及重叠计算和通信过程以减少同步过程的代价）
  * 实现了 LOSP（通过重载 *<u>PyTorch</u>* 训练和更新参数时的默认行为来实现）- 运行在 workers 上的状态机将控制 RPC 调用，进而操作本地或全局的神经网络参数；也实现了其他 3 种分布式训练算法以供比较
  * 编写了 Python 程序以：

    * 执行自动化训练，每种神经网络架构（CNN/AlexNet/LSTM/ResNet/DenseNet）会在不同的集群大小（4/8/16）和各种超参数组合下进行训练
    * 从 workers 采集各个本地模型在每一个 epoch 中的训练时间、loss 等评价数据

    * 定期评估全局模型的在测试集上的 accuracy
  * 以 Local-SGD 算法为 baseline，LOSP 达到了：

    * 绝大部分模型**收敛时间缩短为原来的约 50%** （且达到同样甚至更好的 accuracy）
    * **更高的 GPU 利用率**（空闲等待时间几乎为 **0**）
    * **显著降低的通信代价**（需要发送和接受的数据减少，同步过程的次数也减少）
  * 发表论文：H. Wang, Z. Qu, S. Guo, N. Wang, R. Li and W. Zhuang, ”LOSP: Overlap Synchronization Parallel With Local Compensation for Fast Distributed Training,” in IEEE Journal on Selected Areas in Communications, vol. 39, no. 8, pp. 2541-2557, Aug. 2021, doi: 10.1109/JSAC.2021.3087272.

* **Micro-Computer on FPGA**
  * **硬件层**：
    * 设计并使用 *<u>Verilog</u>* 实现了一个 *<u>MIPS32</u>* **CPU** 及 **Coprocessor 0**，支持中断、异常、系统调用；CPU 带有 **cache** 和 **5-stage pipeline**（静态、动态流水线都已实现）
    * 使用 DDR2 SDRAM 作为**内存**；实现了 SD 卡的读写控制器，从而使用 SD 卡作为**外存**
    * 构建了**以太网卡**的 adapter，使得 micro-computer 能够与其他设备通信
    * 构建了 **VGA 屏幕**的 adapter 及 buffer，以让 micro-computer 能够输出彩色图案和文字
  * **软件层**：
    * 编写了相应的软件 infrastructure 以收发**以太网帧**
    * 编写了一个运行在 micro-computer 上的游戏（由汇编语言编写并储存在 SD 卡上），用户可以通过运行在另一台电脑（通过网线连接到 micro-computer）上的 Python 程序控制游戏并获取游戏结果

    * 实现了一个 **bootloader** 以初始化各个外围设备并将游戏从 SD 卡加载入内存

* **计算机系统和基础设施项目**
  * **实时操作系统内核**：一个基本内核，支持多线程、抢占调度、上下文切换、优先级调度、互斥锁
  * **类 UNIX 文件系统**：一个简化版本的 UNIX 文件系统，带有读写缓存
  * **分布式文件系统**：使用读写锁构建的一个分布式文件系统，支持单写者和多读者
  * **动态内存分配机制**：即 malloc 及 free
  * **Linux Shell**：一个简易版本的 shell 程序，支持前后台任务切换、信号处理、I/O 重定向
  * **多线程网络代理服务器**：带有同步 cache 以缓存 web objects
  * **无锁队列**：使用 C++ 构建了一个 CAS 无锁队列
  * **RPC 框架**：使用 *Golang* 构建的一个通用的 RPC 框架
  * **Raft 一致性算法**：使用 Golang 复现该算法
  * **编译器**：
    * 根据输入的文法动态生成 LL(1) 或 SLR(1) parser（即 parser generator）
    * 通过 parser 分析一个类 C 语言，得到 AST 后转化为中间代码
    * 对于中间代码进行**处理器无关优化**及**窥孔优化**
    * 生成可在 x86 处理器上运行的汇编代码



## 其他

* **语言**：C++、C、Objective-C、Golang、Java，Scala、Python、R、JavaScript、TypeScript、Verilog、汇编语言
* **工具与技能**：
  * **系统软件**：CMake、Make、LLVM、GDB、perf、Valgrind
  * **Web 全栈**：React、Nginx、Django、Node.js、Gofiber、Vert.x、Kafka、MySQL、NoSQL、Redis、Docker、Kubernetes
  * **云计算、数据科学、机器学习**：Terraform、Spark、MapReduce、HBase、HDFS、pandas、NumPy、scikit-learn、PyTorch、TensorFlow

