import win32com.client as win32

def emailer(text, subject, recipient, display=True):
    
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient
    
    mail.Subject = subject
    mail.HTMLBody = text
    

    
    if display:
        mail.Display(True)
    else:
        mail.send()


if __name__ == "__main__":    
    msg = "<h1>HELLO WORLD</h1><img src=D:\\BuyProg\\new\\tropical_pics\\Ginger_Med_Pink.jpg></img>"
    subject = "hello2"
    recipient = "antoinewood@gmail.com"
    emailer(msg, subject, recipient)
