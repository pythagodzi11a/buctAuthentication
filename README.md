# BUCT校园网自动认证
用selenium实现的，主要放在树莓派上。
使用systemd管理自启动。

用crontab理论上也行。

由于用到了logging。所以service里面要加上`WorkingDirectory=/path/to/programe`。出错先找找权限问题。

---

现在还是有点问题。比如说没有连接wifi的情况下，request的get会报ssl error然后直接退出。except也不好用。
我的解决方法就是service里面`Restart=always`,`RestartSec=60`。实测下来是能正常认证的。

用request来检测纯属闲的，本来还是拿selenium检测的。反正能跑管他呢。