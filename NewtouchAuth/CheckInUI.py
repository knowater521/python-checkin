__author__ = 'YangKui'
#_*_encoding:utf-8_*_

from Tkinter import *

from PIL import Image, ImageTk
from Config import *

from AuthCode import *


class CheckInUI(Frame):
    def doSubmit(self):
        inputAuthCode = self.inputText.get()
        data = self.currentUser.get()
        if (inputAuthCode == ''):
            self.consoleText.tag_configure('TEXTERROR', foreground='red')
            self.consoleText.insert('end', 'ERROR:验证码不能为空!\n', ("TEXTERROR"))
        elif (self.authCode is None):
            self.consoleText.tag_configure('TEXTERROR', foreground='red')
            self.consoleText.insert('end', 'ERROR:验证码未获取!\n', ("TEXTERROR"))
        else:
            try:
                self.consoleText.tag_configure('TEXTGREEN', foreground='green')
                message = '开始考勤\n'
                print message
                self.consoleText.insert('end', message, ("TEXTGREEN"))
                postData = data + "&captcha=" + inputAuthCode
                self.authCode.kaoQin(self.config.POSTURL, postData)
            except Exception, e:
                self.consoleText.tag_configure('TEXTERROR', foreground='red')
                errorMsg = '####提交异常##### ', e.message, '\n'
                self.consoleText.insert('end', errorMsg, ("TEXTERROR"))
                print 'Exception:', e

        print 'hello'

    def getAuthCode(self):
        self.consoleText.insert('end', '获取验证码\n')
        self.authCode = AuthCode()
        self.authCode.saveImage(self.config.AUTHCODEURL)
        self.img = Image.open(self.authCode.imageFilename)
        self.photoImg = ImageTk.PhotoImage(self.img)
        self.authCodeImageLabel['image'] = self.photoImg

    def __init__(self, master=None):
        Frame.__init__(self, master, relief="sunken", width=100, height=80)
        master.title('考勤')
        self.authCode = None
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=(N, W, E, S))
        self.createWidgets()

    def createWidgets(self):
        # # self.loadConfig()
        self.config = Config()
        # self.label1 = Label(self, text='验证码地址:')
        # self.label1.grid(row=0, column=0, sticky=(N, W, E, S))
        # # self.label1.pack(side='left')
        #
        # self.authCodeURL = Entry(self, width=60)
        # self.authCodeURL.insert(0, self.config.AUTHCODEURL)
        # self.authCodeURL.grid(row=0, column=1, columnspan=2, sticky=(N, W, E, S))
        # # self.authCodeURL.pack(side='left')
        #
        # self.label2 = Label(self, text='提交地址:')
        # self.label2.grid(row=1, column=0, sticky=(N, W, E, S))
        # # self.label1.pack(side='left')

        # self.postURL = Entry(self, width=60)
        # self.postURL.insert(0, self.config.POSTURL)
        # self.postURL.grid(row=1, column=1, columnspan=2, sticky=(N, W, E, S))

        self.label2 = Label(self, text='选择用户:')
        self.label2.grid(row=0, column=0, columnspan=1, sticky=(W, E))

        # self.listbox = Listbox(self, height=2,width=40)
        i = 0
        self.currentUser = StringVar()
        for key, value in self.config.USER.items():
            radio = Radiobutton(self, text=key, value=value.data, variable=self.currentUser)
            radio.grid(row=0, column=i + 1, columnspan=1, sticky=(W, E))
            if i == 0:
                self.currentUser.set(value.data) #set default radio value
            i = i + 1

        self.label2 = Label(self, text='验证码:', height=3)
        self.label2.grid(row=1, column=0, columnspan=1, sticky=(N, W, E, S))

        self.authCodeImageLabel = Label(self, text="none", height=3)
        # self.authCodeImageLabel.pack()
        self.authCodeImageLabel.grid(row=1, column=1, columnspan=1, sticky=(N, W, E, S))

        self.btn1 = Button(self, text='获取验证码', command=self.getAuthCode, height=1)
        self.btn1.grid(row=1, column=2, sticky=(N, W, E, S))

        self.label2 = Label(self, text='输入验证码:')
        self.label2.grid(row=2, column=0, sticky=(N, W, E, S))

        self.inputText = Entry(self)
        self.inputText.grid(row=2, column=1, sticky=(N, W, E, S))
        # self.inputText.pack()

        self.submit = Button(self, text='提交数据', command=self.doSubmit)
        self.submit.grid(row=2, column=2, sticky=(N, W, E, S))
        # self.submit.pack()

        self.consoleText = Text(self, width=50, height=10)
        self.consoleText.grid(row=3, column=0, columnspan=3, sticky=(N, W, E, S))
        # self.consoleText.pack()

        # self.getAuthCode()


root = Tk()
# root['width'] = root.winfo_screenwidth()
# root['height'] = root.winfo_screenheight()
app = CheckInUI(master=root)
app.mainloop()
# root.destroy()

# authCode = AuthCode()
# root = Tk()
# root.title("Login")
# img = Image.open(authCode.imageFilename)
# photoImg = ImageTk.PhotoImage(img)
# button3 = Button(root, image=photoImg)
# text = Entry(root)
# listbox = Listbox(root)
#
# button3.pack()
# text.pack()
# listbox.pack()
#
# # cv = Canvas(root,bg = 'white')
#
# # cv.create_image((150,150),image = img)
# # cv.pack()
# print '0k'
#
# root.mainloop()