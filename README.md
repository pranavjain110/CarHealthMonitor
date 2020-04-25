# MECH 550C Project : Car Health Monitoring System

---
Authors: Ajay, Chinmay, Pranav, Sameer

Date: 17 April, 2020

Version: 1.0

---

## File Structure

```
CarHealthMonitor
|
├── .gitignore
├── Source
|   ├── README.md
|   ├── LICENSE
|   ├── CarHealthMonitor.py
|   ├── GUI_1
|   │   |── SimulatorGUI.py
|   │   ├── sender.py
|   │   ├── carsensors.ico
|   │   ├── decrease.png
|   │   ├── increase.png
|   ├── GUI_2
|   │   ├── 
|   │   ├── alertloop.py
|   │   ├── alertsys.py
|   │   ├── MonitorGUI.py
|   │   ├── plotting_function.py
|   │   ├── receiver.py
|   │   └── graph.ico
```
## Description

- Car Health Monitor is an application which is used to monitor different parameters
of the car and notify the user about the part that has high probability of failure 
in coming future.
- Car Health Monitor is used to monitor the parameters Engine Oil and Tire Health with 
the help of the sensor data. 
- The sensor data is sent to a CSV file through Advanced Message queuing Protocol.
- The data is read from the CSV file and is used for plotting failure curves for both
parameters. 
- On plotting the graph if the probability of failure I above certain value the user gets
notified by an email
- The email will notify what parameter of the car needs to be changed and must be serviced.
This will help the customer to predict the failure of the part and assist the user to 
avoid break down of the car due to sudden failure.


## Execution
- Install [RabbitMQ](https://www.rabbitmq.com/download.html)
- Install [Erlang](https://www.erlang.org/downloads)
- In Command Prompt run the following command:  
``` python -m pip install pika --upgrade```
- Run CarHealthMonitor.exe to run the application


### Commands used to convert .py files to .exe:
```
pip install auto-py-to-exe
auto-py-to-exe

pip install pyinstaller
pyinstaller filename.py --onefile
```

## Dependencies
- AMQP
    - rabbitmq-server == 3.8.2
    - Erlang/OTP == 22.2
- Python version 3.8.1
    - Python packages:
        - pandas == 1.0.1
        - numpy == 1.18.1
        - matplotlib == 3.2.1
        - json == 2.0.9
        - tkinter == 8.6
        - pika == 1.1.0
        - Python Standard Libraries
    - Python Standard Libraries
        - inspect — Inspect live objects
        - os — Miscellaneous operating system interfaces
        - time — Time access and conversions
        - smtplib — SMTP protocol client
        - csv — CSV File Reading and Writing
- pyInstaller is used to convert the following code into .exe file
- OS: Windows 10 64-bit

## IDE

- Visual Studio Code
