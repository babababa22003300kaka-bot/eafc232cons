# ╔══════════════════════════════════════════════════════════════════════════╗
# ║              👑 FC26 ADMIN MESSAGES - رسائل الادارة                     ║
# ║                     Admin Messages Handler                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝

from typing import List, Dict
from datetime import datetime

class AdminMessages:
    """رسائل لوحة الادارة"""
    
    @staticmethod
    def get_main_admin_message(admin_id: int) -> str:
        """رسالة لوحة الادارة الرئيسية"""
        return f"""👑 <b>لوحة الادارة - FC26</b>

🆔 <b>الادمن:</b> <code>{admin_id}</code>
⏰ <b>الوقت:</b> {datetime.now().strftime('%Y-%m-%d %H:%M')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>الخدمات المتاحة:</b>

💰 <b>إدارة الأسعار:</b>
• عرض جميع الأسعار الحالية
• تعديل أسعار بيع الكوينز
• مراجعة تاريخ التعديلات

📊 <b>الإحصائيات:</b>
• مراجعة أداء البوت
• عرض سجل العمليات
• تقارير المبيعات

⚙️ <b>إعدادات النظام:</b>
• إدارة المستخدمين
• تحديث إعدادات البوت
• النسخ الاحتياطي

اختر الخدمة المطلوبة من الأزرار أدناه 👇"""

    @staticmethod
    def get_price_management_message() -> str:
        """رسالة إدارة الأسعار"""
        return """💰 <b>إدارة أسعار بيع الكوينز</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>الخيارات المتاحة:</b>

📋 <b>عرض الأسعار:</b>
• عرض جميع الأسعار الحالية
• مقارنة الأسعار بين المنصات
• تاريخ آخر تحديث

✏️ <b>تعديل الأسعار:</b>
• تعديل أسعار PlayStation
• تعديل أسعار Xbox  
• تعديل أسعار PC

📊 <b>السجلات:</b>
• مراجعة تاريخ التعديلات
• إحصائيات التغييرات
• تقرير الأسعار

⚠️ <b>تنبيه:</b> جميع التعديلات يتم حفظها في السجل

اختر العملية المطلوبة:"""

    @staticmethod
    def get_current_prices_message(prices: List[Dict]) -> str:
        """رسالة عرض الأسعار الحالية"""
        if not prices:
            return "❌ لا توجد أسعار محفوظة في قاعدة البيانات"
        
        message = "📊 <b>الأسعار الحالية - جميع المنصات</b>\n\n"
        
        # تجميع الأسعار حسب المنصة
        platforms = {}
        for price in prices:
            platform = price['platform']
            if platform not in platforms:
                platforms[platform] = {}
            
            platforms[platform][price['transfer_type']] = {
                'price': price['price'],
                'amount': price['amount'],
                'updated': price['updated_at']
            }
        
        # عرض الأسعار
        platform_names = {
            'playstation': '🎮 PlayStation',
            'xbox': '🎮 Xbox', 
            'pc': '🖥️ PC'
        }
        
        for platform, platform_prices in platforms.items():
            platform_name = platform_names.get(platform, platform)
            message += f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"<b>{platform_name}</b>\n\n"
            
            if 'normal' in platform_prices:
                normal = platform_prices['normal']
                message += f"📅 <b>عادي:</b> {normal['price']:,} ج.م\n"
                message += f"   💰 الكمية: {normal['amount']:,} كوين\n"
                message += f"   📅 آخر تحديث: {normal['updated'][:16]}\n\n"
            
            if 'instant' in platform_prices:
                instant = platform_prices['instant']
                message += f"⚡️ <b>فوري:</b> {instant['price']:,} ج.م\n"
                message += f"   💰 الكمية: {instant['amount']:,} كوين\n"
                message += f"   📅 آخر تحديث: {instant['updated'][:16]}\n\n"
        
        message += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        message += "💡 <b>ملاحظة:</b> الأسعار بالجنيه المصري"
        
        return message

    @staticmethod
    def get_platform_edit_message(platform: str) -> str:
        """رسالة تعديل أسعار منصة معينة"""
        platform_names = {
            'playstation': '🎮 PlayStation',
            'xbox': '🎮 Xbox',
            'pc': '🖥️ PC'
        }
        
        platform_name = platform_names.get(platform, platform)
        
        return f"""✏️ <b>تعديل أسعار {platform_name}</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎯 <b>اختر نوع التحويل للتعديل:</b>

📅 <b>التحويل العادي:</b>
• المدة: خلال 24 ساعة
• السعر الحالي سيتم عرضه

⚡️ <b>التحويل الفوري:</b>
• المدة: خلال ساعة واحدة
• السعر الحالي سيتم عرضه

⚠️ <b>تحذير:</b>
• تأكد من السعر قبل الحفظ
• التعديل يؤثر فوراً على المستخدمين
• سيتم تسجيل التعديل في السجل

اختر نوع التحويل:"""

    @staticmethod
    def get_price_edit_prompt(platform: str, transfer_type: str, current_price: int) -> str:
        """رسالة طلب السعر الجديد"""
        platform_names = {
            'playstation': '🎮 PlayStation',
            'xbox': '🎮 Xbox',
            'pc': '🖥️ PC'
        }
        
        transfer_names = {
            'normal': '📅 عادي',
            'instant': '⚡️ فوري'
        }
        
        platform_name = platform_names.get(platform, platform)
        transfer_name = transfer_names.get(transfer_type, transfer_type)
        
        return f"""💰 <b>تعديل السعر</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎮 <b>المنصة:</b> {platform_name}
⏰ <b>نوع التحويل:</b> {transfer_name}
💎 <b>الكمية:</b> 1,000,000 كوين

💰 <b>السعر الحالي:</b> <code>{current_price:,} ج.م</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✏️ <b>أدخل السعر الجديد:</b>

📝 <b>قواعد الإدخال:</b>
• أرقام فقط (بدون فواصل أو رموز)
• السعر بالجنيه المصري
• الحد الأدنى: 1000 ج.م
• الحد الأقصى: 50000 ج.م

💡 <b>مثال:</b> 5500

اكتب السعر الجديد:"""

    @staticmethod
    def get_price_update_success(platform: str, transfer_type: str, old_price: int, new_price: int) -> str:
        """رسالة نجاح تحديث السعر"""
        platform_names = {
            'playstation': '🎮 PlayStation',
            'xbox': '🎮 Xbox',
            'pc': '🖥️ PC'
        }
        
        transfer_names = {
            'normal': '📅 عادي',
            'instant': '⚡️ فوري'
        }
        
        platform_name = platform_names.get(platform, platform)
        transfer_name = transfer_names.get(transfer_type, transfer_type)
        
        return f"""✅ <b>تم تحديث السعر بنجاح!</b>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 <b>تفاصيل التحديث:</b>

🎮 <b>المنصة:</b> {platform_name}
⏰ <b>نوع التحويل:</b> {transfer_name}
💎 <b>الكمية:</b> 1,000,000 كوين

💰 <b>السعر القديم:</b> <s>{old_price:,} ج.م</s>
💰 <b>السعر الجديد:</b> <code>{new_price:,} ج.م</code>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ <b>وقت التحديث:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

✨ <b>التحديث مفعل الآن:</b>
• جميع المستخدمين سيرون السعر الجديد
• تم حفظ التعديل في السجل
• يمكن تعديل السعر مرة أخرى في أي وقت

🔙 استخدم الأزرار للعودة أو التعديل مرة أخرى"""

    @staticmethod
    def get_admin_logs_message(logs: List[Dict]) -> str:
        """رسالة عرض سجل أعمال الادمن"""
        if not logs:
            return "📝 <b>سجل الأعمال فارغ</b>\n\nلا توجد عمليات مسجلة حتى الآن."
        
        message = "📝 <b>سجل أعمال الادارة</b>\n\n"
        
        for i, log in enumerate(logs[:10], 1):  # أول 10 عمليات
            action_icons = {
                'UPDATE_PRICE': '💰',
                'ADMIN_LOGIN': '🔐', 
                'VIEWED_PRICES': '👁️',
                'ACCESSED_PRICE_MANAGEMENT': '⚙️'
            }
            
            icon = action_icons.get(log['action'], '📋')
            timestamp = log['timestamp'][:16]  # فقط التاريخ والوقت
            
            message += f"{i}. {icon} <b>{log['action']}</b>\n"
            message += f"   ⏰ {timestamp}\n"
            
            if log['details']:
                message += f"   📝 {log['details'][:50]}...\n"
            
            message += "\n"
        
        if len(logs) > 10:
            message += f"... و {len(logs) - 10} عملية أخرى"
        
        return message

    @staticmethod
    def get_unauthorized_message() -> str:
        """رسالة عدم وجود صلاحية"""
        return """🚫 <b>غير مصرح لك!</b>

❌ <b>عذراً، ليس لديك صلاحية للوصول لهذه الخدمة</b>

🔐 <b>هذه الخدمة مخصصة للإدارة فقط</b>

💬 إذا كنت تعتقد أن هذا خطأ، تواصل مع الدعم الفني"""

    @staticmethod
    def get_error_message(error_type: str = "general") -> str:
        """رسائل الأخطاء المختلفة"""
        errors = {
            "invalid_price": "❌ <b>سعر غير صحيح!</b>\n\nيرجى إدخال رقم صحيح بين 1000 و 50000",
            "database_error": "❌ <b>خطأ في قاعدة البيانات!</b>\n\nحدث خطأ أثناء الحفظ، يرجى المحاولة مرة أخرى",
            "general": "❌ <b>حدث خطأ!</b>\n\nيرجى المحاولة مرة أخرى أو التواصل مع الدعم الفني"
        }
        
        return errors.get(error_type, errors["general"])