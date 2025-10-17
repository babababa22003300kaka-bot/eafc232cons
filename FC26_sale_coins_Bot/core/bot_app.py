# ╔══════════════════════════════════════════════════════════════════════════╗
# ║              🤖 BOT APPLICATION FACTORY                                  ║
# ║              مصنع تطبيق البوت - مع Persistence                          ║
# ╚══════════════════════════════════════════════════════════════════════════╝

"""
مصنع تطبيق البوت
- تفعيل PicklePersistence
- إدارة الجلسات الدائمة
"""

from pathlib import Path

from telegram.ext import Application, PicklePersistence

from config import BOT_TOKEN


class FC26BotApp:
    """مصنع تطبيق البوت"""

    def create_application(self):
        """
        إنشاء تطبيق البوت مع تفعيل Persistence

        Returns:
            Application: تطبيق البوت جاهز
        """
        print("\n🤖 [BOT-APP] Creating application with persistence...")

        # ═══════════════════════════════════════════════════════════════════
        # 1️⃣ إنشاء مجلد data/ إذا لم يكن موجوداً
        # ═══════════════════════════════════════════════════════════════════
        data_dir = Path("data")
        data_dir.mkdir(parents=True, exist_ok=True)
        print(f"   📁 Data directory ready: {data_dir}")

        # ═══════════════════════════════════════════════════════════════════
        # 2️⃣ إنشاء كائن PicklePersistence
        # ═══════════════════════════════════════════════════════════════════
        session_file = data_dir / "sessions.pkl"

        persistence = PicklePersistence(
            filepath=str(session_file),
            update_interval=60,  # حفظ كل 60 ثانية
        )
        print(f"   💾 Persistence configured: {session_file}")
        print(f"   ⏱️ Update interval: 60 seconds")

        # ═══════════════════════════════════════════════════════════════════
        # 3️⃣ بناء التطبيق مع Persistence
        # ═══════════════════════════════════════════════════════════════════
        app = (
            Application.builder()
            .token(BOT_TOKEN)
            .persistence(persistence)  # 🔥 تفعيل Persistence
            .build()
        )

        print(f"   ✅ Application created successfully")
        print(f"   🔥 Persistence ENABLED")
        print()

        return app
