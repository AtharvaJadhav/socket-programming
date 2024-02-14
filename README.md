# Client-Server Socket Programming

This repository contains basic examples of client-server socket programming in Python, C++, and Java. The examples demonstrate how to set up a TCP server that can handle multiple client connections concurrently and a client that can connect to the server, send messages, and receive responses. The primary focus is on establishing a foundation for network programming across different programming languages, showcasing simple communication between a client and a server.

## Contents

- **Python**: Simple server and client that use the built-in `socket` library for communication.
- **C++**: Demonstrates server-client communication using POSIX socket programming.
- **Java**: Implementation of server-client communication using Java's `java.net` library.

## How to Run the Examples

### Python

#### Requirements

- Python 3.x

#### Running the Server

```sh
python server.py
```

#### Running the Client

```sh
python client.py
```

### C++

#### Requirements

- A C++ compiler supporting C++11 (e.g., GCC, Clang)
- Make sure to have the POSIX environment for socket programming

#### Compiling and Running the Server

```sh
g++ -o server server.cpp -pthread
./server
```

#### Compiling and Running the Client

```sh
g++ -o client client.cpp
./client
```

### Java

#### Requirements

- Java Development Kit (JDK)

#### Compiling and Running the Server

```sh
javac Server.java
java Server
```

#### Compiling and Running the Client

```sh
javac Client.java
java Client
```

## Inter-Language Communication

As of now, the examples provided focus on communication between a client and server written in the same programming language. Inter-language communication, i.e., a client written in one language communicating with a server written in another, has not yet been achieved in this repository. This functionality may be explored in future updates, considering the universal nature of TCP/IP protocols that allow for such interoperability.

## Conclusion

This repository serves as a starting point for those interested in the basics of network programming and socket communication across different programming languages. Whether you're a beginner or looking to refresh your knowledge, these examples provide a practical understanding of how clients and servers interact over a network.
