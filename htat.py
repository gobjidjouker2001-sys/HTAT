import time
import os
import sys
import installer

# التأكد من التبعيات
installer.setup()

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
        Layout(name="body", size=18),
        Layout(name="footer", size=3)
    )
    return layout

class Header:
    def __rich__(self) -> Panel:
        grid = Table.grid(expand=True)
        grid.add_column(justify="center", ratio=1)
        grid.add_row(Text("HTAT ULTIMATE v3.5 - نظام التحكم السيبراني", style="bold cyan"))
        return Panel(grid, style="bright_green")

def make_dashboard_table() -> Table:
    table = Table(expand=True, border_style="bright_blue", pad_edge=False)
    table.add_column("الرمز", justify="center", style="bold yellow")
    table.add_column("القسم", justify="center", style="bold magenta")
    table.add_column("المهام المتاحة", justify="right", style="white")

    table.add_row("📡", "الشبكات", "1) فحص الأهداف | 2) وضع المراقبة (ALFA)")
    table.add_row("🕵️", "التنصت", "3) Bettercap الذكي (Sniffing)")
    table.add_row("🤖", "البوتات", "4) محرك أتمتة الحسابات (Selenium)")
    table.add_row("⚙️", "النظام", "5) تحديث شامل | 6) معلومات العتاد")
    table.add_row("🛑", "خروج", "0) إغلاق الأداة وآثارها")
    return table

def run_task_animation(task_name):
    # تم إصلاح الخطأ هنا عبر إزالة الـ f-string المعقد مع العربي
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task_description}"),
        transient=True,
    ) as progress:
        desc = "جاري تنفيذ " + task_name + "..."
        progress.add_task(description=desc, total=None)
        time.sleep(1.5)

def main():
    while True:
        os.system('clear')
        console.print(Header())
        console.print(Panel(make_dashboard_table(), title="[لوحة التحكم]", border_style="blue"))
        
        choice = console.input("\n[bold green]HTAT[/bold green] @ [bold yellow]Root[/bold yellow] > ")

        if choice == '1':
            run_task_animation("فحص الشبكة")
            Actions.network_scan()
        elif choice == '2':
            run_task_animation("تهيئة ALFA")
            Actions.start_alfa_monitor()
        elif choice == '3':
            run_task_animation("Bettercap")
            Actions.run_bettercap_auto()
        elif choice == '4':
            console.print("[bold cyan]فتح محرك البوتات...[/bold cyan]")
            # سيتم استدعاء كود السيلينيوم هنا
            Actions.social_bot_status()
        elif choice == '0':
            console.print("[bold red]إيقاف جميع العمليات...[/bold red]")
            break
        
        input("\nإضغط Enter للعودة للمركز...")

if __name__ == "__main__":
    main()
