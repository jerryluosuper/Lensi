# Lensi
## 说明
### 主程序说明
+ Lensi GUI为360 qq scoop choco winget hippo的聚合搜索软件。
+ Lensi CLI为360 qq hippo的聚合搜索命令行工具。
+ CLI安装 `pip install Lensi`
+ 打包后的exe大小超过100MB，在github发行（gitee：https://gitee.com/lensit/lensi）。
+ ![GUL](media/media%20(2).png)
### 源代码说明
+ Lensi_init.py为初始化安装scoop和choco的脚本。
+ Lensi_search.py 为360 qq scoop choco winget 的聚合搜索。
+ Lensi_search写了一点点注释，可以阅读学习。
+ Lensi_all.py为所有函数。
+ Lensi_GUI.py为GUI模板。
+ Lensi_main.py为主程序，需要有Lensi_GUI和Lensi_all放在一个目录下就可以运行。
+ Lensi_CLI.py为命令行工具。
### BUG说明
+ Winget 有时候搜索会失败
+ Choco 安装有可能失败（搜索没问题）
+ qq detail 有时会显示失败
+ 如果搜索结果小于5个，则上一次搜索不会替换
