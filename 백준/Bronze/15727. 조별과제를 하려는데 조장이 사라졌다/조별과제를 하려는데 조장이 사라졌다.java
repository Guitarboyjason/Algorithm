import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int L = sc.nextInt();
		System.out.println((L / 5 + (L % 5 != 0 ? 1 : 0)));
	}
}