import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	// 윗자리부터 확인하며 각 자리에 등장하는 알파벳의 횟수를 구하자
	// 혹은 987 879
	// 혹은 각 자리마다 가산점을 준다..?

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

//		HashMap<Character, Integer> map = new HashMap<>();
		long[] alpha_cnt = new long[10];
		for (int i = 0; i < 10; i++) {
			alpha_cnt[i] = 0;
		}
//		for (int i = 65; i < 65 + 10; i++) {
//			map.put((char) i, 0);
//		}
//		map.get('A')+=1;
//		for(int i )
//		System.out.println(map.get('A'));
//		System.out.println(map);
		boolean[] can_zero_arr = new boolean[10];
		for (int i = 0; i < 10; i++) {
			can_zero_arr[i] = true;
		}
		for (int i = 0; i < N; i++) {
//			int cnt = 0;
			String alphaNum = br.readLine();
			for (int j = alphaNum.length() - 1; j >= 0; j--) {// 뒤에서부터 확인
				alpha_cnt[(int) alphaNum.charAt(j) - 65] += (long) Math.pow(10, (alphaNum.length() - 1) - j);
			}
			can_zero_arr[alphaNum.charAt(0) - 65] = false; // 얘는 처음은 안돼

		}
//		System.out.println(Arrays.toString(alpha_cnt));

		// 제일 작은 애 먼저 볼까
		int alphabet_cnt = 0;
		for (int i = 0; i < 10; i++) {
			if (alpha_cnt[i] > 0)
				alphabet_cnt++;

		}

		if (alphabet_cnt == 10) { // 0이 있어야해
			long min_val = Long.MAX_VALUE;
			int min_index = -1;
			for (int i = 0; i < 10; i++) {
				if (can_zero_arr[i] && min_val > alpha_cnt[i]) { // 0이 될 수 있음
					min_val = alpha_cnt[i];
					min_index = i;
				}
			}

			alpha_cnt[min_index] = 0; // 어차피 곱해봐야 0임

		}

		long sum = 0;
//		Arrays.sort(alpha_cnt, (o1, o2) -> {o1 - o2}); // 역순으로 출력
		Arrays.sort(alpha_cnt);
		for (int i = 9; i >= 0; i--) {
			sum += i * alpha_cnt[i];
		}
		System.out.println(sum);

	}
}