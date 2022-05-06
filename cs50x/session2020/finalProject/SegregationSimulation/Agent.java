public class Agent
{
    private int category;
    private boolean satisfied;
    
    public Agent(int c, boolean s)
    {
        category = c;
        satisfied = s;
    }
    
    public int getCategory()
    {
        return category;
    }
    
    public boolean getSatisfied()
    {
        return satisfied;
    }
    
    public void setCategory(int cat)
    {
        category = cat;
    }
    
    public void setSatisfied(boolean mood)
    {
        satisfied = mood;
    }
}