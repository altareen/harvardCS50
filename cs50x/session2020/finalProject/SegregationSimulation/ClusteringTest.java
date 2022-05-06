public class ClusteringTest
{
    public static void displayGrid(Agent[][] arr)
    {
        for (Agent[] row : arr)
        {
            for (Agent item : row)
            {
                System.out.print(item.getCategory() + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    
    // debugging purposes
    public static void displayMood(Agent[][] arr)
    {
        for (Agent[] row : arr)
        {
            for (Agent item : row)
            {
                System.out.print(item.getSatisfied() + " ");
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args)
    {
        Clustering c = new Clustering(15, 0.3);
        
        for (int i = 0; i < 100; i++)
        {
            c.assessMood();
            c.migrate();
            displayGrid(c.getNeighbourhood());
        }
    }
}
