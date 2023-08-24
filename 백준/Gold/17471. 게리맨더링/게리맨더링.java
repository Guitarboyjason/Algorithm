import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static boolean[] vote_area;
	static int N;
	static ArrayList<ArrayList<Integer>> neighbors;
	static int MinDiffs = Integer.MAX_VALUE;
	static int MAX_SUM = 0;
	static int[] area;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		N = Integer.parseInt(br.readLine());

		StringTokenizer st = new StringTokenizer(br.readLine());

		area = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			area[i] = Integer.parseInt(st.nextToken());
			MAX_SUM += area[i];
		}

		neighbors = new ArrayList<>();
		for (int i = 0; i < N + 1; i++)
			neighbors.add(new ArrayList<>());
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			int neiCnt = Integer.parseInt(st.nextToken());

			for (int j = 0; j < neiCnt; j++) {
				int nei = Integer.parseInt(st.nextToken());
				neighbors.get(i).add(nei);
//				neighbors
			}

		}

		// 인접리스트들을 만들었으니 각 선거구마다 어디에 속하는지를 저장할까
		vote_area = new boolean[N + 1];
		// 근데 하나의 선거구에만 속하면 안됨.
		// 하나의 선거구에 속하는 갯수를 파악해서 해당 선거구에 몰려있는지, 하나도 없는지 정도를 파악하자

//		for(int i = 1; i <= N ; i ++) {
//			
//		}
		circular(0);
		System.out.println(MinDiffs == Integer.MAX_VALUE ? -1 : MinDiffs);
	}

	static int selectIdx;

	static void circular(int selectIdx) {
		if (selectIdx == N) {
			if (checker()) {
				bfs();
			}
			return;
		}

		vote_area[selectIdx] = true;
		circular(selectIdx + 1);
		vote_area[selectIdx] = false;
		circular(selectIdx + 1);

	}

	static void bfs() {
		int sum = 0;
		ArrayList<Integer> one_vote_area = new ArrayList<>();
		ArrayList<Integer> two_vote_area = new ArrayList<>();
		for (int i = 1; i <= N; i++) { // 1번 선거군
			if (vote_area[i] == true) {
				one_vote_area.add(i); // 얘네가 다 들어왔는지를 확인하기 위함
			} else {
				two_vote_area.add(i); // 얘네가 다 들어왔는지를 확인하기 위함
			}
		}
		boolean[] visited = new boolean[N + 1];
		Queue<Integer> queue = new ArrayDeque<>();

		queue.add(one_vote_area.get(0));

		visited[one_vote_area.get(0)] = true;
		while (!queue.isEmpty()) {
			int node = queue.poll();
			sum += area[node];
//			for(int i = 0 ; i < neighbors.get(i).size(); i ++) {
//				
//			}
			for (int i : neighbors.get(node)) {
				if (!visited[i] && vote_area[i]) {
					visited[i] = true;
					queue.offer(i);
				}
			}

		}

		// 다 끝나고 나면 다 들렀는지, 다 들렀다면 얼마나 차이가 나는지를 저장한다.

		queue = new ArrayDeque<>();

		queue.add(two_vote_area.get(0));
		visited[two_vote_area.get(0)] = true;

		while (!queue.isEmpty()) {
			int node = queue.poll();
			sum -= area[node]; // 여기선 빼기로 값의 차를 알게된다.
			for (int i : neighbors.get(node)) {
				if (!visited[i] && !vote_area[i]) {
					visited[i] = true;
					queue.offer(i);
				}
			}

		}

		boolean done = true;
		for (int i = 1; i <= N; i++) {
			if (!visited[i]) {
				done = false;
				break;
			}
		}

		if (done)
			MinDiffs = Math.min(MinDiffs, Math.abs(sum));

//		for (int i = 1; i <= N; i++) { // 2번 선거군
//			if (vote_area[i] == false) {
//
//			}
//		}
	}

	static boolean checker() {
		int sum = 0;
		for (int i = 1; i <= N; i++) {
			if (vote_area[i] == true) {
				sum += 1;
			}
		}
		if (sum == N || sum == 0)
			return false;

		return true;
	}
}