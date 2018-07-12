using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace BaRenZhuan
{
    class Program
    {
        static void Main(string[] args)
        {
            var sw = new Stopwatch();
            /*
            1 2 3 4 5 6 7 8
            1 3 5 7 2 4 6 8
            1 4 6 7 2 3 5 8
            1 5 2 6 3 7 4 8
            1 6 3 8 2 5 4 7
            1 7 2 8 3 5 4 6
            1 8 4 5 2 7 3 6  
              
            1 2 3 4 7 8 5 6
            1 3 6 7 2 4 5 8 
            1 4 5 7 2 3 6 8 
            1 5 2 6 4 7 3 8
            1 6 4 8 3 7 2 5 
            1 7 2 8 3 6 4 5
            1 8 3 5 2 7 4 6 
            */
            //验证正确否
            //BaRenZhuan1._result.Add(new int[] { 2, 3, 6, 8, 1, 4, 5, 7 });
            //BaRenZhuan1._result.Add(new int[] { 2, 4, 5, 8, 1, 3, 6, 7 });
            //BaRenZhuan1._result.Add(new int[] { 2, 6, 1, 5, 4, 7, 3, 8 });
            //BaRenZhuan1._result.Add(new int[] { 2, 7, 4, 6, 3, 5, 1, 8 });
            //BaRenZhuan1._result.Add(new int[] { 2, 8, 1, 7, 3, 6, 4, 5 });
            //BaRenZhuan1._result.Add(new int[] { 3, 4, 1, 2, 7, 8, 5, 6 });
            //BaRenZhuan1._result.Add(new int[] { 3, 7, 2, 5, 1, 6, 4, 8 });
            //BaRenZhuan1.CalcNumber();

            while (true)
            {
                sw.Restart();
                //BaRenZhuan1._resultFlag = new List<int[]>();
                //BaRenZhuan1._result = new List<int[]>();
                var result = BaRenZhuan1.Generate();
                //BaRenZhuan1._outResult.Add(result[0]);
                foreach (var item in result)
                {
                    for (int i = 0; i < item.Length; i++)
                    {
                        Console.Write(item[i] + " ");
                    }
                    Console.Write(Environment.NewLine);
                }
                sw.Stop();
                Console.WriteLine("耗时:" + sw.ElapsedMilliseconds + "ms");
            }

        }
    }
}
