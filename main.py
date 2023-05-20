# -*-coding: utf-8 -*-
from aifc import Error
import logging
from ntpath import join
from os import times
import sqlite3
import random
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import quote_html
from datetime import datetime, timedelta
from decimal import Decimal
from time import gmtime
from time import strptime
import asyncio


logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token='6116567454:AAHRdMnmGbADfMXEpYO70PO5uT4OV8cRvtU')
dp = Dispatcher(bot)


# datebase
connect = sqlite3.connect("LAY.db")
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    user_id BIGINT,
    user_name STRING,
    user_tg_name STRING,
    user_status STRING,
    balance INT,
    bank BIGINT,
    ethereum INT,
    rating INT,
    status_block STRING,
    time_register INT,
    pref STRING,
    donate_coins INT,
    game INT,
    bank2 INT,
    depozit INT,
    stats_status STRING
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot(
    user_id BIGJNT,
    chat_id INTERGEN,
    last_stavka INTERGEN,
    last_depozit INTERGEN
)
""")


cursor.execute("""CREATE TABLE IF NOT EXISTS mine(
    user_id INT,
    user_name STRING,
    pick STRING,
    iron INT,
    metall INT,
    silver INT,
    bronza INT,
    gold INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS user_case(
    user_id INT,
    case_money INT,
    case_donate INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS farm(
    user_id INT,
    user_name STRING,
    rake STRING,
    linen INT,
    cotton INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS house(
    user_id INT,
    user_name STRING,
    house INT,
    basement INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
    user_id INT,
    user_name STRING,
    cars INT,
    hp INT,
    benz INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bot_time(
    user_id INT,
    stavka_games INTERGEN,
    stavka_bank INTERGEN,
    stavka_bonus INT,
    stavka_depozit INTERGEN,
    time_pick INT,
    time_rake INT,
    time_craft INT,
    time_kit INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time_bank(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS ob_time(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time_prefix(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS time_sms(
    user_id INT,
    stavka INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS warn(
    user_id INT,
    warn INT 
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS console(
    user_id INT,
    status STRING 
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS channel_pov(
    user_id INT,
    members INT   
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS avatarka(
    user_id INT,
    avatarka STRING   
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS reput(
    user_id INT,
    reput INT   
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo1(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo2(
    user_id INT,
    members INT,
    ob_members INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS promo3(
    user_id INT,
    members INT,
    ob_members INT
)
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS promo4(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo5(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo6(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo7(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo8(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo9(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo10(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo11(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo12(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo13(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo14(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo15(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo16(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo17(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo18(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo19(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo20(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo21(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo22(
    user_id INT,
    members INT,
    ob_members INT
)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS promo23(
    user_id INT,
    members INT,
    ob_members INT
)
""")



@dp.message_handler(commands=['gamevb'])
async def start_cmd(message):
   msg = message
   user_id = msg.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   period = 5

   balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
   balance = int(balance[0])

   gamevbmenu = InlineKeyboardMarkup(row_width=1)
   gamevb = InlineKeyboardButton(text='ИГРАТЬ 🎮', callback_data='gamevb')
   gamevbmenu.add(gamevb)

   get = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
   last_stavka = f"{INTERGEN(get[0])}"
   stavkatime = time.time() - float(last_stavka)
   if stavkatime > period:
      if balance > 0:
         await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вы уверены что хотите сыграть в GAME-VB ? 🧊

ℹ️ | В этой игре вы играете сразу на весь <b>баланс</b>

↘️ Выберите одну кнопку ниже         
""",reply_markup=gamevbmenu,  parse_mode='html')
      else:
         await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! У вас недостаточно средств! ", parse_mode='html')
   else:
      await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, играть можно раз в 5 секунд", parse_mode='html')         
      

# start command
@dp.message_handler(commands=['start'])
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    user_name = msg.from_user.full_name
    full_name = msg.from_user.full_name
    user_status = "Player"
    user_name = 'Игрок'
    chat_id = message.chat.id
    avatarka_start = 'none'
    cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?);", (user_id, 10000, 0, user_name, user_status, 0))
        cursor.execute("INSERT INTO avatarka VALUES(?, ?);",(user_id, avatarka_start))
        cursor.execute("INSERT INTO cars VALUES(?, ?, ?, ?, ?);",(user_id, user_name, 0, 0, 0))
        cursor.execute("INSERT INTO house VALUES(?, ?, ?, ?);",(user_id, user_name, 0, 0))
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        connect.commit()
        print(f'Зарегестрировался в боте пользователь: {full_name}')
    else:
        cursor.execute("INSERT INTO bot VALUES(?, ?);", (chat_id, 0))
        connect.commit()

    reg = InlineKeyboardMarkup(row_width=2)    
    btn6 = InlineKeyboardButton(text='🆘 Добавить в чат', url='https://t.me/leonqamebot?startgroup')       
    reg.add(btn6)

    reg = InlineKeyboardMarkup(row_width=1)
    register_help = InlineKeyboardButton(text='🆘 Помощь', callback_data='register_help')
    reg.add(register_help)
    
    name = message.from_user.get_mention(as_html=True)
    await bot.send_message(message.chat.id, f'''
🙋 | Привет {name}, я игровой бот Lay🍀 Тебе выдано <code>10.000€</code>\n🆘 | Для ознакомление с моими командами, введи команду Помощь, или нажмина на кнопку нижи\n➕ | Если я тебе понравлюсь добавишь меня в свой чатик?)
    ''', reply_markup=reg, parse_mode='html')         
@dp.message_handler(commands=['мут', 'mute'], commands_prefix='!?./', is_chat_admin=True)
async def mute(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   try:
      muteint = int(message.text.split()[1])
      mutetype = message.text.split()[2]
      comment = " ".join(message.text.split()[3:])
   except IndexError:
      await message.reply('ℹ | Не хватает аргументов!\nПример:\n<code>/мут 1 ч причина</code>')
      return
   if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
      dt = datetime.now() + timedelta(hours=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'👤 | Администратор: {name1}\n🛑 | Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')
   if mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
      dt = datetime.now() + timedelta(minutes=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'👤 | Администратор: {name1}\n🛑 | Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')
   if mutetype == "д" or mutetype == "дней" or mutetype == "день":
      dt = datetime.now() + timedelta(days=muteint)
      timestamp = dt.timestamp()
      await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
      await message.reply(f'👤 | Администратор: {name1}\n | 🛑Замутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: {muteint} {mutetype}\n📃 | Причина: {comment}',  parse_mode='html')

@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='!?./', is_chat_admin=True)
async def unmute(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f'👤 | Администратор: {name1}\n🔊 | Размутил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')

@dp.message_handler(commands=['ban', 'бан', 'кик', 'kick'], commands_prefix='!?./', is_chat_admin=True)
async def ban(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   comment = " ".join(message.text.split()[1:])
   await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
   await message.reply(f'👤 | Администратор: {name1}\n🛑 | Забанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | Срок: навсегда\n📃 | Причина: {comment}',  parse_mode='html')

@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!?./', is_chat_admin=True)
async def unban(message):
   name1 = message.from_user.get_mention(as_html=True)
   if not message.reply_to_message:
      await message.reply("ℹ | Эта команда должна быть ответом на сообщение!")
      return
   await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
   await message.reply(f'👤 | Администратор: {name1}\n📲 | Разбанил: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')
@dp.message_handler(commands=['report'])
async def report(message):
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_id = message.from_user.id

    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    text = message.text[7:]
    
    if text == '':
       await bot.send_message(message.chat.id, f"📖 | <a href='tg://user?id={user_id}'>{user_name}</a> Вы отписали слишком кратко ваш репорт", parse_mode='html')
       return
    rows = cursor.execute('SELECT user_id FROM users where user_status = "Helper_Admin"').fetchall()
    for row in rows:
       await bot.send_message(row[0], f"<b>🆘ВАМ ПРИШЁЛ РЕПОРТ🆘</b>\n👨 | Отправитель: <a href='tg://user?id={user_id}'>{user_name}</a>\n💬 |Сообщение: <i>{text}</i>", parse_mode='html')

    await bot.send_message(1887634547,f"""
<b>🆘ВАМ ПРИШЁЛ РЕПОРТ🆘</b>
👨 | Отправитель: <a href='tg://user?id={user_id}'>{user_name}</a>  
💬 |Сообщение: <i>{text}</i>
    """, parse_mode='html')  
    await bot.send_message(message.chat.id, f"✅ | <a href='tg://user?id={user_id}'>{user_name}</a>, ваш репорт был успешно отправлен администрации", parse_mode='html')  
@dp.message_handler(commands=['m'])
async def start_cmd(message):
   try:
      text = ' '.join(message.text.split()[2:])

      msg = message
      user_id = msg.from_user.id
      user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
      user_name = str(user_name[0])

      reply_user_id = int(message.text.split()[1])
      reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
      reply_user_name = str(reply_user_name[0])

      period = 5
      get = cursor.execute("SELECT stavka FROM time_sms WHERE user_id = ?", (message.from_user.id,)).fetchone()
      last_stavka = f"{int(get[0])}"
      stavkatime = time.time() - float(last_stavka)

      if len(text) > 50:
         await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, сообщение не может быть более чем 50 символов ", parse_mode='html')
         return
      if stavkatime > period:
         await bot.send_message(user_id, f"💬 | [Я ➡️ <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>] {text}", parse_mode='html')
         await bot.send_message(reply_user_id, f"💬 | [<a href='tg://user?id={user_id}'>{user_name}</a> ➡️ Я] {text}", parse_mode='html')
         cursor.execute(f'UPDATE time_sms SET stavka = {time.time()} WHERE user_id = {user_id}')
         connect.commit()
         return
      else:
         await bot.send_message(user_id, f"🆘 | Игрок, сообщение писать можно раз в 5 секунд", parse_mode='html')
         return
   except:
      await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ошибка! Либо вы не правильно ID, или данный игрок не играет в бота", parse_mode='html')
      return    
@dp.message_handler(commands=['help_admins'])
async def help_admins(message):
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_id = message.from_user.id

    await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот информация для администрации чата ⛔️

1️⃣ /channel_mute [количество] [м\д\ч] [причина] - Выдача затычки игроку 
2️⃣ /channel_ban [количество] [м\д\ч] [причина] - Выдача бана игроку
3️⃣ /channel_unmute - снятие затычки игроку 
4️⃣ /channel_unban - снятие бана игроку 

ℹ️Команды работают ответом на сообщение нарушителя     
    """, parse_mode='html')

@dp.message_handler(commands=['reset'])
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    
    

    if user_status == 'Owner':
       await bot.send_message(message.chat.id, f"⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Масовое обнуление\n💈 | Время: навсегда\n👨 | Игроку: Всем игрокам", parse_mode='html')
       cursor.execute(f'UPDATE users SET balance = {10000}')
       cursor.execute(f'UPDATE users SET user_name = "Игрок"')
       cursor.execute(f'UPDATE users SET bank = {1000}')
       cursor.execute(f'UPDATE users SET depozit = {0}')
       cursor.execute(f'UPDATE users SET rating = {0}')
       cursor.execute(f'UPDATE users SET ethereum = {100}')
       cursor.execute(f'UPDATE mine SET iron = {0}')
       cursor.execute(f'UPDATE mine SET metall = {0}')
       cursor.execute(f'UPDATE mine SET silver = {0}')
       cursor.execute(f'UPDATE mine SET bronza = {0}')
       cursor.execute(f'UPDATE mine SET gold = {0}')
       cursor.execute(f'UPDATE farm SET linen = {0}')
       cursor.execute(f'UPDATE farm SET cotton = {0}')
       cursor.execute(f'UPDATE house SET house = {0}')
       cursor.execute(f'UPDATE house SET basement = {0}')
       cursor.execute(f'UPDATE cars SET cars = {0}')
       cursor.execute(f'UPDATE cars SET hp = {0}')
       cursor.execute(f'UPDATE cars SET benz = {0}')
       cursor.execute(f'UPDATE bot_time SET stavka_games = {0} ')
       cursor.execute(f'UPDATE bot_time SET stavka_bank = {0} ')
       cursor.execute(f'UPDATE bot_time SET stavka_bonus = {0} ')
       cursor.execute(f'UPDATE bot_time SET stavka_depozit = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_pick = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_rake = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_craft = {0} ')
       cursor.execute(f'UPDATE bot_time SET time_kit = {0} ')

       connect.commit()
       full_name = msg.from_user.full_name
       print(f'{full_name} сделал масовое обнуление')
       return
    else:
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"OWNER\"", parse_mode='html')
             
@dp.callback_query_handler(text='ava_admin')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_status = str(user_status[0])

   if user_status in ['Admin', 'Helper_Admin', 'Owner']:
      await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"АДМИН\"", parse_mode='html')
      cursor.execute(f'UPDATE avatarka SET avatarka = "admin" WHERE user_id = {user_id}')
      connect.commit()
      return
   else:
      await callback.message.answer( f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику ⚠️", parse_mode='html')

@dp.callback_query_handler(text='ava_girl')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"ДЕВУШКА\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "girl" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_dyp')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"ДЮППЕР\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "dyp" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_apper')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"АППЕР\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "apper" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_cheat')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"ЧИТЕР\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "cheat" WHERE user_id = {user_id}')
   connect.commit()

@dp.callback_query_handler(text='ava_strach')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   await callback.message.answer( f"🖼 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно поставили аватарку \"СТРАЖ\"", parse_mode='html')
   cursor.execute(f'UPDATE avatarka SET avatarka = "strach" WHERE user_id = {user_id}')
   connect.commit()
         
@dp.message_handler(commands=['post'])
async def posting(message):
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_id = message.from_user.id
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    text = message.text[5:]
    
    if user_status == 'Owner':
       rows = cursor.execute('SELECT user_id FROM users').fetchall()
       for row in rows:
          await bot.send_message(row[0], text, parse_mode='html')
    else:
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, данная команда доступна от прав администратора \"OWNER\"", parse_mode='html')      
@dp.message_handler(commands=['ban_id'])
async def start_cmd(message):
    msg = message
    user_id = msg.from_user.id
    reply_user_id = int(message.text.split()[1])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?", (message.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    reply_user_name = cursor.execute(f"SELECT user_name from users where user_id = {reply_user_id}").fetchone()
    reply_user_name = str(reply_user_name[0])

    


    if user_status == 'Owner':
       await bot.send_message(reply_user_id, f"📛 | <a href='tg://user?id={user_id}'>{reply_user_name}</a>, ваш аккаунт был заблокирован по ID", parse_mode='html')

       await bot.send_message(message.chat.id, f"⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 | Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "on"  WHERE user_id = {reply_user_id}')
       full_name = msg.from_user.full_name
       
       print(f'{full_name} выдал бан игроку: {reply_user_name}')
       connect.commit()
       return
    if user_status == 'Helper_Admin':
       await bot.send_message(reply_user_id, f"📛 | <a href='tg://user?id={user_id}'>{reply_user_name}</a>, ваш аккаунт был заблокирован по ID", parse_mode='html')
       await bot.send_message(1887634547, f"⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 | Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')

       await bot.send_message(message.chat.id, f"⛔️ | Администратор: <a href='tg://user?id={user_id}'>{user_name}</a>\n⚙️ | Действие: Бан аккаунта\n💈 | Время: навсегда\n👨 | Игроку: <a href='tg://user?id={user_id}'>{reply_user_name}</a>", parse_mode='html')
       cursor.execute(f'UPDATE users SET status_block = "on"  WHERE user_id = {reply_user_id}')
       full_name = msg.from_user.full_name
       
       print(f'{full_name} выдал бан игроку: {reply_user_name}')
       connect.commit()
       return
    else:
       await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a> , данная функция доступна только с категории администратора \"HELPER ADMIN\"", parse_mode='html')             ###########################################БАЛАНС###########################################
@dp.message_handler()
async def prof_user(message: types.Message):
    if message.forward_date != None:
        rx = ['😌','🥱','🙄','😎','😏']
        rdrx = random.choice(rx)
        await bot.send_message(message.chat.id,f"")
        return
    if message.text.lower() in ["баланс", "Баланс", "Б", "б"]:
       msg = message
       user_id = msg.from_user.id
       
       chat_id = message.chat.id

       avatarka = cursor.execute("SELECT avatarka from avatarka where user_id = ?",(message.from_user.id,)).fetchone()
       avatarka = avatarka[0]

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       balance2 = '{:,}'.format(balance)
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = int(bank[0])
       bank2 = '{:,}'.format(bank)

       c = 999999999999999999999999999999999999999999999999999999999999999999
       if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
          balance = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       else:
        pass
       if bank >= 999999999999999999999999999999999999999999999999999999999999999999:
          bank = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{:,}'.format(bank)
       else:
        pass

       if avatarka == 'apper':
          ava = open('apper.jpg', 'rb')
          await bot.send_photo(message.chat.id, ava, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance2}€\n✏️ | Префикс: {pref}\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
          return
       
       if avatarka == 'creator':
          ava = open('IMG_20220611_032148_654.jpg', 'rb')
          await bot.send_photo(message.chat.id, ava, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance2}€\n✏️ | Префикс: {pref}\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
          return
          
       if avatarka == 'admin':
          ava = open('админ.jpg', 'rb')
          await bot.send_photo(message.chat.id, ava, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance2}€\n✏️ | Префикс: {pref}\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
          return
          
       if avatarka == 'girl':
          ava = open('girl.jpg', 'rb')
          await bot.send_photo(message.chat.id, ava, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance2}€\n✏️ | Префикс: {pref}\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
          return
       
       if avatarka == 'cheat':
          ava = open('cheat.jpg', 'rb')
          await bot.send_photo(message.chat.id, ava, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance2}€\n✏️ | Префикс: {pref}\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
          return
       
       if avatarka == 'dyp':
          ava = open('дюп.jpg', 'rb')
          await bot.send_photo(message.chat.id, ava, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance}€\n✏️ | Префикс: {pref}\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
          return
       
       if avatarka == 'strach':
          ava = open('страж.jpg', 'rb')
          await bot.send_photo(message.chat.id, ava, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance2}€\n✏️ | Префикс: {pref}\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
          return


       await bot.send_message(message.chat.id, f"🤵 | Ник: <a href='tg://user?id={user_id}'>{user_name}</a>\n💶 | Баланс: {balance2}€\n✏️ | Префикс: [Разработке]\n🏦 | В Банке: {bank2}€\n💹 | Иены: [РАЗРАБОТКА]¥", parse_mode='html')
       
    if message.text.lower() in ["Мой банк", "банк", "Банк", "мой банк"]:
       msg = message
       user_id = msg.from_user.id
       
       chat_id = message.chat.id

       avatarka = cursor.execute("SELECT avatarka from avatarka where user_id = ?",(message.from_user.id,)).fetchone()
       avatarka = avatarka[0]

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       balance2 = '{:,}'.format(balance)
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = int(bank[0])
       bank2 = '{:,}'.format(bank)

       c = 999999999999999999999999999999999999999999999999999999999999999999
       if balance >= 999999999999999999999999999999999999999999999999999999999999999999:
          balance = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET balance = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          balance2 = '{:,}'.format(balance) 
       else:
        pass
       if bank >= 999999999999999999999999999999999999999999999999999999999999999999:
          bank = 999999999999999999999999999999999999999999999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999999999999999999999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
          bank2 = '{:,}'.format(bank)
       else:
        pass

       await bot.send_message(message.chat.id, f"👋 | <a href='tg://user?id={user_id}'>{user_name}</a> Добро пожаловать в банк <b>«💸Lay»</b>\n❗️Ваш банковский счёт: {bank2}€", parse_mode='html')
       
    if message.text.lower() in ["профиль", "Профиль"]:
       msg = message
       chat_id = message.chat.id
       name1 = message.from_user.get_mention(as_html=True)
       
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       
       user_id = msg.from_user.id
       balance = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
       bank = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
       rating = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance = int(balance[0])
       bank = int(bank[0])
       rating = int(rating[0])
       
       cars = cursor.execute("SELECT cars from cars where user_id = ?",(message.from_user.id,)).fetchone()
       cars = int(cars[0])

       house = cursor.execute("SELECT house from house where user_id = ?",(message.from_user.id,)).fetchone()
       house = int(house[0])

       d5 = 0

       if house == 1:
          house2 = '\n    🏠Дом: Коробка\n'
          d5 += 1
       if house == 2:
          house2 = '\n    🏠Дом: Сарай\n'
          d5 += 1
       if house == 3:
          house2 = '\n    🏠Дом: Маленький домик\n'
          d5 += 1
       if house == 4:
          house2 = '\n    🏠Дом: Квартира\n'
          d5 += 1
       if house == 5:
          house2 = '\n    🏠Дом: Огромный дом\n'
          d5 += 1
       if house == 6:
          house2 = '\n    🏠Дом: Коттедж\n'
          d5 += 1
       if house == 7:
          house2 = '\n    🏠Дом: Вилла\n'
          d5 += 1
       if house == 8:
          house2 = '\n    🏠Дом: Загородный дом\n'
          d5 += 1
       else:
          house2 = ''
       if cars == 1:
          cars2 = '    🚘Машина: Самокат\n'
          d5 += 1
       if cars == 2:
          cars2 = '    🚘Машина: Велосипед\n'
          d5 += 1
       if cars == 3:
          cars2 = '    🚘Машина: Гироскутер\n'
          d5 += 1
       if cars == 4:
          cars2 = '    🚘Машина: Сегвей\n'
          d5 += 1
       if cars == 5:
          cars2 = '    🚘Машина: Мопед\n'
          d5 += 1
       if cars == 6:
          cars2 = '    🚘Машина: Мотоцикл\n'
          d5 += 1
       if cars == 7:
          cars2 = '    🚘Машина: ВАЗ 2109\n'
          d5 += 1
       if cars == 8:
          cars2 = '    🚘Машина: Квадроцикл\n'
          d5 += 1
       if cars == 9:
          cars2 = '    🚘Машина: Багги\n'
          d5 += 1
       if cars == 10:
          cars2 = '    🚘Машина: Вездеход\n'
          d5 += 1
       if cars == 11:
          cars2 = '    🚘Машина: Лада Xray\n'
          d5 += 1
       if cars == 12:
          cars2 = '    🚘Машина: Audi Q7\n'
          d5 += 1
       if cars == 13:
          cars2 = '    🚘Машина: BMW X6\n'
          d5 += 1
       if cars == 14:
          cars2 = '    🚘Машина: Toyota FT-HS\n'
          d5 += 1
       if cars == 15:
          cars2 = '    🚘Машина: BMW Z4 M\n'
          d5 += 1
       if cars == 16:
          cars2 = '    🚘Машина: Subaru WRX STI\n'
          d5 += 1
       if cars == 17:
          cars2 = '    🚘Машина: Lamborghini Veneno\n'
          d5 += 1
       if cars == 18:
          cars2 = '    🚘Машина: Tesla Roadster\n'
          d5 += 1
       else:
          cars2 = ''

       if d5 == 0:
          d6 = '\n      У вас нету имущества 🙁'
       else:
          d6 = '🕋 | Имущество:'
       
       c = 999999999999999999999999999
       if int(balance) in range(0, 1000):
          balance3 = cursor.execute("SELECT balance from users where user_id = ?",(message.from_user.id,)).fetchone()
          balance3 = int(balance3[0])
       if int(balance) in range(1000, 999999):
          balance1 = balance / 1000
          balance2 = round(balance1)
          balance3 = f'{balance2} тыс'
       if int(balance) in range(1000000, 999999999):
          balance1 = balance / 1000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млн'
       if int(balance) in range(1000000000, 999999999999):
          balance1 = balance / 1000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} млрд'
       if int(balance) in range(1000000000000, 999999999999999):
          balance1 = balance / 1000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трлн'
       if int(balance) in range(1000000000000000, 999999999999999999):
          balance1 = balance / 1000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квдр'
       if int(balance) in range(1000000000000000000, 999999999999999999999):
          balance1 = balance / 1000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} квнт'
       if int(balance) in range(1000000000000000000000, 999999999999999999999999):
          balance1 = balance / 1000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} скст'
       if int(balance) in range(1000000000000000000000000, 999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трикс'
       if int(balance) in range(1000000000000000000000000000,999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} твинкс'
       if int(balance) in range(1000000000000000000000000000000, 999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} септ'
       if int(balance) in range(1000000000000000000000000000000000, 999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} октл'
       if int(balance) in range(1000000000000000000000000000000000000, 999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} нонл'
       if int(balance) in range(1000000000000000000000000000000000000000, 999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} декал'
       if int(balance) in range(1000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} эндк'
       if int(balance) in range(1000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} доктл'
       if int(balance) in range(1000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} гугл'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} кинд'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} трипт'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999) :
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} срист'
       if int(balance) in range(1000000000000000000000000000000000000000000000000000000000000, 999999999999999999999999999999999999999999999999999999999999999):
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} манит'
       if int(balance) >= 1000000000000000000000000000000000000000000000000000000000000000:
          balance1 = balance / 1000000000000000000000000000000000000000000000000000000000000000
          balance2 = round(balance1)
          balance3 = f'{balance2} гвинт'
       if bank >= 999999999999999999999999999:
          bank = 999999999999999999999999999
          cursor.execute(f'UPDATE users SET bank = {999999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()   
       else:
        pass
       if int(bank) in range(0, 1000):
          bank3 = cursor.execute("SELECT bank from users where user_id = ?",(message.from_user.id,)).fetchone()
          bank3 = int(bank3[0])
       if int(bank) in range(1000, 999999):
          bank1 = bank / 1000
          bank2 = round(bank1)
          bank3 = f'{bank2} тыс'
       if int(bank) in range(1000000, 999999999):
          bank1 = bank / 1000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млн'
       if int(bank) in range(1000000000, 999999999999):
          bank1 = bank / 1000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} млрд'
       if int(bank) in range(1000000000000, 999999999999999):
          bank1 = bank / 1000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} трлн'
       if int(bank) in range(1000000000000000, 999999999999999999):
          bank1 = bank / 1000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квдр'
       if int(bank) in range(1000000000000000000, 999999999999999999999):
          bank1 = bank / 1000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} квнт'
       if int(bank) in range(1000000000000000000000, 999999999999999999999999):
          bank1 = bank / 1000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} скст'
       if int(bank) in range(1000000000000000000000000, 999999999999999999999999999):
          bank1 = bank / 1000000000000000000000000
          bank2 = round(bank1)
          bank3 = f'{bank2} септ'
       if rating >= 999999999999999999999999:
          rating = 999999999999999999999999
          cursor.execute(f'UPDATE users SET rating = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
          connect.commit()
       else:
        pass
       if int(rating) in range(0, 1000):
          rating3 = cursor.execute("SELECT rating from users where user_id = ?",(message.from_user.id,)).fetchone()
          rating3 = int(rating3[0])
       if int(rating) in range(1000, 999999):
          rating1 = rating / 1000
          rating2 = round(rating1)
          rating3 = f'{rating2} тыс'
       if int(rating) in range(1000000, 999999999):
          rating1 = rating / 1000000
          rating2 = round(rating1)
          rating3 = f'{rating2} млн'
       if int(rating) in range(1000000000, 999999999999):
          rating1 = rating / 1000000000
          rating2 = round(rating1) 
          rating3 = f'{rating2} млрд'
       if int(rating) in range(1000000000000, 999999999999999):
          rating1 = rating / 1000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} трлн'
       if int(rating) in range(1000000000000000, 999999999999999999):
          rating1 = rating / 1000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квдр'
       if int(rating) in range(1000000000000000000, 999999999999999999999):
          rating1 = rating / 1000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} квнт'
       if int(rating) in range(1000000000000000000000, 999999999999999999999999):
          rating1 = rating / 1000000000000000000000
          rating2 = round(rating1)
          rating3 = f'{rating2} скст'
       if int(rating) in range(1000000000000000000000000000, 999999999999999999999999999):
          rating1 = rating / 1000000000000000000000000 
          rating2 = round(rating1)          
          rating3 = f'{rating2} септ'          
          
       await bot.send_message(message.chat.id, f"{name1} Ваш профиль\n👤 | Ник: {name1}\n 🔎 |  ID {user_id}\n👑 | Рейтинг: {rating3}\n💸 | Деньги: {balance3}€\n🏦 | В банке: {bank3}€\n💹 | Иены: <b>В Разработке</b>¥",  parse_mode='html')   
       
###################################### ДОМА############# ####################################
     
    if message.text.lower() == 'мой дом':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       house = cursor.execute("SELECT house from house where user_id = ?", (message.from_user.id,)).fetchone()
       house = int(house[0])

       if house == 1:
          house2 = 'Коробка'
       
       if house == 2:
          house2 = 'Сарай'

       if house == 3:
          house2 = 'Маленький домик'

       if house == 4:
          house2 = 'Квартира'

       if house == 5:
          house2 = 'Огромный дом'

       if house == 6:
          house2 = 'Коттедж'

       if house == 7:
          house2 = 'Вилла'

       if house == 8:
          house2 = 'Загородный дом'
         
       if house > 0:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за ваш дом🏡\n\n👤 | Владелец: {user_name}\n🏠 | Дом: {house2}\n\nℹ️ Чтобы продать дом введите команду  \"Продать дом\"", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас нету дома, что бы купить дом введите команду \"Дома\"", parse_mode='html')
    
    
    if message.text.lower() == 'продать дом':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_Id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       house = cursor.execute("SELECT house from house where user_id = ?", (message.from_user.id,)).fetchone()
       house = int(house[0])

       if house == 1:
          house2 = 'Коробка'
          summ = 500000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 1


       if house == 2:
          house2 = 'Сарай'
          summ = 3000000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 2
      
       if house == 3:
          house2 = 'Маленький домик'
          summ = 5000000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 3
      
       if house == 4:
          house2 = 'Квартира'
          summ = 7000000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 4
      
       if house == 5:
          house2 = 'Огромный дом'
          summ = 10000000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 5

       if house == 6:
          house2 = 'Коттедж'
          summ = 50000000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 6

       if house == 7:
          house2 = 'Вилла'
          summ = 100000000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 7

       if house == 8:
          house2 = 'Загородный дом'
          summ = 5000000000 + summ_basement
          summ2 = '{:,}'.format(summ)
          member_house = 8

       if house > 0:
          await bot.send_message(message.chat.id, f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏡 | Действие: Продажа дома\n🏠 | Дом: {house2}\n💈 | Продано за: {summ2}€", parse_mode='html')
          cursor.execute(f'UPDATE house SET house = {0} WHERE user_id = {user_id}')
          connect.commit()
          return
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас и так нету дома! Что бы купить дом введите команду \"Дома\"", parse_mode='html')
          return

    if message.text.startswith('купить дом'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_Id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       house = cursor.execute("SELECT house from house where user_id = ?", (message.from_user.id,)).fetchone()
       house = int(house[0])

       member = int(message.text.split()[2])

       if member == 1:
          house2 = 'Коробка'
          summ = 500000
          summ2 = '{:,}'.format(summ)
          member_house = 1


       if member == 2:
          house2 = 'Сарай'
          summ = 3000000
          summ2 = '{:,}'.format(summ)
          member_house = 2
      
       if member == 3:
          house2 = 'Маленький домик'
          summ = 5000000
          summ2 = '{:,}'.format(summ)
          member_house = 3
      
       if member == 4:
          house2 = 'Квартира'
          summ = 7000000
          summ2 = '{:,}'.format(summ)
          member_house = 4
      
       if member == 5:
          house2 = 'Огромный дом'
          summ = 10000000
          summ2 = '{:,}'.format(summ)
          member_house = 5

       if member == 6:
          house2 = 'Коттедж'
          summ = 50000000
          summ2 = '{:,}'.format(summ)
          member_house = 6

       if member == 7:
          house2 = 'Вилла'
          summ = 100000000
          summ2 = '{:,}'.format(summ)
          member_house = 7

       if member == 8:
          house2 = 'Загородный дом'
          summ = 5000000000
          summ2 = '{:,}'.format(summ)
          member_house = 8

       if house == 0:
          if member > 0:
             if member < 9:
                if summ <= balance:
                   await bot.send_message(message.chat.id, f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏡 | Действие: Покупка дома\n🏠 | Дом: {house2}\n💈 | Стоимость: {summ2}€", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE house SET house = {member_house} WHERE user_id = {user_id}')
                   connect.commit()
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нехватает средств!", parse_mode='html')               
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Нету такого номера дома!", parse_mode='html')
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Нету такого номера дома!", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас уже есть дом, что бы продать дом введите команду \"Продать дом\"", parse_mode='html')



    if message.text.startswith('Купить дом'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_Id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       house = cursor.execute("SELECT house from house where user_id = ?", (message.from_user.id,)).fetchone()
       house = int(house[0])

       member = int(message.text.split()[2])

       if member == 1:
          house2 = 'Коробка'
          summ = 500000
          summ2 = '{:,}'.format(summ)
          member_house = 1


       if member == 2:
          house2 = 'Сарай'
          summ = 3000000
          summ2 = '{:,}'.format(summ)
          member_house = 2
      
       if member == 3:
          house2 = 'Маленький домик'
          summ = 5000000
          summ2 = '{:,}'.format(summ)
          member_house = 3
      
       if member == 4:
          house2 = 'Квартира'
          summ = 7000000
          summ2 = '{:,}'.format(summ)
          member_house = 4
      
       if member == 5:
          house2 = 'Огромный дом'
          summ = 10000000
          summ2 = '{:,}'.format(summ)
          member_house = 5

       if member == 6:
          house2 = 'Коттедж'
          summ = 50000000
          summ2 = '{:,}'.format(summ)
          member_house = 6

       if member == 7:
          house2 = 'Вилла'
          summ = 100000000
          summ2 = '{:,}'.format(summ)
          member_house = 7

       if member == 8:
          house2 = 'Загородный дом'
          summ = 5000000000
          summ2 = '{:,}'.format(summ)
          member_house = 8

       if house == 0:
          if member > 0:
             if member < 9:
                if summ <= balance:
                   await bot.send_message(message.chat.id, f"👨 |Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏡 | Действие: Покупка дома\n🏠 | Дом: {house2}\n💈 | Стоимость: {summ2}€", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE house SET house = {member_house} WHERE user_id = {user_id}')
                   connect.commit()
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, у вас нехватает средств!", parse_mode='html')               
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Нету такого номера дома!", parse_mode='html')
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Нету такого номера дома!", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас уже есть дом, что бы продать дом введите команду \"Продать дом\"", parse_mode='html')





    if message.text.lower() == 'дома':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, доступные дома:
🏠 1. Коробка - 500.000€
🏠 2. Сарай - 3.000.000€
🏠 3. Маленький домик - 5.000.000€
🏠 4. Квартира - 7.000.000€
🏠 5. Огромный дом - 10.000.000€
🏠 6. Коттедж - 50.000.000€
🏠 7. Вилла - 100.000.000€
🏠 8. Загородный дом - 5.000.000.000€

🛒 Для покупки дома введите "Купить дом [номер]"
       
       """, parse_mode='html')  
       
    if message.text.lower() in ["рп-команды", "РП-команды"]:
       user_name = message.from_user.get_mention(as_html=True)
       await bot.send_message(message.chat.id, f"{user_name}, список РП-команд:\n🤗 | Обнять\n👏 | Похлопать\n👨‍💻 | Заскамить\n☕️ | Пригласить на чай\n👉👌 | Изнасиловать\n🤝 | Взять за руку\n📱 | Подарить айфон\n✋ | Дать пять\n😬 | Укусить\n🤛 | Ударить\n🤲 | Прижать\n💋 | Чмок\n💋 | Поцеловать\n😼 | Кусь\n🤲 | Прижать\n🔪 | Убить\n🤜 | Уебать\n💰 | Украсть\n🔞 | Выебать\n👅 | Отсосать\n👅 | Отлизать\n🔞 | Трахнуть\n🔥 | Сжечь", parse_mode='html')

    if message.text.lower() in ["чмок", "Чмок"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} чмокнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["кусь", "Кусь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😼 | {user_name} кусьнул(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["обнять", "Обнять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤗 | {user_name} обнял(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["поцеловать", "Поцеловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💋 | {user_name} поцеловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["дать пять", "Дать пять"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"✋ | {user_name} дал(-а) пять {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["подарить айфон", "Подарить айфон"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"📱 | {user_name} подарил(-а) айфон {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["ударить", "Ударить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤛 | {user_name} ударил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["заскамить", "Заскамить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👨‍💻 | {user_name} заскамил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["укусить", "Укусить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"😬 | {user_name} укусил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["взять за руку", "Взять за руку"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤝 | {user_name} взял(-а) за руку {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["прижать", "Прижать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤲 | {user_name} прижал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["похлопать", "Похлопать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👏 | {user_name} похлопал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["изнасиловать", "Изнасиловать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👉👌 | {user_name} изнасиловал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["пригласить на чай", "Пригласить на чай"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"☕️ | {user_name} пригласил(-а) на чай {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["убить", "Убить"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔪 | {user_name} убил(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["уебать", "Уебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🤜 | {user_name} уебал(-а) {reply_user_name}", parse_mode='html')
    if message.text.lower() in ["украсть", "Украсть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"💰 | {user_name} украл(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отсосать", "Отсосать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отсосал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["отлизать", "Отлизать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"👅 | {user_name} отлизал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["выебать", "Выебать"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} выебал(-а) {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["сжечь", "Сжечь"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔥 | {user_name} сжёг {reply_user_name}", parse_mode='html')

    if message.text.lower() in ["трахнуть", "Трахнуть"]:
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply = message.reply_to_message
       if reply:
          replyuser = reply.from_user
          await bot.send_message(message.chat.id, f"🔞 | {user_name} трахнул(-а) {reply_user_name}", parse_mode='html')     
          #################################################### !канал ################################
    if message.text.lower() in ['канал', "!канал"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       channel_pov = cursor.execute("SELECT members from channel_pov where user_id = ?", (message.from_user.id,)).fetchone()
       channel_pov = int(channel_pov[0])

       if channel_pov > 0:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже получили деньги за подписку")
          return
       
       sub_pov = InlineKeyboardMarkup(row_width=1)
       channel_push = InlineKeyboardButton(text='КАНАЛ 🔈', url='https://t.me/LayDev')
       channel_poverk = InlineKeyboardButton(text='ПРОВЕРИТЬ ✅', callback_data='channel_poverk')
       sub_pov.add(channel_push, channel_poverk)

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>,, вот условия задание 💠

🔈 | Подписаться на канал

💰 | Приз: 500.000.000.000.000.000€

↘️ Виберите одну кнопку ниже...       
       """, reply_markup=sub_pov, parse_mode='html')
       user_channel_status = await bot.get_chat_member(chat_id="@LayDev", user_id=message.from_user.id)
       if user_channel_status['status'] != 'left':
          print('GOOD')
       else:
          print('Luser')
###########МАШИНЫ#######################################################
    if message.text.lower() == 'моя машина':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_Id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_Id = ?", (message.from_user.id,)).fetchone()
       cars = int(cars[0])

       hp = cursor.execute("SELECT hp from cars where user_Id = ?", (message.from_user.id,)).fetchone()
       hp = int(hp[0])

       benz = cursor.execute("SELECT benz from cars where user_Id = ?", (message.from_user.id,)).fetchone()
       benz = int(benz[0])
       if benz < 0:
             benz2 = 0
       else:
          benz2 = benz
       if cars == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       
       if hp in range(76,100):
          hp2 = 'Хорошое 🟩'

       if hp in range(51,75):
          hp2 = 'Среднее 🟧 '
         
       if hp in range(26,50):
          hp2 = 'Плохое 🟥'

       if hp in range(2,25):
          hp2 = 'Ужасное 🛑'

       if hp < 2:
          hp2 = 'Требуется ремонт ⛔️'

       else:
          if hp == 100:
             hp2 = 'Хорошое 🟩'
          if hp == 76:
             hp2 = 'Хорошое 🟩'
          if hp == 75:
             hp2 = 'Среднее 🟧'
          if hp == 51:
             hp2 = 'Среднее 🟧'
          if hp == 50:
             hp2 = 'Плохое 🟥'
          if hp == 26:
             hp2 = 'Плохое 🟥'
          if hp == 25:
             hp2 = 'Ужасное 🛑'
          if hp == 2:
             hp2 = 'Ужасное 🛑'

       if cars > 0:
          await bot.send_message(message.chat.id, f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные за ваш автомобиль🚘\n\n👤 | Владелец: {user_name}\n🚓 | Автомобиль: {cars_name}\n🚨 | Состояние: {hp2}\n⛽️ | Бензин: {benz2}%\n💰 | Стоимость: {cars_summ2}€\n\nℹ️ Чтобы продать машину введите команду \"Машину продать\"", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Подождите! У вас и так нету машины", parse_mode='html')
     


    if message.text.lower() == 'машину продать':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_Id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_Id = ?", (message.from_user.id,)).fetchone()
       cars = int(cars[0])

       if cars == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)


       if cars > 0:
          await bot.send_message(message.chat.id, f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🚗 |Действие: Продажа машины\n🚘 | Машина: {cars_name}\n💈 |Проданно за: {cars_summ2}€", parse_mode='html')
          cursor.execute(f'UPDATE cars SET cars = {0} WHERE user_id = {user_id}')
          cursor.execute(f'UPDATE cars SET hp = {0} WHERE user_id = {user_id}')
          cursor.execute(f'UPDATE cars SET benz = {0} WHERE user_id = {user_id}')
          connect.commit()
          return
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Подождите! У вас и так нету машины", parse_mode='html')
          return
      
    if message.text.startswith('Купить машину'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_Id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_Id = ?", (message.from_user.id,)).fetchone()
       cars = int(cars[0])

       member = int(message.text.split()[2])
       
       if member == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)


       if member > 0:
          if member < 19:
             if cars == 0:
                if balance >= cars_summ:
                   await bot.send_message(message.chat.id, f"🧑🏻‍🦱 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🚗 |Действие: Покупка машины\n🚘 | Машина: {cars_name}\n💈 |Стоимость: {cars_summ2}€", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - cars_summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE cars SET cars = {member} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE cars SET hp = {100} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE cars SET benz = {100} WHERE user_id = {user_id}')
                   connect.commit()
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств!", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! У вас уже есть машина", parse_mode='html')
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Подождите! Нету такого номера машины", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Подождите! Нету такого номера машины", parse_mode='html')

    if message.text.startswith('купить машину'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_Id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_Id = ?", (message.from_user.id,)).fetchone()
       cars = int(cars[0])

       member = int(message.text.split()[2])
       
       if member == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if member == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)


       if member > 0:
          if member < 19:
             if cars == 0:
                if balance >= cars_summ:
                   await bot.send_message(message.chat.id, f"👨 | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🚗 |Действие: Покупка машины\n🚘 | Машина: {cars_name}\n💈 |Стоимость: {cars_summ2}€", parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - cars_summ} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE cars SET cars = {member} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE cars SET hp = {100} WHERE user_id = {user_id}')
                   cursor.execute(f'UPDATE cars SET benz = {100} WHERE user_id = {user_id}')
                   connect.commit()
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, недостаточно средств!", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Ошибка! У вас уже есть машина", parse_mode='html')
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Подождите! Нету такого номера машины", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, Подождите! Нету такого номера машины", parse_mode='html')










    if message.text.lower() == 'машины':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, доступные машины:
🚗 1. Самокат - 10.000.000€
🚗 2. Велосипед - 15.000.000€
🚗 3. Гироскутер - 30.000.000€
🚗 4. Сегвей - 50.000.000€
🚗 5. Мопед - 90.000.000€
🚗 6. Мотоцикл - 100.000.000€
🚗 7. ВАЗ 2109 - 250.000.000€
🚗 8. Квадроцикл - 400.000.000€
🚗 9. Багги - 600.000.000€
🚗 10. Вездеход - 900.000.000€
🚗 11. Лада Xray - 1.400.000.000€
🚗 12. Audi Q7 - 2.500.000.000€
🚗 13. BMW X6 - 6.000.000.000€
🚗 14. Toyota FT-HS - 8.000.000.000€
🚗 15. BMW Z4 M - 10.000.000.000€
🚗 16. Subaru WRX STI - 40.000.000.000€
🚗 17. Lamborghini Veneno - 100.000.000.000€
🚗 18. Tesla Roadster - 300.000.000.000€

🛒 Для покупки машины введите "Купить машину [номер]"    
       
""", parse_mode='html')
            
#######################################ГОНКА###############
    if message.text.startswith('гонка'):

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       loser = ['😐', '😕','😟','😔','😓']
       rloser = random.choice(loser)

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_id = ?", (message.from_user.id,)).fetchone()
       cars = cars[0]

       hp = cursor.execute("SELECT hp from cars where user_id = ?", (message.from_user.id,)).fetchone()
       hp = int(hp[0])

       benz = cursor.execute("SELECT benz from cars where user_id = ?", (message.from_user.id,)).fetchone()
       benz = int(benz[0])

       summ = float(message.text.split()[1])
       summ2 = '{:,}'.format(summ)

       if cars == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)


       rx = random.randint(0,1000)
       rx2 = random.randint(1,25)
       summ3 = summ * 2
       summ4 = '{:,}'.format(summ3)

       period = 5
       getе = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(getе[0])
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if summ <= balance:
             if cars > 0:
                if hp > 0:
                   if benz > 0:
                      if int(rx) in range(0,600):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}€\n🧾 | Выигрыш: 0€", parse_mode='html')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                      if int(rx) in range(601, 1000):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}€\n🧾 | Выигрыш: {summ4}€", parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance + summ * 2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                   else:
                      await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас закончился бензин в автомобиле", parse_mode='html')
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас поломался автомобиль , вы не можете участвовать в гонках", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Какие гонки без автомобиля? Купите автомобиль", parse_mode='html') 
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас нехватает средств", parse_mode='html') 
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! играй можно раз в {period} секунд", parse_mode='html') 


    if message.text.startswith('Гонка'):

       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id
       
       loser = ['😐', '😕','😟','😔','😓']
       rloser = random.choice(loser)

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       cars = cursor.execute("SELECT cars from cars where user_id = ?", (message.from_user.id,)).fetchone()
       cars = cars[0]

       hp = cursor.execute("SELECT hp from cars where user_id = ?", (message.from_user.id,)).fetchone()
       hp = int(hp[0])

       benz = cursor.execute("SELECT benz from cars where user_id = ?", (message.from_user.id,)).fetchone()
       benz = int(benz[0])

       summ = float(message.text.split()[1])
       summ2 = '{:,}'.format(summ)

       if cars == 1:
          cars_name = 'Самокат'
          cars_summ = 10000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 2:
          cars_name = 'Велосипед'
          cars_summ = 15000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 3:
          cars_name = 'Гироскутер'
          cars_summ = 30000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 4:
          cars_name = 'Сегвей'
          cars_summ = 50000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 5:
          cars_name = 'Мопед'
          cars_summ = 90000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 6:
          cars_name = 'Мотоцикл'
          cars_summ = 100000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 7:
          cars_name = 'ВАЗ 2109'
          cars_summ = 250000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 8:
          cars_name = 'Квадроцикл'
          cars_summ = 400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 9:
          cars_name = 'Багги'
          cars_summ = 600000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 10:
          cars_name = 'Вездеход'
          cars_summ = 900000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 11:
          cars_name = 'Лада Xray'
          cars_summ = 1400000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 12:
          cars_name = 'Audi Q7'
          cars_summ = 2500000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 13:
          cars_name = 'BMW X6'
          cars_summ = 6000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 14:
          cars_name = 'Toyota FT-HS'
          cars_summ = 8000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 15:
          cars_name = 'BMW Z4 M'
          cars_summ = 10000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 16:
          cars_name = 'Subaru WRX STI'
          cars_summ = 40000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 17:
          cars_name = 'Lamborghini Veneno'
          cars_summ = 100000000000
          cars_summ2 = '{:,}'.format(cars_summ)
       if cars == 18:
          cars_name = 'Tesla Roadster'
          cars_summ = 300000000000
          cars_summ2 = '{:,}'.format(cars_summ)


       rx = random.randint(0,1000)
       rx2 = random.randint(1,25)
       summ3 = summ * 2
       summ4 = '{:,}'.format(summ3)

       period = 5
       getе = cursor.execute("SELECT stavka_games FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(getе[0])
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if summ <= balance:
             if cars > 0:
                if hp > 0:
                   if benz > 0:
                      if int(rx) in range(0,600):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}€\n🧾 | Выигрыш: 0€", parse_mode='html')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                      if int(rx) in range(601, 1000):
                         await bot.send_message(message.chat.id, f"🤵‍♂️ | Игрок: <a href='tg://user?id={user_id}'>{user_name}</a>\n🏎 | Игра: Гонки\n🚘 | Машина: {cars_name}\n🎟 | Ставка: {summ2}€\n🧾 | Выигрыш: {summ4}€", parse_mode='html')
                         cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE users SET balance = {balance + summ * 2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET hp = {hp - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE cars SET benz = {benz - rx2} WHERE user_id = {user_id}')
                         cursor.execute(f'UPDATE bot_time SET stavka_games = {time.time()} WHERE user_id = {user_id}')
                         connect.commit()
                   else:
                      await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас закончился бензин в автомобиле", parse_mode='html')
                else:
                   await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас поломался автомобиль , вы не можете участвовать в гонках", parse_mode='html')
             else:
                await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! Какие гонки без автомобиля? Купите автомобиль", parse_mode='html') 
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! У вас нехватает средств", parse_mode='html') 
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, подождите! играй можно раз в {period} секунд", parse_mode='html') 
          
###ССЫЛКИ###########          
    if message.text.lower() in ["Ссылки", "ссылки"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        rx = random.randint(0,100)
        await bot.send_message(message.chat.id, f'{rwin} {user_name} Вот официальные ссылки бота -\n\n💬Чат: @LayGame\n📊Канал: @LayDev\n🧑‍💻Разработчик: @XennuKinDer', parse_mode='html')     
###################################### аватарки #######################################
    if message.text.lower() in ['убрать аву', "убрать аватарку", "удалить аву", "удалить аватарку"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0]) 

       await bot.send_message(message.chat.id, f"🪣 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно удалили свою аватарку", parse_mode='html')
       cursor.execute(f'UPDATE avatarka SET avatarka = "none" WHERE user_id = {user_id}')
       connect.commit()


    if message.text.lower() in ['ава', 'аватарки', "аватарка", "фото"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       strach_photo = open('страж.jpg', 'rb')

       cheat_photo = open('cheat.jpg', 'rb')

       apper_photo = open('apper.jpg', 'rb')

       dyp_photo = open('дюп.jpg', 'rb')

       girl_photo = open('girl.jpg', 'rb')

       admin_photo = open('админ.jpg', 'rb')

       ava_strach = InlineKeyboardMarkup(row_width=1)
       ava_strach2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_strach')
       ava_strach.add(ava_strach2)

       ava_cheat = InlineKeyboardMarkup(row_width=1)
       ava_cheat2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_cheat')
       ava_cheat.add(ava_cheat2)

       ava_apper = InlineKeyboardMarkup(row_width=1)
       ava_apper2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_apper')
       ava_apper.add(ava_apper2)

       ava_dyp = InlineKeyboardMarkup(row_width=1)
       ava_dyp2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_dyp')
       ava_dyp.add(ava_dyp2)

       ava_girl = InlineKeyboardMarkup(row_width=1)
       ava_girl2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_girl')
       ava_girl.add(ava_girl2)

       ava_admin = InlineKeyboardMarkup(row_width=1)
       ava_admin2 = InlineKeyboardButton(text='ПОСТАВИТЬ 🖼', callback_data='ava_admin')
       ava_admin.add(ava_admin2)

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, добро пожаловать в меню аватарок 🗾

ℹ️ | Всего аватарок: 4

ℹ️ | Доступные аватарки: ДЮППЕР, СТРАЖ, АППЕР, ЧИТЕР, ДЕВУШКА

⛔️ | Админ: АДМИН

ℹ️ | Аватарка ставиться на баланс

↘️ | Виберите одну аватарок ниже 
       """, parse_mode='html')
       await bot.send_photo(message.chat.id, strach_photo, '', reply_markup=ava_strach)
       await bot.send_photo(message.chat.id, cheat_photo, '', reply_markup=ava_cheat)
       await bot.send_photo(message.chat.id, apper_photo, '', reply_markup=ava_apper)
       await bot.send_photo(message.chat.id, dyp_photo, '', reply_markup=ava_dyp)
       await bot.send_photo(message.chat.id, girl_photo, '', reply_markup=ava_girl)
       await bot.send_photo(message.chat.id, admin_photo, '', reply_markup=ava_admin)         
#############ШАНС#############################################
    if message.text.lower() in ["Шанс", "шанс"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        rx = random.randint(0,100)
        await bot.send_message(message.chat.id, f'🔮 | {user_name}, шанс этого: {rx}%', parse_mode='html')
    if message.text.lower() in ["Шансы", "шансы"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        await bot.send_message(message.chat.id,f'🔮 {user_name}, Вот так правильно пользоваться командой\n\nℹ️ Отвечаем сообщением командой (шанс)', parse_mode='html')
###########################################ОСТОЛЬНОЕ###########################################
    if message.text.lower() in ["Остальное", "остальное"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        win = ['🙂', '😋', '👊', '🤑', '😌']
        rwin = random.choice(win)
        await bot.send_message(message.chat.id,
                               f'⚠️  {user_name}, Вот все команды по пункту  остальное, {rwin} \n🎯 Шанс - узнать шанс казино,\n🎰 Шансы - узнать полную информацию о команде "шанс"\n🧑‍💻 Правила - узнать особенные правила бота\n 🌪 Ссылки - узнать список проверенных и официальных ссылок бота\n 💰 Донат - информация по поводу доната',
                               parse_mode='html')

###########################################ПОМОЩЬ###########################################
    if message.text.lower() in ["помощь", "Помощь"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       help2 = InlineKeyboardMarkup(row_width=2)
       Osn2 = InlineKeyboardButton(text='Основные 📝', callback_data='Osn2')
       game2 = InlineKeyboardButton(text='Игры 🎮', callback_data='game2')
       rabot2 = InlineKeyboardButton(text='Работы 🔨', callback_data='rabot2')
       Im2 = InlineKeyboardButton(text='Имущество 🏘 ', callback_data='Im2')
       Priv2 = InlineKeyboardButton(text='Привилегии 📖', callback_data='Priv2')
       Adm2 = InlineKeyboardButton(text='Admins menu ⛔️', callback_data='Admins_menu_up')
       help2.add(Osn2, game2, rabot2, Im2, Priv2, Adm2)
       await bot.send_message(message.chat.id, f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, виберите категории🔍

📝 | Основные
🎮 | Игры 
🔨 | Работы
🏘 | Имущество
📖 | Привилегии
⛔️ | Admins menu 

Разработчик: @XennuKinDer💻
Наша беседа: <tg-spoiler>@LayGame</tg-spoiler> 💬 
Наша беседа: <tg-spoiler>@LayGame2</tg-spoiler> 💬 
    ''', reply_markup=help2, parse_mode='html')

###########################################ПРАВИЛА###########################################
    if message.text.lower() in ["Правила", "правила"]:
       await bot.send_message(message.chat.id, f"""
🤬 | 1. Оскорбление [Мут - 15 минут ]
🤬 | 1.1 Оскорбление друзей личности [Мут - 10 минут]
🤬 | 1.2 Оскорбление родителем/родственников [Мут - 2 часа] + [ Варн ]
🤬 | 1.3 Оскорбление администрации [Мут - от 2 до 5 часов ] + [ Варн ]
🤬 | 1.4 Провокация на оскорбление [Мут - 5 минут]
🔞 | 2. Порнография в любом виде [Мут - 5 минут]
🔞 | 2.1 Спам контента порнографии [ Мут - 15 минут ]
🚷 | 3. Обман игроков [ Бан - 1 день ] + [ Варн ]
⛔️ | 4. Продажа игровой валюты [ Бан - 7 дней ] + [ Варн ] + [ Обнуление ]
⛔️ | 4.1 Продажа "Схем заработка" [Бан - 3 дня ] + [ Варн ]
⚠️ | 5. Капс (ПРИМЕР) [ Мут - 1 минута ]
⚠️ | 5.1 Флуд , спам [ Мут - 15 минут ]
⚠️ | 5.2 Не соглашёная реклама [ Мут - 1 час ] 
🆘 | 6. Любые действия связанные с вредом проекту [ Бан - 1 день ] + [ Варн ] [Если вред был нанесён тогда чс проекта ]
🆘 | 6.1 Читерство/Дюпинг в боте [ Обнуление ] + [ Варн ]      
       """, parse_mode='html')                               
###########################################АДМИН КОМАНДЫ###########################################
    if message.text.startswith("выдать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"📖 | {user_name} Вы выдали {perevod2}€ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"📖 | {user_name} Вы выдали {perevod2}€ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("Выдать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы выдали {perevod2}€ Игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы выдали {perevod2}€ игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("забрать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы забрали {perevod2}€ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы забрали {perevod2}€ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.startswith("Забрать"):
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы забрали {perevod2}€ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"💰 | Вы забрали {perevod2}€ у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 - perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')  

    if message.text.lower() in ["обнулить", "Обнулить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status[0] == 'Admin':
          await message.reply(f"💰 | Вы обнулили игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Owner':
          await message.reply(f"📖 | {user_name} Вы обнулили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a> {rwin}", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.lower() in ["забанить", "Забанить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Blocked"
       if user_status2[0] == "Admin":
          await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы забанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET bank = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET rating = {0} WHERE user_id = "{reply_user_id}"')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')

    if message.text.lower() in ["повысить", "Повысить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Admin"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы выдали админа бота игроку: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
    
    if message.text.lower() in ["разжаловать", "Разжаловать"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = "Player"
       if user_status2[0] == "Owner":
          await message.reply(f"🛑 | Вы забрали админа бота у игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       if user_status2[0] == 'Admin':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь создателем бота!", parse_mode='html')
       
    if message.text.lower() in ["разбанить", "Разбанить"]:
       msg = message
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = reply_user_name[0]
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       reply_user_id = msg.reply_to_message.from_user.id
       user_id = msg.from_user.id
       user_status = "Player"
       user_status2 = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       if user_status2[0] == "Admin":
          await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == "Owner":
          await message.reply(f"✅ | Вы разбанили игрока: <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = \"{user_status}\" WHERE user_id = "{reply_user_id}"')
          connect.commit()
       if user_status2[0] == 'Player':
          await message.reply(f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не являетесь администратором бота!", parse_mode='html')
###########################################БАНК###########################################
    # bank
    if message.text.startswith("банк положить"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_p = int(msg.text.split()[2])
       print(f"{name} положил в банк: {bank_p}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_p)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if bank_p > 0:
          if balance >= bank_p:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили в банк {bank2}€ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя положить в банк отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("банк снять"):
       msg = message
       chat_id = message.chat.id
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_s = int(msg.text.split()[2])
       print(f"{name} снял с банка: {bank_s}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_s)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       if bank_s > 0:
          if bank >= bank_s:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно сняли с банковского счёта {bank2}€ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств на банковском счету! {rloser}', parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя снять с банка отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("+банк"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       name = msg.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)

       bank_p = int(msg.text.split()[1])
       print(f"{name} положил в банк: {bank_p}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_p)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if bank_p > 0:
          if balance >= bank_p:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно положили в банк {bank2}€ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - bank_p} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET bank = {bank + bank_p} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(balance) < int(bank_p):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if bank_p <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя положить в банк отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("-банк"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)

       bank_s = int(msg.text.split()[1])
       print(f"{name} снял с банка: {bank_s}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       bank = cursor.execute("SELECT bank from users where user_id = ?", (message.from_user.id,)).fetchone()
       bank = round(int(bank[0]))
       bank2 = '{:,}'.format(bank_s)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       if bank_s > 0:
          if bank >= bank_s:  
             await bot.send_message(message.chat.id, f'{user_name}, вы успешно сняли с банковского счёта {bank2}€ {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET bank = {bank - bank_s} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance + bank_s} WHERE user_id = "{user_id}"') 
             connect.commit()    
   
          elif int(bank) < int(bank_s):
             await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств на банковском счету! {rloser}', parse_mode='html')

       if bank_s <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя снять с банка отрицательное число! {rloser}', parse_mode='html')  

###########################################АДМИН КОМАНДЫ###########################################
    if message.text.startswith("выдать"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Helper_Admin':
          await message.reply(f'👨 | Игрок: {user_name}\n⚙️ | Действие: Выдача денег\n💈 | Сумма: {perevod2}€\n👨 | Игроку: {reply_user_name}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')  

    if message.text.startswith("Выдать"):
       msg = message
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       perevod = int(msg.text.split()[1])
       reply_user_id = msg.reply_to_message.from_user.id
       perevod2 = '{:,}'.format(perevod)
       user_id = msg.from_user.id
       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])
       if user_status[0] == 'Helper_Admin':
          await message.reply(f'👨 | Игрок: {user_name}\n⚙️ | Действие: Выдача денег\n💈 | Сумма: {perevod2}€\n👨 | Игроку: {reply_user_name}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
          connect.commit() 
       if user_status[0] == 'Player':
          await message.reply(f'ℹ️ | {user_name}, вы не являетесь администратором бота!', parse_mode='html')       
       
# nick
    if message.text.lower() in ["ник", "Ник"]:
       msg = message 
       chat_id = message.chat.id
       user_name = msg.from_user.full_name
       await bot.send_message(message.chat.id, f"🤝 Ваш ник - {user_name}")    

###################################### КИТ-БОНУСЫ ##################################################
    if message.text.lower() == 'получить кит бонус':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       user_status = cursor.execute('SELECT user_status from users where user_id = ?', (message.from_user.id,)).fetchone()
       user_status = user_status[0]

       balance = cursor.execute('SELECT balance from users where user_id = ?', (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       rating = cursor.execute('SELECT rating from users where user_id = ?', (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       period = 43200 #43200 s = 12h
       get = cursor.execute("SELECT time_kit FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if user_status == 'Player':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1,000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 5,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 5000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 5000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return         
          if user_status == 'vip':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 50.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 15,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 50000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 15} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 0} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'apper':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 100,000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 50,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 100000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 50000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'donater':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 500,000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 500000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return

          if user_status == 'donater2':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1,000.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 5,000,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 5000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, администрация бота не может получать кит-бонус", parse_mode='html') 
             return   
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, получать кит-бонус можно раз в 12ч", parse_mode='html')   
    if message.text.lower() == 'Получить кит бонус':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       user_status = cursor.execute('SELECT user_status from users where user_id = ?', (message.from_user.id,)).fetchone()
       user_status = user_status[0]

       balance = cursor.execute('SELECT balance from users where user_id = ?', (message.from_user.id,)).fetchone()
       balance = int(balance[0])

       rating = cursor.execute('SELECT rating from users where user_id = ?', (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       period = 43200 #43200 s = 12h
       get = cursor.execute("SELECT time_kit FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if user_status == 'Player':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1,000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 5,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 5000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 5000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return         
          if user_status == 'vip':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 50.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 15,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 50000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE mine SET gold = {gold + 15} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET ethereum = {ethereum + 0} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'apper':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 100,000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 50,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 100000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 50000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          if user_status == 'donater':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 500,000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 500,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 500000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 500000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return

          if user_status == 'donater2':
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 1,000.000,000,000,000,000$", parse_mode='html')
             time.sleep(0.2)
             await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили 💎 5,000,000 шт.", parse_mode='html')
             time.sleep(0.2)
             cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE users SET rating = {rating + 5000000} WHERE user_id = {user_id}')
             cursor.execute(f'UPDATE bot_time SET time_kit = {time.time()} WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, администрация бота не может получать кит-бонус", parse_mode='html') 
             return   
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, получать кит-бонус можно раз в 12ч", parse_mode='html')   
                        
    if message.text.lower() in ['кит-бонусы', 'кит бонусы', 'кит бонус', 'кит-бонус']:
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id 

       await bot.send_message(message.chat.id, f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот данные о кит-бонусах 🎁

🎀 | Игрок:
      💰 | 1,000,000,000,000,000€
      💎 | 5.000 шт.

👑 | VIP+
      💰 | 50,000,000,000,000,000€
      💎 | 15,000 шт.

🎁 | МегаАппер:
      💰 | 100.000,000,000,000,000€
      💎 |  100,000 шт.
      
💵 | Донатер:
      💰 | 500.000,000,000,000,000$
      💎 |  500,000 шт.
      
💎 | МегаДонатер:
      💰 | 1.000.000,000,000,000,000€
      💎 |  5,000,000 шт.

ℹ️ Чтобы получить кит-бонус введите команду \"Получить кит-бонус\" 
ℹ️ Кит-бонус получить можно раз в 12ч      
       """, parse_mode='html')

###########################################ДОНАТ###########################################
    if message.text.lower() in ["донат", "Донат"]:
       msg = message 
       chat_id = message.chat.id
       user_name = msg.from_user.full_name
       await bot.send_message(message.chat.id, f'🧑‍⚖ | {user_name}, Вы открыли панель донат\n1⃣ | VIP+👑 | Можно выиграть в розыгрыше❗\n2⃣ | МегаАппер🎁 | Можно получить если вы были 15 раз топ 1 по балансу | предоставьте 15 фото где вы топ 1 | \n3⃣ | Донатер💵 | Можно получить если вы задонатили больше 50р | Получите больше чем (вип, аппер,)+ Смайлик в прификс что вы донатер |\n4⃣ | МегаДонатер💎 | Если вы задонатили больше 250р вы станете админам(группы) + у вас все Возможности Донатера💵, МегаАппера🎁, и VIP+👑. +иногда вам будет придоставляться админ(бота) с привилегри МегаДонатер можно менять префиксы| \n➖➖➖➖➖➖➖➖➖➖➖➖\n\n💶 | Курс Игровой валюты | курс игровой валюты меняется так что пишите | @XennuKinDer или ждите  пока будет пост и курсом\n❓| Есть вопросы пишите разработчику \n❕| Есть идея что добавить пишите разработчику', parse_mode='html')
              
########################################################БОНУСЫ##########################################################
    if message.text.lower() in ['Работать', "работать"]:
        msg = message
        user_name = message.from_user.get_mention(as_html=True)
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))

        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)

        user_id = msg.from_user.id
        user_status = cursor.execute("SELECT user_status from users where user_id = ?",
                                     (message.from_user.id,)).fetchone()

        period = 86400
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if user_status[0] == 'Owner':
                await message.reply(f'{user_name} 🛠 Вы поработали шахтером и заработали: 1.000.000.000.000€{rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 1000000000000} WHERE user_id = "{user_id}"')
                connect.commit()
            if user_status[0] == 'Zam':
                await message.reply(f'{user_name}🔦 | Ты поработал(а) охранником и заработал(а): 100.000.000.000.000€{rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 100000000000000} WHERE user_id = "{user_id}"')
                connect.commit()

            if user_status[0] == 'Admin':
                await message.reply(f'{user_name} 🏎 Вы починили машину директору автосалона и заработали: 500.000.000.000.000€ {rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 500000000000000} WHERE user_id = "{user_id}"')
                connect.commit()
            if user_status[0] == 'Player':
                await message.reply(f'🛢 {user_name}  Вы поработали на СТО и заработали: 500.0000.000€{rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance + 500000000} WHERE user_id = "{user_id}"')
                connect.commit()
        else:
            await bot.send_message(message.chat.id,f'🔦 {user_name} Попробуйте чуть позже так как вы исчерпали свой лимит! {rloser}', parse_mode='html')
            ###########################################СПИН#############################################
    if message.text.startswith("спин"):
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        balance2 = '{:,}'.format(balance)
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id
        rx = random.randint(0, 105)
        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
        print(f"{name} поставил в спин: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        loz = ['💩|👑|👑', '💩|🖕|👑', '💎|🖕|👑', '💎|💣|🍌', '👑|🍌|🖕', '💎|🍓|💣']
        win = ['💎|🍓|🍌', '👑|💎|🍓', '🍓|👑|💎', '💎|🍓|🍌', '💎|🍓|🍓', '🍌|🍌|💎']
        Twin = ['💎|💎|💎', '🍓|🍓|🍓', '👑|👑|👑', '🍌|🍌|🍌']
        smtwin = ['🤯', '🤩', '😵', '🙀']
        smwin = ['🙂', '😋', '😄', '🤑', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rsmtwin = random.choice(smtwin)
        rsmtwin2 = random.choice(smtwin)
        rtwin = random.choice(Twin)
        rloser = random.choice(loser)
        rloser2 = random.choice(loser)
        rwin = random.choice(win)
        rloz = random.choice(loz)
        rsmwin = random.choice(smwin)
        rsmwin2 = random.choice(smwin)
        if balance >= 999999999999999999999999:
            balance = 999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(80, 100):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rwin} - вы выиграли {c2}€{rsmwin}\n——————\nПозравляю вас!{rsmwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return

        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 70):
                        c = Decimal(summ * 0)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rloz} - вы проиграли {c2}€{rloser}\n——————\nПриймите мои соболезнования!{rloser2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 0)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(101, 103):
                        c = Decimal(summ * 25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rtwin} - ДЖЕКПОТ, ВЫ ВЫИГРАЛИ {c2}€{rsmtwin}\n——————\nПОЗДРАВЛЯЮ У ВАС ДЖЕКПОТ!{rsmtwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("Спин"):
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])
        balance2 = '{:,}'.format(balance)
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id
        rx = random.randint(0, 105)
        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
        print(f"{name} поставил в спин: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        loz = ['💩|👑|👑', '💩|🖕|👑', '💎|🖕|👑', '💎|💣|🍌', '👑|🍌|🖕', '💎|🍓|💣']
        win = ['💎|🍓|🍌', '👑|💎|🍓', '🍓|👑|💎', '💎|🍓|🍌', '💎|🍓|🍓', '🍌|🍌|💎']
        Twin = ['💎|💎|💎', '🍓|🍓|🍓', '👑|👑|👑', '🍌|🍌|🍌']
        smtwin = ['🤯', '🤩', '😵', '🙀']
        smwin = ['🙂', '😋', '😄', '🤑', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rsmtwin = random.choice(smtwin)
        rsmtwin2 = random.choice(smtwin)
        rtwin = random.choice(Twin)
        rloser = random.choice(loser)
        rloser2 = random.choice(loser)
        rwin = random.choice(win)
        rloz = random.choice(loz)
        rsmwin = random.choice(smwin)
        rsmwin2 = random.choice(smwin)
        if balance >= 999999999999999999999999:
            balance = 999999999999999999999999
            cursor.execute(f'UPDATE users SET balance = {999999999999999999999999}  WHERE user_id = ?', (user_id,))
            connect.commit()
            balance2 = '{:,}'.format(balance)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(80, 100):
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rwin} - вы выиграли {c2}€{rsmwin}\n——————\nПозравляю вас!{rsmwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return

        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(0, 70):
                        c = Decimal(summ * 0)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rloz} - вы проиграли {c2}€{rloser}\n——————\nПриймите мои соболезнования!{rloser2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 0)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if int(rx) in range(101, 103):
                        c = Decimal(summ * 25)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id,
                                               f'{name1}, вот ваши результаты\n——————\n{rtwin} - ДЖЕКПОТ, ВЫ ВЫИГРАЛИ {c2}€{rsmtwin}\n——————\nПОЗДРАВЛЯЮ У ВАС ДЖЕКПОТ!{rsmtwin2}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 25)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
# Смена имени
    if message.text.startswith('Сменить ник'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       user_id = message.from_user.id
       name = " ".join(message.text.split()[2:])

       if len(name) <= 20:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно поменяли свое имя на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_name = \"{name}\" WHERE user_id = "{user_id}"')
          print(f"{user_name} сменил ник на {name}")
       else: 
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a> , ваш ник не может быть длинее 20 символов!", parse_mode='html')
    if message.text.startswith('сменить ник'):
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       chat_id = message.chat.id
       user_id = message.from_user.id
       name = " ".join(message.text.split()[2:])
       if len(name) <= 20:
          await bot.send_message(message.chat.id, f"✏️ | <a href='tg://user?id={user_id}'>{user_name}</a> , вы успешно поменяли свое имя на: {name}!", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_name = \"{name}\" WHERE user_id = "{user_id}"')
          print(f"{user_name} сменил ник на {name}")
       else: 
          await bot.send_message(message.chat.id, f"ℹ️ | <a href='tg://user?id={user_id}'>{user_name}</a> , ваш ник не может быть длинее 20 символов!", parse_mode='html')
 
    if message.text.startswith('cменить префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[2:])
       if len(prefix) <= 20:
          if user_status in ['donater2', 'Admin', 'Helper_Admin', 'Owner']:
             await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили свой префикс на {prefix}")
             cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"МегаДонатер\"", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return

    if message.text.startswith('Сменить префикс'):
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = str(user_status[0])

       prefix = ' '.join(message.text.split()[2:])
       if len(prefix) <= 20:
          if user_status in ['donater2', 'Admin', 'Helper_Admin', 'Owner']:
             await bot.send_message(message.chat.id, f"🔒 | Вы успешно сменили свой префикс на {prefix}")
             cursor.execute(f'UPDATE users SET pref = "{prefix}" WHERE user_id = {user_id}')
             connect.commit()
             return
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, менять префикс можно только от привилегии \"МегаДонатер\"", parse_mode='html')
             return
       else:
          await bot.send_message(message.chat.id, f"🆘 | Игрок, менять префикс не может быть более 20 символов!", parse_mode='html')
          return    
#Ограбить банк
    if message.text.lower() == 'ограбить банк':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       
       x = random.randint(1,3)
       period = 86400 #86400 s 24h
       get = cursor.execute("SELECT stavka_bank FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(get[0])
       stavkatime = time.time() - float(last_stavka)
       rx = random.randint(1000000,25000000)
       rx2 = '{:,}'.format(rx)
       if stavkatime > period:
          if int(x) in range(2,3):
             await bot.send_message(message.chat.id, f"🏦 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно ограбили банк на {rx2}€✅", parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance + rx} WHERE user_id ="{user_id}"')
             cursor.execute(f'UPDATE bot_time SET stavka_bank = {time.time()} WHERE user_id = "{user_id}"')
             connect.commit()
          else:
             await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, вам не удалось ограбить банк", parse_mode='html')
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, ограбить банк можно раз в 24ч⏳", parse_mode='html')
# bonus 24h
    
    
    if message.text.lower() == 'ежедневный бонус':
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = user_name[0]
       user_id = message.from_user.id

       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       period = 86400 #86400 s = 24h
       get = cursor.execute("SELECT stavka_bonus FROM bot_time WHERE user_id = ?", (message.from_user.id,)).fetchone()
       last_stavka = int(get[0])
       stavkatime = time.time() - float(last_stavka)
       
       rx = random.randint(1000000000,250000000000)
       rx2 = '{:,}'.format(rx)

       if stavkatime > period:
          await bot.send_message(message.chat.id, f"🎁 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили ежедневный бонус в сумме {rx2}€ 💵", parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + rx}  WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE bot_time SET stavka_bonus = {time.time()} WHERE user_id = "{user_id}"')
          connect.commit()
       else:
          await bot.send_message(message.chat.id, f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, получать ежедневный бонус можно раз в 24ч⏳", parse_mode='html')           
###########################################ЧЁТНОЕ\НЕ ЧЁТНОЕ#################################
    if message.text.startswith("Нечётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        print(f"{name} поставил на нечётное: {summ} и выпало: {rkyb}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}€ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}€ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("нечётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
        print(f"{name} поставил на нечётное: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}€ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}€ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("чётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
        print(f"{name} поставил на Чётное: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}€ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}€ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return
    if message.text.startswith("Чётное"):
        msg = message
        user_id = msg.from_user.id
        chat_id = message.chat.id

        win = ['🙂', '😋', '😄', '😃']
        loser = ['😔', '😕', '😣', '😞', '😢']
        rx = random.randint(0, 120)
        rwin = random.choice(win)
        rwin2 = random.choice(win)
        rloser = random.choice(loser)

        msg = message
        name1 = message.from_user.get_mention(as_html=True)
        name = msg.from_user.last_name
        summ = float(msg.text.split()[1])
        print(f"{name} поставил на Чётное: {summ} и выиграл/проиграл: {rx}")
        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = round(int(balance[0]))
        period = 5
        kyb = ['🎲1', '🎲2', '🎲3', '🎲4', '🎲5', '🎲6']
        rkyb = random.choice(kyb)
        get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
        last_stavka = f"{int(get[0])}"
        stavkatime = time.time() - float(last_stavka)
        if stavkatime > period:
            if balance >= summ:
                if summ > 0:
                    if rkyb in ['🎲2', '🎲4', '🎲6']:
                        c = Decimal(summ * 2)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы выиграли {c2}€ {rwin}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                    if rkyb in ['🎲1', '🎲3', '🎲5']:
                        c = Decimal(summ)
                        c2 = round(c)
                        c2 = '{:,}'.format(c2)
                        await bot.send_message(chat_id, f'{name1} , вам выпало: {rkyb}\nВы проиграли {c2}€ {rloser}',
                                               parse_mode='html')
                        cursor.execute(
                            f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                        cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                        connect.commit()
                        return
                elif summ <= 1:
                    await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}',
                                           parse_mode='html')
            elif int(balance) <= int(summ):
                await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
        else:
            await bot.send_message(chat_id, f'{name1}, извини. но играть можно только каждые 5️⃣ секунд. {rloser}',
                                   parse_mode='html')
            return                   
###########################################КАЗИНО###########################################
    if message.text.startswith("Казино"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,110)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       name = msg.from_user.last_name 
       summ = float(msg.text.split()[1])
       print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()   
                   return                           
                if int(rx) in range(10,29):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0.25) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return   
                if int(rx) in range(30,44):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0.5) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(45,54):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0.75) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(55,64):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}€ (x1) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()
                   return 
                if int(rx) in range(65,69):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x1.25) {rwin}', parse_mode='html')

                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()           
                   return 
                if int(rx) in range(70,74):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x1.5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(75,84):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x1.75) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(85,95):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x2) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) in range(100,108):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x3) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) == 109:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                if int(rx) == 108:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x10) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
             elif summ <= 1:
                  await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                      
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'{name1}, Играть можно каждые 5⃣ секунд {rloser}', parse_mode='html')
        return

    if message.text.startswith("казино"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id

       win = ['🙂', '😋', '😄', '🤑', '😃']
       loser = ['😔', '😕', '😣', '😞', '😢']
       rx = random.randint(0,110)
       rwin = random.choice(win)
       rloser = random.choice(loser)

       msg = message
       name1 = message.from_user.get_mention(as_html=True)
       name = msg.from_user.last_name 
       summ = float(msg.text.split()[1])
       print(f"{name} поставил в казино: {summ} и выиграл/проиграл: {rx}")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       period = 5
       get = cursor.execute("SELECT last_stavka FROM bot WHERE chat_id = ?", (message.chat.id,)).fetchone()
       last_stavka = f"{int(get[0])}"
       stavkatime = time.time() - float(last_stavka)
       if stavkatime > period:
          if balance >= summ:
             if summ > 0:
                if int(rx) in range(0,9):
                   c = Decimal(summ)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()   
                   return                           
                if int(rx) in range(10,29):
                   c = Decimal(summ - summ * 0.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0.25) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.75} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return   
                if int(rx) in range(30,44):
                   c = Decimal(summ * 0.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0.5) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.5} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(45,54):
                   c = Decimal(summ - summ * 0.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы проиграли {c2}€ (x0.75) {rloser}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {balance - summ * 0.25} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return  
                if int(rx) in range(55,64):
                   c = summ * 1
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, ваши деньги остаются при вас {c2}€ (x1) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()
                   return 
                if int(rx) in range(65,69):
                   c = Decimal(summ * 1.25)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x1.25) {rwin}', parse_mode='html')

                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.25)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()           
                   return 
                if int(rx) in range(70,74):
                   c = Decimal(summ * 1.5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x1.5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(75,84):
                   c = Decimal(summ * 1.75)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x1.75) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 1.75)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit()  
                   return 
                if int(rx) in range(85,95):
                   c = Decimal(summ * 2)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x2) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 2)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) in range(100,108):
                   c = Decimal(summ * 3)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x3) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 3)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
                if int(rx) == 109:
                   c = Decimal(summ * 5)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x5) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 5)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                if int(rx) == 108:
                   c = Decimal(summ * 10)
                   c2 = round(c)
                   c2 = '{:,}'.format(c2)
                   await bot.send_message(chat_id, f'{name1}, вы выиграли {c2}€ (x10) {rwin}', parse_mode='html')
                   cursor.execute(f'UPDATE users SET balance = {(balance - summ) + (summ * 10)} WHERE user_id = "{user_id}"')
                   cursor.execute(f'UPDATE bot SET last_stavka=? WHERE chat_id=?', (time.time(), chat_id,))
                   connect.commit() 
                   return 
             elif summ <= 1:
                  await bot.send_message(chat_id, f'{name1}, нельзя ставить отрицательное число! {rloser}', parse_mode='html')                                      
          elif int(balance) <= int(summ):
               await bot.send_message(chat_id, f'{name1}, недостаточно средств! {rloser}', parse_mode='html')
       else:
        await bot.send_message(chat_id, f'{name1}, Играть можно каждые 5⃣ секунд {rloser}', parse_mode='html')
        return

###########################################РЕЙТИНГ###########################################
    if message.text.lower() == 'забрать права':
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(reply_user_name[0])

       reply_user_id = msg.reply_to_message.from_user.id

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = user_status[0]

       if user_status == 'Owner':
          await message.reply(f"⛔️ | Разработчик: <a href='tg://user?id={user_id}'>{user_name}</a> забрал все права администрации у игрока <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = "Player" WHERE user_id = {reply_user_id}')
          connect.commit()

       else:
          await message.reply(f"🆘 | Данная команда доступна только администрации с уровнем \"OWNER\"")
    if message.text.lower() == 'передать права':
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(reply_user_name[0])

       reply_user_id = msg.reply_to_message.from_user.id

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = user_status[0]

       if user_status == 'Owner':
          await message.reply(f"⛔️ | Разработчик: <a href='tg://user?id={user_id}'>{user_name}</a> передал все права игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = "Owner" WHERE user_id = {reply_user_id}')
          connect.commit()

       else:
          await message.reply(f"🆘 | Данная команда доступна только администрации с уровнем \"OWNER\"")
    if message.text.lower() == 'выдать админа':
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])

       reply_user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.reply_to_message.from_user.id,)).fetchone()
       reply_user_name = str(reply_user_name[0])

       reply_user_id = msg.reply_to_message.from_user.id

       user_status = cursor.execute("SELECT user_status from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_status = user_status[0]

       if user_status == 'Owner':
          await message.reply(f"⛔️ | Разработчик: <a href='tg://user?id={user_id}'>{user_name}</a> выдал права администратора уровня \"ADMIN\" игроку <a href='tg://user?id={reply_user_id}'>{reply_user_name}</a>", parse_mode='html')
          cursor.execute(f'UPDATE users SET user_status = "Admin" WHERE user_id = {reply_user_id}')
          connect.commit()

       else:
          await message.reply(f"🆘 | Данная команда доступна только администрации с уровнем \"OWNER\"")
          
    if message.text.startswith("рейтинг купить"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = float(msg.text.split()[2])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       rating2 = '{:,}'.format(summ)
       c = summ * 150000000
       c2 = '{:,}'.format(c)
       if summ > 0:
        if int(balance) >= int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}€! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
          connect.commit()

 
        if int(balance) < int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if summ <= 0:
         await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')
    
    if message.text.startswith("рейтинг продать"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = float(msg.text.split()[2])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       c = summ * 100000000
       c2 = '{:,}'.format(c)
       rating2 = '{:,}'.format(summ)
       if summ > 0:
        if int(rating) >= int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}€! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
          connect.commit()

        if int(rating) < int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, у вас недостаточно рейтинга для его продажи! {rloser}', parse_mode='html')

       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}', parse_mode='html')

    if message.text.startswith("+рейтинг"):
       msg = message
       user_id = msg.from_user.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = float(msg.text.split()[1])
       chat_id = message.chat.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       rating2 = '{:,}'.format(summ)
       c = summ * 150000000
       c2 = '{:,}'.format(c)
       if summ > 0:
        if int(balance) >= int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, вы повысили количество вашего рейтинга на {rating2}👑 за {c2}€! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance - c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating + summ} WHERE user_id = "{user_id}"')
          connect.commit()

 
        if int(balance) < int(summ * 150000000):
          await bot.send_message(message.chat.id, f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if summ <= 0:
         await bot.send_message(message.chat.id, f'{user_name}, нельзя купить отрицательное число! {rloser}', parse_mode='html')
    
    if message.text.startswith("-рейтинг"):
       msg = message
       user_id = msg.from_user.id
       chat_id = message.chat.id
       user_name = message.from_user.get_mention(as_html=True)
       summ = float(msg.text.split()[1])
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = int(balance[0])
       rating = cursor.execute("SELECT rating from users where user_id = ?", (message.from_user.id,)).fetchone()
       rating = int(rating[0])
       c = summ * 100000000
       c2 ='{:,}'.format(c)
       rating2 = '{:,}'.format(summ)
       if summ > 0:
        if int(rating) >= int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, вы понизили количество вашего рейтинга на {rating2}👑 за {c2}€! {rwin}', parse_mode='html')
          cursor.execute(f'UPDATE users SET balance = {balance + c} WHERE user_id = "{user_id}"')
          cursor.execute(f'UPDATE users SET rating = {rating - summ} WHERE user_id = "{user_id}"')
          connect.commit()
 
        if int(rating) < int(summ):
          await bot.send_message(message.chat.id, f'{user_name}, у вас недостаточно рейтинга для его продажи! {rloser}', parse_mode='html')

       if summ <= 0:
          await bot.send_message(message.chat.id, f'{user_name}, нельзя продать отрицательное число! {rloser}', parse_mode='html')
#######################################################ФАРМ###########################################################
    if message.text.lower() in ["суббота начать", "Суббота начать"]:
        msg = message
        chat_id = message.chat.id
        name1 = message.from_user.get_mention(as_html=True)
        user_name = msg.from_user.full_name
        user_id = msg.from_user.id

        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)


        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])

        await bot.send_message(message.chat.id, f"ℹ️ <a href='tg://user?id={user_id}'>{user_name}</a> Ище не наступила Суббота какой Заработок? Подождите!", parse_mode='html')
        cursor.execute(f'UPDATE users SET balance = {balance + 0} WHERE user_id = "{user_id}"')
        connect.commit() 
#######################################################КЛИК###########################################################
    if message.text.lower() in ["клик", "Клик"]:
        msg = message
        chat_id = message.chat.id
        name1 = message.from_user.get_mention(as_html=True)
        user_name = msg.from_user.full_name
        user_id = msg.from_user.id

        win = ['🙂', '😋', '😄', '🤑', '😃']
        rwin = random.choice(win)
        loser = ['😔', '😕', '😣', '😞', '😢']
        rloser = random.choice(loser)


        balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
        balance = int(balance[0])

        random_money = random.randint(50000000,60000000)
        random_money2 = '{:,}'.format(random_money)


        await bot.send_message(message.chat.id, f'{user_name}, вы получили {random_money2}€ {rwin}')
        cursor.execute(f'UPDATE users SET balance = {balance + random_money} WHERE user_id = "{user_id}"')
        connect.commit()        
###########################################ТОП###########################################
    if message.text.lower() in ["топ", "Топ"]:
       list = cursor.execute(f"SELECT * FROM users ORDER BY rating DESC").fetchmany(10)
       top_list = []
       chat_id = message.chat.id
       name = message.from_user.get_mention(as_html=True)
       num = 0
       for user in list:
           if user[5] >= 999999999999999999999999:
              c6 = 999999999999999999999999
           else:
              c6 = user[5]

           if int(user[1]) < 0:
              balance3 = 0
           if int(user[1]) in range(1000, 999999):
              balance1 = user[1] / 1000
              balance2 = round(balance1)
              balance3 = f'{balance2} тыс'

           if int(user[1]) in range(1000000, 999999999):
              balance1 = user[1] / 1000000
              balance2 = round(balance1)
              balance3 = f'{balance2} млн'

           if int(user[1]) in range(1000000000, 999999999999):
              balance1 = user[1] / 1000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} млрд'

           if int(user[1]) in range(1000000000000, 999999999999999):
              balance1 = user[1] / 1000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} трлн'

           if int(user[1]) in range(1000000000000000, 999999999999999999):
              balance1 = user[1] / 1000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} квдр'

           if int(user[1]) in range(1000000000000000000, 999999999999999999999):
              balance1 = user[1] / 1000000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} квнт'

           if int(user[1]) in range(1000000000000000000000, 999999999999999999999999):
              balance1 = user[1] / 1000000000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} скст'
           if int(user[1]) in range(1000000000000000000000000000, 999999999999999999999999999):
              balance1 = user[1] / 10000000000000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} септ'
           if int(user[1]) in range(1000000000000000000000000000, 999999999999999999999999999):
              balance1 = user[1] / 10000000000000000000000000
              balance2 = round(balance1)
              balance3 = f'{balance2} окт'
           num += 1
           c = Decimal(c6)
           c2 = '{:,}'.format(c)
           
           top_list.append(f"{num}. {user[3]}  — 💎{c2} | €{balance3}")
       top = "\n".join(top_list)
       await bot.send_message(message.chat.id, f"{name},Топ 10 игроков бота\n" + top, parse_mode='html')        
###########################################ПЕРЕВОДЫ###########################################
    if message.text.lower() in ["админ", "Админ"]:
       user_id = message.from_user.id
       user_name = cursor.execute("SELECT user_name from users where user_id = ?",(message.from_user.id,)).fetchone()
       user_name = str(user_name[0])
       admin_menu = InlineKeyboardMarkup(row_width=1)
       Admins_menu_up = InlineKeyboardButton(text='Выполнить вход❄️', callback_data='Admins_menu_up')
       admin_menu.add(Admins_menu_up)
       await bot.send_message(message.chat.id,f"ℹ️ <a href='tg://user?id={user_id}'>{user_name}</a>, Войдите в админ меню️", reply_markup=admin_menu, parse_mode='html')
       
    if message.text.startswith("передать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = float(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       if not message.reply_to_message:
          await message.reply("Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'Вы передали {perevod2}€ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("Передать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = float(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       if not message.reply_to_message:
          await message.reply("Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'Вы передали {perevod2}€ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("дать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = float(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       if not message.reply_to_message:
          await message.reply("Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'Вы передали {perevod2}€ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  

    if message.text.startswith("Дать"):
       msg = message
       user_id = msg.from_user.id
       name = msg.from_user.last_name 
       rname =  msg.reply_to_message.from_user.last_name 
       user_name = message.from_user.get_mention(as_html=True)
       reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
       reply_user_id = msg.reply_to_message.from_user.id
       win = ['🙂', '😋', '😄', '🤑', '😃']
       rwin = random.choice(win)
       loser = ['😔', '😕', '😣', '😞', '😢']
       rloser = random.choice(loser)

       perevod = float(msg.text.split()[1])
       perevod2 = '{:,}'.format(perevod)
       print(f"{name} перевел: {perevod} игроку {rname}")

       cursor.execute(f"SELECT user_id FROM users WHERE user_id = '{user_id}'")
       balance = cursor.execute("SELECT balance from users where user_id = ?", (message.from_user.id,)).fetchone()
       balance = round(int(balance[0]))
       balance2 = cursor.execute("SELECT balance from users where user_id = ?", (message.reply_to_message.from_user.id,)).fetchone()
       balance2 = round(balance2[0])

       if not message.reply_to_message:
          await message.reply("Эта команда должна быть ответом на сообщение!")
          return
       
       if reply_user_id == user_id:
          await message.reply_to_message.reply(f'Вы не можете передать деньги сами себе! {rloser}', parse_mode='html')
          return

       if perevod > 0:
          if balance >= perevod:  
             await message.reply_to_message.reply(f'Вы передали {perevod2}€ игроку {reply_user_name} {rwin}', parse_mode='html')
             cursor.execute(f'UPDATE users SET balance = {balance - perevod} WHERE user_id = "{user_id}"') 
             cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
             connect.commit()    
   
          elif int(balance) <= int(perevod):
             await message.reply( f'{user_name}, недостаточно средств! {rloser}', parse_mode='html')

       if perevod <= 0:
          await message.reply( f'{user_name}, нельзя перевести отрицательное число! {rloser}', parse_mode='html')  

@dp.callback_query_handler(text='admins_comands')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0]) 
    if user_status == 'Owner':
       commands = '''
1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /ban
6️⃣ | /unban
7️⃣ |Выдать админа
8️⃣ | Выдать хелпера
9️⃣ | Передать права
🔟 | Забрать права
1️⃣1️⃣ | Поделить [количество]

       '''
    if user_status == 'Helper_Admin':
       commands = '''
1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /ban
6️⃣ | /unban
7️⃣ | Поделить [количество]


       '''
    if user_status == 'Admin':
       commands = '''
1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
       '''
    if user_status == 'Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    if user_status == 'Helper_Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    if user_status == 'Owner':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/XennuKinDer/'>Xennu</a>  ⚠️", parse_mode='html')

@dp.callback_query_handler(text='stats222')
async def ob_Statisyik(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = user_status[0]
    
    sqlite_select_query2 = """SELECT * from users where user_status = \"Player\""""
    cursor.execute(sqlite_select_query2)
    records2 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Admin\""""
    cursor.execute(sqlite_select_query2)
    records2 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Helper_Admin\""""
    cursor.execute(sqlite_select_query2)
    records3 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Owner\""""
    cursor.execute(sqlite_select_query2)
    records4 = cursor.fetchall()

    if user_status == 'Owner':
       await callback.message.answer(f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот общая статистика бота 🔎

🔓 | Основная
         👤 | Игроков: {len(records)}

🛑 | Администрация
         ⛔️ | ADMIN: {len(records2)}
         ⚠️ | HELPER-ADMIN: {len(records3)}
         ✅ | OWNER: {len(records4)}        
       """, parse_mode='html')
    else:
       await callback.message.answer(f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, статистика бота доступна только от прав администратора \"HELPER-ADMINS\" ", parse_mode='html')


@dp.callback_query_handler(text='statistic')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Admin\""""
    cursor.execute(sqlite_select_query2)
    records2 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Helper_Admin\""""
    cursor.execute(sqlite_select_query2)
    records3 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Owner\""""
    cursor.execute(sqlite_select_query2)
    records4 = cursor.fetchall()

    stats222 = InlineKeyboardMarkup(row_width=1)
    ob_statistik2 = InlineKeyboardButton(text='Общая статистика 🔎', callback_data='ob_statistik2')
    
    stats222.add(ob_statistik2)

    if user_status == "Admin":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222, parse_mode='html')
       return
    if user_status == "Helper_Admin":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222 , parse_mode='html')
       return

    if user_status == "Owner":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222 , parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/XennuKinDer/'>Разраб</a>  ⚠️ ", parse_mode='html')
@dp.callback_query_handler(text='Admins_menu_up')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    admins_menu = InlineKeyboardMarkup(row_width=2)
    statistic = InlineKeyboardButton(text='Статистика 👥', callback_data='statistic')
    admins_comands = InlineKeyboardButton(text='Админ команды 📝', callback_data='admins_comands')
    admins_menu.add(statistic, admins_comands)
    if user_status == 'Owner':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: OWNER\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return

    if user_status == 'Helper_Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: HELPER ADMINS\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return
    if user_status == 'Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: ADMINS\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику <a href='t.me/XennuKinDer/'>Xennu</a>  ⚠️ ", parse_mode='html')

@dp.callback_query_handler(text='channel_poverk')
async def craft_resurs3(callback: types.CallbackQuery):
   user_id = callback.from_user.id
   user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
   user_name = str(user_name[0])

   balance = cursor.execute("SELECT balance from users where user_id = ?",(callback.from_user.id,)).fetchone()
   balance = int(balance[0])
   user_channel_status = await bot.get_chat_member(chat_id="@LayGame", user_id=callback.from_user.id)

   channel_pov = cursor.execute("SELECT members from channel_pov where user_id = ?", (callback.from_user.id,)).fetchone()
   channel_pov = int(channel_pov[0])

   if channel_pov > 0:
      await callback.message.answer( f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы уже получили деньги за подписку", parse_mode='html')
      return

   if user_channel_status['status'] != 'left':
      await callback.message.answer( f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно подписались на канал ✅", parse_mode='html')
      await callback.message.answer( f"💸 | <a href='tg://user?id={user_id}'>{user_name}</a>, вы получили приз в размере  500.000.000.000.000.000€", parse_mode='html')
      cursor.execute(f'UPDATE channel_pov SET members = {1} WHERE user_id = {user_id}')
      cursor.execute(f'UPDATE users SET balance = {balance + 500000000000000000} WHERE user_id = {user_id}')
      connect.commit()
   else:
      await callback.message.answer( f"❌ | <a href='tg://user?id={user_id}'>{user_name}</a>, вы не подписались на канал, попробуйте снова", parse_mode='html')
 
@dp.callback_query_handler(text='Priv2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a> , вот все доступные привилегии📝

<b>🎀 | Игрок
👑 | VIP+
🎁 | МегаАппер 
💵 | Донатер
💎 | МегаДонатер</b>

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='Im2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот все команды на имущество📝

<code>🏠 | Дома
         🏡 Мой дом 
         🏡 Купить подвал [номер]
         🏡 Продать подвал 
         🏡 Крафтить 
         🏡 Система крафта 

🚘 | Машины
        🚗 Моя машина
        🚗 Заправить 
        🚗 Поченить</code>

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='rabot2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот список работних команд📝

<i>⛏ | Шахта
      Купить кирку ⛏
      Копать руду ⛏
      Продать [название руды] [количество] ⛏

🌾 | Ферма 
      Купить грабли 🌾
      Собрать [название урожая] 🌾
      Продать [название урожая] [количество] 🌾</i>

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='game2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот список игровых команд 📝

<b>🧊 | /gamevb - ВБ
⚽️ | Футбол\Фб [ставка]
🎱 | Dice [ч\к] [ставка] - Wheel
🤵‍♀️ | Казино [сумма]
◾️ | Плинко [сумма]
🎰 | Спин [сумма]
🎲 | Кубик [число] [сумма]
🎲 | Чётное\нечётное [сумма]
🏎 | Гонка [сумма]</b>

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='admins_comands')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0]) 
    if user_status == 'Owner':
       commands = '''
<b>1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /ban
6️⃣ | /unban
7️⃣ |Выдать админа
8️⃣ | Выдать хелпера
9️⃣ | Передать права
🔟 | Забрать права
1️⃣1️⃣ | /reset
1️⃣2️⃣ | /warn
1️⃣3️⃣ | reset_id [ID]
1️⃣4️⃣ | /info
1️⃣5️⃣ | /info_id [ID]
1️⃣6️⃣ | Поделить [количество]
1️⃣7️⃣ | /ban_id [ID]
1️⃣8️⃣ | /unban_id [ID]
1️⃣9️⃣ | /warn_id [ID]
2️⃣0️⃣ | /unwarn_id [ID]</b>

       '''
    if user_status == 'Helper_Admin':
       commands = '''
<i>1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /ban
6️⃣ | /unban
7️⃣ | /warn
8️⃣ | reset_id [ID]
9️⃣ | /info
🔟 | /info_id [ID]
1️⃣1️⃣ | Поделить [количество]
1️⃣2️⃣ | /ban_id [ID]
1️⃣3️⃣ | /unban_id [ID]
1️⃣4️⃣ | /warn_id [ID]
1️⃣5️⃣ | /unwarn_id [ID]</i>


       '''
    if user_status == 'Admin':
       commands = '''
<i>1️⃣ | Выдать [сумма]
2️⃣ | Забрать [сумма]
3️⃣ | Умножить [количество]
4️⃣ | Обнулить
5️⃣ | /info
6️⃣ | Поделить [количество]</i>
       '''
    if user_status == 'Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    if user_status == 'Helper_Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    if user_status == 'Owner':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот список администраторских команд 📝\n{commands}", parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику ⚠️", parse_mode='html')

@dp.callback_query_handler(text='stats222')
async def ob_Statisyik(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = user_status[0]

    sqlite_select_query21 = """SELECT * from users where user_status = \"Player\""""
    cursor.execute(sqlite_select_query21)
    Player = cursor.fetchall()

    sqlite_select_query22 = """SELECT * from users where user_status = \"vip\""""
    cursor.execute(sqlite_select_query22)
    vip = cursor.fetchall()

    sqlite_select_query23 = """SELECT * from users where user_status = \"apper\""""
    cursor.execute(sqlite_select_query23)
    apper = cursor.fetchall()

    sqlite_select_query24 = """SELECT * from users where user_status = \"donater\""""
    cursor.execute(sqlite_select_query24)
    donater = cursor.fetchall()

    sqlite_select_query25 = """SELECT * from users where user_status = \"donater2\""""
    cursor.execute(sqlite_select_query25)
    donater2 = cursor.fetchall()

    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Admin\""""
    cursor.execute(sqlite_select_query2)
    records2 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Helper_Admin\""""
    cursor.execute(sqlite_select_query2)
    records3 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Owner\""""
    cursor.execute(sqlite_select_query2)
    records4 = cursor.fetchall()

    if user_status == 'Owner':
       await callback.message.answer(f"""
<a href='tg://user?id={user_id}'>{user_name}</a>, вот общая статистика бота 🔎

<b>🔓 | Основная
         👤 | Игроков: {len(records)}

🔰 | Привилегии
         👑 | VIP+ {len(vip)}
         🎁 | Мега Аппер {len(apper)}
         💵 | Донатер {len(donater)}
         💎 | МегаДонатер  {len(donater2)}</b>

<b>🛑 | Администрация
         ⛔️ | ADMIN: {len(records2)}
         ⚠️ | HELPER-ADMIN: {len(records3)}
         ✅ | OWNER: {len(records4)}</b>
       """, parse_mode='html')
    else:
       await callback.message.answer(f"🆘 | <a href='tg://user?id={user_id}'>{user_name}</a>, статистика бота доступна только от прав администратора \"HELPER-ADMINS\" ", parse_mode='html')


@dp.callback_query_handler(text='statistic')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0])
    
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Admin\""""
    cursor.execute(sqlite_select_query2)
    records2 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Helper_Admin\""""
    cursor.execute(sqlite_select_query2)
    records3 = cursor.fetchall()

    sqlite_select_query2 = """SELECT * from users where user_status = \"Owner\""""
    cursor.execute(sqlite_select_query2)
    records4 = cursor.fetchall()

    stats222 = InlineKeyboardMarkup(row_width=1)
    ob_statistik2 = InlineKeyboardButton(text='Общая статистика 🔎', callback_data='ob_statistik2')
    
    stats222.add(ob_statistik2)

    if user_status == "Admin":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222, parse_mode='html')
       return
    if user_status == "Helper_Admin":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222 , parse_mode='html')
       return

    if user_status == "Owner":
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вот статистика бота  📊\n🤵 | Игроков: {len(records)}\n👨‍⚖️ | OWNER: {len(records4)}\n👮‍♀️ | HELPER-ADMINS: {len(records3)}\n🤠 | ADMIN: {len(records2)}",reply_markup=stats222 , parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику⚠️ ", parse_mode='html')
@dp.callback_query_handler(text='Admins_menu_up')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    user_status = cursor.execute("SELECT user_status from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_status = str(user_status[0])

    admins_menu = InlineKeyboardMarkup(row_width=2)
    statistic = InlineKeyboardButton(text='Статистика 👥', callback_data='statistic')
    admins_comands = InlineKeyboardButton(text='Админ команды 📝', callback_data='admins_comands')
    admins_menu.add(statistic, admins_comands)
    if user_status == 'Owner':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: OWNER\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return

    if user_status == 'Helper_Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: HELPER ADMINS\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return
    if user_status == 'Admin':
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>, вы успешно вошли в админ меню ✅\n\n⛔️ | Права администратора: ADMINS\n\n🔐 | Категории:\n     👥 | Статистика бота\n     📝 | Админ команды\n\n↘️ Выбери одну из категорий", reply_markup=admins_menu , parse_mode='html')
       return
    else:
       await callback.message.answer(f"<a href='tg://user?id={user_id}'>{user_name}</a>,Вы не являетесь администратором бота 👮. Для получение прав администратора обратитесь к разработчику⚠️ ", parse_mode='html')
@dp.callback_query_handler(text='Osn2')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, вот список основных команд📝

<b>🖼 | Аватарка | Работает
      Удалить аватарку 🔒
🕴 | Профиль
🔎 | Ник 
      Сменить ник [сообщения] ⚙️
      Сменить префикс [сообщения] ⚙️
      Сменить игроку префикс [сообщения] ⚙️
👝 | Б\Баланс
🏦 | Банк
      Банк снять [сумма] 🏛
      Банк положить [сумма] 🏛
      Депозит положить [сумма] 🏛
      Депозит снять [сумма] 🏛
      Процент снять [сумма] 🏛
💹 | Иены
       Иены купить [количество]
        Иены продать [количество]
         Иены курс [количество]
💎 | Рейтинг
      Рейтинг купить [количество] 💎
       Рейтинг продать [количество] 💎
🤝 | Дать [сумма]
💰 | Ограбить банк 
🎁 | Ежедневный бонус
👑 | Топ
🏛 | Топ богачей\ Топ Б
      Получить кит-бонус 🎁
👮‍♂️ | Репорт
💭 | Рп-команды</b>

ℹ️ Что бы использовать команду , напишите команду сообщением
    ''', parse_mode='html')

@dp.callback_query_handler(text='register_help')
async def help(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_name = cursor.execute("SELECT user_name from users where user_id = ?",(callback.from_user.id,)).fetchone()
    user_name = str(user_name[0])


    help2 = InlineKeyboardMarkup(row_width=2)
    Osn2 = InlineKeyboardButton(text='Основные 📝', callback_data='Osn2')
    game2 = InlineKeyboardButton(text='Игры 🎮', callback_data='game2')
    rabot2 = InlineKeyboardButton(text='Работы 🔨', callback_data='rabot2')
    Im2 = InlineKeyboardButton(text='Имущество 🏘 ', callback_data='Im2')
    Priv2 = InlineKeyboardButton(text='Привилегии 📖', callback_data='Priv2')
    Adm2 = InlineKeyboardButton(text='Admins menu ⛔️', callback_data='Admins_menu_up')
    help2.add(Osn2, game2, rabot2, Im2, Priv2, Adm2)
    await callback.message.answer(f'''
<a href='tg://user?id={user_id}'>{user_name}</a>, виберите категории🔍

<code>📝 | Основные
🎮 | Игры 
🔨 | Работы
🏘 | Имущество
📖 | Привилегии
⛔️ | Admins menu</code>

Разработчик: @GoormHikka 💻
Наша беседа: @userbotikchat  💬
    ''', reply_markup=help2, parse_mode='html')     
    
    
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
