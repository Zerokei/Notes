---
date-created: 2022-08-16 14:11
date-updated: 2022-08-18 10:36
---

# The Art of the Readable Code

!!! info
	本篇笔记主要摘自《编写可读代码的艺术》（The Art of Readable Code）。有多年工程代码编程经验的作者，由浅入深地介绍了如何编写可读代码的技巧与原则，从代码风格到逻辑框架的构建，给出了不少实用的建议。




## 1 表面层次的改进

### 1.1 起名的艺术

💡建议一：避免空洞的词汇，比如：`get`, `size`...，可替换成 `height`, `fetch`, `load`...

| 单词    | 更多选择                          |
| ----- | ----------------------------- |
| send  | deliver, dispatch, distribute |
| find  | search, extract, locate       |
| start | create, begin, open           |
| make  | create, build, add            |

💡建议二：正确使用特殊词汇。

比如索引和迭代器：`i`，`j`，`it`...；或者临时变量 `tmp`... 在循环中，为使得不会错位使用迭代器，可以在迭代器中加入相关信息，如 `number_i`，`club_i`。

💡建议三：给名字附上额外的信息。

- 已转化为 UTF-8 **格式**的 html 字节：`html_utf8`
- 程序开始时间，以毫秒为**单位**：`start_ms`

💡建议四：不宜过长。

当然在变量中一味地存储信息也是不得当的，不然就可能会使它又臭又长，可以适当使用一些方法使其缩短。

1. 使用首字母缩略词：但仅仅应用于约定俗成的缩写，如 `evaluation` -> `eval`，`documentation` -> `doc`。书中提出了一个很直截了当的使用场景判断方法：让这些缩写对项目的**新成员**来说**不陌生和费解**。
2. 丢掉没用的词汇，如 `ConvertToString` -> `ToString`。

💡建议五：在小的作用域中使用较短的名字；相反，作用域大的词汇应尽可能长且详细。

💡建议六：避免歧义。

建议虽短，但其实很难做到完美。比如对于布尔值，`bool read_password = true`，就容易产生两种意思：1）要去读密码 2）已经读入密码，此时就可以通过 `need_password` 或 `user_is_authenticated` 替代。

### 1.2 排版

书中此块的内容是《审美》，但总体是和代码排版相关的，所以使用排版作为概括可能更为恰当。首先，书中提出了三条原则：

1. 使用一致的布局，让读者能快速适应
2. 当相似的代码尽可能相似
3. 把相关的代码分组，形成代码块

具体而言，为了让代码变得整齐，我们有如下可以参考的方法。

💡方法一：使用函数。

就如书中三条原则中的第二条，我们应当让相似功能的代码在外观上也尽可能相似。

```cpp
assert(ExpendFullName(database_connection, "Doug Adams", &error)
	  == "Mr. Douglas Adams");
assert(error == "");
assert(ExpendFullName(database_connection, "Jake Brown", &error)
	  == "Mr. Jocob Brown III");
assert(error == "");
assert(ExpendFullName(database_connection, "No Such Guy", &error) == "");
assert(error == "on match found");
assert(ExpendFullName(database_connection, "John", &error) == "");
assert(error == "more than one result");
```

上面的代码就不适用于这条规则，它的单条语句过长以致需要换行，同时我们发现它的功能是重复的。此时可以使用函数对其进行包裹与整理，就可以达到下面的状态：

```cpp
CheckFullName("Doug Adams", "Mr. Douglas Adams"  , "");
CheckFullName("Jake Brown", "Mr. Jocob Brown III", "");
CheckFullName("No such Guy", "", "no match found");
CheckFullName("John", "", "more than one result");
```

💡方法二：使用列对齐。

> 列的边提供了“可见的栏杆”，阅读起来很方便，这是个“让相似的代码看起来相似的好例子”。

对于方法一中用函数整理过的代码，其实看起来仍不是很直观，可能的原因就是无法一眼看出当前的字符串是第一个参数。此时就可以使用列对齐使其语义更加一目了然。

```cpp
CheckFullName("Doug Adams" , "Mr. Douglas Adams"  , "");
CheckFullName("Jake Brown" , "Mr. Jocob Brown III", "");
CheckFullName("No such Guy", ""                   , "no match found");
CheckFullName("John"       , ""                   , "more than one result");
```

💡方法三：固定顺序。

很多时候，对于一个类中的很多变量，无论是在声明还是在使用时，最好能保持一定的顺序（比如重要性，或者字符大小等等），并在后面一直沿用此顺序。

💡方法四：分段代码。

对代码进行分段有诸多好处，首先它将相似功能的代码放在一起，能帮助理解代码的逻辑，快速通读代码（特别是配合注释阅读时）。同时也可以帮助读者定位自己现在所阅读的位置。以下是一个例子：

```python
def suggest_new_friends(user, email_password):
	# Get the user's friends' email addresses.
	friends = user.friends();
	friends_emails = set(f.email for f in friends)

	# Import all email addresses from this user's email account.
	contacts = import_contacts(user.email, email_password)
	contact_emails = set(c.email for c in contacts)

	# Find matching users that they aren't already friends with.
	non_friend_emails = contact_emails - friend_emails
	suggested_friends = User.objects.select(email_in=non_friend_emails)

	# Display these lists on the page.
	display['user'] = user
	display['friends'] = friends
	display['suggested_friends'] = suggested_friends

	return render("sugguested_friends.html", display)
```

### 1.3 注释

首先我们需要知道在哪些情况下是不需要注释的：

1. 为了写注释而写注释，即没有提供更多信息的注释
2. 为解释晦涩的命名的注释。好代码>坏代码+好注释

在很多时候，我们可能对如何写注释仍无从下手，作者给出了一些经典的应用场景。

🏝 场景一：为代码中的瑕疵写注释。

| 标记     | 通常的意义              |
| ------ | ------------------ |
| TODO:  | 还没有处理的事情           |
| FIXME: | 已知的无法运行的代码         |
| HACK:  | 对一个问题不得不采用的比较粗糙的方法 |

```C
// TODO: add connect function
```

🏝 场景二：为常量加注释。

一般来说，每个常量都有一个设置为该值的缘由。

```C
// Impose a reasonable limit - no human can read that much anyway
const int MAX_RSS_SUBSCRIPTION = 1000;
```

🏝 场景三：可能引起歧义的地方。

🏝 场景四：可能存在问题的地方。

🏝 场景五：总结性的注释。

对于一些代码块，在前面加上注释可以方法读者在阅读代码细节前有一个总体的印象。就如排版的第四个方法的例子中的应用那样，和代码分块配合使用，会有1+1>2的效果。

## 2 简化循环逻辑

### 2.1 优化控制流

✅ 建议一：调整判断条件的左右顺序

对于以下两条指令，相信你会更喜欢前者而不是后者，这可能与我们的思维习惯有关系。在编写代码时，请尽量将常量放在右边，而会变化的，被用于检查、比较的值放在左边。

```cpp
// 变量在左，常量在右
if (length >= 10) {
	// do something
}
// 常量在左，变量在右
if (10 <= length) {
	// do something
}
```

✅ 建议二：调整条件语句的前后顺序

- 一般情况下，我们可能喜欢**正**逻辑大于**负**逻辑。
	```cpp
	// 正逻辑
	if (a == b) {
		// do somehting
	} 
	else {
		// do something
	}
	// 负逻辑
	if (a != b) {
		// do something
	}
	else {
		// do something
	}
	```
- 先处理**简单**的逻辑，再处理**复杂**的逻辑
	当然，很多情况下，逻辑的复杂与否和前面的正负逻辑会发生冲突，这时就需要进行取舍和考量了。以下就是为先处理重要的逻辑而同时“违背”简单逻辑原则和正逻辑原则的经典例子：
	```python
	if not file:
		# Log the error ...
	else:
		# ...
	```

✅ 建议三：谨慎使用可能影响可读性的表达式。

- 三目运算符 `return exponent >=0 ? mantissa * (1 << exponent) : mantissa / (1 << -exponent);`
- do/while 循环
- goto

✅ 建议四：最小化条件语句嵌套。

很多情况下，在前人基础上进行功能添加时，就容易出现在语句中嵌套条件语句，例如下方时代码原有逻辑。

```cpp
if (user_result == SUCCESS) {
	reply.WriteErrors("");
} else {
	reply.WriteErrors(user_result);
}
```

后来增加逻辑后变为：

```cpp
if (user_result == SUCCESS) {
	if (permission_result != SUCCESS) {
		reply.WriteErrors("error reading permissions");
		return;
	}
	reply.WriteErrors("");
} else {
	reply.WriteErrors(user_result);
}
```

实际上，只要再略加思考，就能将上面不美观且难以理解的代码逻辑简化。

```cpp
if (user_result != SUCCESS) {
	reply.WriteErrors(user_result);
}
else if (permission_result != SUCCESS) {
	reply.WriteErrors("error reading permissions");
}
else {
	reply.WriteErrors("");
}
```

### 2.2 拆分长表达式

拆分长表达式的内容在 1.2 排版 中略有提及，表达式过长有两个缺点，一方面是不够美观，另一方面可读性也不够强。就如下方代码，判断条件的左边部分又是 `split` 又是 `strip` ，含义并不够清除明白。

```python
if line.split(':')[0].strip() == "root":
	# do something
elif line.split(':')[0].strip() == "user1":
	# do something
```

若将被判断的值赋给一个变量，就可以使得判断条件更加直观可读。

```python
username = line.split(':')[0].strip()
if  username == "root":
	# do something
elif username == "user1":
	# do something	
```

当然除了使用**变量**外，也可以使用**函数**/**宏定义**在合适的场景中达到拆分长表达式的目的。

### 2.3 合理设置变量

在上一章中，我们可能会为了增加代码可读性拆分长表达式而增设变量，但是在代码可读性不受影响的情况下，我们当尽可能地减少变量，并尽可能地使用常量。对于一个变量，缩小起作用域也可以避免制造过多的 bug。
比如下方代码，若 `now` 只在一个地方用到，则不如删去 `now` 以缩减不必要的变量，且这样的作法几乎不会影响可读性。

```python
now = datatime.datetime.now()
root_message.last_view_time = now
```

```python
root_message.last_view_time = datatime.datetime.now()
```

## 3 重新组织代码

> 该部分会讨论可以在函数级别对代码做更大的改动，具体来讲，我们会讲到三种组织代码的方法：
>
> 1. 抽取出那些与程序主要目的“不相关的子问题”。
> 2. 重新组织代码使他一次只做一件事情。
> 3. 先用自然语言描述代码，然后用这个描述来帮助你找到更整洁的解决方案。

✅ 建议一：分离代码。

简而言之，即把“一般代码和项目专有的代码分开”。

✅ 建议二：一次只做一件事。

将所有要做的任务分出来，并这些任务变成单独的函数抑或代码中的一个段落。

✅ 建议三：将想法变成代码。

✅ 建议四：少些代码。

在遇到问题时，第一反应不当是自己去写一个功能去解决需求。若能诉诸现有的库或者系统工具解决，使用这些成熟的工具可能要比从头开始设计可靠的多。
