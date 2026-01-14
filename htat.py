import os
from core import Actions
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def show_main_menu():
    os.system('clear')
    console.print(Panel.fit(
        "   [bold cyan]HTAT v2.0 - نظام التحكم المتكامل[/bold cyan]   \n"
        "[bold white]مساعدك العربي الشامل في كالي لينكس[/bold white]",
        border_style="bright_blue"
    ))

    # إنشاء جدول الأقسام
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("القسم", justify="center", style="yellow")
    table.add_column("الأدوات والمهام المتاحة", justify="right")

    table.add_row("📡 الشبكات", "1) فحص سريع | 2) تفعيل وضع المراقبة (ALFA) | 3) Bettercap (MITM)")
    table.add_row("👤 الحسابات", "4) مدير الحسابات | 5) أتمتة المتابعة | 6) مصنع الصفحات")
    table.add_row("⚙️ النظام", "7) تحديث شامل | 8) تنظيف النظام | 9) معلومات الأجهزة")
    table.add_row("❌ خروج", "0) إغلاق الأداة")

    console.print(table)

def start():
    while True:
        show_main_menu()
        choice = input("\n[HTAT] أدخل رقم المهمة: ")

        if choice == '1': Actions.net_scan()
        elif choice == '2': Actions.alfa_monitor_mode()
        elif choice == '3': Actions.run_bettercap_full()
        elif choice == '4': Actions.account_automation_info()
        elif choice == '7': Actions.full_update()
        elif choice == '0':
            console.print("[bold red]تم إغلاق النظام.[/bold red]")
            break
        else:
            console.print("[bold yellow]جاري تطوير هذا القسم...[/bold yellow]")
        
        input("\nاضغط Enter للعودة للقائمة...")

if __name__ == "__main__":
    start()
