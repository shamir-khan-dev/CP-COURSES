package cp213;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import java.awt.print.PrinterException;
import java.awt.print.PrinterJob;
import java.text.DecimalFormat;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 * The GUI for the Order class.
 *
 * @author your name here
 * @author Abdul-Rahman Mawlood-Yunis
 * @author David Brown
 * @version 2025-09-07
 */
@SuppressWarnings("serial")
public class OrderPanel extends JPanel {

    /**
     * Implements an ActionListener for the 'Print' button. Prints the current
     * contents of the Order to a system printer or PDF.
     */
    private class PrintListener implements ActionListener {

        @Override
        public void actionPerformed(final ActionEvent e) {
            PrinterJob pj = PrinterJob.getPrinterJob();
            pj.setPrintable(order);
            if (pj.printDialog()) {
                try {
                    pj.print();
                } catch (PrinterException ex) {
                    ex.printStackTrace();
                }
            }
        }
    }

    /**
     * Implements a FocusListener on a JTextField. Accepts only positive integers,
     * all other values are reset to 0. Adds a new MenuItem to the Order with the
     * new quantity, updates an existing MenuItem in the Order with the new
     * quantity, or removes the MenuItem from the Order if the resulting quantity is
     * 0.
     */
    private class QuantityListener implements FocusListener {
        private MenuItem item = null;

        QuantityListener(final MenuItem item) {
            this.item = item;
        }

        @Override
        public void focusGained(final FocusEvent e) {
            JTextField source = (JTextField) e.getSource();
            source.selectAll();
        }

        @Override
        public void focusLost(final FocusEvent e) {
            JTextField source = (JTextField) e.getSource();
            String text = source.getText();
            int quantity = 0;
            try {
                quantity = Integer.parseInt(text);
                if (quantity < 0) {
                    quantity = 0;
                }
            } catch (NumberFormatException nfe) {
                quantity = 0;
            }
            source.setText(String.valueOf(quantity));
            order.update(this.item, quantity);

            subtotalLabel.setText(priceFormat.format(order.getSubTotal()));
            taxLabel.setText(priceFormat.format(order.getTaxes()));
            totalLabel.setText(priceFormat.format(order.getTotal()));
        }
    }

    // Attributes
    private Menu menu = null;
    private final Order order = new Order();
    private final DecimalFormat priceFormat = new DecimalFormat("$##0.00");
    private final JButton printButton = new JButton("Print");
    private final JLabel subtotalLabel = new JLabel("$0.00");
    private final JLabel taxLabel = new JLabel("$0.00");
    private final JLabel totalLabel = new JLabel("$0.00");

    private JLabel nameLabels[] = null;
    private JLabel priceLabels[] = null;
    // TextFields for menu item quantities.
    private JTextField quantityFields[] = null;

    /**
     * Displays the menu in a GUI.
     *
     * @param menu The menu to display.
     */
    public OrderPanel(final Menu menu) {
        this.menu = menu;
        this.nameLabels = new JLabel[this.menu.size()];
        this.priceLabels = new JLabel[this.menu.size()];
        this.quantityFields = new JTextField[this.menu.size()];
        this.layoutView();
        this.registerListeners();
    }

    /**
     * Uses the GridLayout to place the labels and buttons.
     */
    private void layoutView() {
        this.setLayout(new GridLayout(this.menu.size() + 4, 3));

        for (int i = 0; i < this.menu.size(); i++) {
            MenuItem item = this.menu.getItem(i);

            this.nameLabels[i] = new JLabel(item.getName());
            this.priceLabels[i] = new JLabel(this.priceFormat.format(item.getTariff()));
            this.quantityFields[i] = new JTextField("0", 5);
            this.quantityFields[i].setHorizontalAlignment(JTextField.RIGHT);

            this.add(this.nameLabels[i]);
            this.add(this.priceLabels[i]);
            this.add(this.quantityFields[i]);
        }

        // Subtotal
        this.add(new JLabel("Subtotal:"));
        this.add(new JLabel(""));
        this.add(this.subtotalLabel);

        // Tax
        this.add(new JLabel("Tax:"));
        this.add(new JLabel(""));
        this.add(this.taxLabel);

        // Total
        this.add(new JLabel("Total:"));
        this.add(new JLabel(""));
        this.add(this.totalLabel);

        // Button
        this.add(new JLabel(""));
        this.add(new JLabel(""));
        this.add(this.printButton);
    }

    /**
     * Register the widget listeners with the widgets.
     */
    private void registerListeners() {
        // Register the PrinterListener with the print button.
        this.printButton.addActionListener(new PrintListener());

        for (int i = 0; i < this.menu.size(); i++) {
            this.quantityFields[i].addFocusListener(new QuantityListener(this.menu.getItem(i)));
        }
    }
}