#include <iostream>
#include <thread>
#include <vector>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h> // For read, write, and close

void handle_client(int client_socket)
{
    char buffer[1024] = {0};
    read(client_socket, buffer, 1024);
    std::cout << "Message from client: " << buffer << std::endl;

    // Echo back the message to the client
    write(client_socket, buffer, strlen(buffer));
    close(client_socket);
}

int main()
{
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);

    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    while (true)
    {
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0)
        {
            perror("accept");
            exit(EXIT_FAILURE);
        }

        // Use a lambda function to correctly handle passing of new_socket to the thread
        std::thread t([new_socket]()
                      { handle_client(new_socket); });
        t.detach(); // Detach the thread to run independently
    }

    return 0;
}
