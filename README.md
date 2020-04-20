# ICTFE
Intergrated CTF Environment

集成式CTF解题环境

采用PyQt5编写, 2020年03月25日开工, 欢迎fork, 开发相关功能并pull到本仓库.

## 如何参与

fork本仓库, 使用PyQt5进行开发, 然后发起一个Pull Request.

如果你没有学习过PyQt5, 可以简单的查看[QuickDevelopingDocs](QuickDevelopingDocs/0_ICTFE密码学插件开发指北.md)中的文档, 然后尝试进行开发.

如果你用有丰富的UI开发经验, 可以帮开发者优化一下界面和逻辑代码并做好模块化, 感激不尽~

### 已知开发问题

在测试之后请不要push Resources文件夹下的DIY.sqlite数据库, 或者将此数据库删掉后再push

软件使用时不存在问题, 但是使用Pycharm提交之后数据库里面会被以文本形式插入一些奇奇怪怪的东西,
暂不清楚这些语句是怎么插入进去的, 这些文本会破坏数据库的完整性, 从而造成软件无法打开.
删掉之后软件启动时会自动创建一个空的.

## 如何使用

clone本仓库到本地, 安装PyQt5

```
pip install PyQt5 PyQt5-sip PyQtWebEngine -i https://pypi.tuna.tsinghua.edu.cn/simple

# 如果需要在Windows上进行打包，则需要安装 pyinstaller

pip install gmpy2 pycrypto python-poppler-qt5 qtpy networkx

# 这里请注意, gmpy2在Windows平台上可能不会正常工作.
# 请Windows平台的用户前往 https://www.lfd.uci.edu/~gohlke/pythonlibs/
# 下载对应版本的gmpy2并本地安装.
# 待软件开发完成后将进行不依赖于开发环境的打包工作, 敬请期待.

```

请不要使用Windows应用商店提供的python环境， 那个存在问题。

运行

```
./Run.py
```

后续随着工具集成会加入所需要的Python模块说明.

# 目前进度:

## 小工具

添加暂存池, 方便在不同分类之间传递数据.

## 逆向工程

无

## Web

无

## 密码与编码

### 密码学重构完成, 请参照Modules文件夹下的实例编写模块, 文档稍后上线.

### Base系列
Base64 Base32 Base16 Base85-ASCII Base85-RFC1924

支持任意字符的换表操作, 支持对Python格式的bytes进行编码与解码. 支持Base64隐写提取.

~~支持文件操作. 添加了明文和密文的快速交换键, 用于反base套娃 (误~~

~~### Quoted-Printable~~
~~支持文件和字符串的编码和解码.~~

### Url编码
支持自定义字符集的Url编码解码.

~~### Hex编码~~
~~支持Hex编码(UTF-8)~~

~~### HTML编码~~
~~支持HTML编码~~

~~### Escape~~
~~支持JavaScript的Escape编码~~

~~### 敲击码~~
~~Tap Code, 简单的编码解码支持.~~

~~### 摩斯电码~~
~~Morse Code, 提供基础的编码解码支持, 支持自定义分隔符.~~

### Hash计算
~~支持计算大文件哈希值,~~支持计算几乎所有哈希类型, 如md5, sha512等等.
支持计算普通文本和bytes类型数组的哈希值.
支持计算时加入指定长度的随机盐.

~~### 凯撒密码~~
~~Caesar Cipher, 提供无限位移功能~~

~~### 栅栏密码~~
~~Rail-Fence Cipher, 提供不限大小的分组功能~~

~~### ROT系列~~
~~ROT13和ROT47加密解密支持~~

~~### 笔画密码~~
~~Strokes Cipher, 提供约2w字左右的汉字笔画密码查询~~

## Pwn

无

## 杂项

无

## 启动器

支持创建 最多 120 个自定义分区, 每个分区支持最多54个链接按钮. 采用SQLite进行自动存储.
支持快速添加和删除按钮, 支持拖放文件, 并支持一次性拖入多个不同种类的文件.

所设定的文件将尝试执行, 若不可执行则调用命令使用相关软件打开当前文件.

## CyberChef

即**数据神厨**分区. 至于为什么要把CyberChef翻译成数据神厨, 这个问题就不必纠结了... 因为实在想不到什么好翻译了

如果直接写CyberChef的话好像会超出按钮的长度所以就翻译成中文了 (逃

本分区集成了CyberChef的所有功能, 支持文件输入输出, 尽力与官方版本保持同步.

## CTF Wiki

集成了完整的离线CTF Wiki. 将来本wiki将会和官方wiki同步更改.

## Kiwix

集成了Kiwix阅读器, 支持阅读zim格式的百科数据文件.

## 浏览器

集成了一个具有基本浏览功能的浏览器. 支持Flash插件的使用.
Windows上的H5不包含h.264的解码器, 无法进行H5播放. Linux上一切正常.

# 当前完成状态预览
![image.png](https://i.loli.net/2020/04/20/DYJ2dFvqcCpnj74.png)
![image.png](https://i.loli.net/2020/04/20/8JRqxuGfwtIvsOH.png)
![image.png](https://i.loli.net/2020/04/20/kTM4l5AC6JYasDQ.png)
![image.png](https://i.loli.net/2020/04/20/6gGrTaN9ZiPzu3K.png)
![image.png](https://i.loli.net/2020/04/20/f3RyghxNBS9TWmF.png)
![image.png](https://i.loli.net/2020/04/20/YXHvW4NSdFCsVBD.png)
![image.png](https://i.loli.net/2020/04/20/iw4vIoV5WdZg1Qb.png)

