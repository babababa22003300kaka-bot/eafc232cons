# ╔══════════════════════════════════════════════════════════════════════════╗
# ║              🎮 FC26 WELCOME MESSAGES - رسائل الترحيب                   ║
# ║                      Welcome & Greeting Messages                         ║
# ╚══════════════════════════════════════════════════════════════════════════╝

from typing import Dict

class WelcomeMessages:
    """Welcome and greeting messages for the bot"""
    
    @staticmethod
    def get_start_message() -> str:
        """Get main start/welcome message"""
        return """🎮 <b>مرحباً بك في FC26</b>
منصة الألعاب الاحترافية

🚀 <b>اختر منصتك المفضلة للبدء:</b>

<b>🎯 خطوات التسجيل:</b>

1️⃣ اختيار المنصة
2️⃣ تأكيد رقم الواتساب
3️⃣ اختيار طريقة الدفع
4️⃣ إدخال تفاصيل الدفع
5️⃣ إتمام التسجيل

🔥 <b>ابدأ رحلتك الآن!</b>"""
    
    @staticmethod
    def get_platform_selected_message(platform_name: str) -> str:
        """Get platform selection success message"""
        return f"""✅ <b>تم اختيار المنصة بنجاح!</b>

🎮 <b>المنصة المختارة:</b> {platform_name}

<b>📱 تأكيد رقم الواتساب</b>

🔹 أرسل رقم الواتساب الخاص بك
🔹 <b>مثال:</b> 01012345678
🔹 <b>يجب أن يبدأ بـ:</b> 010, 011, 012, أو 015

⚠️ <b>تأكد من صحة الرقم لأنه سيتم التواصل معك عليه</b>"""
    
    @staticmethod
    def get_whatsapp_confirmed_message(phone_display: str) -> str:
        """Get WhatsApp confirmation message"""
        return f"""✅ <b>تم تأكيد رقم الواتساب بنجاح!</b>

📱 <b>الواتساب:</b> <code>{phone_display}</code>

<b>💳 اختيار طريقة الدفع</b>

🔹 <b>اختر الطريقة المناسبة لك:</b>

<b>📋 قائمة طرق الدفع الكاملة:</b>

⭕️ <b>فودافون كاش</b> - رقم 11 خانة يبدأ بـ 010/011/012/015
🟢 <b>اتصالات كاش</b> - رقم 11 خانة يبدأ بـ 010/011/012/015
🍊 <b>أورانج كاش</b> - رقم 11 خانة يبدأ بـ 010/011/012/015
🟣 <b>وي كاش</b> - رقم 11 خانة يبدأ بـ 010/011/012/015
🏦 <b>محفظة بنكية</b> - رقم 11 خانة لأي شبكة مصرية
💳 <b>تيلدا</b> - رقم كارت 16 رقماً بالضبط
🔗 <b>إنستا باي</b> - رابط كامل يحتوي على instapay.com.eg أو ipn.eg"""
    
    @staticmethod
    def get_payment_method_selected_message(payment_name: str, instruction: str) -> str:
        """Get payment method selection message"""
        return f"""✅ <b>تم اختيار طريقة الدفع بنجاح!</b>

💳 <b>طريقة الدفع:</b> {payment_name}

<b>📝 إدخال التفاصيل</b>

🔹 {instruction}

⚠️ <b>تأكد من صحة البيانات قبل الإرسال</b>"""
    
    @staticmethod
    def get_continue_registration_message(step: str, context: Dict = None) -> str:
        """Get continue registration message based on current step"""
        base_message = "🔄 <b>استكمال التسجيل</b>\n\n"
        
        if step == "choosing_platform":
            return base_message + """🎮 <b>اختر منصتك المفضلة:</b>

📍 <b>موضعك الحالي:</b> اختيار المنصة"""
        
        elif step == "entering_whatsapp" and context:
            return base_message + f"""🎮 <b>المنصة:</b> {context.get('platform_name', 'غير محدد')}

<b>📱 أرسل رقم الواتساب الخاص بك:</b>

🔹 <b>مثال:</b> 01012345678
🔹 <b>يجب أن يبدأ بـ:</b> 010, 011, 012, أو 015

📍 <b>موضعك الحالي:</b> تأكيد رقم الواتساب"""
        
        elif step == "choosing_payment" and context:
            return base_message + f"""📱 <b>الواتساب:</b> <code>{context.get('whatsapp', 'غير محدد')}</code>

<b>💳 اختر طريقة الدفع:</b>

📍 <b>موضعك الحالي:</b> اختيار طريقة الدفع"""
        
        elif step == "entering_payment_details" and context:
            return base_message + f"""💳 <b>طريقة الدفع:</b> {context.get('payment_name', 'غير محدد')}

<b>📝 أرسل تفاصيل الدفع:</b>

🔹 {context.get('instruction', 'أدخل التفاصيل')}

📍 <b>موضعك الحالي:</b> إدخال تفاصيل الدفع"""
        
        else:
            return base_message + "📍 <b>موضعك الحالي:</b> غير محدد"
    
    @staticmethod
    def get_help_message() -> str:
        """Get help message"""
        return """📚 <b>مساعدة FC26 Gaming Bot</b>

<b>🤖 الأوامر المتاحة:</b>
• /start - بدء أو متابعة التسجيل
• /profile - عرض الملف الشخصي
• /sell - بيع كوينز FIFA 💰
• /delete - حذف الملف الشخصي
• /help - عرض هذه المساعدة

<b>🎮 المنصات المدعومة:</b>
• PlayStation (PS4/PS5)
• Xbox (One/Series X|S)
• PC (Origin/Steam)

<b>💳 طرق الدفع المدعومة:</b>
• فودافون كاش (010)
• اتصالات كاش (011)
• أورانج كاش (012)
• وي كاش (015)
• محفظة بنكية (أي شبكة)
• كارت تيلدا (16 رقم)
• إنستا باي (رابط كامل)

<b>📱 أرقام الهاتف:</b>
• يجب أن تبدأ بـ 010/011/012/015
• يجب أن تتكون من 11 رقماً بالضبط
• لا تضع كود الدولة (+20)

<b>🔗 روابط إنستاباي:</b>
• يجب أن تحتوي على instapay.com.eg
• أو ipn.eg
• مثال: https://instapay.com.eg/abc123

<b>🗑️ حذف الملف الشخصي:</b>
• استخدم /delete أو الزر في /profile
• تأكيد مزدوج مطلوب للحماية
• العملية لا يمكن التراجع عنها

<b>💰 خدمة بيع الكوينز:</b>
• استخدم /sell لبيع كوينز FIFA
• أفضل الأسعار في السوق المصري
• دفع فوري وآمن 100%
• جميع المنصات مدعومة

<b>📞 للدعم الفني:</b>
تواصل مع فريق الدعم إذا واجهت أي مشكلة"""
    
    @staticmethod
    def get_about_message() -> str:
        """Get about bot message"""
        return """ℹ️ <b>حول FC26 Gaming Bot</b>

🎮 <b>عن المنصة:</b>
FC26 هي منصة احترافية لألعاب FIFA و EA Sports FC، نوفر خدمات متنوعة للاعبين في المنطقة العربية.

🚀 <b>خدماتنا:</b>
• شراء وبيع العملات
• تجارة اللاعبين
• خدمات التطوير
• دعم فني متخصص

🔐 <b>الأمان:</b>
• حماية كاملة للبيانات
• معاملات آمنة ومضمونة
• دعم فني على مدار الساعة

💎 <b>الجودة:</b>
• فريق محترف ومتخصص
• أسعار تنافسية
• خدمة سريعة وموثوقة

📞 <b>التواصل:</b>
نحن هنا لخدمتك في أي وقت"""