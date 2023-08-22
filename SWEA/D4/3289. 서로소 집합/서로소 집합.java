import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int[] parent;
//	static int n = 10;
	static int n, m;

	public static void main(String[] args) throws IOException {
//		n = 10;

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringBuilder sb = new StringBuilder();
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());

			makeSet();
			sb.append("#" + tc + " ");
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());

				int command = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());

				if (command == 0)
					union(a, b);

				else {
					int pa = findSet(a);
					int pb = findSet(b);

					if (pa == pb)
//						System.out.println("#"+tc+" "+);
						sb.append(1);
					else
						sb.append(0);
				}

			}
//			System.out.println(Arrays.toString(parent));
			System.out.println(sb);
		}
	}

	// 서로소 집합을 표현하는 자료구조 생성 및 초기화
	static void makeSet() {
		parent = new int[n + 1];
		for (int i = 0; i <= n; i++) {
			parent[i] = i;
		}
	}

	// 소속된 서로소 집합의 대표 원소를 리턴
	static int findSet(int x) {
		// 기저조건
		// value와 index 같은 조건
		if (parent[x] == x)
			return x;

		return parent[x] = findSet(parent[x]);
	}

	// 두 서로소 집합을 하나로 합친다.
	// x의 대표자, y의 대표자 찾아서 합침
	static void union(int x, int y) {
		int px = findSet(x); // x 최종 대표자
		int py = findSet(y); // y 최종 대표자

//		if (px == py) { // 만약 px==py <= x,y는 같은 서로소 집합
		// 그렇지 않으면 다른 서로소 집합
		parent[py] = px;

//		}

	}
}