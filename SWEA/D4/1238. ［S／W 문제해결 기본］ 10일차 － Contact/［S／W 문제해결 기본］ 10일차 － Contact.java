import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	// bfs 인 것 같음

	static int cnt = 0;
	static int last = -1;
	static ArrayList<ArrayList<Integer>> graph;
	static int N;

	public static void main(String[] args) throws IOException {
		int T = 10;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int tc = 1; tc <= 10; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());

			int start = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());

//			ArrayList<>
			graph = new ArrayList<>();
			for (int i = 0; i <= 100; i++)
				graph.add(new ArrayList<>());
			for (int i = 0; i < N / 2; i++) {
				int from = Integer.parseInt(st.nextToken());
				int to = Integer.parseInt(st.nextToken());

				graph.get(from).add(to);
			}

			// 전체 bfs로 순회하면서 마지막에 나오는 걸 확인함

			bfs(start);
			System.out.println("#" + tc + " " + last);
		}
	}

	static void bfs(int start) {

		Queue<int[]> queue = new ArrayDeque<>();

		queue.offer(new int[] { start, 0 });

		boolean[] visited = new boolean[101];
//		visited[]
		visited[start] = true;
		while (!queue.isEmpty()) {
			int[] tmp = queue.poll();
			if (tmp[1] > cnt || tmp[0] > last) // 어차피 무조건 cnt가 더 작거나 같다
				last = tmp[0];

			cnt = tmp[1];

			for (int i = 0; i < graph.get(tmp[0]).size(); i++) {
//				graph.get(i)
				if (!visited[graph.get(tmp[0]).get(i)]) {
					visited[graph.get(tmp[0]).get(i)] = true;
					queue.offer(new int[] { graph.get(tmp[0]).get(i), cnt + 1 });
				}
			}

		}
	}

}