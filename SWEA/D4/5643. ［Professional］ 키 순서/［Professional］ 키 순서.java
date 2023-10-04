import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int M = Integer.parseInt(br.readLine());
//
//			ArrayList<Set<Integer>> arrayList = new ArrayList<>();
//			arrayList.add(new HashSet<>());
//			for (int i = 1; i <= N; i++) {
//				arrayList.add(new HashSet<>());
//				arrayList.get(i).add(i); // 처음걸 넣어줘
//			}
//			for (int i = 0; i < M; i++) {
//				StringTokenizer st = new StringTokenizer(br.readLine());
//				int a = Integer.parseInt(st.nextToken());
//				int b = Integer.parseInt(st.nextToken());
//
//				arrayList.get(b).addAll(arrayList.get(a));
//			}

			int[][] graph = new int[N + 1][N + 1];
			// 각 노드별로 이어지는지 아닌지를 1로 표기하자

			for (int i = 0; i < M; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());

				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());

				graph[a][b] = 1;
			} // 입력 완료

			// 이제 플로이드 와샬을 써볼까//

			// 쓸 때 다른 지점을 거쳐갈 수 있으면 거쳐가는걸로

			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (graph[i][j] != 1)
						graph[i][j] = Integer.MAX_VALUE / 2;
				}
			}

			// 이러고 경로를 구함

			for (int m = 1; m <= N; m++) {
				for (int i = 1; i <= N; i++) {
					for (int j = 1; j <= N; j++) {
						if (graph[i][j] > graph[i][m] + graph[m][j])
							graph[i][j] = graph[i][m] + graph[m][j];
					}
				}
			}

			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (graph[i][j] == Integer.MAX_VALUE / 2)
						graph[i][j] = 0;
				}
			}
//			for (int i = 0; i < N + 1; i++) {
//				System.out.println(Arrays.toString(graph[i]));
//			}

			int sum = 0;

			for (int i = 1; i <= N; i++) {
				int cnt = 0;
				for (int j = 1; j <= N; j++) {
					if (graph[i][j] != 0) {
						cnt += 1;
					}
					if (graph[j][i] != 0) {
						cnt += 1;
					}
				}
				if (cnt == N - 1)
					sum += 1;
			}
			System.out.println("#" + tc + " " + sum);

		}
	}
}