import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int N;
	static int[][] cave;
	static int[][] dijk;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		int problem_num = 1;
		while (N != 0) {
			cave = new int[N][N];

			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					cave[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			dijkstra();

//			for (int i = 0; i < N; i++) {
//				System.out.println(Arrays.toString(dijk[i]));
//			}

//			System.out.println();
			sb.append("Problem " + (problem_num++) + ": " + dijk[N - 1][N - 1]).append("\n");

			// 최소비용을 알아야함. 한 위치에서 다른 위치로 도달하는 방법에 대한 걸 그래프로 나타낸다면
			// 그냥 0,0 에서부터 출발해서 어떻게 최종까지 도달할 수 있을지를 보자
			N = Integer.parseInt(br.readLine());
		}
		System.out.println(sb);
	}

	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { 1, 0, -1, 0 };

	public static void dijkstra() {
		dijk = new int[N][N];

		// 오른쪽, 아래만 보면되겠다.
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				dijk[i][j] = Integer.MAX_VALUE / 2;
			}
		}

		dijk[0][0] = cave[0][0];
		Queue<int[]> queue = new ArrayDeque<>();

		queue.offer(new int[] { 0, 0 });

		while (!queue.isEmpty()) {
			int[] tmp = queue.poll();
			int x = tmp[0];
			int y = tmp[1];
			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];

				if (nx < 0 || nx >= N || ny < 0 || ny >= N)
					continue;
				if (dijk[nx][ny] > dijk[x][y] + cave[nx][ny]) {
					dijk[nx][ny] = dijk[x][y] + cave[nx][ny];
					queue.offer(new int[] { nx, ny });
				}
			}

		}

	}
}