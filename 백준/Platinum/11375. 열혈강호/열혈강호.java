import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static int[][] employee;
	static boolean[] c;
	static int[] works;
	// int형식으로 해서 0이면 비어있다.
	// 아니면

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		employee = new int[N + 1][];
		c = new boolean[M + 1];
		works = new int[M + 1];
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			int cnt_works = Integer.parseInt(st.nextToken());

			employee[i] = new int[cnt_works];

			for (int c = 0; c < cnt_works; c++) {
				employee[i][c] = Integer.parseInt(st.nextToken());
			} // 직원 i가 할 수 있는 일 c들
		}
		int cnt = 0;
		for (int w = 1; w <= N; w++) {

			Arrays.fill(c, false);
			if (dfs(w))
				cnt += 1;
//			System.out.println(Arrays.toString(works));
//			System.out.println(Arrays.toString(c));
		}
		System.out.println(cnt);
	}

	static boolean dfs(int cWorker) {
//		if (c[cWorker])
//			return false;
//		c[cWorker] = true;
		for (int w : employee[cWorker]) {
			if (c[w])
				continue;
			c[w] = true;
			if (works[w] == 0 || dfs(works[w])) {
				works[w] = cWorker;
				return true;
			}
//			c[w] = true;
		}
//		c[cWorker] = false;
		return false;
	}
}