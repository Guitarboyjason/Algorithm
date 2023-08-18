import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	// 각 플레이어가 가진 수의 배수 마다 int형 배열에 접근하여 -1
	static int SIZE = 1000001;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] nums = new int[N];
		for (int i = 0; i < N; i++)
			nums[i] = Integer.parseInt(st.nextToken());
//		System.out.println(Arrays.toString(nums));
		int[] numsScore = new int[SIZE];

		for (int i = 0; i < N; i++) {
			for (int j = nums[i] * 2; j < SIZE; j += nums[i]) {
//				System.out.println(j);
				numsScore[j] -= 1;
			}
		}

		int[] winScores = new int[SIZE];
		for (int i = 0; i < N; i++) {
			if (numsScore[nums[i]] < 0) { // 나누어짐
				// 약수들에게 +1을 해주자
				for (int j = 1; j <= (int) Math.pow(nums[i], 0.5); j++) {
					if (nums[i] % j == 0) {
						winScores[j] += 1;
						if (j != nums[i] / j && nums[i] / j != nums[i])
							winScores[nums[i] / j] += 1;
					}
				}
			}
//			System.out.print(numsScore[nums[i]] + " ");
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < N; i++) {
			sb.append(numsScore[nums[i]] + winScores[nums[i]]).append(" ");
		}
		System.out.print(sb);
	}
}