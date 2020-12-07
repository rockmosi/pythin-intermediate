# Useful information of Ubuntu

## ubuntu xrdp black screen
how to install: https://websiteforstudents.com/how-to-connect-via-remote-desktop-rdp-to-ubuntu-20-04-18-04/
after installation, sometimes shows black screen.
usually due to login on somewhere else!!
이미 어딘가 로그인 되어 있음!!
solotuion: 
 - who -a
 - kill process

## ubuntu xrdp authentication is required to create a color managed device
- ref: https://webhack.dynu.net/tip/20200227.001
- sudo vi /etc/polkit-1/localauthority/50-local.d/color.pkla
- after that paste it\
[Allow colord for all users]
Identity=unix-user:*\
Action=org.freedesktop.color-manager.create-device;org.freedesktop.color-manager.create-profile;org.freedesktop.color-manager.delete-device;org.freedesktop.color-manager.delete-profile;org.freedesktop.color-manager.modify-device;org.freedesktop.color-manager.modify-profile\
ResultAny=yes\
ResultInactive=yes\
ResultActive=yes\
