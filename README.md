# Phone Book 📞
Консольная телефонная книга, работающая с .csv файлом.
С помощью неё можно:
- 👀 Смотреть все записи в книге с пагинацией.
- 🆕 Добавлять новые записи в книгу.
- 🗳️ Удалять ненужные записи.
- 🔄 Обновлять записи.
- 👓 Искать записи по одному или нескольким критериям.

## Установка
1. Склонируйте себе этот репозиторий:

    ```bash
   git clone https://github.com/xaer981/phone_book.git
   ```

   ```bash
   cd phone_book/
   ```

2. Затем создайте виртуальное окружение и установите зависимости:

   <details>
     <summary>Windows</summary>

     ```bash
     python -m venv venv
     ```

     ```bash
     source venv/Scripts/activate
     ```

     ```bash
     pip install -r requirements.txt
     ```
   </details>

   <details>
     <summary>Mac</summary>

      ```bash
      python3 -m venv venv
      ```

      ```bash
      source venv/bin/activate
      ```

      ```bash
      pip install -r requirements.txt
      ```
   </details>

3. Запускаем!

   ```bash
   python -m src.main <режим работы>
   ```

4. Для добавления тестовых данных в книгу:
   <details>
     <summary>Через консоль</summary>

   ```bash
   mkdir -p src/book
   ```

   ```bash
   cp phone_book.csv src/book/
   ```
   </details>
   <details>
       <summary>Через графический интерфейс ОС</summary>
       
       1. Создайте папку book внутри папки src.
       2. Скопируйте в папку src/book файл phone_book.csv
   </details>
## Режимы работы и флаги
1. **get-all - получение всех записей в книге.**
   - Можно не передавать ничего дополнительно, автоматически выводятся первые 5 записей.
     Над таблицей отображается текущая страница и общее количество страниц.
   - Для навигации по страницам используйте флаг -p (--page), например:

     `python -m src.main get-all -p 2`
     или
     `python -m src.main get-all --page 3`

2. add - добавить запись в книгу.
   - После запуска команды начинается сбор данных о контакте.
   - Обязательные поля - имя, номер телефона.
   - Остальные поля необязательны (отмечены значком [])
   - Номер телефона и рабочий номер телефона можно вводить:
       - в привычном формате `89991234567`
       - или в международном `+79991234567` `79991234567`.

3. delete - удалить запись из книги.
   - Обязательно следует посмотреть ID удаляемого контакта через get-all, а затем передать этот ID через параметр -i (--id).
   `python -m src.main delete -i 1` или `python -m src.main delete --id 2`

4. update - обновить данные о контакте.
   - Обязательно следует посмотреть ID обновляемого контакта через get-all, а затем передать этот ID через параметр -i (--id).
   - `python -m src.main update -i 1` или `python -m src.main update --id 2`.
   - После этого начинается сбор данных о контакте, аналогично добавлению нового контакта.

5. search - найти нужного контакта в книге.
   - Нужный контакт можно найти с помощью одного (или нескольких) параметров:
     - -f (--first_name) - поиск контакта по имени. `python -m src.main search -f Андрей`
     - -l (--last_name) - поиск контакта по фамилии. `python -m src.main search -l Петров`
     - -fr (--father_name) - поиск контакта по отчеству. `python -m src.main search -fr Игоревич`
     - -c (--company) - поиск контакта по компании. `python -m src.main search -c Effective Mobile`
     - -n (--number) - поиск контакта по номеру телефона. `python -m src.main search -n +7 999 123 45 67`
     - -wn (--work_number) - поиск контакта по рабочему номеру телефона. `python -m src.main search -wn +7 999 123 45 67`
> [!TIP]
> Можно использовать сразу несколько фильтров! `python -m src.main search -f Андрей -l Петров`
> 
> В случае, если найденных контактов много, то можно использовать пагинацию с помощью параметра страницы -p (--page). `python -m src.main search -f Андрей -l Петров -p 2`

<p align=center>
  Made by: <a href="https://github.com/xaer981">xaer981</a>
</p>
<p align=center>
  <a href="url"><img src="https://github.com/xaer981/xaer981/blob/main/main_cat.gif" align="center" height="40" width="128"></a>
</p>



