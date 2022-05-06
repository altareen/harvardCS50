public class Clustering
{
    private Agent[][] neighbourhood;
    private double threshold;
    
    public Clustering(int size, double t)
    {
        int variety;
        double choice;
        neighbourhood = new Agent[size+2][size+2];
        for (int row = 0; row < neighbourhood.length; row++)
        {
            for (int col = 0; col < neighbourhood[0].length; col++)
            {
                if (row==0 || col==0 || row==neighbourhood.length-1 || col==neighbourhood[0].length-1)
                    variety = 0;
                else
                {
                    choice = Math.random();
                    if (choice < 0.45)
                        variety = 1;
                    else if (choice > 0.55)
                        variety = 2;
                    else
                        variety = 0;
                }
                neighbourhood[row][col] = new Agent(variety, true);
            }
        }
        threshold = t;
    }
    
    public Agent[][] getNeighbourhood()
    {
        return neighbourhood;
    }
    
    public void assessMood()
    {
        for (int row = 1; row < neighbourhood.length-1; row++)
        {
            for (int col = 1; col < neighbourhood[0].length-1; col++)
            {
                int person = neighbourhood[row][col].getCategory();
                int ones = 0;
                int twos = 0;
                for (int i = row-1; i < row+2; i++)
                {
                    for (int j = col-1; j < col+2; j++)
                    {
                        if (neighbourhood[i][j].getCategory()==1 && !(i==row && j==col))
                            ones++;
                        else if (neighbourhood[i][j].getCategory()==2 && !(i==row && j==col))
                            twos++;
                    }
                }
                
                if (person == 1)
                {
                    if (1.0*ones/(ones+twos) > threshold)
                        neighbourhood[row][col].setSatisfied(true);
                    else
                        neighbourhood[row][col].setSatisfied(false);
                }
                else if (person == 2)
                {
                    if (1.0*twos/(ones+twos) > threshold)
                        neighbourhood[row][col].setSatisfied(true);
                    else
                        neighbourhood[row][col].setSatisfied(false);
                }
            }
        }
    }
    
    public void migrate()
    {
        for (int row = 1; row < neighbourhood.length-1; row++)
        {
            for (int col = 1; col < neighbourhood[0].length-1; col++)
            {
                Agent human = neighbourhood[row][col];
                if (human.getSatisfied() == false && human.getCategory() != 0)
                {
                    boolean settled = false;
                    while (!settled)
                    {
                        int randrow = (int) (Math.random()*(neighbourhood.length-2)) + 1;
                        int randcol = (int) (Math.random()*(neighbourhood[0].length-2)) + 1;
                        if (neighbourhood[randrow][randcol].getCategory() == 0)
                        {
                            neighbourhood[randrow][randcol].setCategory(human.getCategory());
                            human.setCategory(0);
                            settled = true;
                        }
                    }
                }
            }
        }
    }
}