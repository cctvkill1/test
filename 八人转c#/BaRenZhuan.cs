using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BaRenZhuan
{
    /// <summary>
    /// 全队列穷举 然后深度优先 优化剪枝 效果不行
    /// </summary>
    class BaRenZhuan
    {
        static int length = 8;
        static int[][] all = GetAllCombination();
        static List<int[]> result = new List<int[]>();
        static bool rivalFlag = false;
        static bool teammateFlag = false;
        //全组合(只考虑1开头的)
        public static int[][] GetAllCombination()
        {
            var all = new int[length];
            for (int i = 0; i < length; i++)
            {
                all[i] = i + 1;
            }
            var allCombinationNum = 1;
            for (int i = 1; i < length; i++)
            {
                allCombinationNum = i * allCombinationNum;
            }
            var rs = new int[allCombinationNum + 1][];
            var last = length - 1;
            var z = 0;
            var x = last;
            var j = 0;
            rs[j] = new int[length];
            Array.Copy(all, rs[j++], length);
            while (x > 0 && all[0] == 1)
            {
                var y = x--;
                if (all[x] < all[y])
                {
                    z = last;
                    while (all[x] > all[z])
                    {
                        z--;
                    }
                    var tmp = all[z];
                    all[z] = all[x];
                    all[x] = tmp;
                    for (int i = last; i > y; i--, y++)
                    {
                        var temp = all[y];
                        all[y] = all[i];
                        all[i] = temp;
                    }
                    rs[j] = new int[length];
                    Array.Copy(all, rs[j++], length);
                    x = last;
                }
            }
            return rs;
        }

        //统计每个人的对手数量
        public static void TotalNum()
        {
            rivalFlag = false;
            teammateFlag = false;
            var tArr = new int[length + 1][];
            var teamArr = new int[length + 1][];
            for (int i = 0; i < length + 1; i++)
            {
                tArr[i] = new int[length + 1];
                teamArr[i] = new int[length + 1];
            }
            for (int x = 0; x < result.Count; x++)
            {
                for (int y = 0; y < length; y++)
                {
                    var t = result[x][y];
                    var z = y / 2;
                    int t1 = 0;
                    int t2 = 0;
                    int t3 = 0;
                    int t4 = 0;
                    switch (z)
                    {
                        case 0:
                            t1 = result[x][2];
                            t2 = result[x][3];
                            t3 = result[x][0];
                            t4 = result[x][1];
                            break;
                        case 1:
                            t1 = result[x][0];
                            t2 = result[x][1];
                            t3 = result[x][2];
                            t4 = result[x][3];
                            break;
                        case 2:
                            t1 = result[x][6];
                            t2 = result[x][7];
                            t3 = result[x][4];
                            t4 = result[x][5];
                            break;
                        case 3:
                            t1 = result[x][4];
                            t2 = result[x][5];
                            t3 = result[x][6];
                            t4 = result[x][7];
                            break;
                    }
                    if (t1 != 0 && t2 != 0 && t3 != 0 && t4 != 0)
                    {
                        tArr[t][t1]++;
                        tArr[t][t2]++;
                        if (t != t3)
                            teamArr[t][t3]++;
                        if (t != t4)
                            teamArr[t][t4]++;
                        if (tArr[t][t1] > 2)
                        {
                            rivalFlag = true;
                            return;
                        }
                        if (tArr[t][t2] > 2)
                        {
                            rivalFlag = true;
                            return;
                        }
                        if (teamArr[t][t3] > 1)
                        {
                            teammateFlag = true;
                            return;
                        }
                        if (teamArr[t][t4] > 1)
                        {
                            teammateFlag = true;
                            return;
                        }
                    }
                }
            }
        }
        public static List<int[]> Generate(int step = 0)
        {
            if (step == 7)
                return result;
            var tt = result.Count > 0 ? result[result.Count - 1] : null;
            for (int k = 0; k < all.Length; k++)
            {
                var temp = all[k];
                if (tt != null && temp[1] != step + 2) continue;
                if (tt != null && tt[1] >= temp[1]) continue;
                if (tt != null && tt[1] < temp[1] - 1) continue;
                if (result.Contains(temp)) continue;
                result.Add(temp);
                TotalNum();
                if (teammateFlag || rivalFlag)
                {
                    result.Remove(temp);
                    continue;
                }
                Generate(step + 1);
                result.Remove(temp);
            }
            return result;
        }
    }
}
