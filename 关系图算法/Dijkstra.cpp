#include <iostream>
#include <cstdio>
#define MAX 1005
using namespace std;
int n, m, s, t;
int map[MAX][MAX];
int dis[MAX];
int vis[MAX];

int MIN(int x, int y)
{
    if (x < y)
        return x;
    else
        return y;
}

void Dijkstra()
{
    for (int i = 1; i <= n; i++)
        dis[i] = map[s][i];
    vis[s] = 1;
    dis[s] = 0;

    // 枚举每个点
    for (int i = 1; i < n; i++)
    {
        // 找最短距离
        int min = 0x7f7f7f7f;
        int pos;
        for (int j = 1; j <= n; j++)
        {
            if (!vis[j] && dis[j] < min)
            {
                min = dis[j];
                pos = j;
            }
        }
        if (min == 0x7f7f7f7f)
            break;

        vis[pos] = 1;

        // 扩展最短点
        for (int j = 1; j <= n; j++)
            dis[j] = MIN(dis[j], map[pos][j] + dis[pos]);
    }
}

int main()
{
    scanf("%d %d %d %d", &n, &m, &s, &t);
    memset(vis, 0, sizeof(vis));
    memset(map, 0x7f7f7f7f, sizeof(map));
    while (m--)
    {
        int x, y, w;
        scanf("%d %d %d", &x, &y, &w);
        map[x][y] = map[y][x] = MIN(map[x][y], w);
    }

    Dijkstra();

    cout << dis[t] << endl;

    return 0;
}