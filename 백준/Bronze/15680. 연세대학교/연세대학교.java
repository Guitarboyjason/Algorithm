import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String s;
		if (n == 0) {
			s = "YONSEI";
		} else {
			s = "Leading the Way to the Future";
		}
		System.out.println(s);
	}

}