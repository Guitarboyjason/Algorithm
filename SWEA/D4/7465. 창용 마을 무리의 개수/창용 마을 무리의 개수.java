import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution {
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static int groupCnt = 0;
	static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			groupCnt = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());

			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());

			graph = new ArrayList<>();
			parents = new int[N + 1];
			for (int i = 0; i <= N; i++) {
				graph.add(new ArrayList<>());
				parents[i] = i;
			}
			for (int i = 0; i < M; i++) {
				// 서로 알고 있는 관계가 나온다
				// 그래프 형식으로 하자
				st = new StringTokenizer(br.readLine());
				int p1 = Integer.parseInt(st.nextToken());
				int p2 = Integer.parseInt(st.nextToken());
				graph.get(p1).add(p2);
				graph.get(p2).add(p1);
			}
			// 총 몇명이 있는가

			for (int i = 1; i <= N; i++) {
				for (int j : graph.get(i)) {
					merge_parents(i, j);
				}
			}

			int cnt = 0;
			Set<Integer> parentsSet = new HashSet<>();
			for (int i = 1; i <= N; i++) {
				parentsSet.add(find_parent(i));
			}

			System.out.println("#" + tc + " " + parentsSet.size());
		}
	}

	public static void merge_parents(int p1, int p2) {
		if (find_parent(p1) == find_parent(p2))
			return;

		parents[find_parent(p1)] = p2;
	}

	public static int find_parent(int person) {
		if (parents[person] == person)
			return person;
		return parents[person] = find_parent(parents[person]);
	}
}