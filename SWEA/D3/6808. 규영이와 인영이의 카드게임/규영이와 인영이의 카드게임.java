import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static boolean[] cards;
	static int[] gyu;
	static int[] in;

//	static boolean[] selected = new boolean[9];
//
//	static int[] selectedCards = new int[9];
	static boolean[] check;
	static int[] result;
	static int count;
//	static int idx = 0;
	static StringBuilder sb = new StringBuilder();

	public static void main(String[] args) throws IOException {
		// 그냥 완탐으로 돌려도 될 것 같기는해

		int T = Integer.parseInt(br.readLine());
//		cards = new boolean[19];
//		for(int i = 1 ; i <= 18 ; i++) {
//			cards[i] = true;
//		}
		for (int testCase = 1; testCase <= T; testCase++) {
//			Arrays.fill(cards, true);
			cards = new boolean[19];
//			System.out.println(Arrays.toString(cards));
			st = new StringTokenizer(br.readLine());

			gyu = new int[9];
			in = new int[9];

			for (int i = 0; i < 9; i++) {
				int tmp = Integer.parseInt(st.nextToken());
				cards[tmp] = true;
				gyu[i] = tmp;
			}
			int cnt = 0;
			for (int i = 1; i <= 18; i++) {
				if (!cards[i]) {
					in[cnt++] = i;
				}
			}

			result = new int[9];
			check = new boolean[9];

			count = 0;
			perm(0);

			sb.append("#"+ testCase + " " + count + " " + (362880 - count)).append("\n");

		}
		System.out.print(sb);
	}

	static void perm(int idx) {
		if (idx == 9) {
			int gyuScore = 0;
			int InScore = 0;

//			System.out.println(Arrays.toString(result));
//			System.out.println(Arrays.toString(in));
			for (int i = 0; i < 9; i++) {
				if (gyu[i] > result[i])
					gyuScore += gyu[i] + result[i];
				else
					InScore += gyu[i] + result[i];

			}

			if (gyuScore > InScore) {
//				System.out.println(InScore);
				count += 1;
			}
			return;

		}

		for (int i = 0; i < 9; i++) {
			if (!check[i]) {
				result[idx] = in[i];
				check[i] = true;
				perm(idx + 1);
				check[i] = false;
			}
		}
	}

//	static void  
	// 순서 정하는거 어떻게 하지
//	static int[] traversal(int selectedIdx) {
//		if (selectedIdx == 9) {
//			// 확인해
//			int scoreGyu = 0;
//			int scoreIn = 0;
//
//			for (int i = 0; i < 9; i++) {
//				if (gyu[i] > in[selectedCards[i]])
//					scoreGyu += gyu[i] + in[selectedCards[i]];
//				else
//					scoreIn += gyu[i] + in[selectedCards[i]];
//			}
//
//			if (scoreGyu > scoreIn) {
////				int[] answer = { 1, 0 };
//				return (new int[] { 1, 0 });
//			} else {
//				return (new int[] { 0, 1 }); // gyu, in
//			}
//		}
////		selected[selectedIdx] = true; // 저장
//		for(int i = 0 ; i < 9 ; i ++) {
//			if(selected[i]) == 
//		}
//		
//	}

}