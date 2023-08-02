import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

//	static int T;
	static int SIZE = 1_000_000;
	static long[] dp = new long[SIZE + 1];

	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());

		pre_process();
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());

			sb.append(dp[N]).append("\n");

			// g(x) 는 x보다 작거나 같은 모든 자연수 y의 f(y)값을 더한 값
			// f(x)는 자연수 x의 약수의 합

			// 그럼 어떻게 진행하면 좋을까
			// 일단 하나씩 해보자

		}
		System.out.print(sb.toString().trim());
	}

	static void pre_process() {
//		Arrays.fill(1, dp);
		Arrays.fill(dp, 0); // 전체가 1이라는 약수를 갖고 있
		for (int i = 1; i <= SIZE; i++) {
			for (int j = 1; i * j <= SIZE; j++) {
				dp[i * j] += i;
			}
			dp[i] += dp[i - 1];
		}

//		for (int i = 0; i < 10; i++) {
//			System.out.println(dp[i]);
//		}
	}

}