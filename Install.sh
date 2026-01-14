#!/bin/bash

echo "--- جاري تهيئة أداة HTAT في النظام ---"

# منح صلاحيات التنفيذ
chmod +x htat.py

# إنشاء اختصار في النظام
sudo ln -sf "$(pwd)/htat.py" /usr/local/bin/htat

echo "[+] تم التثبيت! يمكنك الآن تشغيل الأداة من أي مكان بكتابة أمر: htat"
