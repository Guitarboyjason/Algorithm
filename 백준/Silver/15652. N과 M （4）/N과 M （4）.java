import java.util.Scanner;

public class Main {
	static int n, k;
	static int[] selected;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
		selected = new int[k];
//		int [] arr = new int 

//		for (int i = 1; i < n; i++)
		perm(1, 0);

	}

	static void perm(int selectNum, int srcIdx) {
		if (srcIdx == k) {
			for (int i = 0; i < k; i++)
				System.out.print(selected[i] + " ");
			System.out.println();
			return;
		}

		else {
			if (selectNum > n)
				return;
			else {

//				for (int i = selectNum; i >= 1; i--)
//					
				selected[srcIdx] = selectNum;
				perm(selectNum, srcIdx + 1);

				perm(selectNum + 1, srcIdx);

			}
		}
	}
}