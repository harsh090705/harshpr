import java.util.Scanner; // Import the Scanner class

public class Addition {
    public static void main(String[] args) {
        // Create a Scanner object to read input
        Scanner sc = new Scanner(System.in);

        System.out.println("--- Simple Addition Program ---");

        // Input first number
        System.out.print("Enter the first number: ");
        int num1 = sc.nextInt();

        // Input second number
        System.out.print("Enter the second number: ");
        int num2 = sc.nextInt();

        // Perform addition
        int sum = num1 + num2;

        // Display the result
        System.out.println("\nThe sum of " + num1 + " and " + num2 + " is: " + sum);

        // Close the scanner to prevent memory leaks
        sc.close();
    }
}
