# 6841_Project

A cybersecurity research project implementing a keylogger with network transmission capabilities for educational purposes.

## ⚠️ Important Disclaimer

This project is developed for educational and cybersecurity research purposes only. The keylogger functionality should only be used on systems you own or have explicit permission to monitor. Unauthorized keylogging is illegal and unethical. Users are responsible for ensuring compliance with all applicable laws and regulations.

## Project Overview

This project consists of a client-server keylogger system that demonstrates:
- Keystroke capture and processing
- Network communication between client and server
- Real-time data transmission
- MacOS application packaging

## Features

- **Keystroke Logging**: Captures keyboard input including special keys
- **Network Transmission**: Sends logged data to a remote server via TCP sockets
- **Real-time Processing**: Handles backspace operations with strikethrough formatting
- **Stealth Operation**: Runs as a background application on macOS
- **Automated Reporting**: Sends data at regular intervals (configurable)

## Project Structure

```
├── README.md
├── app/
│   └── TypingRace.app/          # Packaged macOS application
├── images/
│   └── icon.icns                # Application icon
└── src/
    ├── keylogger2.py            # Main keylogger client
    ├── receiver.py              # Server component
    ├── setup.py                 # Application packaging script
    └── logs.txt                 # Output log file
```

## Components

### 1. Keylogger Client (`keylogger2.py`)
- Captures keyboard events using the `pynput` library
- Processes special keys (space, enter, backspace, tab)
- Implements strikethrough functionality for backspace operations
- Transmits data via TCP socket connection
- Configurable reporting interval (default: 15 seconds)

### 2. Server/Receiver (`receiver.py`)
- Listens for incoming connections on port 2000
- Receives and processes JSON-encoded keystroke data
- Logs received data with timestamps to `logs.txt`
- Handles connection errors gracefully

### 3. Application Packaging (`setup.py`)
- Uses py2app to create a standalone macOS application
- Configures the app to run in background mode
- Sets up the disguised "TypingRace" identity

## Technical Details

### Dependencies
- `pynput`: For keyboard event capture
- `socket`: For network communication
- `json`: For data serialization
- `threading`: For concurrent operations
- `py2app`: For macOS application packaging

### Network Configuration
- **Default Server**: `SET_AS_YOUR_IP:2000` (set as ip address of receiver)
- **Local Testing**: `127.0.0.1:2000` (commented out)
- **Protocol**: TCP Socket Communication
- **Data Format**: JSON-encoded strings

### Key Features Implementation
- **Backspace Handling**: Uses Unicode strikethrough characters (`\u0336`)
- **Special Key Mapping**: Converts keyboard events to readable format
- **Periodic Transmission**: Timer-based data sending
- **Error Handling**: Graceful connection failure management

## Usage (Educational Purposes Only)

### Running the Server
```bash
cd src
python receiver.py
```

### Running the Client
```bash
cd src
python keylogger2.py
```

### Building the macOS Application
```bash
cd src
python setup.py py2app
```

## Security Considerations

This project demonstrates several cybersecurity concepts:
- **Social Engineering**: Application disguised as "TypingRace"
- **Data Exfiltration**: Network transmission of sensitive data
- **Persistence**: Background operation without user awareness
- **Steganography**: Hidden functionality within legitimate-looking app

## Educational Value

This project serves as an example for:
- Understanding malware behavior patterns
- Learning about network-based data exfiltration
- Studying keystroke logging techniques
- Analyzing application packaging and disguise methods
- Cybersecurity awareness training

## Legal and Ethical Guidelines

- Only use on systems you own or have explicit written permission to monitor
- Comply with all local, state, and federal laws
- Respect privacy and confidentiality
- Use only for legitimate security research and education
- Do not use for malicious purposes

## License

This project is for educational use only. See course guidelines for specific usage terms and conditions.
