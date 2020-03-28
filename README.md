# ICTFE
Intergrated CTF Environment

集成式CTF解题环境

采用PyQt5编写, 2020年03月25日开工, 欢迎fork, 开发相关功能并pull到本仓库.

## 如何参与

fork本仓库, 使用PyQt5进行开发, 然后发起一个Pull Request.

如果你用有丰富的UI开发经验, 可以帮开发者优化一下界面和逻辑代码并做好模块化, 感激不尽~

## 如何使用

clone本仓库到本地, 安装PyQt5

```python
pip install PyQt5
```

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

### Base系列
Base64 Base32 Base16 Base85

支持任意字符的换表操作, 支持对Python格式的bytes进行编码与解码. 支持Base64隐写提取.

支持文件操作

### Quoted-Printable
支持文件和字符串的编码和解码.

### Url编码
支持自定义字符集的Url编码解码.

### Hex编码
支持Hex编码(UTF-8)

### HTML编码
支持HTML编码

### Escape
支持JavaScript的Escape编码

## Pwn

无

## 杂项

无

# 当前完成状态预览

![图片.png](https://i.loli.net/2020/03/28/PiozhculbHMSUEB.png)
