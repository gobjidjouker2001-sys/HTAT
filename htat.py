import time
import os
import sys
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from core import Actions

console = Console()

def create_layout() -> Layout:
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", size=20),
        Layout(name="footer", size=3)
    )
    return layout

class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row(Text("HTAT ULTIMATE v3.0 - مساعد التحكم المتقدم", style="bold cyan"))
        return Panel(grid, style="green")

def make_dashboard_table() -> Table:
    table = Table(expand=True, border_style="bright_blue")
    table.add_column("القسم", justify="center", style="bold yellow")
    table.add_column("الخيار", justify="center", style="cyan")
    table.add_column("الوصف الوظيفي", justify="right", style="white")

    table.add_row("📡 الشبكات", "1", "فحص الأهداف + خريطة الشبكة")
    table.add_row("📶 ALFA", "2", "تفعيل Monitor Mode + حقن الحزم")
    table.add_row("🕵️ Bettercap", "3", "هجوم MITM تلقائي (Sniffing)")
    table.add_row("🤖 الحسابات", "4", "نظام الأتمتة (تسجيل دخول + متابعة)")
    table.add_row("⚙️ النظام", "5", "تحديث شامل + تنظيف العمق")
    table.add_row("🛑 إغلاق", "0", "خروج آمن من الأداة")
    return table

def run_task_animation(task_name):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task_description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=f"جاري تنفيذ: {task_name}...", total=None)
        time.sleep(2) # محاكاة وقت التحميل

def main():
    layout = create_layout()
    layout["header"].update(Header())
    
    with Live(layout, refresh_per_second=4, screen=True):
        while True:
            layout["body"].update(Panel(make_dashboard_table(), title="لوحة التحكم الرئيسية", border_style="blue"))
            layout["footer"].update(Panel(Text("أدخل رقم العملية لبدء التنفيذ...", justify="center", style="dim")))
            
            # ملاحظة: في وضع Live الكامل نحتاج لإدخال خارجي
            # سنستخدم هنا واجهة الإدخال التقليدية لكن بتنسيق أفضل
            break 

    while True:
        os.system('clear')
        console.print(Header())
        console.print(Panel(make_dashboard_table(), border_style="blue"))
        
        choice = console.input("\n[bold green]HTAT[/bold green] > ")

        if choice == '1':
            run_task_animation("فحص الشبكة")
            Actions.network_scan()
        elif choice == '2':
            run_task_animation("تهيئة كارت ALFA")
            Actions.start_alfa_monitor()
        elif choice == '3':
            run_task_animation("تشغيل هجوم Bettercap")
            Actions.run_bettercap_auto()
        elif choice == '4':
            # هنا سنربط كود السيلينيوم القادم
            console.print("[bold magenta]جاري تشغيل محرك الأتمتة...[/bold magenta]")
            Actions.social_bot_status()
        elif choice == '0':
            console.print("[bold red]إغلاق الأنظمة... وداعاً[/bold red]")
            break
        
        input("\nإضغط Enter للعودة...")

if __name__ == "__main__":
    main()
