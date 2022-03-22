# Lensi
## 说明
### 主程序说明
+ Lensi为360 qq scoop choco winget hippo的聚合搜索软件。
+ 由于打包后的exe大小超过100MB，暂时不发行。
+ ![主程序](media/media%20(2).png)
+ ![搜索示例](media/media%20(3).png)
### 源代码说明
+ Lensi_init.py为初始化安装scoop和choco的脚本。
+ Lensi_search.py 为360 qq scoop choco winget 的聚合搜索。
+ Lensi_search写了一点点注释，可以阅读学习。
+ Lensi_all.py为所有函数。
+ Lensi_GUL.py为GUL格式。
+ Lensi_main.py为主程序，需要有Lensi_GUL和Lensi_all放在一个目录下就可以运行。
### BUG说明
+ Winget 有时候搜索会失败
+ Choco 安装有可能失败（搜索没问题）
+ qq detail 有时会显示失败
+ 如果搜索结果小于5个，则上一次搜索不会替换
### TODO
+ Detail&Info界面未完成
+ BUG修理
+ aira2代理









