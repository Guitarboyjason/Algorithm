import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
//	static int[] src;
	static int COUNT = 0;
	static int[] tgt;
	static boolean[] visited;
	static int N, M;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		visited = new boolean[N + 1];

		tgt = new int[M];
//		src = new int[N];
//		
//		for (int i = 0; i < N + 1;)
		cnt_perm(0);

	}

	static void cnt_perm(int index) {
		if (index == M) {
			for (int i = 0; i < tgt.length; i++) {
				System.out.print(tgt[i] + " ");
			}
			System.out.println();
			return;
		}
		int cnt = 0;

		for (int i = 1; i < N + 1; i++) {
			if (visited[i] != true) {
				visited[i] = true;
				tgt[index] = i;
				cnt_perm(index + 1);
				visited[i] = false;
			}
		}
	}
}