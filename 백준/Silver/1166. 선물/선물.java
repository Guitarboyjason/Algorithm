import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static long L, W, H;

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	public static void main(String[] args) throws IOException {

		st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		L = Long.parseLong(st.nextToken());
		W = Long.parseLong(st.nextToken());
		H = Long.parseLong(st.nextToken());

		double start = 0;

		double end = Math.min(Math.min(L, W), H);
		double max_save = 0;
		for (int i = 0; i < 10000; i++) {
			double middle = (double) (start + end) / 2;
			if ((long) (L / middle) * (long) (W / middle) * (long) (H / middle) >= N) {
				max_save = middle;
				start = middle;
			} else
				end = middle;

		}
		System.out.println(max_save);
	}
}