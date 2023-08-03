import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[] books;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
//	static int books;
	static boolean[] done;
	static int[][] students;

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());
		for (int testCase = 0; testCase < T; testCase++) {
			st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			books = new int[N + 1];
			Arrays.fill(books, 0);
			done = new boolean[N + 1];

			students = new int[M + 1][2];
			for (int i = 1; i <= M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				students[i][0] = a;
				students[i][1] = b;

			}

			int cnt = 0;
			for (int i = 1; i <= M; i++) {

				Arrays.fill(done, false);
				if (dfs(i))
					cnt++;
			}
			System.out.println(cnt);

		}
	}

	static boolean dfs(int student) {

//		for(int b : students[student])
		int start = students[student][0];
		int end = students[student][1];

		for (int i = start; i <= end; i++) {
			if (done[i]) {
				continue;
			}
			done[i] = true;
			if (books[i] == 0 || dfs(books[i])) {
				books[i] = student;
				return true;
			}
		}
		return false;
	}
}