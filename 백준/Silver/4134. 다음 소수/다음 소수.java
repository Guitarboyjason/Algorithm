import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class Main {
//	1_000_000_000
//	static long SIZE = 4 * 1_000_000_000;'
//	static long SIZE = new long(4_000_000_001);
//	static boolean[] primeNums = new boolean[SIZE];

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {

		int T = Integer.parseInt(br.readLine());
		for (int testCase = 0; testCase < T; testCase++) {
			long n = Long.parseLong(br.readLine());

			BigInteger bigNum = new BigInteger(String.valueOf(n));
			if (bigNum.isProbablePrime(10)) {
				sb.append(bigNum);
			} else {
				sb.append(bigNum.nextProbablePrime());
			}
			sb.append("\n");
		}
		System.out.print(sb);

	}
}