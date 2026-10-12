Uy e’loni ko‘rsatilganda esa quyidagi inline tugmalar bo‘lishi mumkin:
- ❤️ Sevimlilarga qo‘shish
- 📄 Batafsil ma’lumot
- 📩 Murojaat yuborish
- 🌐 Saytda ko‘rish
- ⬅️ Keyingi uy / Oldingi uy


2. Uy qidirish uchun inline keyboard
Mijoz 🏠 Uy qidirish tugmasini bossa, bot keyingi tanlovlarni ko‘rsatadi.
Qanday turdagi ko‘chmas mulk qidiryapsiz?
🏠 Sotib olish

🔑 Ijaraga olish

🔎 Filtrlarni tanlash

⬅️ Asosiy menyu


3. Administrator uchun keyboard
Administrator uchun alohida menyu bo‘ladi. Uni faqat vakolatli foydalanuvchilar ko‘ra olishi kerak.
⚙️ Admin panel
📊 Statistika


📩 Yangi murojaatlar


🏠 E’lonlar


👥 Mijozlar


💳 To‘lovlar nazorati


📈 Moliyaviy hisobot


📢 Xabar yuborish


⚙️ Sozlamalar


class UserRoles(Enum):
    ADMIN = "admin"
    AGENT = "agent"
    ACCOUNTANT = "accountant"
    OWNER = "owner"
    CUSTOMER = "customer"