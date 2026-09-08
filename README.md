<div align="center">

# ⏳ Time For Everyone ⏳
### *Your Telegram identity, alive in real time.*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Termux](https://img.shields.io/badge/Runs%20on-Termux-000000?style=for-the-badge&logo=android&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-Private-red?style=for-the-badge)

</div>

---

## 🇬🇧 English

**Time For Everyone** turns your Telegram profile into a living display — updating itself every single minute, with zero effort from you.

### ✨ What it does

| ✦ | Feature |
|---|---|
| 🕐 | Bold, oversized live clock in your last name |
| 👑 | A royal title that shifts with the hour of the day |
| 🌡️ | Real-time weather for your city |
| 🔋 | Battery percentage & charging status |
| 📶 | Connection type — WiFi or mobile data |
| 🎵 | Currently playing track, pulled from notifications |
| 🌙 | Precise astronomical moon phase |

All of it, woven automatically into your name and bio. Set it once — forget it forever.

### 🚀 Getting Started (Termux)

```bash
# 1. Update & install the essentials
pkg update -y && pkg upgrade -y
pkg install python git termux-api -y
```

> 📌 Also install the **Termux:API** companion app from the *same source* as Termux itself (F-Droid / GitHub), and grant it permissions once opened.

```bash
# 2. Get the project & install dependencies
cd ~/storage/downloads/Time-For-Everyone
pip install -r requirements.txt
```

```bash
# 3. Configure your Telegram credentials
nano config.py
```
Fill in your `API_ID` and `API_HASH` (from **my.telegram.org**), then save (`Ctrl+O`, `Enter`) and exit (`Ctrl+X`).

```bash
# 4. Launch it
python main.py
```
On first run, you'll be asked for your phone number and the login code Telegram sends you.

### 🔄 Keep it running in the background

```bash
pkg install tmux -y
tmux new -s clock
python main.py
```
Press `Ctrl+B` then `D` to detach — it keeps running even if you close Termux.
Reattach anytime with `tmux attach -t clock`.

---

## 🇮🇶 العربية

**Time For Everyone** يحوّل بروفايلك بتليجرام إلى واجهة حية تتحدث نفسها بنفسها كل دقيقة، بدون أي مجهود منك.

### ✨ شنو يسوي؟

| ✦ | الميزة |
|---|---|
| 🕐 | ساعة حية بأرقام عريضة بارزة داخل اسمك الأخير |
| 👑 | لقب ملكي يتغير حسب وقت اليوم |
| 🌡️ | حالة الطقس اللحظية لمدينتك |
| 🔋 | نسبة شحن البطارية وحالتها |
| 📶 | نوع الاتصال — واي فاي أو بيانات |
| 🎵 | المقطع الشغال حاليًا من الإشعارات |
| 🌙 | مرحلة القمر الفلكية الدقيقة |

كل هذا ينسج تلقائيًا باسمك ونبذتك. تضبطه مرة وحدة، وتنساه للأبد.

### 🚀 التثبيت (عبر Termux)

```bash
# 1. تحديث وتثبيت الأساسيات
pkg update -y && pkg upgrade -y
pkg install python git termux-api -y
```

> 📌 نصّب أيضًا تطبيق **Termux:API** من نفس مصدر Termux (F-Droid أو GitHub)، وافتحه مرة وحدة واعطيه الصلاحيات.

```bash
# 2. جيب المشروع ونصّب المكتبات
cd ~/storage/downloads/Time-For-Everyone
pip install -r requirements.txt
```

```bash
# 3. اضبط بياناتك الخاصة بتليجرام
nano config.py
```
عبّي `API_ID` و `API_HASH` (تحصل عليهم من **my.telegram.org**)، احفظ (`Ctrl+O` ثم `Enter`) واخرج (`Ctrl+X`).

```bash
# 4. شغّله
python main.py
```
أول مرة راح يطلب رقم هاتفك وكود الدخول اللي يرسله تليجرام.

### 🔄 خليه شغال بالخلفية دائمًا

```bash
pkg install tmux -y
tmux new -s clock
python main.py
```
اضغط `Ctrl+B` ثم `D` — يضل شغال حتى لو سكرت ترمكس.
ارجع له وقت ما تريد بأمر: `tmux attach -t clock`

---

<div align="center">

### 🌐 Connect

[![YouTube](https://img.shields.io/badge/YouTube-Subscribe-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@m7jn)
[![Instagram](https://img.shields.io/badge/Instagram-Follow-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/z0_28)

</div>

---

<div align="center">

⚠️ **This project is licensed and time-locked.** ⚠️
Unauthorized modification, decryption, or redistribution of the compiled code is strictly prohibited.
هذا المشروع مرخّص ومربوط بفترة اشتراك محددة — أي تعديل أو فك تشفير أو إعادة توزيع غير مصرح به ممنوع منعًا باتًا.

📩 **Support / التواصل:** Telegram [@K0_MG](https://t.me/K0_MG)

</div>
