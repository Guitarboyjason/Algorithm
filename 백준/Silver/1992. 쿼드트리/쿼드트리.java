import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static StringBuilder sb = new StringBuilder();
	static int[][] graph;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		graph = new int[N][N];

		for (int i = 0; i < N; i++) {
			String row = br.readLine();
			for (int j = 0; j < N; j++) {
				graph[i][j] = Character.getNumericValue(row.charAt(j));
			}
		}
//		for (int i = 0; i < N; i++) {
//			System.out.println(Arrays.toString(graph[i]));
//		}
		quad_tree(0, 0, N);
		System.out.println(sb);
	}

	static void quad_tree(int x, int y, int size) {
		if (size == 1) {
			sb.append(graph[x][y]);
			return;
		}

		else {
			int sum = 0;
			for (int i = x; i < x + size; i++) {
				for (int j = y; j < y + size; j++) {
					sum += graph[i][j];
				}
			}
			if (sum % (size * size) == 0) {
				sb.append(graph[x][y]);
				return;
			} else {
				sb.append("(");
				quad_tree(x, y, size / 2);
				quad_tree(x, y + size / 2, size / 2);
				quad_tree(x + size / 2, y, size / 2);
				quad_tree(x + size / 2, y + size / 2, size / 2);
				sb.append(")");
			}

		}

	}

}