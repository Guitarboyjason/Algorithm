package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_1873_상호의_배틀필드 {
	static char[][] map;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int H, W;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			st = new StringTokenizer(br.readLine());
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());

			map = new char[H][W];
			for (int i = 0; i < H; i++) {
				map[i] = br.readLine().toCharArray();
			}

			int N = Integer.parseInt(br.readLine());

			char[] commands = br.readLine().toCharArray();

			int[] tmp = find_tank_position();
			int x = tmp[0];
			int y = tmp[1];
			int direction = find_tank_direction(x, y);
			// 상,하,좌,우

			for (char command : commands) {
				if (command == 'S') { // shoot
					shoot(x, y, direction);
				} else {
					int[] t_move = move(x, y, command);
					x = t_move[0];
					y = t_move[1];
					direction = t_move[2];
				}
			}
			System.out.print("#" + tc + " ");
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++)
					System.out.print(map[i][j]);
				System.out.println();
			}
		}
	}

	static int[] move(int x, int y, int command) {
		int d = -1;

		if (command == 'U') {
			d = 0;
		} else if (command == 'D') {
			d = 1;
		} else if (command == 'L') {
			d = 2;
		} else {
			d = 3;
		}
		int nx = x + dx[d];
		int ny = y + dy[d];

		if (0 > nx || nx >= H || 0 > ny || ny >= W || map[nx][ny] == '*' || map[nx][ny] == '#' || map[nx][ny] == '-') {
			return (new int[] { x, y, d }); // 이동 불가
		} else {
			map[x][y] = '.';
			if (d == 0)
				map[nx][ny] = '^';
			if (d == 1)
				map[nx][ny] = 'v';
			if (d == 2)
				map[nx][ny] = '<';
			if (d == 3)
				map[nx][ny] = '>';
			return (new int[] { nx, ny, d }); // 이동
		}
	}

	static void shoot(int x, int y, int direction) {
		int nx = x;
		int ny = y;

		while (0 <= nx && nx < H && 0 <= ny && ny < W) {
			nx += dx[direction];
			ny += dy[direction];
			if (map[nx][ny] == '.') {
				continue;
			}
			if (map[nx][ny] == '#') {
				return;
			}
			if (map[nx][ny] == '*') {
				map[nx][ny] = '.';
				return;
			}
		}
		return;
	}

	static int[] find_tank_position() {
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (map[i][j] == '<' || map[i][j] == '^' || map[i][j] == 'v' || map[i][j] == '>') {
					return (new int[] { i, j });
				}
			}
		}
		return (new int[] { 0, 0, });
	}

	static int find_tank_direction(int x, int y) {
		if (map[x][y] == '^') {
			return 0;

		}
		if (map[x][y] == 'v') {
			return 1;

		}
		if (map[x][y] == '<') {
			return 2;

		}
		if (map[x][y] == '>') {
			return 3;

		}
		return -1;
	}
}
