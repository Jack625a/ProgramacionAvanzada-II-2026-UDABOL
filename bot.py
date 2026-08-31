from multiprocessing import Process
import time

from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes

def simulacion():
    print("Proceso inciado...")
    for i in range(10):
        print(f"Proceso {i} iniciado")
        time.sleep(1)
    print("Procesos finalizados")

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    proceso=Process(target=simulacion)
    proceso.start()
    await update.message.reply_text("El proceso fue iniciado...")


async def comando2(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola bienvenido") 

async def productos(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Productos....")

app=ApplicationBuilder().token("").build()
app.add_handler(CommandHandler("procesar",start))
app.add_handler(CommandHandler("start",comando2))
app.add_handler(CommandHandler("productos",productos))

print("Bot iniciado...")
app.run_polling()