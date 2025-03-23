# 导入所需模块
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# 定义一个异步函数，用于处理用户消息
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 获取用户的名字、用户 ID 和用户名
    user_name = update.effective_user.first_name
    user_id = update.effective_user.id
    username = update.effective_user.username if update.effective_user.username else "无用户名"
    
    # 打印用户的名字、用户 ID 和用户名到终端
    print(f"用户消息来自: {user_name} (ID: {user_id}, 用户名: {username})")
    print(f"消息内容: {update.message.text}")

    # 检测消息中是否包含关键词“你好”或“大家好”
    if "你好" in update.message.text or "大家好" in update.message.text:
        # 回复消息
        await update.message.reply_text("你好！")

# 定义 /ip 指令，用于查询 IP 地址的地理位置
async def ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 检查是否提供了 IP 地址参数
    if len(context.args) == 0:
        await update.message.reply_text("请使用 /ip [IP地址] 查询地理位置，例如：/ip 8.8.8.8")
        return

    ip_address = context.args[0]  # 获取用户输入的 IP 地址
    API_URL = f"http://ip-api.com/json/{ip_address}"
    
    try:
        response = requests.get(API_URL)
        data = response.json()

        if data["status"] == "success":
            # 格式化查询结果
            result = (
                f"📡 *查询结果*\n"
                f"*IP地址*: `{data['query']}`\n"
                f"*国家*: `{data['country']}`\n"
                f"*省份*: `{data['regionName']}`\n"
                f"*城市*: `{data['city']}`\n"
                f"*经度*: `{data['lon']}`\n"
                f"*纬度*: `{data['lat']}`\n"
                f"*时区*: `{data['timezone']}`\n"
                f"*组织*: `{data.get('org', '无组织信息')}`\n"
                f"*运营商*: `{data.get('isp', '无运营商信息')}`\n"
                f"*AS*: `{data.get('as', '无AS信息')}`\n"
                f"*ZIP*: `{data.get('zip', '无邮编信息')}`\n"
            )

            # 回复用户查询结果
            await update.message.reply_text(result, parse_mode="Markdown")
        else:
            await update.message.reply_text("无法查询此 IP 地址的信息，请检查输入是否正确。")
    except Exception as e:
        await update.message.reply_text(f"查询 IP 地址时发生错误：{str(e)}")


# 导入所需模块
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

# 定义一个异步函数，用于处理用户消息
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 获取用户的名字、用户 ID 和用户名
    user_name = update.effective_user.first_name
    user_id = update.effective_user.id
    username = update.effective_user.username if update.effective_user.username else "无用户名"
    
    # 打印用户的名字、用户 ID 和用户名到终端
    print(f"用户消息来自: {user_name} (ID: {user_id}, 用户名: {username})")
    print(f"消息内容: {update.message.text}")

    # 检测消息中是否包含关键词“你好”或“大家好”
    if "你好" in update.message.text or "大家好" in update.message.text:
        # 回复消息
        await update.message.reply_text("你好！")

# 定义 /ip 指令，用于查询 IP 地址的地理位置
async def ip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 检查是否提供了 IP 地址参数
    if len(context.args) == 0:
        await update.message.reply_text("请使用 /ip [IP地址] 查询地理位置，例如：/ip 8.8.8.8")
        return

    ip_address = context.args[0]  # 获取用户输入的 IP 地址
    API_URL = f"http://ip-api.com/json/{ip_address}"
    
    try:
        response = requests.get(API_URL)
        data = response.json()

        if data["status"] == "success":
            # 格式化查询结果
            result = (
                f"📡 *查询结果*\n"
                f"*IP地址*: `{data['query']}`\n"
                f"*国家*: `{data['country']}`\n"
                f"*省份*: `{data['regionName']}`\n"
                f"*城市*: `{data['city']}`\n"
                f"*经度*: `{data['lon']}`\n"
                f"*纬度*: `{data['lat']}`\n"
                f"*时区*: `{data['timezone']}`\n"
                f"*组织*: `{data.get('org', '无组织信息')}`\n"
                f"*运营商*: `{data.get('isp', '无运营商信息')}`\n"
                f"*AS*: `{data.get('as', '无AS信息')}`\n"
                f"*ZIP*: `{data.get('zip', '无邮编信息')}`\n"
            )

            # 回复用户查询结果
            await update.message.reply_text(result, parse_mode="Markdown")
        else:
            await update.message.reply_text("无法查询此 IP 地址的信息，请检查输入是否正确。")
    except Exception as e:
        await update.message.reply_text(f"查询 IP 地址时发生错误：{str(e)}")


# 定义 /mc 指令，用于查询 Minecraft 服务器状态
async def mc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # 检查是否提供了服务器地址参数
    if len(context.args) == 0:
        await update.message.reply_text("请使用 /mc [服务器地址] 查询 Minecraft 服务器状态，例如：/mc example.com")
        return

    server_address = context.args[0]  # 获取用户输入的服务器地址
    API_URL = f"https://api.mcsrvstat.us/2/{server_address}"  # Minecraft 查询 API 地址

    try:
        response = requests.get(API_URL)
        data = response.json()

        if data["online"]:  # 检查服务器是否在线
            # 格式化服务器状态信息
            result = (
                f"🎮 *Minecraft 服务器状态*\n"
                f"*服务器地址*: `{server_address}`\n"
                f"*IP地址*: `{data.get('ip', '未知')}`\n"
                f"*端口*: `{data.get('port', '未知')}`\n"
                f"*版本*: `{data.get('version', '未知')}`\n"
                f"*在线玩家*: `{data['players']['online']}/{data['players']['max']}`\n"
                f"*MOTD*: `{''.join(data['motd']['clean'])}`"
            )
            await update.message.reply_text(result, parse_mode="Markdown")
        else:
            await update.message.reply_text(f"服务器 `{server_address}` 处于离线状态，无法查询更多信息。")
    except Exception as e:
        await update.message.reply_text(f"查询 Minecraft 服务器状态时发生错误：{str(e)}")


# 创建 Telegram 应用程序实例，并设置机器人令牌
app = ApplicationBuilder().token("7951173156:AAG9EeG0aBZKWEfewSngizDSGCouxByaOUU").build()

# 添加消息处理器，监控所有非命令的文本消息
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

# 添加 /ip 指令处理器
app.add_handler(CommandHandler("ip", ip))

# 在应用中注册 /mc 指令
app.add_handler(CommandHandler("mc", mc))

# 打印机器人运行状态到终端
print("机器人已经成功启动，正在监听消息和指令中...")

# 启动机器人，以轮询模式监听用户消息
app.run_polling()
