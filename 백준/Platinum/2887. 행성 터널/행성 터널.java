import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	// 얘는 prim으로 해보자
	// 정점의 정보를 저장하고

	// 1. 임의의 점을 선택
	// 2. 해당 점에서 다른 모든 점으로의 거리들을 priority queue에 넣음
	// 3. queue에서 가장 짧은 거리를 꺼내면서 확인
	static ArrayList<long[]> graph;
	static int[] parent;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		graph = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			long x = Long.parseLong(st.nextToken());
			long y = Long.parseLong(st.nextToken());
			long z = Long.parseLong(st.nextToken());

			graph.add(new long[] { i, x, y, z });
		}

		// x,y,z 각각의 축을 기준으로 정렬을 한 뒤, 양옆의 노드들끼리의 거리를 집어넣는다

		// 각 축마다 양옆의 거리들을 확인한다.
		// 한번에 모든 축에 대해 다 넣어도 되겠다.

		PriorityQueue<long[]> queue = new PriorityQueue<>((o1, o2) -> o1[2] > o2[2] ? 1 : -1);

		for (int c = 1; c <= 3; c++) {
			final int d = c;
			Collections.sort(graph, (o1, o2) -> o1[d] > o2[d] ? 1 : -1); // x축 기준 정렬
			// 정렬
			for (int i = 0; i < N - 1; i++) {
				queue.add(new long[] { graph.get(i)[0], graph.get(i + 1)[0],
						Math.abs(graph.get(i)[c] - graph.get(i + 1)[c]) });
				// 두 노드의 노드 번호(visited)용, 거리

			}
		}
		int cnt = 0;

		long sum = 0;

		// union find를 해야겠네
//		int [] visited = new int[N];
		parent = new int[N];
		for (int i = 0; i < N; i++) {
			parent[i] = i;
		}
		while (!queue.isEmpty()) {
			if (cnt == N - 1)
				break;

			long[] tmp = queue.poll();

//			if (visited[tmp[0]])

			int p1 = find_root((int) tmp[0]);
			int p2 = find_root((int) tmp[1]);
			if (p1 == p2)
				continue;

			parent[p1] = p2; // 합치기

			sum += tmp[2];
			cnt++;

		}
		System.out.println(sum);

//		// 하나를 선택
//		boolean[] visited = new boolean[N];
//		long sum = 0;
//		PriorityQueue<long[]> queue = new PriorityQueue<>((o1, o2) -> o1[1] > o2[1] ? 1 : -1);
//
////		visited[0] = true;
//		queue.offer(new long[] { 0, 0 }); // index, cost
//
//		int cnt = 0;
//
//		long answer = 0;
//		while (!queue.isEmpty()) {
//			long[] tmp = queue.poll();
//			int cIdx = (int) tmp[0];
//
//			if (visited[(int) tmp[0]])
//				continue;
//			visited[(int) tmp[0]] = true; // 뺄 때 확인해야해
//
//			answer += tmp[1];
//			cnt++; // cnt 값이 N과 같아지면 끝
//			if (cnt == N)
//				break;
//
//			for (int i = 0; i < N; i++) {
//				if (visited[i])
//					continue;
//				queue.offer(new long[] { i, cal_distance(cIdx, i) });
//			}
//		}
//		System.out.println(answer);
	}

	static int find_root(int node) {
		if (parent[node] == node) {
			return node;
		}

		return parent[node] = find_root(parent[node]);
	}

	static long cal_distance(int cIdx, int i) {
		long[] tmp1 = graph.get(cIdx);
		long[] tmp2 = graph.get(i);

		return Math.min(Math.min(Math.abs(tmp1[0] - tmp2[0]), Math.abs(tmp1[1] - tmp2[1])),
				Math.abs(tmp1[2] - tmp2[2]));
	}
}