import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		A = B - A;
		for (int i = 9; i >= 1; i--) {
			if (A % i == 0 && B % i == 0) {
				A /= i;
				B /= i;
			}
		}
		System.out.println(A + " " + B);
	}
}