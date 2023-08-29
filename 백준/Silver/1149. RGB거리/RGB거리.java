import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		int[][] RGB = new int[N][3];
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			for (int j = 0; j < 3; j++) {
				RGB[i][j] = Integer.parseInt(st.nextToken());

			}

		}

		int[][] dp = new int[N][3];

		// 3 색으로 칠했을 때의 최솟값

		dp[0] = RGB[0];

		for (int i = 1; i < N; i++) {

			for (int j = 0; j < 3; j++) {
				int min_value = Integer.MAX_VALUE;
				for (int k = 0; k < 3; k++) {
					if (j == k)
						continue;

					min_value = Math.min(min_value, dp[i - 1][k]);
				}
				dp[i][j] = min_value + RGB[i][j];
			}
		}

//		System.out.println(Arrays.toString(dp[N - 1]));
		System.out.println(Math.min(dp[N - 1][0], Math.min(dp[N - 1][1], dp[N - 1][2])));
	}
}