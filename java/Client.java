// Client.java
import java.io.*;
import java.net.*;

public class Client {
    private static final String HOST = "127.0.0.1";
    private static final int PORT = 8080;

    public static void main(String[] args) {
        try (Socket socket = new Socket(HOST, PORT)) {
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            System.out.println("Connected to the server");

            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in));
            String text;
            do {
                System.out.print("Enter message ('bye' to exit): ");
                text = consoleReader.readLine();
                writer.println(text);
                String response = reader.readLine();
                System.out.println("Server response: " + response);
            } while (!text.equals("bye"));
        } catch (UnknownHostException ex) {
            System.out.println("Server not found: " + ex.getMessage());
        } catch (IOException ex) {
            System.out.println("I/O error: " + ex.getMessage());
        }
    }
}
