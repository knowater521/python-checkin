__author__ = 'YangKui'
#_*_encoding:utf-8_*_

from Tkinter import *

from PIL import Image, ImageTk

from AuthCode import *


class CheckInUI(Frame):
    config = {}

    def doSubmit(self):
        text = self.inputText.get()
        if (text == ''):
            self.consoleText.tag_configure('TEXTERROR', foreground='red')
            self.consoleText.insert('end', 'ERROR:authCode is null !\n', ("TEXTERROR"))
        else:
            try:
                self.consoleText.tag_configure('TEXTGREEN', foreground='green')
                self.consoleText.insert('end', '.....starting do submit...' + text + '\n', ("TEXTGREEN"))
                self.authCode.kaoQin(text)
            except Exception, e:
                self.consoleText.tag_configure('TEXTERROR', foreground='red')
                self.consoleText.insert('end', '..... do submit...error' + e.message + '\n', ("TEXTERROR"))

        print 'hello'

    def getAuthCode(self):
        self.consoleText.insert('end', 'starting get auth code,waiting....\n')
        self.authCode = AuthCode()
        self.authCode.saveImage("http://captcha.qq.com/getimage?aid=1007901&r=0.4029927267692983")
        self.img = Image.open(self.authCode.imageFilename)
        self.photoImg = ImageTk.PhotoImage(self.img)
        # self.authCodeImageLabel['text']='new auth code'
        self.authCodeImageLabel['image'] = self.photoImg
        # self.authCodeImageLabel['height']=5
        # self.authCodeImageLabel.pack()
        self.consoleText.insert('end', ' get auth code success!\n')

    def loadConfig(self):
        print 'loading config.txt file'
        f = file('config.txt')
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print "config:", line
            if (line.find('|') != -1):
                strs = line.split("|")
                self.config[strs[0]] = strs[1]
        f.close()
        print 'loaded config values:', self.config.values()

    def __init__(self, master=None):
        Frame.__init__(self, master, relief="sunken", width=100, height=80)
        master.title('考勤')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=(N, W, E, S))
        # self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.loadConfig()

        self.label1 = Label(self, text='验证码地址:')
        self.label1.grid(row=0, column=0, sticky=(N, W, E, S))
        # self.label1.pack(side='left')

        self.authCodeURL = Entry(self, width=60)
        self.authCodeURL.insert(0, "http://captcha.qq.com/getimage?aid=1007901&r=0.4029927267692983")
        self.authCodeURL.grid(row=0, column=1, columnspan=2, sticky=(N, W, E, S))
        # self.authCodeURL.pack(side='left')

        self.label2 = Label(self, text='提交地址:')
        self.label2.grid(row=1, column=0, sticky=(N, W, E, S))
        # self.label1.pack(side='left')

        self.postURL = Entry(self, width=60)
        self.postURL.insert(0, "http://captcha.qq.com/getimage?aid=1007901&r=0.4029927267692983")
        self.postURL.grid(row=1, column=1, columnspan=2, sticky=(N, W, E, S))

        self.label2 = Label(self, text='选择用户:')
        self.label2.grid(row=2, column=0, sticky=(N, W, E, S))

        self.listbox = Listbox(self, height=2)
        i = 0
        for key, value in self.config.items():
            self.listbox.insert(i, key)
            i = i + 1
            # self.listbox.pack()
        self.listbox.grid(row=2, column=1, columnspan=2, sticky=(N, W, E, S))

        self.label2 = Label(self, text='验证码:')
        self.label2.grid(row=3, column=0, columnspan=1, sticky=(N, W, E, S))

        self.authCodeImageLabel = Label(self, text="none")
        # self.authCodeImageLabel.pack()
        self.authCodeImageLabel.grid(row=3, column=1, columnspan=1, sticky=(N, W, E, S))

        self.btn1 = Button(self, text='获取验证码', command=self.getAuthCode)
        self.btn1.grid(row=3, column=2, sticky=(N, W, E, S))

        self.label2 = Label(self, text='输入验证码:')
        self.label2.grid(row=4, column=0, sticky=(N, W, E, S))

        self.inputText = Entry(self)
        self.inputText.grid(row=4, column=1, sticky=(N, W, E, S))
        # self.inputText.pack()

        self.submit = Button(self, text='提交数据', command=self.doSubmit)
        self.submit.grid(row=4, column=2, sticky=(N, W, E, S))
        # self.submit.pack()

        self.consoleText = Text(self, width=50, height=10)
        self.consoleText.grid(row=5, column=0, columnspan=4, sticky=(N, W, E, S))
        # self.consoleText.pack()

        # self.getAuthCode()


root = Tk()
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