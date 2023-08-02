import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	static int[][] graph;
//	static Deque<ArrayList<Integer>> directions = new ArrayDeque<>();
	static int[][] directions = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

	public static void main(String[] args) throws IOException {
		int T = Integer.parseInt(br.readLine());

		for (int testCase = 1; testCase <= T; testCase++) {
			int N = Integer.parseInt(br.readLine());
			snail(N);
			System.out.println("#" + testCase);

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					System.out.print(graph[i][j] + " ");
				}
				System.out.println();
			}
		}
	}

//	static int [][] direction = {{0,1},{1,0},{

	public static void snail(int n) {
		graph = new int[n][n];
//		directions = new ArrayDeque<>(); // 초기화

//		directions.add(new ArrayList<>());
//		directions.add(new ArrayList<>());
//		directions.add(new ArrayList<>());
//		directions.add(new ArrayList<>());
//		ArrayList<Integer> tmp = new ArrayList<>();
//		tmp.add(0);
//		tmp.add(1);
		graph[0][0] = 1;
		int idx = 0;
		int cnt = 1;

		// 저장 다 했으면 실행하자
		int x = 0;
		int y = 0;
		while (cnt < n * n) {
//			ArrayList<Integer> t_tmp = directions[idx];
			int nx = directions[idx][0] + x;
			int ny = directions[idx][1] + y;

			if (0 <= nx && nx < n && 0 <= ny && ny < n && graph[nx][ny] == 0) {
				graph[nx][ny] = ++cnt;
//				directions.push(t_tmp);
				x = nx;
				y = ny;
			} else {
//				
				idx = (idx + 1) % 4;
//				
			}

		}
	}
}