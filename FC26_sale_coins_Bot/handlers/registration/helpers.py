# ╔══════════════════════════════════════════════════════════════════════════╗
# ║           🛠️ REGISTRATION HELPERS - دوال مساعدة للتسجيل                ║
# ╚══════════════════════════════════════════════════════════════════════════╝

"""دوال مساعدة لخدمة التسجيل"""

from utils.logger import log_user_action


async def show_main_menu(update, user_data):
    """عرض القائمة الرئيسية"""
    user_id = update.effective_user.id
    username = update.effective_user.username or "Unknown"
    platform = user_data.get("platform", "غير محدد")
    whatsapp = user_data.get("whatsapp", "غير محدد")

    main_menu_text = f"""✅ <b>أهلاً وسهلاً بعودتك!</b>

👤 <b>المستخدم:</b> @{username}
🎮 <b>المنصة:</b> {platform}
📱 <b>الواتساب:</b> <code>{whatsapp}</code>

<b>🏠 القائمة الرئيسية:</b>

🔹 <code>/sell</code> - بيع الكوينز
🔹 <code>/profile</code> - عرض الملف الشخصي
🔹 <code>/help</code> - المساعدة والدعم

<b>🎯 خدماتنا:</b>
• شراء وبيع العملات
• تجارة اللاعبين
• خدمات التطوير
• دعم فني متخصص

💬 <b>للحصول على الخدمات تواصل مع الإدارة</b>"""

    await update.message.reply_text(main_menu_text, parse_mode="HTML")
    log_user_action(user_id, "Main menu", f"Platform: {platform}")
