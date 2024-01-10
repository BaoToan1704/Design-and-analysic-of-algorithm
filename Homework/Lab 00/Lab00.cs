namespace Namespace {
    
    using System;
    
    using System.Linq;
    
    using System.Collections.Generic;
    
    public static class Module {
        
        public static object ex1() {
            var X = 0;
            var n = Convert.ToInt32(input("Enter n: "));
            foreach (var i in Enumerable.Range(2, n + 1 - 2)) {
                X += 1 / (1 - Math.Pow(i, i));
            }
            Console.WriteLine("X = ", X);
        }
        
        public static object ex2() {
            var X = 0;
            var m = Convert.ToInt32(input("Enter m: "));
            var n = Convert.ToInt32(input("Enter n: "));
            foreach (var i in Enumerable.Range(1, n + 1 - 1)) {
                X += Math.Pow(-1, i + 1) * 1 / Math.Pow(m, i);
            }
            Console.WriteLine("X = ", X);
        }
        
        public static object ex3() {
            var Z = 0;
            var n = Convert.ToInt32(input("Enter n: "));
            foreach (var i in Enumerable.Range(0, n + 1)) {
                Z += Math.Pow(i, 3);
            }
            Console.WriteLine("Z = ", Z);
        }
        
        public static object ex4() {
            var n = Convert.ToInt32(input("Enter n: "));
            var f = 1;
            foreach (var i in Enumerable.Range(1, n + 1 - 1)) {
                f *= i;
            }
            Console.WriteLine("n! = ", f);
        }
        
        public static object ex5(object n) {
            if (n == 0) {
                return 1;
            }
            return n * ex5(n - 1);
        }
        
        public static object ex6() {
            // check whether all elements in an array are distinct.
            var n = Convert.ToInt32(input("Enter n: "));
            var a = new List<object>();
            foreach (var i in Enumerable.Range(0, n)) {
                a.append(Convert.ToInt32(input("Enter a number: ")));
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(i + 1, n - (i + 1))) {
                    if (a[i] == a[j]) {
                        Console.WriteLine("Not distinct");
                        return;
                    }
                }
            }
            Console.WriteLine("Distinct");
        }
        
        public static object ex7(object a, object n) {
            if (n == 0) {
                return a[0];
            }
            return max(a[n], ex7(a, n - 1));
        }
        
        public static object ex8() {
            var n = Convert.ToInt32(input("Enter n: "));
            var a = new List<object>();
            foreach (var i in Enumerable.Range(0, n)) {
                a.append(Convert.ToInt32(input("Enter a number: ")));
            }
            var max = a[0];
            foreach (var i in Enumerable.Range(1, n - 1)) {
                if (a[i] > max) {
                    max = a[i];
                }
            }
            Console.WriteLine("Max = ", max);
        }
        
        public static object ex9(object a, object n, object x) {
            if (n == 0) {
                return false;
            }
            if (a[n] == x) {
                return true;
            }
            return ex9(a, n - 1, x);
        }
        
        public static object ex10(object a, object n, object x) {
            if (n == 0) {
                return false;
            }
            if (a[n] == x) {
                return true;
            }
            if (a[n] < x) {
                return false;
            }
            return ex10(a, n - 1, x);
        }
        
        public static object ex11() {
            var n = Convert.ToInt32(input("Enter n: "));
            var a = new List<object>();
            foreach (var i in Enumerable.Range(0, n)) {
                a.append(Convert.ToInt32(input("Enter a number: ")));
            }
            var x = Convert.ToInt32(input("Enter x: "));
            foreach (var i in Enumerable.Range(0, n)) {
                if (a[i] == x) {
                    Console.WriteLine("Found");
                    return;
                }
                if (a[i] > x) {
                    Console.WriteLine("Not found");
                    return;
                }
            }
            Console.WriteLine("Not found");
        }
        
        public static object ex12() {
            var n = Convert.ToInt32(input("Enter n: "));
            var a = new List<object>();
            var b = new List<object>();
            var c = new List<object>();
            foreach (var i in Enumerable.Range(0, n)) {
                a.append(new List<object>());
                b.append(new List<object>());
                c.append(new List<object>());
                foreach (var j in Enumerable.Range(0, n)) {
                    a[i].append(Convert.ToInt32(input("Enter a number: ")));
                    b[i].append(Convert.ToInt32(input("Enter a number: ")));
                    c[i].append(0);
                }
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    foreach (var k in Enumerable.Range(0, n)) {
                        c[i][j] += a[i][k] * b[k][j];
                    }
                }
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    Console.WriteLine(c[i][j], end: " ");
                }
                Console.WriteLine();
            }
        }
        
        public static object ex13() {
            var n = Convert.ToInt32(input("Enter n: "));
            var a = new List<object>();
            var b = new List<object>();
            foreach (var i in Enumerable.Range(0, n)) {
                a.append(new List<object>());
                b.append(new List<object>());
                foreach (var j in Enumerable.Range(0, n)) {
                    a[i].append(Convert.ToInt32(input("Enter a number: ")));
                    b[i].append(0);
                }
            }
            var x = Convert.ToInt32(input("Enter x: "));
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    b[i][j] = a[i][j] * x;
                }
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    Console.WriteLine(b[i][j], end: " ");
                }
                Console.WriteLine();
            }
        }
        
        public static object ex14() {
            var n = Convert.ToInt32(input("Enter n: "));
            var a = new List<object>();
            var b = new List<object>();
            var c = new List<object>();
            foreach (var i in Enumerable.Range(0, n)) {
                a.append(new List<object>());
                b.append(new List<object>());
                c.append(new List<object>());
                foreach (var j in Enumerable.Range(0, n)) {
                    a[i].append(Convert.ToInt32(input("Enter a number: ")));
                    b[i].append(Convert.ToInt32(input("Enter a number: ")));
                    c[i].append(0);
                }
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    c[i][j] = a[i][j] - b[i][j];
                }
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    Console.WriteLine(c[i][j], end: " ");
                }
                Console.WriteLine();
            }
        }
        
        public static object ex15() {
            var n = Convert.ToInt32(input("Enter n: "));
            var a = new List<object>();
            var b = new List<object>();
            var c = new List<object>();
            foreach (var i in Enumerable.Range(0, n)) {
                a.append(new List<object>());
                b.append(new List<object>());
                c.append(new List<object>());
                foreach (var j in Enumerable.Range(0, n)) {
                    a[i].append(Convert.ToInt32(input("Enter a number: ")));
                    b[i].append(Convert.ToInt32(input("Enter a number: ")));
                    c[i].append(0);
                }
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    c[i][j] = a[i][j] + b[i][j];
                }
            }
            foreach (var i in Enumerable.Range(0, n)) {
                foreach (var j in Enumerable.Range(0, n)) {
                    Console.WriteLine(c[i][j], end: " ");
                }
                Console.WriteLine();
            }
        }
    }
}
