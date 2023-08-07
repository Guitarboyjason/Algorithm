import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	// I x,y,s -> 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입.
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static LinkedList root;

	public static void main(String[] args) throws IOException {

		for (int T = 1; T < 11; T++) {

			int N = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			root = new LinkedList();
			for (int i = 0; i < N; i++) {
				root.addLast(new LinkedList(Integer.parseInt(st.nextToken())));
			}

			int cntCommand = Integer.parseInt(br.readLine());

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < cntCommand; i++) {
				String command = st.nextToken();
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				int[] addList = new int[y];
				for (int j = 0; j < y; j++) {
					addList[j] = Integer.parseInt(st.nextToken());
				}
				root.addMiddle(x, addList);
			}

			System.out.print("#" + T + " ");
			for (int i = 0; i < 10; i++) {
				root = root.nextNode;
				System.out.print(root.secretNum + " ");
			}
			System.out.println();

		}
	}

	public static class LinkedList {
		int secretNum;
		LinkedList nextNode;

		LinkedList(int secretNum) {
			this.secretNum = secretNum;
		}

		LinkedList() {
		}

		void addLast(LinkedList addNode) {
			searchLast(root).nextNode = addNode;
		}

		void addMiddle(int x, int[] s) {
			LinkedList tmpNode = root;
			for (int i = 0; i < x; i++) { // x개만큼 이동
				tmpNode = tmpNode.nextNode;
			}
			for (int i = 0; i < s.length; i++) {
				LinkedList newNode = new LinkedList(s[i]);
				newNode.nextNode = tmpNode.nextNode;
				tmpNode.nextNode = newNode;
				tmpNode = tmpNode.nextNode;
			}
		}

		LinkedList searchLast(LinkedList Node) {
			if (Node.nextNode == null)
				return Node;
			else {
				return searchLast(Node.nextNode);
			}
		}
	}
}