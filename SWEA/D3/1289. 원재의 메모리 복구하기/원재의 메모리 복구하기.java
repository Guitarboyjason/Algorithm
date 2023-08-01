import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Solution {

	static int T, count;
	static char[] input;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		T = Integer.parseInt(br.readLine());

		for (int t = 1; t <= T; t++) {

			count = 0;
			char current = '0'; // 시작은 초기화 값으로

			input = br.readLine().toCharArray();

			int cnt = input.length;
//			for (int i = 0; i < cnt; i++) {
//
//				
//			}
			recursive(0, cnt, current);

			sb.append("#").append(t).append(" ").append(count).append("\n");
		}
		System.out.println(sb);
	}

	static void recursive(int t_cnt, int cnt, char current) {
		if (t_cnt == cnt) {
			return;
		}

		if (input[t_cnt] != current) { // 다르면
			count++; // 변경 횟수 증가
		}
		current = input[t_cnt];
		t_cnt++;
		recursive(t_cnt, cnt, current);
	}
}