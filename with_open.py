#1
# with open('directories.txt','r') as d:
#     print(d.read())

#2
# login = input('login: ')
# password = input('password: ')
# with open('users.txt', 'w') as u:
#     u.write('login: '+login+"\n")
#     u.write('password: '+password)

#3
# with open('file.txt','r') as f:
#     if "w" in f.read():
#         print("Да в тексте есть w")
#     else:
#         print("Нет, в тексте нету 'w' ")

#4
# t_words = []
# with open('python.txt','r') as p:
#     for word in p.read().split():
#         if "T" in word or "t" in word:
#             t_words.append(word)
# print(t_words)

#5

# def register():
#     while True:
#         acc = input('login name: ')
#         with open('database.txt','r') as db:
#             login = "login:"+acc
#             l = ''.join(db.readlines()).split()
#             if login in l:
#                 print('account already exist!!!')
#             else:
#                 password = input('create password: ')
#                 check_password = input('enter password again: ')
#                 if password != check_password:
#                     print('passwords not same, enter all again!!!')
#                 else:
#                     break
#     with open('database.txt','a') as db:
#         db.write('\n')
#         db.write(login+'\n')
#         db.write('password:'+password+'\n')
#         print('account created succesfuly!!!')
#     return
# register()

#6
# def check_extension(p):
#     extensions = ['jpeg','jpg','png']
#     if "."not in p:
#         return False
#     i = p.index('.')
#     if p[i+1:] in extensions:
#         return True
#     return False

# print('Sign in')
# login = input('Enter login name: ')
# password = input('Enter password: ')
# photo = input("path of your photo: ")
# try:
#     with open(photo,'r') as p:
#         with open('sign_in_form.txt','w') as file:
#             if check_extension(photo) == True:
#                 file.write('login: '+login+'\n')
#                 file.write('password: '+password+'\n')
#                 file.write('photo: '+photo)
#                 print('Account Succesfully Created!!!')
# except Exception:
#     print('Sorry, your path didn\'t find!')


#7
# path_for_photo_to_change = input('path to change: ')
# path_photo_that_will_apply = input('path which photo: ')
# try:
#     with open(path_for_photo_to_change,'rb') as p:
#         p.read()
#         with open(path_for_photo_to_change,'w') as w:
#             w.write(path_photo_that_will_apply)
# except Exception as e:
#     print("Photo or Path didn't find",e)


#8
# need_month = ['May','July','September','November']
# salary = []
# with open('text#2.txt','r') as text:
#     for line in text.readlines():
#         l = line.split()
#         if len(l)>1:
#             if l[0] in need_month:
#                 salary.append(int(l[1]))
# srednee_arithmetic = sum(salary)/len(salary)
# print(srednee_arithmetic)



#9
# with open('num.txt','r') as f:
#     l = []
#     for n in f.read().split():
#         l.append(n)
# f = open('max_min.txt','w')
# f.write("max: "+max(l)+'\n')
# f.write('min: '+min(l))
# f.close()

#10
# text = input('text here: ')
# text = text.split()
# with open('t#9.txt','w') as f:
#     for line in text:
#         f.write(line)
#         f.write('\n')




                








        






        
    