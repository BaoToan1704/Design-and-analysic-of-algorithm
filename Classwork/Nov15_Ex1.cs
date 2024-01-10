namespace Namespace {
    
    using System.Collections.Generic;
    
    using System.Linq;
    
    using System.Collections;
    
    public static class Module {
        
        public static object f(object S) {
            if (S.Count == 0) {
                return new List<object> {
                    new HashSet<object>()
                };
            } else {
                var x = S.pop();
                var subsets = f(S);
                return subsets + (from subset in subsets
                    select (subset | new HashSet({
                        x}))).ToList();
            }
        }

        static void 
    }
}