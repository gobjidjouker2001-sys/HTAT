import os
import subprocess

class Actions:
    # --- قسم الشبكة ---
    @staticmethod
    def net_scan():
        os.system("sudo arp-scan --localnet")

    @staticmethod
    def alfa_monitor_mode():
        # تفعيل وضع المراقبة لكارت الألفا تلقائياً
        os.system("sudo ifconfig wlan0 down")
        os.system("sudo airmon-ng check kill")
        os.system("sudo iwconfig wlan0 mode monitor")
        os.system("sudo ifconfig wlan0 up")
        print("[+] كارت ALFA الآن في وضع المراقبة (Monitor Mode)")

    @staticmethod
    def run_bettercap_full():
        # تشغيل bettercap مع تفعيل الاستنشاق فوراً
        os.system("sudo bettercap -eval 'net.probe on; net.sniff on; set http.proxy.sslstrip true'")

    # --- قسم الحسابات (النواة الأساسية) ---
    @staticmethod
    def account_automation_info():
        print("\n[!] ميزة الأتمتة: تتطلب وجود ملف accounts.txt")
        print("[*] المهام: تسجيل دخول جماعي | متابعة تلقائية | إنشاء صفحات")
        # هنا سنضيف لاحقاً كود السيلينيوم الخاص بك

    # --- قسم النظام ---
    @staticmethod
    def full_update():
        os.system("sudo apt update && sudo apt full-upgrade -y")
