import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	// 100 C 3 해도 그리 오래 걸리진 않을듯

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int N, M;
	static int[] tgt = new int[3];
	static int[] cards;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		cards = new int[N];
		st = new StringTokenizer(br.readLine());

		for (int i = 0; i < N; i++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		System.out.println(comb(0, 0));

	}

	public static int comb(int tgtIdx, int srcIdx) {
		if (tgtIdx == 3) {
			int sum = 0;
			for (int i = 0; i < 3; i++) {
				sum += tgt[i];
			}
//			System.out.println(Arrays.toString(tgt));
			return sum;
		}

		if (srcIdx == cards.length)
			return 0;
		tgt[tgtIdx] = cards[srcIdx];

		int max = -1;
		int tmp = comb(tgtIdx + 1, srcIdx + 1);
		if (tmp <= M && tmp > max)
			max = tmp;
		tmp = comb(tgtIdx, srcIdx + 1);
		if (tmp <= M && tmp > max)
			max = tmp;
		return max;
	}
}