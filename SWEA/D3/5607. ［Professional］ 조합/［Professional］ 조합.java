import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	static StringBuilder sb = new StringBuilder();
	static long P = 1234567891;

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int N = Integer.parseInt(st.nextToken());
			int R = Integer.parseInt(st.nextToken());

			long[] divs = new long[N + 1];
			divs[0] = 1;


			for (int i = 1; i <= N; i++) {
				divs[i] = (divs[i - 1] * i) % 1234567891;
			}
			// N!이 나온다

//			long tmp1 = 1;
//			long tmp2 = 1;
			long tmp1 = div(divs[R], P - 2);
			long tmp2 = div(divs[N - R], P - 2);
//			for (int i = 0; i < 1234567891 - 2; i++) {
//				tmp1 *= divs[R];
//				tmp1 %= 1234567891;
//
//				tmp2 *= divs[N - R];
//				tmp2 %= 1234567891;
//			}
			sb.append("#").append(tc).append(" ").append((((divs[N] * tmp1) % P) * tmp2) % P).append("\n");
		}

		System.out.println(sb);
	}

	public static long div(long base, long exp) {
		long r = 1;

		while (exp > 0) {
			if (exp % 2 == 1) {
				r = (r * base) % P;
				exp -= 1;

			}

			base = (base * base) % P;
			exp >>= 1;

		}
		return r % P;
	}

}