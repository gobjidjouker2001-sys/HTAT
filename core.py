import os

class Actions:
    @staticmethod
    def network_scan():
        os.system("sudo arp-scan --localnet")

    @staticmethod
    def start_alfa_monitor():
        # أوامر كارت الألفا
        os.system("sudo airmon-ng check kill")
        os.system("sudo airmon-ng start wlan0") # تأكد أن اسم الكارت wlan0
        print("\n[+] تم تفعيل وضع Monitor Mode بنجاح.")

    @staticmethod
    def run_bettercap_auto():
        # تشغيل بيتركاب مع واجهة تفاعلية بسيطة
        os.system("sudo bettercap -eval 'net.probe on; net.show'")

    @staticmethod
    def social_bot_status():
        print("\n[🤖] نظام الأتمتة:")
        print("1. تسجيل دخول تلقائي")
        print("2. متابعة جماعية")
        print("3. إنشاء حسابات")
        # هذا الجزء سنملاه بكود Selenium في الخطوة القادمة

    @staticmethod
    def update_system():
        os.system("sudo apt update && sudo apt upgrade -y")
