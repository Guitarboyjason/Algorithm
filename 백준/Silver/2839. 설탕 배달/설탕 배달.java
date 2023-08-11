import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int cnt_5 = 0;
		cnt_5 += N / 5;
		N %= 5;
		int cnt_3 = 0;
		cnt_3 += N / 3;
		N %= 3;
		while (N != 0) {
			if (cnt_5 > 0) {
				cnt_5 -= 1;
				N += 5;
				cnt_3 += N / 3;
				N %= 3;
			} else {
				cnt_5 = -1;
				cnt_3 = 0;
				N = 0;
			}
		}
		System.out.println(cnt_5 + cnt_3);
	}
}