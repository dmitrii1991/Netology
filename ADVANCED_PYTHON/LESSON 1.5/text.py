омашнее задание к лекции 1.5 «Zen of Python - что должен знать каждый разработчик / PEP8 и PEP»
Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы с почтой, но не успел доделать его. Код рабочий. Нужно только провести рефакторинг кода.
Создать класс для работы с почтой;
Создать методы для отправки и получения писем;
Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
Переменные должны быть названы по стандарту PEP8;
Весь остальной код должен соответствовать стандарту PEP8;
Класс должен инициализироваться в конструкции.
if __name__ == '__main__'
Скрипт для работы с почтой.

import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


GMAIL_SMTP = "smtp.gmail.com"
GMAIL_IMAP = "imap.gmail.com"

l = 'login@gmail.com'
passwORD = 'qwerty'
subject = 'Subject'
recipients = ['vasya@email.com', 'petya@email.com']
message = 'Message'
header = None


#send message
msg = MIMEMultipart()
msg['From'] = l
msg['To'] = ', '.join(recipients)
msg['Subject'] = subject
msg.attach(MIMEText(message))

ms = smtplib.SMTP(GMAIL_SMTP, 587)
# identify ourselves to smtp gmail client
ms.ehlo()
# secure our email with tls encryption
ms.starttls()
# re-identify ourselves as an encrypted connection
ms.ehlo()

ms.login(l, passwORD)
ms.sendmail(l,
ms, msg.as_string())

ms.quit()
#send end


#recieve
mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
mail.login(l, passwORD)
mail.list()
mail.select("inbox")
criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
result, data = mail.uid('search', None, criterion)
assert data[0], 'There are no letters with current header'
latest_email_uid = data[0].split()[-1]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
raw_email = data[0][1]
email_message = email.message_from_string(raw_email)
mail.logout()
#end recieve
