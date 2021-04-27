---
title: 简介
---
# VimL 语言编程指北路

[![Netlify Status](https://api.netlify.com/api/v1/badges/5ec08893-b40a-4a31-89bd-d9f3dd81e3d6/deploy-status)](https://app.netlify.com/sites/vimllearn-book/deploys)
![Vercel](https://therealsujitk-vercel-badge.vercel.app/?app=vimllearn-book)

这是使用 Hugo 对 [VimL 语言编程指北路](https://github.com/lymslive/vimllearn) 搭建的在线版本，版权归原作者所有。

在线阅读地址：

1. [https://vimllearn-book.vercel.app/](https://vimllearn-book.vercel.app/)
2. [https://vimllearn-book.netlify.app/](https://vimllearn-book.netlify.app/)

站点的文章内容使用 [Python 脚本](https://github.com/WingLim/vimllearn-book/blob/main/pyscript/main.py) 对原作者文章进行转换，进行了如下更改：

1. 使用 Google 翻译更改文件名，文件名为每个文章的英文标题
2. 文章头部添加元信息，以供 Hugo 渲染

基本目录，详细目录请查看左侧目录树

- [前言](/docs/foreword)
- 基础篇
  - 第一章 VimL 语言主要特点
  - 第二章 VimL 语言基本语法
  - 第三章 Vim 常用命令
- 中级篇
  - 第四章 VimL 数据结构进阶
  - 第五章 VimL 函数进阶
  - 第六章 VimL 内建函数使用
  - 第七章 VimL 面向对象编程
- 高级篇
  - 第八章 VimL 异步编程特性
  - 第九章 VimL 混合编程
  - 第十章 Vim 插件管理与开发
- [附录](/docs/appendix)

---

本教程期望按技术书籍方式讲叙。书名叫“指北”而不是“指南”，主要是考虑有很多指南类
书籍讲 vim 这编辑器工具的使用，而本书则侧重于 VimL 这种脚本语言编程。

全书正文分十章，约摸可再划分为基础篇、中级篇与高级篇三部分，现已完成初稿。后面
有可以计划再补上番外实战篇，写几章开发具体插件实例的实现思路。
然后将这个较为系统化的教程独立出来，可能进行后续的修改与调整。

本书引用的代码段示例都很短，按书照敲或复制也是一种学习方式。[ `example/`](https://github.com/lymslive/vimllearn/tree/master/example) 目录整
理了部分示例代码，但是建议以书内讲叙或外链接为准。作者自己在 linux 系统下以
vim8.1 版本测试，Windows 与低版本虽未全面测试，但相信 vim 本身的兼容性也基本适
用了。

欢迎反馈意见或文字纠错。

本书的 github 地址：
[https://github.com/lymslive/vimllearn](https://github.com/lymslive/vimllearn)
。允许按常规开源库一样 fork ，如有兴趣也可提 issue 讨论或 pr 。

版权声明：基于 MIT 开源协议。允许自由扩散，以及援用部分段落解说与示例代码。但
不允许将整书或整章节用于商业出版。笔者本人保留将来联系出版社以传统纸媒出版的权
利。