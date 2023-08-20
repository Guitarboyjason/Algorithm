import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static boolean[][] visited;
    static int N, M;
    static int[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N][M];

//        int max_num = -1;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
//                if (max_num < arr[i][j])
//                    max_num = arr[i][j]; // 얼마나 돌아야하는지
            }


        }
        // 빡구현하면 될 것 같음
        // 빡구현 하고 매번 줄어들 때 마다 dfs나 bfs로 확인하면서 visited 체크하고
        // 체크 안된 빙산이 있으면 바로 return 해버리는걸로

        int cnt = 0;

//        for (cnt = 0; cnt < max_num; cnt++) { // 중간에 끝나면 그걸 print
        boolean doneFlag = false;
        done:
        while (!doneFlag) {

//            int [][] tmp =
            doneFlag = true;
            visited = new boolean[N][M];
            boolean flag = false;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (arr[i][j] != 0 && !visited[i][j]) {
                        if (!flag) {
                            bfs(i, j);
                            doneFlag = false;
                            flag = true;
                        } else {
                            break done;
                        }
                    }
                }
            }
            cnt++;
        }

        if (doneFlag) {
            System.out.println(0);
        } else {
            System.out.println(cnt);
        }

    }

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    static void bfs(int x, int y) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{x, y});
        visited[x][y] = true;
        while (!queue.isEmpty()) {
            int[] tmp = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = tmp[0] + dx[i];
                int ny = tmp[1] + dy[i];

                if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny]) {
                    // 0이라면 원래 있던 위치에 -1을 하고 아니면 queue에 넣자

                    if (arr[nx][ny] == 0) {
                        if (arr[tmp[0]][tmp[1]] != 0)
                            arr[tmp[0]][tmp[1]] -= 1;
                    } else {

                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                    }
                }
            }
        }
        // 끝나고 나면 -1도 진행됐고 visited도 착실하게 진행됨
    }

}