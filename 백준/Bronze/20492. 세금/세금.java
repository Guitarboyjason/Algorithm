import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int Price = sc.nextInt();
		System.out.println((int) (Price * 0.78) + " " + (int) (Price * 0.956));
	}
}