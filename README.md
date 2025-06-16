# Fan Control Service
This is a fan-control service for raspberry pi. See my [blog post](https://itsrad.io/blog/2025/raspberryos_fan_control/) for instructions on building the associated circuit.

# Installation
1. Clone the repo
```bash
git clone https://github.com/its-radio/fan-control.git
```

2. Place the script
- You can place tne script anywhere you like.
```
cd fan-control
cp fan-control.py /path/to/script/location/
```

3. Update the path in the service
- The path in the service must match the path at which you place the script
```bash
vim fan-control.service
```
- Change the indicated line
```ini
[Unit]
Description=Raspberry Pi Fan Controller
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /CHANGE/THIS/PATH/fan-control.py
Restart=always

[Install]
WantedBy=multi-user.target

```

4. Place the service
```bash
cp fan-control.service /etc/systemd/system/
```

5. Enable and start the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable fan-control
sudo systemctl start fan-control
```

