import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	// 신맛 => 재료의 신맛의 곱
	// 쓴맛 => 합
	// 신맛과 쓴맛의 차이를 작게
	// 재료는 적어도 하나 => 공집합 제외
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N;
	static ArrayList<ArrayList<Integer>> elements;

	public static void main(String[] args) throws IOException {
//		st = new StringTokenizer
		N = Integer.parseInt(br.readLine());
//		int [] elements = new int [N];
		elements = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			elements.add(new ArrayList<>());
			st = new StringTokenizer(br.readLine());
			int sour = Integer.parseInt(st.nextToken());
			int bitter = Integer.parseInt(st.nextToken());
			elements.get(i).add(sour);
			elements.get(i).add(bitter);

		}

		System.out.println(subset(0, 0));

	}

	static int subset(int srcIdx, int mask) {
		if (srcIdx == N) {
			int sour = 1;
			int bitter = 0;
			for (int i = 0; i < elements.size(); i++) {
				if ((mask & 1 << i) != 0) {
					sour *= elements.get(i).get(0);
					bitter += elements.get(i).get(1);
				}
			}
			if (sour == 1 && bitter == 0)
				return -1;
			return Math.abs(sour - bitter);
		}
		int a = subset(srcIdx + 1, mask | 1 << srcIdx);
		int b = subset(srcIdx + 1, mask);
		if (a == -1 || b == -1)
			return Math.max(a, b);
//		System.out.println(Integer.toBinaryString(mask));
		return Math.min(a, b);
//		return Math.min(subset(srcIdx+1,mask|1<<srcIdx), subset(srcIdx+1,mask|1<<srcIdx));

	}
}