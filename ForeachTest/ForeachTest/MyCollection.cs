using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ForeachTest
{
    internal class MyCollection //: IEnumerable
    {
        private readonly List<MyClass> list = new List<MyClass>();

        public MyCollection()
        {
            list.Add(new MyClass {Name = "One"});
            list.Add(new MyClass {Name = "Two"});
            list.Add(new MyClass {Name = "Three"});
        }

        public IEnumerator GetEnumerator()
        {
            return list.GetEnumerator();
        }
    }
}
