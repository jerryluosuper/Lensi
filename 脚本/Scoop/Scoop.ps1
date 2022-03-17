mkdir D:\Scoop_all
mkdir D:\Scoop_all\Scoop
mkdir D:\Scoop_all\GlobalScoopApps
mkdir D:\Scoop_all\ScoopCache

Set-ExecutionPolicy RemoteSigned -scope CurrentUser;

$env:SCOOP='D:\APP\Scoop'
[Environment]::SetEnvironmentVariable('SCOOP', $env:SCOOP, 'User')

$env:SCOOP_GLOBAL='D:\Scoop_all\GlobalScoopApps'
[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')

$env:SCOOP_CACHE='D:\Scoop_all\ScoopCache'
[Environment]::SetEnvironmentVariable('SCOOP_CACHE', $env:SCOOP_CACHE, 'Machine')

iwr -useb https://gitee.com/glsnames/scoop-installer/raw/master/bin/install.ps1 | iex

scoop config SCOOP_REPO 'https://gitee.com/glsnames/Scoop-Core'
scoop update
scoop config SCOOP_REPO 'https://gitee.com/squallliu/scoop'

scoop install aria2 git sudo

scoop config aria2-split 32
scoop config aria2-max-connection-per-server 64

scoop bucket add main 'https://gitclone.com/github.com/ScoopInstaller/Main.git' 
scoop bucket add extras 'https://gitee.com/xumuyao/scoop-extras.git'
scoop bucket add nonportable 'https://gitee.com/lane_swh/scoop-nonportable.git'
scoop bucket add games ‘https://gitee.com/helloCodeke/scoop-games.git’
scoop bucket add java 'https://gitee.com/xumuyao/scoop-java.git'
scoop bucket add versions 'https://gitee.com/lane_swh/scoop-versions.git'
scoop bucket add scoopcn "https://gitclone.com/github.com/scoopcn/scoopcn.git"
scoop bucket add apps 'https://gitee.com/kkzzhizhou/scoop-apps'
scoop bucket add nerd-fonts 'https://gitee.com/helloCodeke/scoop-nerd-fonts.git'
scoop bucket add scoopMain 'https://gitee.com/glsnames/scoop-main.git'
scoop update

sudo scoop install quicklook snipaste typora listary portable-virtualbox 7zip windows-terminal potplayer motrix picgo
sudo scoop install baidudisk tim wechat we-meet trafficmonitor deepl pandoc screentogif geekuninstaller fluent-reader rufus blender 
sudo scoop install gcc g++ vim curl wget mobaxterm python oraclejdk17 openssh coreutils grep sed less concfg pshazz vscode android-studio anaconda3

sudo scoop install docker docker-compose docker-machine
docker-machine create default
docker-machine start
docker-machine env
& "$HOME\AppData\Local\scoop\apps\docker-machine\0.7.0\docker-machine.exe" env | Invoke-Expression
docker run ubuntu /bin/echo 'Hello world'
docker-machine stop

scoop install vim
'
set ff=unix
set cindent
set tabstop=4
set shiftwidth=4
set expandtab
set backupdir=$TEMP
' | out-file ~/.vimrc -enc oem -append

aria2c "https://down5.huorong.cn/sysdiag-all-5.0.65.2-2022.1.17.1.exe"
./sysdiag-all-5.0.65.2-2022.1.17.1.exe
aria2c "https://hub.fastgit.org/sandboxie-plus/Sandboxie/releases/download/1.0.7/Sandboxie-Plus-x64-v1.0.7.exe"
./Sandboxie-Plus-x64-v1.0.7.exe
aria2c "https://hub.fastgit.org/t1m0thyj/WinDynamicDesktop/releases/download/v4.7.0/WinDynamicDesktop_4.7.0_Setup.exe"
./WinDynamicDesktop_4.7.0_Setup.exe
aria2c "https://www.dogfight360.com/blog/wp-content/uploads/2021/12/steamcommunity_302_V12.0.3_%E8%A7%A3%E5%8E%8B%E5%AF%86%E7%A0%81dogfight360.zip"