import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());

			// 그냥 한번 돌고 나머지 앞에서 돌까

			char[] nums = br.readLine().toCharArray();

			// heapq에 넣어서 확인, 중복된건 찾지 마라. 그럼 set?을 먼저쓸까

			Set<Integer> cases = new HashSet<>();

			for (int i = 0; i < N; i++) {
				StringBuilder sb = new StringBuilder();
				for (int j = i; j < i + (N / 4); j++) {
					sb.append(nums[j % N]);
//					cases.add(e)
				}
				cases.add(Integer.parseInt(sb.toString(), 16));
			}

			// heapq에 넣자ㅣ
//			int[] tmp = new int[cases.size()];
//			int idx = 0;

			PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> o2 - o1);
			for (Object o : cases.toArray()) {
//				tmp[idx++] = (int)o;
				pq.add((int) o);
			}

			for (int i = 0; i < K - 1; i++)
				pq.poll();

			System.out.println("#" + tc + " " + pq.poll());
		}
	}
}