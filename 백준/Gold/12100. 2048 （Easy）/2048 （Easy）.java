import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int max_cnt = 0;
	static int N;
	static int[] done_directions = new int[6];

	public static void main(String[] args) throws IOException {
		N = Integer.parseInt(br.readLine());
		int[][] board = new int[N][N];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		game(board, 0, 0);
		System.out.println(max_cnt);

	}

	static int[] dx = { 0, 0, -1, 1 };
	static int[] dy = { -1, 1, 0, 0 };

	public static void game(int[][] board, int cnt, int idx) {

		int[][] t_board = board.clone();
		for (int i = 0; i < N; i++) {
			t_board[i] = board[i].clone();
		}

		if (cnt == 5) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					max_cnt = Math.max(max_cnt, board[i][j]);
				}
			}
//			if (done_directions[0] == 3 && done_directions[1] == 1 && done_directions[2] == 1 && done_directions[3] == 3
//					&& done_directions[4] == 1)
////				System.out.println(1);
////			System.out.println();
//				for (int i = 0; i < N; i++)
//					System.out.println(Arrays.toString(board[i]));
//			if (max_cnt == 128)
//				System.out.println(1);
			return;
		}

		// 먼저 이동한 애들을 확인해야하는데..
		for (int d = 0; d < 4; d++) {
			boolean[][] sumChecker = new boolean[N][N];
			done_directions[idx] = d;
			int nx = dx[d];
			int ny = dy[d];
			switch (d) {
			case 0:
				// 왼쪽
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						int t_i = i;
						int t_j = j;
						// 이동할 때 원래 자리에 0 을 집어넣고 이동, 벽이 아닌 다른 숫자가 나왔을 때
						// 그 숫자가 같은 숫자면 합치고 현재 위치는 0
						if (board[i][j] == 0) // 0이면 굳이 확인할 필요 없다.
							continue;
						while (0 <= i + nx && i + nx < N && 0 <= j + ny && j + ny < N) {
							if (board[i + nx][j + ny] == 0) {
								board[i + nx][j + ny] = board[i][j]; // 이동하려는 위치에 현재 값을 넣음
								board[i][j] = 0;
							}

							else if (board[i + nx][j + ny] == board[i][j] && !sumChecker[i + nx][j + ny]) {
								// 합쳐야하긴하는데 한번 합쳐진애는 합치면 안돼
								// 한번 합쳤는지 아닌지를 어떻게 알까
								// checker에 좌표를 저장해두자

								board[i + nx][j + ny] += board[i][j];// 원래 있던 애 합치고
								board[i][j] = 0; // 0으로 만듦
								sumChecker[i + nx][j + ny] = true;
								// 여기까지 왔으면 사실 더 이상 이동할 수 없음
								break;

							} else {
								break; // 아무곳도 이동 못할 때 탈출
							}
							i += nx; // 좌표 이동
							j += ny; // 좌표 이동

						}
						i = t_i;
						j = t_j;

					}
				}

				break;
			case 1:
				// 오른쪽 부터 확인해야 한다.

				for (int i = 0; i < N; i++) {
					for (int j = N - 1; j >= 0; j--) {
						int t_i = i;
						int t_j = j;
						// 이동할 때 원래 자리에 0 을 집어넣고 이동, 벽이 아닌 다른 숫자가 나왔을 때
						// 그 숫자가 같은 숫자면 합치고 현재 위치는 0
						if (board[i][j] == 0) // 0이면 굳이 확인할 필요 없다.
							continue;
						while (0 <= i + nx && i + nx < N && 0 <= j + ny && j + ny < N) {
							if (board[i + nx][j + ny] == 0) {
								board[i + nx][j + ny] = board[i][j]; // 이동하려는 위치에 현재 값을 넣음
								board[i][j] = 0;
							}

							else if (board[i + nx][j + ny] == board[i][j] && !sumChecker[i + nx][j + ny]) {
								// 합쳐야하긴하는데 한번 합쳐진애는 합치면 안돼
								// 한번 합쳤는지 아닌지를 어떻게 알까
								// checker에 좌표를 저장해두자

								board[i + nx][j + ny] += board[i][j];// 원래 있던 애 합치고
								board[i][j] = 0; // 0으로 만듦
								sumChecker[i + nx][j + ny] = true;
								// 여기까지 왔으면 사실 더 이상 이동할 수 없음
								break;
							} else {
								break; // 아무곳도 이동 못할 때 탈출
							}
							i += nx; // 좌표 이동
							j += ny; // 좌표 이동

						}

						i = t_i;
						j = t_j;

					}
				}

				break;
			case 2:
				// 위쪽

				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						int t_i = i;
						int t_j = j;
						// 이동할 때 원래 자리에 0 을 집어넣고 이동, 벽이 아닌 다른 숫자가 나왔을 때
						// 그 숫자가 같은 숫자면 합치고 현재 위치는 0
						if (board[i][j] == 0) // 0이면 굳이 확인할 필요 없다.
							continue;
						while (0 <= i + nx && i + nx < N && 0 <= j + ny && j + ny < N) {
							if (board[i + nx][j + ny] == 0) {
								board[i + nx][j + ny] = board[i][j]; // 이동하려는 위치에 현재 값을 넣음
								board[i][j] = 0;
							}

							else if (board[i + nx][j + ny] == board[i][j] && !sumChecker[i + nx][j + ny]) {
								// 합쳐야하긴하는데 한번 합쳐진애는 합치면 안돼
								// 한번 합쳤는지 아닌지를 어떻게 알까
								// checker에 좌표를 저장해두자

								board[i + nx][j + ny] += board[i][j];// 원래 있던 애 합치고
								board[i][j] = 0; // 0으로 만듦
								sumChecker[i + nx][j + ny] = true;
								// 여기까지 왔으면 사실 더 이상 이동할 수 없음
								break;
							} else {
								break; // 아무곳도 이동 못할 때 탈출
							}
							i += nx; // 좌표 이동
							j += ny; // 좌표 이동

						}

						i = t_i;
						j = t_j;

					}
				}

				break;
			case 3:
				// 아래쪽 // x가 커진다. // 큰 수부터 이동하는걸 확인해야해
//				if (done_directions[0] == 3)
//					System.out.println(1);
				for (int i = N - 1; i >= 0; i--) {
					for (int j = 0; j < N; j++) {
						int t_i = i;
						int t_j = j;
						// 이동할 때 원래 자리에 0 을 집어넣고 이동, 벽이 아닌 다른 숫자가 나왔을 때
						// 그 숫자가 같은 숫자면 합치고 현재 위치는 0
						if (board[i][j] == 0) // 0이면 굳이 확인할 필요 없다.
							continue;
						while (0 <= i + nx && i + nx < N && 0 <= j + ny && j + ny < N) {
							if (board[i + nx][j + ny] == 0) {
								board[i + nx][j + ny] = board[i][j]; // 이동하려는 위치에 현재 값을 넣음
								board[i][j] = 0;
							}

							else if (board[i + nx][j + ny] == board[i][j] && !sumChecker[i + nx][j + ny]) {
								// 합쳐야하긴하는데 한번 합쳐진애는 합치면 안돼
								// 한번 합쳤는지 아닌지를 어떻게 알까
								// checker에 좌표를 저장해두자

								board[i + nx][j + ny] += board[i][j];// 원래 있던 애 합치고
								board[i][j] = 0; // 0으로 만듦
								sumChecker[i + nx][j + ny] = true;
								// 여기까지 왔으면 사실 더 이상 이동할 수 없음
								break;
							} else {
								break; // 아무곳도 이동 못할 때 탈출
							}
							i += nx; // 좌표 이동
							j += ny; // 좌표 이동

						}

						i = t_i;
						j = t_j;

					}
				}

				break;

			}

			game(board, cnt + 1, idx + 1);
			for (int i = 0; i < N; i++) {
				board[i] = t_board[i].clone();
			}
		}
	}
}