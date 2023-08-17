import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
//	static boolean[][] friendship;
	static List<List<Integer>> friendship = new ArrayList<>();
	static boolean[] visited;
	static boolean done = false;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		for (int i = 0; i < N; i++) {
			friendship.add(new ArrayList<>());
		}
//		friendship = new boolean[N][N];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			friendship.get(a).add(b);
			friendship.get(b).add(a);
//			friendship[b][a] = true;

		}

		visited = new boolean[N];
		for (int i = 0; i < N; i++) {
			visited[i] = true;
			dfs(i, 0);
			if (done) {
				System.out.println(1);
				return;
			}
			visited[i] = false;
		}
		System.out.println(0);

	}

	static void dfs(int root, int cnt) {

		if (done)
			return;

		if (cnt == 4) {
			done = true;
			return;
		}
		visited[root] = true;

		friendship.get(root).forEach((i) -> {
			if (!visited[i]) {
				visited[i] = true;
				dfs(i, cnt + 1);
				visited[i] = false;
			}
		});
//		for(int i = 0 ; i < friendship.get(root).size() ; i ++)
//		for (int i = 0; i < N; i++) {
//			if (friendship[root][i] && !visited[i]) {
//				visited[i] = true;
//				dfs(i, cnt + 1);
//				visited[i] = false;
//			}
//
//		}

	}
}