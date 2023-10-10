import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] room;
	static int R, C, T;
	static int[][] cleaner;

	public static void main(String[] args) throws IOException {
		// 미세먼지는 공청기가 있거나 칸이 없는 경우를 제외하면 다 확산이 된다.
		// 확산되는 양은 (미세먼지 양) / 5 이고 소숫점은 버린다.
		// 남은 미세먼지의 양은 (미세먼지 양 - (미세먼지 /5) * 확산된 갯수)

		// 공청기 작동
		// 공청기 위로는 반시계
		// 공청기 아래로는 시계방향
		input();

		for (int i = 0; i < T; i++) {
			spread_dust();
			airCleaner();
		}

		System.out.println(countDust());

//		for (int i = 0; i < R; i++) {
//			System.out.println(Arrays.toString(room[i]));
//		}

	}

	static int[] dx = { -1, 0, 0, 1 };
	static int[] dy = { 0, -1, 1, 0 };

	static int[] circular_x = { -1, 0, 1, 0 };
	static int[] circular_y = { 0, 1, 0, -1 };

	static int[] reverse_x = { 1, 0, -1, 0 };
	static int[] reverse_y = { 0, 1, 0, -1 };

	public static int countDust() {
		int cnt = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (room[i][j] != -1)
					cnt += room[i][j];
			}
		}
		return cnt;
	}

	public static void airCleaner() {
		// 위는 반시계방향
		// 아래는 시계방향

		// 위쪽
		// 반시계방향이니까 시계방향으로 돌면서 값을 덮어씌우면 되겠다.

		int clean_spot_x = cleaner[0][0] + circular_x[0];
		int clean_spot_y = cleaner[0][1] + circular_y[0];

//		while(clean_spot_x != cleaner[0][0] || cleaner[])
		for (int d = 0; d < 4; d++) {
			while (true) {
				if (clean_spot_x + circular_x[d] > cleaner[0][0] || clean_spot_x + circular_x[d] < 0
						|| clean_spot_y + circular_y[d] < cleaner[0][1] || clean_spot_y + circular_y[d] >= C
						|| room[clean_spot_x + circular_x[d]][clean_spot_y + circular_y[d]] == -1) {
					break; // 범위를 벗어나거나 마지막까지 다다르면 그만
				}

				room[clean_spot_x][clean_spot_y] = room[clean_spot_x + circular_x[d]][clean_spot_y + circular_y[d]];// 덮어씌운다.
				clean_spot_x = clean_spot_x + circular_x[d];
				clean_spot_y = clean_spot_y + circular_y[d];
			}

		}

		clean_spot_x = cleaner[1][0] + reverse_x[0];
		clean_spot_y = cleaner[1][1] + reverse_y[0];

		for (int d = 0; d < 4; d++) {
			while (true) {
				if (clean_spot_x + reverse_x[d] < cleaner[1][0] || clean_spot_x + reverse_x[d] >= R
						|| clean_spot_y + reverse_y[d] < 0 || clean_spot_y + reverse_y[d] >= C
						|| room[clean_spot_x + reverse_x[d]][clean_spot_y + reverse_y[d]] == -1) {
					break; // 범위를 벗어나거나 마지막까지 다다르면 그만
				}

				room[clean_spot_x][clean_spot_y] = room[clean_spot_x + reverse_x[d]][clean_spot_y + reverse_y[d]];// 덮어씌운다.
				clean_spot_x = clean_spot_x + reverse_x[d];
				clean_spot_y = clean_spot_y + reverse_y[d];
			}

		}

		room[cleaner[0][0]][cleaner[0][1] + 1] = 0;
		room[cleaner[1][0]][cleaner[1][1] + 1] = 0;

		// 아래쪽
	}

	public static void spread_dust() {
		// -1로 이루어져있지 않고, 칸이 있는 곳에 확산이 된다.
		// 모든 칸에서 동시에 이루어지니까 하나 새로 만들어서 거기다 추가하는 방식으로 해야겠다.

		int[][] nRoom = new int[R][C];
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (room[i][j] > 0) { // 미세먼지가 존재
					// 네 방향으로 확산
					int cnt = 0;
					for (int d = 0; d < 4; d++) {
						int nx = i + dx[d];
						int ny = j + dy[d];

						if (nx < 0 || nx >= R || ny < 0 || ny >= C || room[nx][ny] == -1)
							continue;

						cnt++;

						nRoom[nx][ny] += room[i][j] / 5;

					}
					nRoom[i][j] += room[i][j] - (room[i][j] / 5) * cnt;
				}
				if (room[i][j] == -1)
					nRoom[i][j] = -1;
			}
		}

		for (int i = 0; i < R; i++) {
			room[i] = nRoom[i].clone();
		}
		// 확산 완료
	}

	static int idx = 0;

	public static void input() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		T = Integer.parseInt(st.nextToken());

		cleaner = new int[2][2];
		room = new int[R][C];
		for (int i = 0; i < R; i++) {
			st = new StringTokenizer(br.readLine());

			for (int j = 0; j < C; j++) {
				room[i][j] = Integer.parseInt(st.nextToken());
				if (room[i][j] == -1) {
					cleaner[idx][0] = i;
					cleaner[idx++][1] = j;
				}
			}
		} // 입력 완료
	}
}