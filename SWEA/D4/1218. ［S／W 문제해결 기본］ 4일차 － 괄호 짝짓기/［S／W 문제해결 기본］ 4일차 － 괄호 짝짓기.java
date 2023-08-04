import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static char[] close = { ')', '}', ']', '>' };
	static char[] open = { '(', '{', '[', '<' };
//
//	static HashMap<Character, Character> gwal = new HashMap<>();

	public static void main(String[] args) throws IOException {
		int T = 10;
//		gwal.put(')', '(');
//		gwal.put('}', '{');
//		gwal.put(']', '[');
//		gwal.put('>', '<');
		for (int testCase = 1; testCase <= T; testCase++) {
			int cntChar = Integer.parseInt(br.readLine());
//			st = new StringTokenizer(br.readLine());

			String str = br.readLine();
			System.out.println("#" + testCase + " " + gwal(str));
		}
	}

	static int gwal(String str) {
		Deque<Character> stack = new ArrayDeque<>();

		for (int i = 0; i < str.length(); i++) {
			char cChar = str.charAt(i);
			boolean flag = true;
			for (int j = 0; j < 4; j++) {
				if (close[j] == cChar) { // 닫
					flag = false;
					if (stack.isEmpty() || stack.pop() != open[j])
						return 0;
				}

			}
			if (flag)
				stack.push(cChar);
		}
		if (!stack.isEmpty())
			return 0;
		return 1;
	}
}