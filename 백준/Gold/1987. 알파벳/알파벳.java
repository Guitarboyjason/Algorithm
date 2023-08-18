import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static char[][] map;
	static int R, C;
	static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		map = new char[R][C];

		for (int i = 0; i < R; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < C; j++) {
				map[i][j] = tmp.charAt(j);
			}
		}

//		boolean [][]visited = new boolean[R][C];
		visited = new boolean[26];
		visited[map[0][0] - 'A'] = true;
		System.out.println(dfs(0, 0, 1));

	}

	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	static int max_cnt = -1;

	static int dfs(int x, int y, int cnt) {
		if (cnt == R * C) {
//			System.out.println(cnt);
			max_cnt = cnt;
			return cnt;
		}

		visited[map[x][y] - 'A'] = true;
		int max_num = 0;
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];

			if (nx < 0 || nx >= R || ny < 0 || ny >= C) {
				continue;
			}
			if (!visited[map[nx][ny] - 'A']) {
				visited[map[nx][ny] - 'A'] = true;
				max_num = Math.max(max_num, dfs(nx, ny, cnt + 1));
				visited[map[nx][ny] - 'A'] = false;
			}

		}
		visited[map[x][y] - 'A'] = false;
		return Math.max(cnt, max_num);

	}
}