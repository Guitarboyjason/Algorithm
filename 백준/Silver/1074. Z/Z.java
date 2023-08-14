import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int cnt = 0;
	static int N, r, c;

	public static void main(String[] args) throws IOException {
		// 1/4 씩 들어가는것 같음

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());

//		for(int i = 0 ; i < )
//		System.out.println();
//		traversal(r, c, (int) Math.pow(2, N + 1));
		traversal(r, c, N);

	}

	static void traversal(int start_x, int start_y, int size) {

		if (size == 0) {
			System.out.println(cnt);
//			cnt++;
			return;
		}

		// 1/4 씩 하면서 들어가자
		int tmpCnt = 0;
		if (start_x >= Math.pow(2, size) / 2) {
			tmpCnt += Math.pow(2, 2 * size - 1);
			start_x -= Math.pow(2, size) / 2;

		}
		if (start_y >= Math.pow(2, size) / 2) {
			tmpCnt += Math.pow(2, 2 * size - 2);
			start_y -= Math.pow(2, size) / 2;
		}
		cnt += tmpCnt;

		traversal(start_x, start_y, size - 1);

//		if (traversal(start_x, start_y, size / 2))
//			return true;
//		if (traversal(start_x, start_y + size / 2, size / 2))
//			return true;
//		if (traversal(start_x + size / 2, start_y, size / 2))
//			return true;
//		if (traversal(start_x + size / 2, start_y + size / 2, size / 2))
//			return true;
//		return false;
	}
}