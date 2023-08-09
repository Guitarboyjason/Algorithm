import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static StringTokenizer st;
	static boolean[][] board;

	public static void main(String[] args) throws IOException {
		board = new boolean[100][100];
//		Arrays.fill(board, false);

		int N = Integer.parseInt(br.readLine());
		int cnt = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			for (int j = x; j < x + 10; j++) {
				for (int k = y; k < y + 10; k++) {
					board[j][k] = true;
				}
			}

		}
		for (int j = 0; j < 100; j++) {
			for (int k = 0; k < 100; k++) {
				if (board[j][k] == true)
					cnt++;
			}
		}
		System.out.println(cnt);
	}
}