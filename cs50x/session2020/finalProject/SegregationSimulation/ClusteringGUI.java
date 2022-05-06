import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.Timer;

public class ClusteringGUI
{
    private static int size = 70;
    private static double threshold = 0.7;
    private static Clustering c = new Clustering(size, threshold);
    private static final JPanel[][] squares = new JPanel[size+2][size+2];
    private static Agent[][] neighbourhood = new Agent[size+2][size+2];

    public static void createAndShowGUI()
    {
        JFrame frame = new JFrame();
        frame.getContentPane().setLayout(null);
        frame.setSize(500,500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        int x = 0;
        int y = 0;
        for (int row = 0; row < squares.length; row++)
        {
            for (int col = 0; col < squares[0].length; col++)
            {
                frame.add(squares[row][col]);
                squares[row][col].setBounds(x,y,500/(size+2),500/(size+2));
                squares[row][col].setBackground(Color.BLUE);
                x += 500/(size+2);
            }
            x = 0;
            y += 500/(size+2);
        }

        Timer timer = new Timer(500/60,new MyActionListener());
        timer.start();
        frame.setVisible(true);
    }

    public static class MyActionListener implements ActionListener
    {
        @Override
        public void actionPerformed(ActionEvent arg0)
        {
            c.assessMood();
            c.migrate();
            neighbourhood = c.getNeighbourhood();
            for (int row = 0; row < neighbourhood.length; row++)
            {
                for (int col = 0; col < neighbourhood[0].length; col++)
                {
                    if (neighbourhood[row][col].getCategory() == 0)
                        squares[row][col].setBackground(Color.GREEN);
                    else if (neighbourhood[row][col].getCategory() == 1)
                        squares[row][col].setBackground(Color.BLUE);
                    else if (neighbourhood[row][col].getCategory() == 2)
                        squares[row][col].setBackground(Color.RED);
                }
            }
        }
    }

    public static void main(String[] args)
    {
        for (int row = 0; row < squares.length; row++)
        {
            for (int col = 0; col < squares[0].length; col++)
            {
                squares[row][col] = new JPanel();
            }
        }
        
        javax.swing.SwingUtilities.invokeLater(new Runnable()
        {
            @Override
            public void run()
            {
                createAndShowGUI();
            }
        });
    }
}
