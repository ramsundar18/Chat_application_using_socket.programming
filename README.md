# Chat Application

A simple chat application built using Python's `socket` and `select` modules. This project consists of a server-side script that handles multiple clients and a client-side script that allows users to connect to the server and send/receive messages.

## Features

- **Real-time messaging:** Send and receive messages in real-time between clients.
- **Multiple clients:** The server can handle multiple client connections simultaneously.
- **Simple CLI interface:** Both server and client have a basic command-line interface for interaction.

## Components

- **Chat Server**: A multi-client server that listens on a specific port for incoming client connections and broadcasts messages to all connected clients.
- **Chat Client**: A command-line client that connects to the server, sends messages, and displays incoming messages.

## Requirements

- Python 3.x
- Basic understanding of socket programming and networking concepts.

## How to Use

### Chat Server

1. Clone the repository or download the `chat_server.py` script.
2. Run the server script on the desired host machine.

   ```bash
   python3 chat_server.py
   ```

3. The server will start listening for connections on port `9999` (default). You can change the port in the script if needed.

### Chat Client

1. Clone the repository or download the `chat_client.py` script.
2. Run the client script by providing the server's IP address and port as command-line arguments:

   ```bash
   python3 chat_client.py <hostname> <port>
   ```

   For example, if the server is running on `127.0.0.1` (localhost) and port `9999`, you can run:

   ```bash
   python3 chat_client.py 127.0.0.1 9999
   ```

3. Once connected, you can start typing messages. To exit the chat, simply close the terminal or interrupt the program with `Ctrl+C`.
