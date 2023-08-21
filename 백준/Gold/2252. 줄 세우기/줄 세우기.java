import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[] topology;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		topology = new int[N + 1];

		boolean[] visited = new boolean[N + 1];
		graph.add(new ArrayList<>());
		for (int i = 1; i <= N; i++) {
			graph.add(new ArrayList<>());
		}
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());

			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());

			graph.get(A).add(B);
			topology[B] += 1;
		}
//		System.out.println(Arrays.toString(topology));

		boolean done = false;

		Queue<Integer> queue = new ArrayDeque<>();

		for (int i = 1; i <= N; i++) {
			if (topology[i] == 0) {
				queue.offer(i); // 0인애들 다 넣어
			}
		}

		while (!queue.isEmpty()) {
			int node = queue.poll();
			System.out.print(node + " ");

			for (int i = 0; i < graph.get(node).size(); i++) {
				topology[graph.get(node).get(i)] -= 1;
				if (topology[graph.get(node).get(i)] == 0)
					queue.offer(graph.get(node).get(i));
			}
//			System.out.println(Arrays.toString(topology));
		}

//		while (!done) {
//			// 전체 체크
//			done = true;
//			for(int i = 1 ; i <= N ; i ++) {
//				if (visited[i] == false)
//					done = false;
//			}
//			
//			if (done)
//				break;
//			
//			// 아직 끝나지 않음
//			
//			for(int i = 1; i <= N ; i ++) {
//				if (!visited[i] && topology[i] == 0) {
//					System.out.print(i+" ");
//					visited[i] = true;
//					
//					for(int nei = 0 ; nei < graph.get(i).size(); nei ++) {
//						topology[nei] -= 1;
//					}
//				}
//			}
//		}

	}
}