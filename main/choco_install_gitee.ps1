mkdir D:\Choco_all
$env:ChocolateyInstall='D:\Choco_all'
[Environment]::SetEnvironmentVariable('ChocolateyInstall', $env:ChocolateyInstall, 'User')
git clone 'https://gitee.com/mirrors/chocolatey.git'
cd .\chocolatey\ 
sudo ./setup.ps1