using System;

namespace Oct25_Ex1
{
    class Program
    {
        public static void DFS(int[,] graph, int[] visited, int start)
        {
            visited[start] = 1;
            Console.Write(start + " "); // print the node
            for (int i = 0; i < graph.GetLength(0); i++)   // for each node
            {
                if (graph[start, i] == 1 && visited[i] == 0) // if there is an edge and the node is not visited
                {
                    DFS(graph, visited, i); // visit the node
                }
            }
            
        }

        // Displays function 
        public static void Display(int[,] graph)
        {
            for (int i = 0; i < graph.GetLength(0); i++)    // for each node
            {
                Console.WriteLine();
                for (int j = 0; j < graph.GetLength(1); j++)    // for each node
                {
                    Console.Write(graph[i, j] + " ");   // print the edge
                }
            }
         
        }
        static void Main(string[] args)
        {
            int[,] graph = new int[5, 5] { { 0, 1, 1, 0, 0 }, { 1, 0, 0, 1, 0 }, { 1, 0, 0, 1, 0 }, { 0, 1, 1, 0, 1 }, { 0, 0, 0, 1, 0 } };
            int[] visited = new int[5];
            Console.WriteLine("The graph is: ");
            Display(graph);
            Console.WriteLine();
            Console.Write("The DFS traversal is: ");
            DFS(graph, visited, 0);
        }        
     
    }
}