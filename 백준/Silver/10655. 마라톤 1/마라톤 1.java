import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    // TODO Auto-generated method stub
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[][] num_array = new int[N][2];

    for (int i = 0; i < N; i++) {
      num_array[i][0] = sc.nextInt();
      num_array[i][1] = sc.nextInt();
    }
    int sum = 0;
    for (int i = 1; i < N; i++) {
      sum += Math.abs(num_array[i][0] - num_array[i - 1][0]);
      sum += Math.abs(num_array[i][1] - num_array[i - 1][1]);
    }

    int[] tmp_array = new int[N - 2];
    for (int i = 0; i < N - 2; i++) {
      tmp_array[i] = Math.abs(num_array[i + 2][0] - num_array[i][0])
          + Math.abs(num_array[i + 2][1] - num_array[i][1]);
      tmp_array[i] -= Math.abs(num_array[i + 1][0] - num_array[i][0])
          + Math.abs(num_array[i + 1][1] - num_array[i][1]);
      tmp_array[i] -= Math.abs(num_array[i + 2][0] - num_array[i + 1][0])
          + Math.abs(num_array[i + 2][1] - num_array[i + 1][1]);

    }
    int min_value = 2001;
    for (int i = 0; i < N - 2; i++) {
      min_value = Math.min(min_value, tmp_array[i]);
    }
    sum += min_value;
    System.out.println(sum);

  }

}
