import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	static int[] parent;
	static int sum = 0;
	static int cnt = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());

		parent = new int[V + 1];
		for (int i = 1; i <= V; i++) {
			parent[i] = i;
		}
		ArrayList<int[]> v = new ArrayList<>();

		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			v.add(new int[] { A, B, C });

		}

		Collections.sort(v, (o1, o2) -> o1[2] - o2[2]);

		for (int i = 0; i < E; i++) {
			int[] tmp = v.get(i);
			if (find_root(tmp[0]) == find_root(tmp[1])) {
				continue;
			} else {
				merge(tmp[0], tmp[1]);
				sum += tmp[2];
				cnt++;
				if (cnt == V - 1)
					break;
			}

		}
		System.out.println(sum);

	}

	static int find_root(int node) {
		if (node == parent[node])
			return node;

		return parent[node] = find_root(parent[node]);
	}

	static void merge(int n1, int n2) {
		parent[find_root(n1)] = find_root(n2);
	}

}