import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) {
		try {
			while (true) {
//		for(int i = 0 ; i < 
				int T = Integer.parseInt(br.readLine());
				Deque<Integer> queue = new ArrayDeque<>();
				st = new StringTokenizer(br.readLine());
				for (int i = 0; i < 8; i++) {
					queue.offer(Integer.parseInt(st.nextToken()));

				}
				int cnt = 1;
				while (true) {
					int tmp = queue.poll();
					if (cnt == 6)
						cnt = 1;
					tmp -= cnt++;
					if (tmp <= 0) {
						tmp = 0;
						queue.offer(tmp);
						break;
					}
					queue.offer(tmp);
				}

				System.out.print("#" + T + " ");
				while (!queue.isEmpty()) {
					System.out.print(queue.poll() + " ");
				}
				System.out.println();
			}
		} catch (Exception e) {

		}
	}
}