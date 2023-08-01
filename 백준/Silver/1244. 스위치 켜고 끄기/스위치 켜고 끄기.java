import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	// 1은 켜져있다. 0 은 꺼져있다.
	// 1 이상, 스위치 개수 이하인 자연수
	// 자신의 성별과 받은 수에 따라 다르게 스위치를 조작
	// 남 : 스위치 번호가 자기가 받은 수의 배수 -> 그 스위치 상태를 바꿈
	// 여 : 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌 우가 대칭이면서 가장 많은 스위치를 포함하는 구간
	// 의 모든 상태를 바꾼다. --> 홀수개
	// 입력으로 스위치들의 처음 상태, 각 학생의 성별, 받은 수
	// 마지막 상태를 출력하라.

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException {
		int switch_cnt = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		boolean[] switches = new boolean[switch_cnt + 1];

		for (int i = 1; i <= switch_cnt; i++) {// 스위치가 1번부터 시작함
			if (st.nextToken().equals("0")) {
				switches[i] = false;
			} else {
				switches[i] = true;
			}
		}

		int student_cnt = Integer.parseInt(br.readLine());

		for (int i = 0; i < student_cnt; i++) {
			st = new StringTokenizer(br.readLine());

			int sex = Integer.parseInt(st.nextToken());
			int num = Integer.parseInt(st.nextToken());

			if (sex == 1) { // 남자라면 해당 수의 배수를 다 바꿈
				for (int j = num; j <= switch_cnt; j += num) {
					switches[j] = !switches[j]; // 뒤집는다.
				}
			} else { // 여자는 대칭되는지를 확인함
				int cnt = 0;

				while (1 <= (num - (cnt + 1)) && (num + cnt + 1) <= switch_cnt) {
					// 대칭하는지 확인해보자
					if (switches[num - (cnt + 1)] == switches[num + (cnt + 1)]) {
						// 대칭한다면 -> cnt += 1
						cnt += 1;
					} else {
						break;
					}

				}
				// 나왔을 때 얼마나 바꿔야할 지 cnt로 나와있음
				for (int j = num - (cnt); j <= (num + cnt); j++) {
					switches[j] = !switches[j]; // 다 뒤집음
				}

			}
		}
		// 이제 출력하면 됨
		for (int i = 1; i <= switch_cnt; i++) {
			int printer = 0;
			if (switches[i])
				printer = 1;
			System.out.print(printer + " ");
			if (i % 20 == 0)
				System.out.println();
		}
	}
}