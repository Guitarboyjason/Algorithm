import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	static int cnt;
	static StringBuilder sb = new StringBuilder();
	static String T, P;
	static int[] pi;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		StringTokenizer st = new StringTokenizer(br.readLine());

		T = br.readLine();
		P = br.readLine();

		kmp(T, P);

		System.out.println(cnt);
		System.out.println(sb);
		// pattern에 대한 pi표를 구현해보자
//		makePi(P);
//
//		System.out.println(Arrays.toString(pi));
//
//		// pi 를 확인하면서 j의 끝까지 가면 끝
//
//		int index = 0;
//		int jndex = 0;
//
////		while (i < )
//
//		char[] pArray = P.toCharArray();
//		char[] tArray = T.toCharArray();
//		ArrayList<Integer> result = new ArrayList<>();
//
//		for (int i = 0; i < T.length(); i++) {
//			while (jndex > 0 && pArray[jndex] != tArray[i]) {
//				jndex = pi[jndex - 1];
//			}
////			System.out.println(jndex);
//			if (pArray[jndex] == tArray[i])
//				jndex++;
//			if (jndex == pArray.length) {
//				result.add(i - jndex + 2);
//
//				System.out.println(jndex);
//				System.out.println();
//
//				jndex = pi[jndex - 2];
//				System.out.println(jndex);
//				System.out.println();
////				jndex = 0;
//			}
////			else {
////				
////			}
//		}
//
//		System.out.println(result.size());
//
//		for (int i = 0; i < result.size(); i++) {
//			System.out.println(result.get(i));
//		}
	}

	static void kmp(String text, String pattern) {

		// pi 배열
		makePi(pattern);

		// pattern 매칭
		int tLength = text.length();
		int pLength = pattern.length();
		char[] tArray = text.toCharArray();
		char[] pArray = pattern.toCharArray();

		int j = 0;

		for (int i = 0; i < tLength; i++) {
			while (j > 0 && tArray[i] != pArray[j]) { // 일치하지 않는 것.
				j = pi[j - 1];
			}

			if (tArray[i] == pArray[j]) { // 일치할 때
				if (j == pLength - 1) {// 모두 일치
					cnt++;
					sb.append(i - j + 1);
					sb.append(" ");
					j = pi[j];
				} else { // 일부 일치
					j += 1;
				}
			}
		}
	}

	static void makePi(String P) {
		pi = new int[P.length()];
		char[] pArray = P.toCharArray();

		// 접두사쪽 인덱스
		int j = 0;

		// 접미사쪽 인덱스
		for (int i = 1; i < pArray.length; i++) {

			// 벗어나려면 pArray[i] == pArray[j] 이거나 j == 0 일때만
			while (j > 0 && pArray[i] != pArray[j]) { // 일치하지 않는 것.
				j = pi[j - 1];
			}

			// 현재 시점은 j == 0이거나 pArray[i] == pArray[j] 일 때

			if (pArray[i] == pArray[j]) { // 일치할 때
				pi[i] = ++j;

			}
		}
	}
}