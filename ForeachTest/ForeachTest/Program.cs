using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ForeachTest
{
    class Program
    {
        static void Main(string[] args)
        {
            var collection = new MyCollection();

            foreach (MyClass item in collection)
            {
                Console.WriteLine(item.Name);
            }

            Console.ReadKey();
        }
    }
}
