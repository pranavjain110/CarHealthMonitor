import pandas as pd
import smtplib

debug = False


def send_email(from_addr, to_addr_list, cc_addr_list,
               subject, message,
               login, password,
               smtpserver='smtp.gmail.com:587'):
    """
    a function which will be used to send email to the specified email address
    with the specified subject and body.

    Parameters
    ----------
    from_addr : string
        contains the from email address
    to_addr_list : list of string
        contains a list of the to email adresses
    cc_addr_list : list of string
        contains a list of the cc email adresses
    subject : string
        contains the subject of the email
    message : string
        contains the body of the email
    login : string
        contains the login email address
    password : string
        contains the app password for the specified email
    smtpserver : string
        contains the smtpserver

    Returns
    -------
    string
        problems: error if there was a problem publishing the email

    """

    header = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems


def checkcond(f, thres1, thres2, thres3, thres4, email):
    """
    checks if data exceeds set thresholds and notifies by email if necessary

    Parameters
    ----------
    f : bool
        bool value indicating if failure or maintainance has occured
    thres1 : float
        threshold value for engine temperature
    thres2 : float
        threshold value for tire pressure
    thres3 : float
        threshold value for tire max distance
    thres4 : float
        threshold value for oil replacement
    email : string
        email which has to be notified

    Returns
    -------
    bool
        flag indicating If maintainance or failure has occuered

    """
    data = pd.read_csv('SensorData.csv')
    data.columns = ['DataStream1', 'DataStream2']
    data = data.tail(10)

    data2 = pd.read_csv('TimeElapsed.CSV', names= ['DataStream3', 'DataStream4'])



    # using flag based calling to ensure the alert is given only once unless it is reset
    flag = f
    message = ""

    # (for debuging) temperory print line meant for debuging
    # print(data['DataStream1'].mean(), data['DataStream2'].mean())

    # checking the mean of the last 10 values to avoid triggers by noise
    if data['DataStream1'].mean() > thres1:
        message = message + "Engine Temperature is high, please carry out maintainance \n"
        flag = True

    if data['DataStream2'].mean() < thres2:
        message = message + "Tire pressure is low, please carry out maintainance \n"
        flag = True

    if data2['DataStream3'].mean() > thres3:
        message = message + "Engine oil need to be replaced, please carry out maintainance \n"
        flag = True

    if data2['DataStream4'].mean() > thres4:
        message = message + "Tire have worn out, please carry out maintainance \n"
        flag = True

    if flag:

        print(message)
        # the below section will be in the final code
        send_email(from_addr='rain.cloud.bot@gmail.com',
                   to_addr_list=[email],
                   cc_addr_list=[],
                   subject='maintainance update',
                   message=message,
                   login='rain.cloud.bot@gmail.com',
                   password='jxixsnxxuukmszul')
        print('EMAIL SENT')
    return flag


if debug:
    # example of the fucntion call which will be implemented in the update loop
    # the threshold can be a bollean value indicating faliure or a limit val
    # outside loop
    f = False
    # inside loop
    for i in range(10):
        if not f:
            f = checkcond(f, 60,15,20,12,"abc")

    input("Press Enter to exit .")
    exit()
