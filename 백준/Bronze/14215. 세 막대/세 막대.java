import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    // 둘레를 최대로 라고 하고, 각 막대의 길이가 양의 정수라고 하였으므로 최대한 비슷한 수로 맞춰야함
    // 가장 긴 길이의 막대를 줄여가야함
    Scanner sc = new Scanner(System.in);
    int a, b, c;
    int tmp;
    a = sc.nextInt();
    b = sc.nextInt();
    c = sc.nextInt();
    if (a < b) {
      tmp = a;
      a = b;
      b = tmp;
    }
    if (a < c) {
      tmp = a;
      a = c;
      c = tmp;
    }
    // a 를 max로 하자
    while (a >= b + c) {
      a -= 1;
    }
    System.out.println(a + b + c);
  }

}
