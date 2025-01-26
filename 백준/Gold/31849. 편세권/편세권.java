import java.util.*;

class Main {
    public static int N;
    public static int M;
    public static int R;
    public static int C;
    public static int[][] graph; 
    public static int[][] dist;  
    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        R = sc.nextInt();
        C = sc.nextInt();

        graph = new int[N][M];
        dist = new int[N][M];

        for (int i = 0; i < R; i++) {
            int roomY = sc.nextInt() - 1;
            int roomX = sc.nextInt() - 1;
            int roomCost = sc.nextInt();
            graph[roomY][roomX] = roomCost;
        }

        for (int i = 0; i < N; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < C; i++) {
            int convY = sc.nextInt() - 1;
            int convX = sc.nextInt() - 1;
            queue.add(new int[]{convX, convY});
            dist[convY][convX] = 0;
        }

        bfs(queue);

        int minScore = Integer.MAX_VALUE;
        for (int y = 0; y < N; y++) {
            for (int x = 0; x < M; x++) {
                if (graph[y][x] > 0) { // 방이 있는 경우
                    int score = dist[y][x] * graph[y][x];
                    minScore = Math.min(minScore, score);
                }
            }
        }

        System.out.println(minScore);
    }

    public static void bfs(Queue<int[]> queue) {
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int d = dist[y][x];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx >= 0 && ny >= 0 && nx < M && ny < N && dist[ny][nx] > d + 1) {
                    dist[ny][nx] = d + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
    }
}
