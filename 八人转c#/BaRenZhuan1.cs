using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace BaRenZhuan
{
    /// <summary>
    /// 根据对阵来排查
    /// </summary>
    class BaRenZhuan1
    {
        static int _length = 8;
        static List<int[]> _all = GetAllCombination();
        public static List<int[]> _resultFlag = new List<int[]>();
        public static List<int[]> _result = new List<int[]>();
        static int[,] _teammateNum = new int[_length + 1, _length + 1];
        static int[,] _rivalNum = new int[_length + 1, _length + 1];
        public static List<int[]> _outResult = new List<int[]>();

        //全部组合
        public static List<int[]> GetAllCombination()
        {
            var rs = new List<int[]>();
            for (int i = 1; i <= _length; i++)
            {
                for (int j = i + 1; j <= _length; j++)
                {
                    rs.Add(new int[] { i, j });
                    Console.Write(i + "-" + j + " ");
                }
                Console.Write(Environment.NewLine);
            }
            return rs;
        }
        //计算队友对手数量
        public static void CalcNumber()
        {
            _teammateNum = new int[_length + 1, _length + 1];
            _rivalNum = new int[_length + 1, _length + 1];
            var len = 4;
            foreach (var item in _result)
            {
                for (int i = 0; i < item.Length / len; i++)
                {
                    for (int j = 0; j < len; j++)
                    {
                        var current = item[i * len + j];
                        switch (j)
                        {
                            case 0:
                                _teammateNum[current, item[i * len + j + 1]]++;
                                _rivalNum[current, item[i * len + j + 2]]++;
                                _rivalNum[current, item[i * len + j + 3]]++;
                                break;
                            case 1:
                                _teammateNum[current, item[i * len + j - 1]]++;
                                _rivalNum[current, item[i * len + j + 1]]++;
                                _rivalNum[current, item[i * len + j + 2]]++;
                                break;
                            case 2:
                                _teammateNum[current, item[i * len + j + 1]]++;
                                _rivalNum[current, item[i * len + j - 2]]++;
                                _rivalNum[current, item[i * len + j - 1]]++;
                                break;
                            case 3:
                                _teammateNum[current, item[i * len + j - 1]]++;
                                _rivalNum[current, item[i * len + j - 2]]++;
                                _rivalNum[current, item[i * len + j - 3]]++;
                                break;
                        }
                    }
                }
            }
        }
        //拼凑每行的组合
        public static int[] DepthRow(int[] row, int depth = 0)
        {
            if (depth == _length / 2)
                return row;
            foreach (var item in _all)
            {
                //搭档过 pass
                if (_teammateNum[item[0], item[1]] >= 1)
                    continue;
                var funcTeammateRow = new Func<int[], bool>((a) =>
                {
                    for (int ia = 0; ia < a.Length / 2; ia++)
                    {
                        if (a[ia * 2] == item[0] || a[ia * 2 + 1] == item[0] || a[ia * 2] == item[1] || a[ia * 2 + 1] == item[1])
                            return false;
                    }
                    return true;
                });
                if (!funcTeammateRow(row))
                    continue;
                //对手2次 pass
                var funcRival = new Func<int[], int, bool>((a, dep) =>
                 {
                     var rivalNum = new int[2, _length + 1];

                     for (int ij = 1; ij <= _length; ij++)
                     {
                         for (int iItem = 0; iItem < 2; iItem++)
                         {
                             rivalNum[iItem, ij] = _rivalNum[item[iItem], ij];
                         }
                     }
                     //判断当前行和之前的对手总数大于2 pass
                     if (dep > 0)
                     {
                         switch (dep)
                         {
                             case 1:
                                 rivalNum[0, a[0]]++;
                                 rivalNum[0, a[1]]++;
                                 rivalNum[1, a[0]]++;
                                 rivalNum[1, a[1]]++;
                                 break;
                             case 2:
                                 rivalNum[0, a[6]]++;
                                 rivalNum[0, a[7]]++;
                                 rivalNum[1, a[6]]++;
                                 rivalNum[1, a[7]]++;
                                 break;
                             case 3:
                                 rivalNum[0, a[4]]++;
                                 rivalNum[0, a[5]]++;
                                 rivalNum[1, a[4]]++;
                                 rivalNum[1, a[5]]++;
                                 break;
                         }
                     }
                     for (int ic = 0; ic < 2; ic++)
                     {
                         for (int ij = 0; ij < _length + 1; ij++)
                         {
                             if (rivalNum[ic, ij] > 2)
                                 return false;
                         }
                     }
                     return true;

                 });

                if (!funcRival(row, depth))
                    continue;
                row[depth * 2] = item[0];
                row[depth * 2 + 1] = item[1];
                DepthRow(row, depth + 1);
                if (!_resultFlag.Any(a => Enumerable.SequenceEqual(a, row)))
                    return row;
                else
                {
                    row[depth * 2] = 0;
                    row[depth * 2 + 1] = 0;
                }
            }
            return row;
        }
        public static List<int[]> Generate(int depth = 0)
        {
            if (depth == _length - 1)
                return _result;
            var last = new int[_length];
            while (_result.Count < _length - 1)
            {

                var rs = new int[_length];
                DepthRow(rs);
                _resultFlag.Add(rs);
                if (!rs.Any(r => r == 0))
                {
                    if (depth == 0 && _outResult.Any(a => Enumerable.SequenceEqual(a, rs)))
                        continue;
                    _result.Add(rs);
                    CalcNumber();
                    Generate(depth + 1);
                }
                else
                {
                    if (_result.Count == depth && depth > 0)
                    {
                        _result.RemoveAt(depth - 1);
                        CalcNumber();
                        break;
                    }
                }
            }

            return _result;
        }
    }
}
