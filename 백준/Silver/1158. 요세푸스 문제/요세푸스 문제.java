import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		Queue<Integer> queue = new ArrayDeque<>();
		for (int i = 1; i <= N; i++) {
			queue.offer(i);
		}

//		System.out.print("<");
		sb.append("<");
		int cnt = 0;
		while (!queue.isEmpty()) {
			int person = queue.poll();
			cnt += 1;
			if (cnt == K) {
				cnt = 0;
				sb.append(person).append(", ");
				continue;

			}

			queue.offer(person);
		}
		sb.deleteCharAt(sb.length() - 1);
		sb.deleteCharAt(sb.lastIndexOf(","));
		sb.append(">");
		System.out.print(sb);

	}
}