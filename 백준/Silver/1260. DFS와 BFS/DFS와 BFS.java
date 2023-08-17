import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static ArrayList[] arr;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int V = Integer.parseInt(st.nextToken());
//		Node [] arrNode =
//		ArrayList<Integer>
//		ArrayList<Integer>[] arr = new ArrayList<Integer>()[N];
		arr = new ArrayList[N + 1];
//		arr[0] = new ArrayList<Integer>();
//		arr[1] = new ArrayList<Integer>();
//		arr[2] = new ArrayList<Integer>();
		for (int i = 1; i <= N; i++) {
			arr[i] = new ArrayList<Integer>();
		}
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int v1 = Integer.parseInt(st.nextToken());
			int v2 = Integer.parseInt(st.nextToken());
			arr[v1].add(v2);
			arr[v2].add(v1);
		}

		for (int i = 1; i <= N; i++) {
//			arr[i].sort((o1, o2) -> (Integer.valueOf((String) o1)) - (Integer.valueOf((String) o2)));
			Collections.sort(arr[i]);
			Collections.reverse(arr[i]);
		}

		dfs(V);
		System.out.println();
		for (int i = 1; i <= N; i++) {
//			
			Collections.reverse(arr[i]);
		}
		bfs(V);

//		for (int i = 1; i <= N; i++) {
//			System.out.println(arr[i]);
//		}

	}

	static void dfs(int root) {
		boolean[] visited = new boolean[N + 1];

		Deque<Integer> stack = new ArrayDeque<>();

		stack.push(root);
//		visited[root] = true;

		while (!stack.isEmpty()) {
			int node = stack.pop();
			if (visited[node] == false) {
				visited[node] = true;
				System.out.print(node + " ");
				for (int nei = 0; nei < arr[node].size(); nei++) {
					stack.push((int) arr[node].get(nei));

				}
			}

		}
	}

	static void bfs(int root) {
		boolean[] visited = new boolean[N + 1];

		Deque<Integer> queue = new ArrayDeque<>();

		queue.offer(root);
//		visited[root] = true;

		while (!queue.isEmpty()) {
			int node = queue.poll();
			if (visited[node] == false) {
				visited[node] = true;
				System.out.print(node + " ");
				for (int nei = 0; nei < arr[node].size(); nei++) {
					queue.offer((int) arr[node].get(nei));

				}
			}

		}
	}

//	class Node {
//		int value;
//		Node next;
//
//		Node(int value) {
//			this.value = value;
//			this.next = null;
//		}
//	}
}