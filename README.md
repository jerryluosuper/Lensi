# Lensi_all
## 说明
### 主程序说明
+ Lensi GUI为360 qq scoop choco winget hippo的聚合搜索软件。
+ Lensi CLI为360 qq hippo的聚合搜索命令行工具。
+ CLI安装 `pip install Lensi`  https://github.com/jerryluosuper/lensi_cli
+ 打包后的exe大小超过100MB，在github发行（gitee：https://gitee.com/lensit/lensi ）。
+ ![GUI](media/media%20(2).png)
+ 更多CLI版的说明和使用方法在后面
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
# Lensi_CLI
## 简介
+ Lensi安装`pip install lensi`
+ Lensi CLI为360 qq scoop choco winget hippo的聚合命令行工具。
+ Lensi 现更新到0.1.3 （更新内容： Aria2代理下载,批量下载，Scoop json代理替换）
+ 这有可能是Lensi_CLI的最后一个版本了 /(ㄒoㄒ)/~~
+ PS. 本人即将面临中考，暂时没有长期维护打算
## 软件特色
+ 聚合搜索：解决在Scoop，Choco，Winget中的选择困难症
+ Scoop 增强：自动解析buckets，加快搜索速度；github等网站自动替换为镜像站，加快下载速度
+ 360，QQ 软件源：官方软件，安全有保障；摆脱下载XX卫士的烦恼
+ 卸载软件：支持所有软件，不仅仅是由lensi安装的，并支持清除文件夹
+ 更新软件：一键更新所有由lensi下载的软件
+ 批量安装：创建一个txt,其中为如下格式,即可批量安装（lensi list out可以导出app_list）：
  ```
  <app_name1> <app_source1>
  <app_name2> <app_source2>
  ...         ...
  ```
## P.S.
+ 若您想为lensi添加更多的源，请注意最好需要如下函数：
  ``` python
  def xx_search(app_name,lmmit_num,...):
      return search_list[list1,list2]
  	# list格式：app_name_real(软件真实名称）,app_version,app_detail,app_homepage（软件官网）,app_id(没有则为app_name_real)，app_icon,fuzz.partial_ratio(app_name,app_name_real),app_source
  def xx_info(app_name):
      return info_text
  ```
## 使用方法
### 主要命令: 
+ (简介) [具体参数(可选参数) (备注)
+ clean：(清除Download缓存) 
  `lensi clean`
+ download：(只下载文件，并打开文件夹) 
  `lensi download <app_name> (<app_source>)`
+ info：(显示软件的详细信息) 
  `lensi info <app_name> (<app_source>)`
+ init：(消除整个lensi文件夹) 
  `lensi init`
+ install：(正常安装软件) 
  `lensi install <app_name> (<app_source>)`
+ list：(显示由lensi安装的软件) 
  `lensi list (<list_options>)`
  (lensi list out将在当前目录下生成安装软件列表，lensi install app_list.txt即可以批量安装)
+ search：(搜索功能，聚合搜索) 
  `lensi search <app_name> (<app_source> <limmit_num>)`
+ set：(一些设置) 
  `lensi set <set_options>` (具体设置看下文，lensi set显示所有设置)
+ uninstall：(卸载软件(软件范围是电脑中的所有软件)) 
  `lensi uninstall <app_name>`
+ upgrade：(更新软件(只限通过lensi下载安装的软件)) 
  `lensi upgrade (<app_name>)` (其中lensi upgrade代表更新所有）
+ 各个命令具体参数使用help可查看
### 设置（备注）：
+ `qq_num = 1`（qq搜索个数，默认1）
+ `360_num = 1`（360搜索个数，默认1）
+ `Scoop_num = 1`（Scoop搜索个数，默认1）
+ `Winget_num = 1`（Winet搜索个数，默认1）
+ `Choco_num = 1`（Choco搜索个数，默认1）
+ `DAI(DeletedAfterInstalled) = True`
下载安装包后自动删除，默认开启
+ `SO(SimplyOpen) = False`
安装包只是简单的打开，默认关闭，若开启则只是简单的打开下载的文件
+ `ES(EnableScoop) = True`
Scoop搜索是否开启，默认开启，运行时会检测是否装有Scoop，若没有则自动调为False
+ `EC(EnableChoco) = True`
Choco搜索是否开启，默认开启，运行时会检测是否装有Choco，若没有则自动调为False
+ `EW(EnableWinget) = True`
Winget搜索是否开启，默认开启（Choco，Winget开启可能会延长搜索时间）
+ `SIP(ScoopInstallPath) = D:\Scoop`
Scoop安装路径，默认在“ D:\Scoop”（lensi会自动解析Scoop\buckets文件夹，加快Scoop搜索速度）
+ `NI(NormalInstall) = qq`
lensi install <app_name>不加app_source的默认源，默认qq
The available source is : qq(q) 360(b) scoop(s) hippo(h) choco(c) winget(w)
+ `WT(Waittime) = 3`
搜索等待时间，默认3，若为0或负数则为等待所有源搜索完毕
+ `HAF(HowAccurateFuzzywuzzy) = 80`
更新，卸载所用检测是否存在这个软件的参数，默认80，可以调到80以上更加准确，但有可能查找不到
+ `EAD(EnableAria2Download) = False`
使用Aria2代理下载，默认关闭
+ `AP(Aria2Path) = D:\Scoop\shims\aira2c.exe`
Aria2安装地址，默认为由Scoop安装的地址
+ `CDS(CreateDesktopShotcut) = True`
  对于携带版的软件(下载文件后缀为.zip)是否创建桌面快捷方式，默认开启
+ `CSS(CreateStartmenuShotcut) = False`
  对于携带版的软件(下载文件后缀为.zip)是否创建开始菜单快捷方式(同时创建Lensi Apps文件夹)，默认关闭
+ `TR(ToReplace)=github.com`
+ `RT(ReplaceTo)=hub.fastgit.xyz`
  安装Scoop的软件自动讲其中的TR替换为RT，默认将github.com替换为hub.fastgit.xyz
