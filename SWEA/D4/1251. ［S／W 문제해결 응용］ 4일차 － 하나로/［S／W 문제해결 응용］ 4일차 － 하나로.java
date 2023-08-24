import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {
	static int[] parent;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			int N = Integer.parseInt(br.readLine());
			ArrayList<Integer> islands_x = new ArrayList<>();
			ArrayList<Integer> islands_y = new ArrayList<>();

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				int x = Integer.parseInt(st.nextToken());
//				int y = Integer.parseInt(st.nextToken());
				islands_x.add(x);
//				islands_y.add(y);
//				islands.add(new int[] { x, y });
			}
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
//				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
//				islands_x.add(x);
				islands_y.add(y);
//				islands.add(new int[] { x, y });
			}

			double E = Double.parseDouble(br.readLine());
			ArrayList<long[]> relations = new ArrayList<>();
//			Collections.sort(islands, (o1, o2) -> o1[0] - o2[0]);

			for (int i = 0; i < N - 1; i++) {
				for (int j = i + 1; j < N; j++) {
					int x1 = islands_x.get(i);
					int y1 = islands_y.get(i);
					int x2 = islands_x.get(j);
					int y2 = islands_y.get(j);
					long distance = (long) (Math.pow((long) x1 - (long) x2, 2) + Math.pow((long) y1 - (long) y2, 2));
					relations.add(new long[] { i, j, distance });
				}
			}
			parent = new int[N];

			for (int i = 0; i < N; i++) {
				parent[i] = i;
			}

//			System.out.println-);
//			for (int i = 0; i < relations.size(); i++)
//				System.out.println(Arrays.toString(relations.get(i)));
//			System.out.println();
			try {
				Collections.sort(relations, (o1, o2) -> o1[2] >= o2[2] ? 1 : -1);
			} catch (Exception e) {

			}

			double sum = 0;
			for (int i = 0; i < relations.size(); i++) {
				long[] tmp = relations.get(i);

				int p1 = find_root((int) tmp[0]);
				int p2 = find_root((int) tmp[1]);

				if (p1 == p2)
					continue;

				parent[p1] = p2;

				sum += tmp[2];
			}

			sum *= E;
			System.out.println("#" + tc + " " + Math.round(sum));

		}
	}

	static int find_root(int node) {
		if (node == parent[node])
			return node;
		return parent[node] = find_root(parent[node]);
	}
}