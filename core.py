import os
import subprocess

class Actions:
    @staticmethod
    def network_scan():
        # فحص الشبكة المحلية
        return os.system("sudo arp-scan --localnet")

    @staticmethod
    def run_bettercap():
        # تشغيل بيتر كاب
        return os.system("sudo bettercap")

    @staticmethod
    def update_kali():
        # تحديث المستودعات
        return os.system("sudo apt update && sudo apt upgrade -y")

    @staticmethod
    def sys_info():
        # معلومات النظام
        return os.system("uname -a && lscpu")
