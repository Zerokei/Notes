---
date-created: 2022-09-05 09:59
date-updated: 2022-09-07 15:45
---

# Verilog 语法手册

!!! info
	因为要当 **2022-2023 Fall 计算机系统Ⅱ** 的助教，所以特地来复习一下 verilog。


## 0 推荐资料

- [USTC Verilog OJ | 掌握 Verilog 基础语法与易错点](https://verilogoj.ustc.edu.cn/oj/)
- [Synthesizable Coding of Verilog | 阅读17-31页](http://www.ee.ncu.edu.tw/~jfli/vlsidi/lecture/Verilog-2012.pdf)

## 1 语法补充

### 1.1 Case

```verilog
always@(*) begin
	case(sel)         // case 语句使用方法：case ... endcase
		3'b000: begin // 多语句使用 begin...end 包裹
			out = data0;
		end
		3'b001: out = data1;
		3'b010: out = data2;
		3'b011: out = data3;
		default: out = 4'b0;
	endcase
end
```

### 1.2 位拼接

```verilog
module top_module (
    input [4:0] a, b, c, d, e, f,
    output [7:0] w, x, y, z );
    assign {w, x, y, z} = {a, b, c, d, e, f, 2'b11}; // 位拼接，需保持前后位宽一致。
endmodule
```

### 1.3 归约运算符

```verilog
x1 = & a[3:0] // AND: a[3]&a[2]&a[1]&a[0]. Equivalent to (a[3:0] == 4'hf)  
x2 = | b[3:0] // OR: b[3]|b[2]|b[1]|b[0]. Equivalent to (b[3:0] != 4'h0)  
x3 = ^ c[2:0] // XOR: c[2]^c[1]^c[0]
```

### 1.4 模块定义及其实例化

在定义模块时，我们会在**括号**中定义此模块的读口和写口，同时在 `module...endmodule` 中描述整个模块的行为（包括一些 `assign` 语句、`always` 块，抑或是 `reg` 和 `wire` 的申明等等）。

对于模块的写口，一共有两种写法，一种是 `output reg xxx`，一种是 `output wire xxx`（也可被简写为 `output xxx`）。[^out]

- 若写口在 `always` 语句中被赋值，则声明成 `reg` 类型；
- 若写口在 `assign` 语句中被赋值，则声明成 `wire` 类型（wire 可省略）。

关于模块的实例化，可以参考下方代码。

```verilog
module mod_a ( // 一个模块
    output   out1, // 写口
    input    in1,  // 读口
    input    in2  );
    // 描述模块行为
    assign out1 = in1 & in2;
endmodule

module top_module (  // 顶层模块
	input	a,
    input	b,
    output	out1
);
	// 实例化模块 mod_a，格式：[模块名] [实例名称]( );
    mod_a mod( 
        .in1(a), // 将 top_module 的 a 与 mod_a 的 in1 连接
        .in2(b),
        .out1(out1)
    );
endmodule
```

## 2 语法区分

### 2.1 阻塞赋值 & 非阻塞赋值[^block]

在Verilog中，有三种赋值方式，分别为：

- 连续赋值（如 `assign x = y;` ），该赋值方式只能用于过程块（如 always 块）之外；
- 阻塞赋值（如 `x = y;` ），该赋值方式只能用在过程块（如 `always@（*）`）内；
- 非阻塞赋值（如 `x <= y;` ），该赋值方式只能用在过程块内（ 如 `always@（posedge clk）` ）。

在设计Verilog模块时，请遵循以下原则：

- 在组合逻辑的 always 块内采用阻塞赋值；
- 时序逻辑的 always 块内采用非阻塞赋值。

从原理上来讲，非阻塞赋值的语句是同时执行的；而阻塞赋值的语句是顺序执行的。

```verilog
// 在 clk 上升沿时，交换 a 和 b。
always@(posedge clk) begin
	a <= b;
	b <= a;
end
```

我们也可以通过下方的例子，来具体感受阻塞赋值和非阻塞赋值的区别。

```verilog
always@(posedge clk) begin
	b = a;
	c = b;
end
```

阻塞赋值生成的电路图如下图所示：
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220905225058.png)

```verilog
always@(posedge clk) begin
	b <= a;
	c <= b;
end
```

非阻塞赋值生成的电路图如下图所示：
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220905224951.png)

### 2.2 使用 always 的组合电路[^always]

一般都说组合逻辑电路使用 `always@(*) {}`，那么其中的 `*` 表达的是什么意思呢？

答：`always` 语句后的括号内放的是敏感变量列表，对于 `always@(*) out = a & b | c ^ d` 来说，其完整写法是 `always@(a, b, c, d) out = a & b | c ^ d`。

组合逻辑电路中，`always` 块和 `assign` 语句二者生成的硬件电路一般是等效的。 但是 `always` 语句可以支持更加复杂的语法。

- `always` 中可以使用 `if...else...`，`case` 等语法。
- `always` 中，等号左边的变量为 `Reg` 类型；`assign` 中，等号左边的变量为 `wire` 类型。
- `always` 块内可对多个信号进行赋值，`assign` 语句只能对一个信号进行赋值。

## 3 易错点

### 3.1 分支语句缺失导致锁存器[^latch]

```verilog
always @(*) begin
    if (cpu_overheated)
       shut_off_computer = 1;
end
```

由于缺少 `else` 的情况，`shut_off_computer` 在 `cpu_overhead` 为 0 时，会保持原来的值。
![](https://zerokei-imgurl.oss-cn-hangzhou.aliyuncs.com/img/20220905150232.png)

若想要在 `cpu_overheated = 0` 时，将 `shut_off_computer` 置为 0，则需要使用下方逻辑：

```verilog
always @(*) begin
    if (cpu_overheated)
	    shut_off_computer = 1;
    else 
		shut_off_computer = 0;
end
```

### 3.2 组合逻辑中自我反馈

```verilog
// 错误示范
always @(*) begin // 组合逻辑
	a = a + 1; // 自我反馈
end
```

[^out]: https://stackoverflow.com/questions/5360508/using-wire-or-reg-with-input-or-output-in-verilog

[^block]: https://verilogoj.ustc.edu.cn/oj/problem/68

[^always]: https://verilogoj.ustc.edu.cn/oj/problem/62

[^latch]: https://verilogoj.ustc.edu.cn/oj/problem/95
