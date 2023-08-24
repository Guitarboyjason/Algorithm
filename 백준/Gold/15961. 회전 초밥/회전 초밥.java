import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		int[] dishes = new int[N + k];
		for (int i = 0; i < N; i++) {
			dishes[i] = Integer.parseInt(br.readLine());

		}

		for (int i = 0; i < k; i++) {
			dishes[N + i] = dishes[i];
		}

		int[] kinds = new int[d + 1];
		// 먹은 가짓수

		// -1 -> 0 ==> 가짓수 -1
		// 0 -> 1 ==> 가짓수 +1

		int start = 0;
		int end = k - 1;

		int max_num_fishes = -1;
		int num_fishes = 0;
		for (int i = 0; i <= k - 1; i++) {
			kinds[dishes[i]] += 1;
			if (kinds[dishes[i]] == 1)
				num_fishes += 1;
			if (kinds[c] == 0)
				max_num_fishes = Math.max(max_num_fishes, num_fishes + 1);
			else
				max_num_fishes = Math.max(max_num_fishes, num_fishes);
		}

		while (end < N + k - 1) {
			end += 1;

			kinds[dishes[end]] += 1;
			if (kinds[dishes[end]] == 1) {
				num_fishes += 1;
			}

			kinds[dishes[start]] -= 1;
			if (kinds[dishes[start]] == 0) {
				num_fishes -= 1;
			}

			if (kinds[c] == 0)
				max_num_fishes = Math.max(max_num_fishes, num_fishes + 1);
			else
				max_num_fishes = Math.max(max_num_fishes, num_fishes);
//			max_num_fishes = Math.max(max_num_fishes, num_fishes);
			start += 1;
		}
		System.out.println(max_num_fishes);
	}
}