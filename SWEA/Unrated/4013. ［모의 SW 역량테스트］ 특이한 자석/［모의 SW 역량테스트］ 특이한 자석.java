import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
	static int[] pointers;
	static ArrayList<char[]> magnets;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			int K = Integer.parseInt(br.readLine());

//			StringTokenizer st = new StringTokenizer(br.readLine());

			magnets = new ArrayList<>();
//			if (tc == 2) {
//				System.out.println(1);
//			}
			for (int i = 0; i < 4; i++) {
				magnets.add(new char[8]);
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < 8; j++) {
					magnets.get(i)[j] = st.nextToken().charAt(0);
				}
			}
			// 포인터를 기준으로 +2 에 오른쪽, +6 위치에 왼쪽 자석이 있다.

			pointers = new int[4];
			for (int i = 0; i < 4; i++) {
				pointers[i] = 0;
			} // 초기화
			int score = 0;
//			boolean[] visited = new boolean[4];
			for (int q = 0; q < K; q++) {
				StringTokenizer st = new StringTokenizer(br.readLine());

				int magnetNum = Integer.parseInt(st.nextToken());
				int direction = Integer.parseInt(st.nextToken());
				boolean[] visited = new boolean[4];
				visited[magnetNum - 1] = true;
				turn(magnetNum - 1, direction, visited);

			}
			for (int p = 0; p < 4; p++) {
				// 각 포인터마다 자석에 접근해서 해당 위치에 1이면 2**(p-1)정도 하면 될 듯

				if (magnets.get(p)[pointers[p]] == '1') {
					score += Math.pow(2, p);
				}

			}
			System.out.println("#" + tc + " " + score);

		}
	}

	public static void turn(int magnetNum, int direction, boolean[] visited) {

		// 만약 다른데도 움직일 수 있다면 걔의 num 과 반대 direction을 넣어서 구현하자
		// 1이면 시계방향으로 돌리니까 pointer는 반대로 돌아가야함

//		

		// 만약 왼쪽이 있다면
		if (magnetNum > 0) {
			// 만약 왼쪽의 pointer +2 와 현재 보고있는 포인터 +6이 다르다면

			if (!visited[magnetNum - 1] && magnets.get(magnetNum)[(pointers[magnetNum] + 6) % 8] != magnets
					.get(magnetNum - 1)[(pointers[magnetNum - 1] + 2) % 8]) {
				visited[magnetNum - 1] = true;
				turn(magnetNum - 1, -direction, visited);
				visited[magnetNum - 1] = false;
			}

		}

		if (magnetNum < 3) {
			if (!visited[magnetNum + 1] && magnets.get(magnetNum + 1)[(pointers[magnetNum + 1] + 6) % 8] != magnets
					.get(magnetNum)[(pointers[magnetNum] + 2) % 8]) {
				visited[magnetNum + 1] = true;
				turn(magnetNum + 1, -direction, visited);
				visited[magnetNum + 1] = false;

			}

		}

		// 이제 돌리자

//		System.out.println(-1 % 8);

		pointers[magnetNum] = (8 + pointers[magnetNum] - direction) % 8;
		// 끝

	}
}