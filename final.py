user_name = input("Введите имя пользователя: ")
content = input("Введите описание вашей заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату создания заметки в формате дд.мм: ")
issue_date = input("Введите планируемую дату окончания заметки в формате дд.мм: ")
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("введите третий заголовок: ")
title123 = [title1, title2, title3]
note = [user_name, content, status, created_date[0:5], issue_date[0:5], title123]



print("Имя: ",note[0],"\nОписание заметки: ",note[1],"\nСтатус заметки: ",note[2],"\nДата создания (дд,мм): ",note[3],
      "\nДата окончания (дд.мм): ",note[4],"\nЗаголовок 1: ",title123[0],"\nЗаголовок 2: ",title123[1],
"\nЗаголовок 3: ",title123[2])



