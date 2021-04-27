# vimllearn-book

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
