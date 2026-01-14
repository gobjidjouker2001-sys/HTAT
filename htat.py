import installer
installer.setup() # التأكد من المكتبات عند كل تشغيل

import os
from core import Actions
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def main_menu():
    os.system('clear')
    console.print(Panel.fit(
        "   [bold cyan]HTAT - مساعد الهكر العربي[/bold cyan]   \n"
        "[bold white]Hacky Terminal Assistant Tool v1.0[/bold white]",
        border_style="green"
    ))
    
    table = Table(show_header=True, header_style="bold yellow")
    table.add_column("الرقم", justify="center", style="cyan")
    table.add_column("الأمر الوظيفي", justify="right", style="white")

    table.add_row("1", "فحص الأجهزة المتصلة بالشبكة")
    table.add_row("2", "تشغيل أداة Bettercap")
    table.add_row("3", "تحديث نظام كالي والأدوات")
    table.add_row("4", "عرض مواصفات الجهاز والنظام")
    table.add_row("0", "إغلاق الأداة")

    console.print(table)

def start():
    while True:
        main_menu()
        choice = input("\n[HTAT] اختر عملية: ")
        
        if choice == '1':
            Actions.network_scan()
        elif choice == '2':
            Actions.run_bettercap()
        elif choice == '3':
            Actions.update_kali()
        elif choice == '4':
            Actions.sys_info()
        elif choice == '0':
            console.print("[bold red]تم الخروج من HTAT.. وداعاً[/bold red]")
            break
        else:
            console.print("[yellow]خيار غير معروف![/yellow]")
        
        input("\nاضغط Enter للعودة...")

if __name__ == "__main__":
    start()
