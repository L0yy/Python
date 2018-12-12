##知识准备：
##快速了解电子邮件的收发原理及用到的协议
##https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005156604f38836be1707453eb025ce8c3079978d000
##---------------------------------------------------案例-----------------------------------------------------
##参考：
##http://www.runoob.com/python/python-email.html
##https://www.cnblogs.com/wang1122/p/8059193.html
##https://www.cnblogs.com/yufeihlf/p/5726619.html
##https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000
##https://blog.csdn.net/hanchaobiao/article/details/73348354
##https://study.163.com/course/courseLearn.htm?courseId=1004106037#/learn/video?lessonId=1050546667&courseId=1004106037
##https://mp.weixin.qq.com/s/MiOTENGSe_8x4wAJelVisA

##案例1 发送邮件：发送内容为纯文本
##import smtplib#内置库,用于连接服务器和登陆，发送邮件
##from email.mime.text import MIMEText#内置库,用于构造邮件文本
##
####（1） 设置邮件参数
##mail_host = "smtp.qq.com"#smtp服务器地址
##mail_user = "494639141@qq.com"#用户名
##f = open("授权码.txt")#授权码
##mail_pwd = f.read()
##f.close()
##mail_receiver = ["********@qq.com","********@qq.com"]#收件人,可以为多个
##
####（2）设置邮件信息
##mail_subject = "来自陈老师的问候"#主题
##mail_content = '你好，这是测试邮件 by 陈汉斌'#纯文本内容
##
####（3）构造邮件内容(三个参数:邮件内容、邮件类型、邮件编码)
##msg = MIMEText(mail_content,'plain','utf-8')
##msg['Subject'] = mail_subject
##msg['From'] = 'TeacherChen<'+mail_user+'>'
##msg['To'] = ";".join(mail_receiver)
##
####（4） 登录服务器、发送、退出
##client = smtplib.SMTP_SSL(mail_host,465)#连接服务器
##client.login(mail_user,mail_pwd)#登录服务器
##client.send_message(msg)#发送
####client.sendmail(mail_user,mail_receiver,str(msg))#发送
##client.quit()#退出

##案例2 个性化发送邮件：给成绩中不及格的人发邮件
##import smtplib#内置库,用于连接服务器和登陆，发送邮件
##from email.mime.text import MIMEText#内置库,用于构造邮件文本
##
####（1） 设置邮件参数
##mail_host = "smtp.qq.com"#smtp服务器地址
##mail_user = "494639141@qq.com"#用户名
##f = open("授权码.txt")#授权码
##mail_pwd = f.read()
##f.close()
##
####（2）设置邮件信息
##mail_subject = "成绩通知"#主题
##mail_content = ''#内容
##names = []
##mails = []
##scores = []
##f = open("成绩.txt")#授权码
##for line in f:
##    s = line.split()
##    if eval(s[2]) < 60: 
##        names.append(s[0])
##        mails.append(s[1])
##        scores.append(s[2])
##f.close()
##
####登录服务器
##client = smtplib.SMTP_SSL(mail_host,465)#连接服务器
##client.login(mail_user,mail_pwd)#登录服务器
##for name,mail,score in zip(names,mails,scores):
##    ##（3）构造邮件内容(三个参数:邮件内容、邮件类型、邮件编码)
##    mail_content = "你好:{} \n\t很遗憾的通知你，分数为:{:3d} \n\t请注意补考通知。".format(name,eval(score))
##    msg = MIMEText(mail_content,'plain','utf-8')
##    msg['Subject'] = mail_subject
##    msg['From'] = 'TeacherChen<'+mail_user+'>'
##    msg['To'] = mail
##    ##（4） 发送  
##    client.send_message(msg)#发送
##client.quit()#退出

##案例3 发送邮件:内容为HTML链接
##import smtplib#内置库,用于连接服务器和登陆，发送邮件
##from email.mime.text import MIMEText#内置库,用于构造邮件文本
##
####（1） 设置邮件参数
##mail_host = "smtp.qq.com"#smtp服务器地址
##mail_user = "494639141@qq.com"#用户名
##f = open("授权码.txt")#授权码
##mail_pwd = f.read()
##f.close()
##mail_receiver = ["********@qq.com","********@qq.com"]#收件人,可以为多个
##
####（2）设置邮件信息
##mail_subject = "来自陈老师的问候"#主题
##mail_content = '点此<a href="http://www.python.org">链接</a>访问我<br/>by 陈汉斌'#HTML内容
##
####（3） 构造邮件内容(三个参数:邮件内容、邮件类型、邮件编码)
##msg = MIMEText(mail_content,'html','utf-8')
##msg['Subject'] = mail_subject
##msg['From'] = 'TeacherChen<'+mail_user+'>'
##msg['To'] = ";".join(mail_receiver)
##
####（4） 登录服务器、发送、退出
##client = smtplib.SMTP_SSL(mail_host,465)#连接服务器
##client.login(mail_user,mail_pwd)#登录服务器
##client.send_message(msg)#发送
####client.sendmail(mail_user,mail_receiver,str(msg))#发送
##client.quit()#退出

##案例4 发送邮件:添加附件
##import smtplib#内置库,用于连接服务器和登陆，发送邮件
##from email.mime.text import MIMEText#内置库,用于构造邮件文本
##from email.mime.application import MIMEApplication#用于构造附件
##from email.mime.multipart import MIMEMultipart #大盒子，将文本和附件都装入
##
####（1） 设置邮件参数
##mail_host = "smtp.qq.com"#smtp服务器地址
##mail_user = "494639141@qq.com"#用户名
##f = open("授权码.txt")#授权码
##mail_pwd = f.read()
##f.close()
##mail_receiver = ["********@qq.com","********@qq.com"]#收件人,可以为多个
##
####（2）设置邮件信息
##mail_subject = "来自陈老师的问候"#主题
##mail_content = '点此<a href="http://www.python.org">链接</a>访问我<br/>by 陈汉斌'#HTML内容
##
####（3）构造邮件内容
##
###添加文本内容
##msg= MIMEMultipart() #大盒子
##msg['Subject'] = mail_subject
##msg['From'] = 'TeacherChen<'+mail_user+'>'
##msg['To'] = ";".join(mail_receiver)
##msg.attach(MIMEText(mail_content,'html','utf-8'))
##
#####添加附件1
##att1 = MIMEApplication(open('鸟巢.jpg','rb').read())
##att1.add_header("Content-Disposition","attachment",filename=("gbk", "", "附件1_鸟巢.jpg"))
##msg.attach(att1)
##
###添加附件2
##att2 = MIMEApplication(open('成绩.txt','rb').read())
##att2.add_header("Content-Disposition","attachment",filename=("gbk", "", "附件2_成绩.txt"))
##msg.attach(att2)
##
####（4） 登录服务器、发送、退出
##client = smtplib.SMTP_SSL(mail_host,465)#连接服务器
##client.login(mail_user,mail_pwd)#登录服务器
##client.send_message(msg)#发送
##client.quit()#退出


##案例5 发送邮件:将图片显示在正文里
##import smtplib#内置库,用于连接服务器和登陆，发送邮件
##from email.mime.text import MIMEText#内置库,用于构造邮件文本
##from email.mime.image import MIMEImage#内置库,用于构造图片
##from email.mime.multipart import MIMEMultipart #大盒子，将文本和附件都装入
##
####（1） 设置邮件参数
##mail_host = "smtp.qq.com"#smtp服务器地址
##mail_user = "494639141@qq.com"#用户名
##f = open("授权码.txt")#授权码
##mail_pwd = f.read()
##f.close()
##mail_receiver = ["********@qq.com","********@qq.com"]#收件人,可以为多个
##
####（2）设置邮件信息
##mail_subject = "来自陈老师的问候"#主题
##mail_content = '点此<a href="http://www.python.org">链接</a>\
##访问我<br/>by 陈汉斌\
##<p><img src="cid:image1"></p>'
##
####（3）构造邮件内容
###添加内容
##msg= MIMEMultipart()
##msg['Subject'] = mail_subject
##msg['From'] = 'TeacherChen<'+mail_user+'>'
##msg['To'] = ";".join(mail_receiver)
##msg.attach(MIMEText(mail_content,'html','utf-8'))
##
###添加图片
##f = open('鸟巢.jpg', 'rb')
##msgImage = MIMEImage(f.read())
##f.close()
##msgImage.add_header('Content-ID', '<image1>')#定义图片 ID，在 HTML 文本中引用
##msg.attach(msgImage)
##
####（4） 登录服务器、发送、退出
##client = smtplib.SMTP_SSL(mail_host,465)#连接服务器
##client.login(mail_user,mail_pwd)#登录服务器
##client.send_message(msg)#发送
##client.quit()#退出
