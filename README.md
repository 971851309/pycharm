# pycharm

## 1. 项目概述

本仓库为 Python 练习与爬虫实验集合。已阅读源码的示例包括：使用 `requests` 与 `lxml` 解析百度搜索结果标题与链接的 `hello,world.py`，以及通过自封装 `DelayRequests` 按主机名限速访问的 `识别网站技术.py`。目录中还包含 `subline代码`/`BOOK` 等第三方书籍配套源码、本地虚拟环境 `venv` 及若干独立脚本，用于机器学习与可视化等主题的扩展学习。

## 2. 技术栈

### 前端

- 若存在 `line.html` 等静态页面，用于简单展示或实验（以具体文件为准）

### 后端

- Python 3（仓库内 `venv` 为 Python 3.7 线索）
- HTTP 客户端：`requests`
- HTML 解析：`lxml.etree`、XPath

### 数据库

无（已读示例未涉及）。

### 开发工具与运维

- PyCharm / VS Code 等本地 IDE
- 虚拟环境：`venv/`（依赖包体积大，README 目录树中不展开）

## 3. 项目架构

各脚本**相互独立**，无统一 Web 框架：

- **爬虫实验**：`hello,world.py` 中 `get_html(url)` 拉取页面，`etree.HTML` 后 `xpath` 抽取 `content_left` 下结果块；`main` 中拼接百度搜索 URL。
- **访问节奏控制**：`识别网站技术.py` 中 `DelayRequests` 用 `urllib.parse` 取 `netloc`，按域名记录上次访问时间，`time.sleep` 实现间隔。

数据流：URL → HTTP 响应 → 字节/文本 → DOM 解析或状态码打印。

## 4. 目录结构

```
pycharm/
├── README.md
├── hello,world.py           # 百度搜索结果解析示例（requests + lxml）
├── 识别网站技术.py          # 按域名限速的请求示例
├── 代码库2.0.py 等          # 其他独立脚本（需逐个打开确认用途）
├── subline代码/             # 子目录内可能含 BOOK、notebook 等学习资源
├── BOOK/                    # 若存在：深度学习等参考书配套代码
├── line.html 等            # 静态或实验用页面
└── venv/                    # 本地虚拟环境（.gitignore 建议忽略；不在此展开）
```

## 5. 核心文件说明

### 项目入口文件和配置文件

- `hello,world.py`：入口在 `if __name__ == '__main__': main()`，默认请求写死的百度搜索 URL。
- `识别网站技术.py`：脚本末尾直接实例化 `DelayRequests` 并循环请求 CSDN 主页，无 `main` 函数封装。

### 核心业务逻辑实现

- `get_html(url)`：状态码 200 时用 XPath 取标题与链接；分支中混用 `for/else`（属 Python 语法特性，逻辑上以源码为准）。
- `DelayRequests.wait(url)`：计算与上次同站请求的时间差并可能 `sleep`。

### 数据模型和 API 接口

- 无后端 API；对外依赖为第三方网站 HTTP 接口（百度、CSDN 等）。

### 关键组件和服务模块

- **解析组件**：`lxml.etree` + XPath 表达式（见文件内注释中的路径片段）。
- **节奏控制组件**：`DelayRequests` 类维护 `urls` 字典。

阅读其他 `.py` 文件时请直接打开源码核对功能，避免仅凭文件名推断。
