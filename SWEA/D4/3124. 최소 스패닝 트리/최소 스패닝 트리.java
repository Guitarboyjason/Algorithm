import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
	static int[] parent;
	static int V, E;
	static ArrayList<int[]> graph;
	static long sum;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			graph = new ArrayList<>();
			sum = 0;
			for (int i = 0; i < E; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());

				graph.add(new int[] { a, b, c });
			}

			Collections.sort(graph, (o1, o2) -> o1[2] - o2[2]);

			make_parent();

			simulation();
			System.out.println("#" + tc + " " + sum);

		}
	}

	static void make_parent() {
		parent = new int[V + 1];

		for (int i = 1; i <= V; i++) {
			parent[i] = i;
		}
	}

	static int find_root(int node) {
		if (parent[node] == node)
			return node;
		return parent[node] = find_root(parent[node]);
	}

	static void simulation() {
		int cnt = 0;
//		int sum = 0;
		for (int i = 0; i < E; i++) {
			if (cnt == V - 1)
				return;

			int[] tmp = graph.get(i);

			int p1 = find_root(tmp[0]);
			int p2 = find_root(tmp[1]);
			if (p1 == p2)
				continue;

			parent[p1] = p2;
			sum += tmp[2];
		}
	}
}