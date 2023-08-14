import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static Deque<Deque<Integer>> paper = new ArrayDeque<>();
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		Deque<Character> commandStack = new ArrayDeque<>();
		
		int k = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		
		for(int i = 0 ; i < 2*k; i ++) {
			commandStack.push(st.nextToken().charAt(0));
			
		}
		
		int h = Integer.parseInt(br.readLine());
		Deque<Integer> tmp = new ArrayDeque<>();
		tmp.push(h);
		paper.push(tmp);
//		System.out.println(paper.peek().peek());
		while(!commandStack.isEmpty()) {
			char command = commandStack.pop();
			hole(command);
		}
//		System.out.println();
//		for(int i = 0 ; i < N ; i ++) {
//			for(int j = 0 ;  j < N ; j ++) {
//				System.out.print(graph[i][j]);
//			}
//		}
		
		while (!paper.isEmpty()) {
			Deque<Integer> row = paper.pollFirst();
			while(!row.isEmpty()) {
				System.out.print(row.pollFirst()+ " ");
			}
			System.out.println();
		}
	}
	static void hole(char command) {
		Deque<Deque<Integer>> t_paper = new ArrayDeque<>();
		
		switch (command){
			case 'R':
				while(!paper.isEmpty()) {
					Deque<Integer> tmp = paper.pollFirst(); //한줄씩 뜯어내기
					Deque<Integer> tmpForAdd = new ArrayDeque<>();
					while(!tmp.isEmpty()) {// 하나씩 뜯으면서 좌 우 대칭되게
						int tmpElement = tmp.pollFirst(); // 왼쪽부터 뜯어
						
						tmpForAdd.offerLast(tmpElement);	// 오른쪽에 넣어
						
						if (tmpElement == 1)
							tmpElement =0;
						else if (tmpElement == 3)
							tmpElement =2;
						else
							tmpElement ++; // 뒤집어서 
						
						tmpForAdd.offerFirst(tmpElement);//넣기 (좌우 대칭) // 왼쪽에 넣어
						
					}
					t_paper.offerLast(tmpForAdd);
				}
				paper = t_paper;
				break;
			case 'L':
				while(!paper.isEmpty()) {
					Deque<Integer> tmp = paper.pollFirst(); //한줄씩 뜯어내기
					Deque<Integer> tmpForAdd = new ArrayDeque<>();
					while(!tmp.isEmpty()) {// 하나씩 뜯으면서 좌 우 대칭되게
						int tmpElement = tmp.pollLast(); // 오른쪽부터 뜯어
						
						tmpForAdd.offerFirst(tmpElement); // 왼쪽에 넣어
						
						if (tmpElement == 1)
							tmpElement =0;
						else if (tmpElement == 3)
							tmpElement =2;
						else
							tmpElement ++; // 뒤집어서 
						
						tmpForAdd.offerLast(tmpElement);//넣기 (좌우 대칭) // 왼쪽에 넣어
						
					}
					t_paper.offerLast(tmpForAdd);
				}
				paper = t_paper;
				break;
			case 'D':
				while(!paper.isEmpty()) {
					Deque<Integer> tmp = paper.pollFirst(); //한줄씩 뜯어내기 ( 위쪽부터)
					Deque<Integer> clone = new ArrayDeque<>();
					// 원소 하나하나를 복사해서 다시 넣어야함
					
//					t_paper.push(tmp);
					Deque<Integer> tmpForReverse = new ArrayDeque<>();
					while(!tmp.isEmpty()) {// 하나씩 뜯으면서 위 아래 대칭되게
						int tmpElement = tmp.pollFirst(); // 순서 상관은 없음
						clone.offerLast(tmpElement);	// 원래의 원소를 넣음
						tmpElement += 2;
						tmpElement %= 4;	// 상 하 대칭
						tmpForReverse.offerLast(tmpElement);//넣기 어디 넣-든 상관은 없음
						
					}
					t_paper.offerLast(clone);
					t_paper.offerFirst(tmpForReverse);
				}
				paper = t_paper;
				break;
			case 'U':
				while(!paper.isEmpty()) {
					Deque<Integer> tmp = paper.poll(); //한줄씩 뜯어내기 ( 위쪽부터)
					Deque<Integer> clone = new ArrayDeque<>();
					// 원소 하나하나를 복사해서 다시 넣어야함
//					t_paper.offer(tmp);
					Deque<Integer> tmpForReverse = new ArrayDeque<>();
					while(!tmp.isEmpty()) {// 하나씩 뜯으면서 위 아래 대칭되게
						int tmpElement = tmp.pollFirst(); // 순서 상관은 없음
						clone.offerLast(tmpElement);	// 원래의 원소를 넣음
						tmpElement += 2;
						tmpElement %= 4;	// 상 하 대칭
						tmpForReverse.offerLast(tmpElement);//넣기 어디 넣-든 상관은 없음
						
					}
					t_paper.offerFirst(clone);
					t_paper.offerLast(tmpForReverse);
				}
				paper = t_paper;
				break;
		}
	}
}