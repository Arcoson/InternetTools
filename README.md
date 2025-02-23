# InternetTools

A powerful command-line network monitoring tool that provides detailed information about your network interfaces, internet speed, and real-time traffic statistics.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/internet-tools.git
cd internet-tools
```

2. Install required packages:
```bash
pip install typer rich psutil speedtest-cli netifaces
```

## Usage

The tool provides three main commands:

### Network Information
```bash
python script.py network-info
```
Displays detailed information about all network interfaces.

### Speed Test
```bash
python script.py speed-test
```
Runs an internet speed test and shows:
- Download speed (Mbps)
- Upload speed (Mbps)
- Ping (ms)

### Real-time Monitor
```bash
python script.py speed-test
```
Monitors network traffic in real-time, showing:
- Bytes sent/received
- Packets sent/received
- Network errors
Press Ctrl+C to stop monitoring.

## Requirements

- Python 3.7+
- Linux/macOS/Windows

## Dependencies

- typer: CLI interface
- rich: Terminal formatting
- psutil: System and process utilities
- speedtest-cli: Internet speed testing
- netifaces: Network interface information

## License

MIT License
