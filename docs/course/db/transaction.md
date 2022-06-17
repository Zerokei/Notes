---
date-created: 2022-06-16 19:54
date-updated: 2022-06-17 08:19
---


# Transaction

## Basic concepts

### ACID

- 原子性(Atomicity): 事务中的所有步骤只能commit或者rollback。
- 一致性(Consistency): 单独执行事务可以保持数据库的一致性。
- 隔离性(Isolation): 事务在并行执行的时候不能感知到其他事务正在执行，中间结果对于其他执行的事务是隐藏的。
- 持续性(Durability): 更新之后哪怕软件出了问题，更新的数据也必须存在。

### 状态

- active：初始状态，执行中的事务都处于这个状态。
- partially committed：在最后一句指令被执行之后。
- failed：在发现执行失败之后。
- aborted：回滚结束，会选择是重新执行事务还是结束。
- committed：事务被完整的执行

![pic|300](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220616200220.png)

## Concurrent Executions

- **serial schedule** 串行调度：一个事务调度完成之后再进行下一个
- **equivalent schedule** 等价调度：改变处理的顺序但是和原来等价
- **conflict serializability** 冲突可串行化
	- **conflict equivalent**：两个调度之间可以通过改变一些不冲突的指令来转换，就叫做冲突等价
	- **conflict serializable**：冲突可串行化：当且仅当一个调度S可以和一个串行调度等价
	- **Precedence graph** 前驱图
- **Recoverable Schedules** 可恢复调度
	- 如果一个事务$T_1$要读取某一部分数据，而$T_2$要写入同一部分的数据，则$T_1$必须在 $T_2$commit之前就commit，否则就会造成dirty read
- **Cascading Rollbacks** 级联回滚: 单个事务的fail造成了一系列的事务回滚
- **Cascadeless Schedules** 避免级联回滚的调度
	- Cascadeless Schedules也是可恢复的调度

## Concurrency Control

- Lock-Based Protocols
	- exclusive(X) lock: 可读可写
	- shared(S) lock: 可读不可写
	- Lock-compatibility matrix![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220616215733.png)
- Two-Phase Locking Protocol
	- Phase 1: Growing Phase
		- transaction may obtain locks
		- transaction may not release locks
	- Phase 2: Shrinking Phase
		- transaction may release locks
		- transaction may not obtain locks
	- Two-Phase Locking Protocol assures serializability.
	- 两个变种
		- 严格两阶段封锁协议(strict two-phase locking protocol)：要求事务持有的 X 锁必须在 事务提交之后方可释放。解决级联回滚的问题。
		- 强两阶段封锁协议(rigorous two-phase locking protocol)：要求事务提交前不得释放 任何锁。
    - ![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220617160816.png)
- 锁转换(Lock Conversions)：提供了一种将 S 锁升级为 X 锁，X 锁降级为 S 锁的机制。只能在增 长阶段升级，缩减阶段降级。
- DeadLock
	- 互相持有锁的时候触发死锁
	- 可以通过执行事务前就要求拿到锁以避免运行时死锁（当然这样做就会有相应的性能代价）
	- 通过画依赖图判断是否产生死锁
	- 死锁恢复：选取一些事务进行回滚。当重复选取同样的事务牺牲(victim)并不断陷入死锁时，即陷入starvation(饥饿)

## Recovery System

### log-based Recovery 基于日志的恢复

- 日志(log)被存储在稳定的存储中，包含一系列的日志记录
	- 事务开始`<T start>`
	- 写操作之前之前的日志记录`<Ti, x, V1, V2>`
		- (X)是写的位置，
		- V1，V2分别是写之前和之后的X处的值
	- 事务结束的时候写入`<T commit>`
- 对于更新事务的两条规则
	- commit rule：新的数据在commit之前必须被写在**非易失性**的存储器中
	- logging rule：旧的值在新的写入之前需要被写在日志里

### Aries算法

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220617080817.png)

- Log
	- 记录一些必要信息![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220617081431.png)

- Page LSN
	- 每一页的LSN
	- 是每一页中最后一条起作用的日志记录的LSN编号

- Log Buffer
	- 记录的缓冲区，还没有写入Stable log

- Dirty Page Table
	- 存储在缓冲区的，记录已经被更新过的page的表
	- 每个页的RecLSN，表示这一页的日志记录中，在RecLSN之前的Log已经都被写入Stable log

- Checkpoint
	- 记录脏页表信息和活跃事务的LastLSN
	- 和log-based Recovery不同的是，它不会把内存页写入磁盘

- 恢复操作
	- 分析阶段
		- 读取最后一条完整的checkpoint日志记录信息
			- 设置RedoLSN = min RecLSN(脏页表中的)，如果脏页表是空的就设置为checkpoint的LSN(决定从哪里开始redo)
			- 设置undo-list：checkpoint中记录的事务
			- 读取undo-list中每一个事务的最后一条记录的LSN
		- 从checkpoint开始正向扫描
			- 如果发现了不在undo-list中的记录就写入undo-list
			- 当发现一条更新记录的时候，如果这一页不在脏页表中，用该记录的LSN作为 RecLSN写入脏页表中
			- 如果发现了标志事务结束的日志记录(commit, abort) 就从undo-list中移除这个事务
	- Redo阶段
		- 从RedoLSN开始正向扫描，当发现更新记录的时候如果这一页不在脏页表中。或者这一条记录的LSN小于页面的RecLSN就忽略这一条
		- 否则从磁盘中读取这一页，如果磁盘中得到的这一页的PageLSN比这一条要小，就redo，否则就忽略这一条记录
	- Undo阶段
		- 从日志末尾先前向前搜索，undo所有undo-list中有的事务
		- 用分析阶段的最后一个LSN来找到每个日志最后的记录
        - 每次选择一个最大的LSN对应的事务undo
        - 在undo一条记录之后
            - 对于普通的记录，将NextLSN设置为PrevLSN
            - 对于CLR记录，将NextLSN设置为UndoNextLSN
        - 如何undo：当一条记录undo的时候
            - 生成一个包含执行操作的CLR
            - 设置CLR的UndoNextLSN为更新记录的LSN

![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220617080800.png)
