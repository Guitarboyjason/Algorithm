import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N, B;
		N = sc.nextInt();
		B = sc.nextInt();
		HashMap<String, String> dictionary = new HashMap<String, String>();
		for (int i = 65; i < 91; i++) {
			dictionary.put(Integer.toString(i - 55), Character.toString((char) i));
		}
		for (int i = 0; i < 10; i++) {
			dictionary.put(Integer.toString(i), Integer.toString(i));
		}

//		System.out.println((int) 'A');
//		char A = (char) 65;
//		System.out.println(A);
//		System.out.println((String)A)

		String answer = "";
		while (N != 0) {
			int tmp;
			tmp = N % B;
			answer = dictionary.get(Integer.toString(tmp)) + answer;
			N /= B;
		}
		System.out.println(answer);

	}

}
