# 纯测试不需要理会这个脚本（因为我的telegram 出问题了在这里折腾的死去活来的！直接删了都没有影响👍

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("你好！这是兼容版本的测试消息。")

app = ApplicationBuilder().token("YOUR_TELEGRAM_BOT_TOKEN").build()
app.add_handler(CommandHandler("start", start))

print("Telegram Bot 已启动...")
app.run_polling()