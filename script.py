import typer
import rich
from rich.console import Console
from rich.table import Table
from rich.progress import track
import psutil
import speedtest
import socket
import netifaces
import subprocess
from datetime import datetime
import time

app = typer.Typer()
console = Console()

def get_network_interfaces():
    interfaces = netifaces.interfaces()
    data = []
    for iface in interfaces:
        addrs = netifaces.ifaddresses(iface)
        if netifaces.AF_INET in addrs:
            ipv4 = addrs[netifaces.AF_INET][0]
            data.append({
                "interface": iface,
                "ip": ipv4.get('addr', 'N/A'),
                "netmask": ipv4.get('netmask', 'N/A'),
                "broadcast": ipv4.get('broadcast', 'N/A')
            })
    return data

def get_speed():
    st = speedtest.Speedtest()
    console.print("[yellow]Testing download speed...[/]")
    download = st.download() / 1_000_000  # Convert to Mbps
    console.print("[yellow]Testing upload speed...[/]")
    upload = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping
    return download, upload, ping

@app.command()
def network_info():
    """Display detailed network interface information"""
    table = Table(title="Network Interfaces")
    table.add_column("Interface", style="cyan")
    table.add_column("IP Address", style="magenta")
    table.add_column("Netmask", style="green")
    table.add_column("Broadcast", style="yellow")
    
    for iface in get_network_interfaces():
        table.add_row(
            iface["interface"],
            iface["ip"],
            iface["netmask"],
            iface["broadcast"]
        )
    
    console.print(table)

@app.command()
def speed_test():
    """Run internet speed test"""
    with console.status("[bold green]Running speed test..."):
        download, upload, ping = get_speed()
    
    table = Table(title="Speed Test Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")
    
    table.add_row("Download", f"{download:.2f} Mbps")
    table.add_row("Upload", f"{upload:.2f} Mbps")
    table.add_row("Ping", f"{ping:.2f} ms")
    
    console.print(table)

@app.command()
def monitor():
    """Monitor network traffic in real-time"""
    try:
        while True:
            net_io = psutil.net_io_counters()
            table = Table(title=f"Network Monitor - {datetime.now().strftime('%H:%M:%S')}")
            table.add_column("Metric", style="cyan")
            table.add_column("Value", style="magenta")
            
            table.add_row("Bytes Sent", f"{net_io.bytes_sent:,} bytes")
            table.add_row("Bytes Received", f"{net_io.bytes_recv:,} bytes")
            table.add_row("Packets Sent", f"{net_io.packets_sent:,}")
            table.add_row("Packets Received", f"{net_io.packets_recv:,}")
            table.add_row("Errors In", str(net_io.errin))
            table.add_row("Errors Out", str(net_io.errout))
            
            console.clear()
            console.print(table)
            time.sleep(1)
    except KeyboardInterrupt:
        console.print("[red]Monitoring stopped[/]")

if __name__ == "__main__":
    console.print("[bold blue]===== InternetTools =====\n[/]")
    app.callback()(lambda: None)
    app()
