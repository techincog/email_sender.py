"""
@AppName: CtechF Email Sender
@Creater: admin@ctechf.com
@Date: 6/17/2019

✓Source Code Can be used free, for commercial and noncommercial use
✓You can make modifications to source and republish it.
✓Crediting isn’t required, but linking back is greatly appreciated and allows us to gain exposure.


Source Code by admin@ctechf.com from https://ctechf.com

For more details visit: https://ctechf.com/
Contact: admin@ctechf.com
"""


#import
import email, smtplib, os
from tkinter import *
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import filedialog
from tkinter import messagebox

#Global Variables
file_location = [] #Save Attachments Links
file_name = [] #Save Attachments Names
email_to = [] #Save Reciver Email Address

email_from = "" #Save Sender Email Address
password = "" #Save Sender Email Password (Plain Text)

#Start SMTP Connection
smOb = smtplib.SMTP('smtp.gmail.com', 587)
smOb.starttls()

#Get Login
def getLogin():
        while True:
                email_from = input("Enter Your Email Address and Press Enter (GMAIL ONLY): ")
                password = input("Enter Password and Press Enter : ")
                try:
                        smOb.login(email_from, password) #Logging to the Gmail
                        print("Successfully logged into your Gmail Account")
                        break
                except Exception as e:
                        print(e)
                        print("")
        


#Attach File
def dopen():
        dfile_location = (filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("All files","*.*"),("Text files","*.txt")))) #Open Dialog Box
        if (dfile_location != ''):
                if (dfile_location in file_location):
                        messagebox.showinfo("Already Attached!", "Files already attahed in this Email")
                else:
                        file_location.append(dfile_location) #Add Attachment location to the list
                        dfile_name = os.path.basename(dfile_location) #Get Attachment Name to the Variable
                        file_name.append(dfile_name) #Add Attachment Name to the List

                        lbl_attach = Label(row2, text=dfile_name + " - Successfully Attached", anchor='w')
                        lbl_attach.pack()
                
#Add Email to the list 
def addEmail():
   if (txtTo.get() != ''):
           demail = txtTo.get()
           if (demail in email_to):
                messagebox.showinfo("Email Added!", "Email Exists in the list")
           else:
                email_to.append(demail) #Email add to the list
                email_add_msg = demail + " - Email Added to List"
                lbl_attach = Label(row2, text=email_add_msg, anchor='w')
                lbl_attach.pack()
                enty_to.delete(0, END) #Clear To: Text


#Sent Email
def sentEmail():
        message = MIMEMultipart("alternative") #Create MIMEMultipart
        if (txtSub.get() != ''):
                message["Subject"] = txtSub.get() #Get Subject Text

                
        plain_body = ""  #Plain Email
        #html_body = ""  #HTML Email

         #Get Message Text
        if (txtBod.get() != ''):
                plain_body = txtBod.get() + """

         Sent By: CtechF Email Sender
        """
                
        
        message.attach(MIMEText(plain_body, 'plain'))
        #message.attach(MIMEText(html_body, 'html'))
                
        #Attachment
        count_attach = len(file_location) #Count Attachment
        for i in range(count_attach):
                email_attach = MIMEBase("application", "octet-stream") 
                attach_file = open(file_location[i], "rb") #Get Attachment File
                email_attach.set_payload(attach_file.read())
                encoders.encode_base64(email_attach) #Encode
                file_name_now = file_name[i]
                email_attach.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {file_name_now}",
                )
                message.attach(email_attach) #Attach File to the email
                

        try:
                #email_from = ":)ctechf:)@pm.me"
                #password = "5iVWiiaSPYtgEtp"
                email_message = message.as_string()
                for email in email_to:
                        smOb.sendmail(email_from, email, email_message) #Send Email
                        email_msg = "Email sent: "+email 
                        lbl_attach = Label(row2, text=email_msg, anchor='w')
                        lbl_attach.pack()
                del email_to[0:] #Clear Email List
                del file_location[0:] #Clear Attachment List
                del file_name[0:] #Clear Attachment Name List
                enty_sub.delete(0, END)
                enty_bod.delete(0, END)
                lbl_attach = Label(row2, text="============Data Cleared============", anchor='w')
                lbl_attach.pack()
        except Exception as e:
                print (e)

#Quit
def quit():
        smOb.quit()

        
getLogin()

#GUI 
scr = Tk()
scr.title("CtechF Email Sender")
scr.geometry('450x600')

#Variables  
txtTo = StringVar()
txtSub = StringVar()      
txtBod = StringVar()    

#To:
row_to = Frame(scr)
lbl_to = Label(row_to, width=10, text="To: ", anchor='w')
lbl_to.pack(side=LEFT)
enty_to = Entry(row_to, textvariable=txtTo)
enty_to.pack(side=LEFT, expand=YES, fill=X)
btnAddemail = Button(row_to, text = 'Add Email', command=addEmail)
btnAddemail.pack(side=RIGHT, fill=X)
row_to.pack(side=TOP, fill=X, padx=5, pady=5)

#Subject:
row_sub = Frame(scr)
lbl_sub = Label(row_sub, width=10, text="Subject: ", anchor='w')
lbl_sub.pack(side=LEFT)
enty_sub = Entry(row_sub, textvariable=txtSub)
enty_sub.pack(side=RIGHT, expand=YES, fill=X)
row_sub.pack(side=TOP, fill=X, padx=5, pady=5)

#Message
row_bod = Frame(scr)
lbl_bod = Label(row_bod, width=10, text="Message: ", anchor='w')
lbl_bod.pack(side=LEFT)
enty_bod = Entry(row_bod, textvariable=txtBod)
enty_bod.pack(side=RIGHT, expand=YES, fill=X)
row_bod.pack(side=TOP, fill=X, padx=5, pady=5)

#Buttons
row1 = Frame(scr)
row1.pack(side=TOP, fill=X, padx=5, pady=5)
btnAttach = Button(row1, text = 'Attach File', command=dopen)
btnAttach.pack(side=LEFT, expand=YES, fill=X)
btnAttach = Button(row1, text = 'Quit', command=scr.destroy)
btnAttach.pack(side=RIGHT, expand=YES, fill=X)

#Frame
row2 = Frame(scr)
row2.pack(side=TOP, fill=Y, padx=5, pady=5)  

#Output
row4 = Frame(scr)
row4.pack(side=TOP, fill=X, padx=5, pady=5)
btnSend = Button(row4, text = 'Send Email', command=sentEmail)
btnSend.pack(side=RIGHT, expand=YES, fill=X)

scr.mainloop()


