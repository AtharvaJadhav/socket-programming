
// Client.java
import java.io.*;
import java.net.*;

public class Client {
    private static final String HOST = "127.0.0.1";
    private static final int PORT = 65432; // Match the server port

    public static void main(String[] args) {
        try (Socket socket = new Socket(HOST, PORT);
                PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in))) {

            System.out.println("Connected to the server");
            String text;
            while (true) {
                System.out.print("Enter message ('bye' to quit): ");
                text = consoleReader.readLine();

                if ("bye".equalsIgnoreCase(text)) {
                    break;
                }

                writer.println(text); // Send message to the server
                String response = reader.readLine(); // Read the response from the server
                System.out.println("Server response: " + response);
            }
        } catch (UnknownHostException ex) {
            System.out.println("Server not found: " + ex.getMessage());
        } catch (IOException ex) {
            System.out.println("I/O error: " + ex.getMessage());
        }
    }
}
