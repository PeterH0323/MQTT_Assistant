# MQTT_Assistant

This is a MQTT Assistant for sending or receiving message from EMQ.

# Code Version

Python 3.5 + PyQt5


# Python packet

1. paho-mqtt: 
    ```
    pip install paho-mqtt
    ```

2. PyQt5: 
    ```
    PyQt5: pip install pyqt5
    ```

3. PyQt5-tools: 
    ```
    pip install pyqt5-tools
    ```
   
4. pyperclip
    ```
    pip install pyperclip
    ```

5. requests
    ```
    pip install requests
    ```


# Tool

You can use `Interface/tool.py` to transform `.ui` to `.py`

# How to use

Use **JT_EMQ_Test_Assistant_Simple.py** to run the programme.

- ScreenShot

<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="./Doc/Software.png">
</center>

### Top of the window:

<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="./Doc/top.jpg">
</center>

When you click the `Connect to EMQ` button the setting of `EMQ Setting` will be saved automatically.

### Left side:

<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="./Doc/Letf_side.jpg">
</center>

When you want to **focus** on one line in `Text Edit` on the left of the window, just click it , it will stop sliding down , then click the button name `Final line` , it will keep showing the latest data.

The software save log to a txt file name `collect.txt` under floder name `Data` by default , if you **DO NOT** want to save it , just unclick the `Save log` check box in the lower left corner of the window.

### Right side:

<center>
    <img style="border-radius: 0.3125em;
    box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" 
    src="./Doc/Right_side.jpg">
</center>


You can send custom message (for example `Hey mate.`) by click the `Send` button (shortcut: `Alt + Q`) **after** you connect EMQ.

You can `add` command in the table by click the nice <img src="/images/add.png" width="3%" height="3%"> button(shortcut: `ctrl + A`) or `delete` by the <img src="/images/Del.png" width="3%" height="3%"> button (shortcut: `ctrl + D`) .

**REMEMBER** : After you edited the table you need to click the button <img src="/images/Save.png" width="3%" height="3%"> to save (shortcut: `ctrl + S`)!

You also can just **Right Click** in the table will show `Delete` .

The **Right click menu** `Send` and button `Single send` do the same job -> send the command you just selected in the table .

If you want to send the command cyclically , you can just click the **checkBox** `Activate` , the software will send command which is activated in column of the table name `Activate` then delay for a while according to command row `Delay_ms` .

Number of times the instruction is sent cyclically according to the **spinBox** name `Times` beside the checkBox name `Activate`. You also can choose infinite loop .

**Progress bar** shows the percentage of completion sent . For example , you activate 10 command in the table , when the software sent 7 commands , the progress bar show `70%`. 