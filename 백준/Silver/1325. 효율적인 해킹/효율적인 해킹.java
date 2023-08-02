import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static int INF = Integer.MIN_VALUE;
	static int N, M;
	static boolean[] visited;
	static int[] costs;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		visited = new boolean[N + 1];

		for (int i = 0; i <= N; i++) { // 1부터 N까지 확인할거임
			graph.add(new ArrayList<Integer>()); // 배열 집어넣기
		}
		for (int i = 1; i <= M; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());

			graph.get(B).add(A); // 단방향 그래프 그리기
			// A 가 B 를 신뢰한다 니까 B에 넣어야겠음

		}
		costs = new int[N + 1];

//		int max_value = -1;
//		for (int i = 1; i < N + 1; i++) {
////			if (visited[i] == false)
//			costs[i] = bfs(i);
//			max_value = Math.max(max_value, costs[i]);
//		}

		int max = -1;
		for (int i = 1; i < N + 1; i++) {
//			max = Math.max(max, dfs(i));
			costs[i] = dfs(i);
			max = Math.max(max, costs[i]);
		}
//		for (int i = 1; i < N + 1; i++) {
//			System.out.println(costs[i]);
//		}

		StringBuilder sb = new StringBuilder();
		for (int i = 1; i < N + 1; i++) {
			if (costs[i] == max) {
				sb.append(i).append(" ");
			}
		}
		System.out.println(sb);

	}

	public static int dfs(int root) {
		boolean[] visited = new boolean[N + 1];

		Deque<Integer> stack = new ArrayDeque<>();

		stack.push(root);
		int cost = 0;
		visited[root] = true;
		while (!stack.isEmpty()) {
			int cNode = stack.pop();

			for (int nNode : graph.get(cNode)) {
				if (visited[nNode] == false) {
					visited[nNode] = true;
					stack.add(nNode);
					cost++;
				}
			}
//			if (visited)
		}
		return cost;

	}

//	public static int dfs(int root) {
//		int result = 0;
//		Queue<Integer> queue = new LinkedList<>();
//
//		queue.offer(root);
//		boolean[] visited = new boolean[N + 1];
//
//		while (!queue.isEmpty()) {
//			int tmp = queue.poll();
//
//			visited[tmp] = true;
//
//			for (int i = 0; i < graph.get(tmp).size(); i++) {
//				int nNode = graph.get(tmp).get(i);
//
//				if (!visited[nNode]) {
//
//					visited[nNode] = true;
//
//					result++;
//
//					queue.add(nNode);
//
//				}
//			}
//
//		}
//
//		int max_value = -1;
//		for (int i = 1; i <= N; i++) {
//			max_value = Math.max(max_value, costs[i]);
//
//		}
//		return result;
//	}

	public static int bfs(int root) {
		// 나오는 거리 최댓값을 리턴하는-걸로 바꾸자

		// 이게 왜 아님 왜 시간초과가 뜨는거임 ㄹㅇ로
		int[] costs = new int[N + 1];

		Deque<Integer> queue = new ArrayDeque<>();

//		int[] tmp = { root, 0 };
		queue.add(root);
		costs[root] = 0;
		visited = new boolean[N + 1];

		int max_value = -1;
		while (!queue.isEmpty()) {
			int cNode = queue.poll();
			int cCost = costs[cNode];
			visited[cNode] = true;

			for (int i = 0; i < graph.get(cNode).size(); i++) {
				int nNode = graph.get(cNode).get(i);

				if (costs[nNode] < cCost + 1 && visited[nNode] == false) {
					costs[nNode] = cCost + 1;
					queue.add(nNode);
//					costs[nNode] = cCost + 1;
					max_value = Math.max(max_value, cCost + 1);
				}
			}

		}
//		for (int i = 1; i <= N; i++) {
//			max_value = Math.max(max_value, costs[i]);
//
//		}
		return max_value;
	}
}