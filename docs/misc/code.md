---
date-created: 2022-08-16 14:11
date-updated: 2022-08-16 20:23
---

# The Art of the Readable Code

## 一、表面层次的改进

### 1. 起名的艺术

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

### 2. 排版

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

### 3. 注释

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

## 二、简化循环逻辑

## 三、重新组织代码
