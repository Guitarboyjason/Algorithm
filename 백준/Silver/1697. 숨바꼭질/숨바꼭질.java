import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, K;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());

		bfs(N);
	}

	static void bfs(int root) {

		Queue<Integer> queue = new ArrayDeque<>();

		queue.offer(root);

		int[] visited = new int[500_000];

		for (int i = 0; i < visited.length; i++) {
			visited[i] = Integer.MAX_VALUE - 100;
		}
		visited[root] = 0;

//		for(int i = 0 ; i < K ; i ++) {
//			visited[i] = /
//		}

		while (!queue.isEmpty()) {
			int node = queue.poll();
			if (node == K) {
				System.out.println(visited[K]);
				break;
			}
			int[] nNode = new int[] { node - 1, node + 1, node * 2 };
			for (int i = 0; i < 3; i++) {
				if (0 <= nNode[i] && nNode[i] < 500000 && visited[nNode[i]] > visited[node] + 1) {
					// 여기 들어왔다 -> 최소값을 구해야함
					visited[nNode[i]] = visited[node] + 1;
//					if ()
					queue.offer(nNode[i]);
				}
			}

		}

//		System.out.println(visited[K]);
	}

}