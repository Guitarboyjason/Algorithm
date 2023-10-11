import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int[] dots;
	static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			N = Integer.parseInt(br.readLine());

			dots = new int[N];
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());

				int tmp = Math.abs(Integer.parseInt(st.nextToken()));
				dots[i] = tmp + Math.abs(Integer.parseInt(st.nextToken()));

			}
			// 입력 완료

			int cnt = 0;
			System.out.print("#" + tc + " ");
			if (!one_side()) // 절대 갈 수 없음
				System.out.println(-1);
			else {
				int maxNum = find_max_num();

				while (maxNum != 0) {
					cnt++;
					maxNum -= cnt;

					if (maxNum < 0) {
						if (maxNum % 2 == 0)
							maxNum = 0;
						else
							maxNum = 1;
					}

				}
				System.out.println(cnt);
			}

		}
	}

	public static int find_max_num() {
		int tmp = -1;

		for (int i = 0; i < N; i++) {
			if (dots[i] > tmp)
				tmp = dots[i];
		}
		return tmp;
	}

	public static boolean one_side() {
		boolean odd = false;
		boolean even = false;
		for (int i = 0; i < N; i++) {
			if (dots[i] % 2 == 1)
				odd = true;
			else
				even = true;
		}

		if (odd && even)
			return false;
		return true;
	}
}