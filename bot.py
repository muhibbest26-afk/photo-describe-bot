import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import random

# التوكن من متغيرات البيئة
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', "8260372022:AAFqLzIrxTLFAH0kzqs6gcqeJQ_OOoqUIZ8")

# إعداد التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# أنماط الزخرفة (نفس الكود الذي لديك)
NAME_STYLES = {
    "arabic_simple": "الزخرفة العربية البسيطة",
    "arabic_fancy": "الزخرفة العربية المتقنة", 
    "english_cool": "الزخرفة الإنجليزية الرائعة",
    "symbols": "زخرفة بالرموز",
    "emoji": "زخرفة بالإيموجي",
    "double_line": "زخرفة مزدوجة"
}

# الدوال (نفس الكود الذي لديك)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
🎨 **بوت استخراج البرومبت من الصور + زخرفة الأسماء**
# ... (نفس المحتوى)
"""
    await update.message.reply_text(welcome_text)

# ... (بقية الدوال كما هي)

def main():
    """الدالة الرئيسية"""
    if not TOKEN:
        logging.error("❌ لم يتم تعيين TELEGRAM_BOT_TOKEN")
        return
    
    app = Application.builder().token(TOKEN).build()
    
    # الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("name", name_command))
    
    # معالجة النصوص
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    
    # معالجة الصور
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    # معالجة الردود
    app.add_handler(CallbackQueryHandler(handle_name_style_selection, pattern="^style_"))
    app.add_handler(CallbackQueryHandler(handle_smart_prompt, pattern="^(smart_prompt_|alt_prompt_)"))
    
    print("🎨 بوت البرومبت والزخرفة يعمل على Render...")
    
    # بدء البوت
    app.run_polling()

if __name__ == "__main__":
    main()
