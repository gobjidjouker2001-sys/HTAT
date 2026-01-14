import subprocess
import sys
import os

def setup():
    dependencies = ['rich', 'requests']
    print("--- HTAT: جاري التحقق من المكتبات ---")
    for lib in dependencies:
        try:
            __import__(lib)
        except ImportError:
            print(f"[*] تثبيت {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
    print("[+] جميع المكتبات جاهزة.")

if __name__ == "__main__":
    setup()
