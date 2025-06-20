# BUCT校园网自动认证
用selenium实现的，主要放在树莓派上。
使用systemd管理自启动。

用crontab理论上也行。

---

## 关于登录账号

在程序的根目录下面新建`.env`文件，里面写
```ini
BUCT_AUTHENTICATION_USERNAME=你的学号
BUCT_AUTHENTICATION_PASSWORD=校园网密码
```

---

## 关于service

由于用到了logging。所以service里面要加上`WorkingDirectory=/path/to/programe`来确保文件可以正常写入 。
出错先找找权限问题，我应该是直接给了755。这里是一个servivce的配置文件例子。
```YAML
[Unit]
  Description=Auto authentication.
  After=network-online.target

[Service]
  Type=simple
  ExecStart=/path/to/your/python /path/to/your/program
  WorkingDirectory=/path/to/your/program
  User=Your_User
  Restart=always
  RestartSec=60

[Install]
  WantedBy=multi-user.target
```

---

~~现在还是有点问题。比如说没有连接wifi的情况下，request的get会报ssl error然后直接退出。except也不好用。~~
虽然我不知道为什么，但是最后还是改成用selenium检测登陆界面元素来做这事。虽然是反璞归真了，但是管他呢它跑得起来就行了。
我的解决方法就是service里面`Restart=always`,`RestartSec=60`。实测下来是能正常认证的。

用request来检测纯属闲的，本来还是拿selenium检测的。反正能跑管他呢。
