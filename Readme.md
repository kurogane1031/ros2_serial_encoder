# Document Title

## dependencies
1. ```pip3 install pyserial```


### 使い方

1. Open new terminal.

2. ```source /opt/ros/dashing/setup.bash```

3. ```cd develop/dev_ws```

4. ```source install/setup.bash```

5. ```sudo chmod 777 /dev/ttyUSB0```

6. ```ros2 run py_encoder_right talker```

7. Wait 2-3 seconds for `publishing: m/s <numbers> km/h <numbers>`.

### 注意

1. DO NOT DO `pyenv activate roswork`

2. If `NameError: name 'ser' is not define` error appear, means you forgot 使い方 Step 5

3. Error message will appear if you did not wait during 使い方 Step 7

### Arduino connection

| Encoder cable color |  Arduino pins |
|:-------------------:|:-------------:|
|        Black        |       2       |
|        White        |       3       |
|        Brown        |       5V      |
|         Blue        |      GND      |
|        Orange       | not connected |
