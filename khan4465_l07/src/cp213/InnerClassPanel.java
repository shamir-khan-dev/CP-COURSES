package cp213;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import java.text.DateFormatSymbols;
import java.util.ArrayList;
import java.util.Arrays;

import javax.swing.BorderFactory;
import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JSeparator;
import javax.swing.JSlider;
import javax.swing.JSpinner;
import javax.swing.JTextField;
import javax.swing.SpinnerListModel;
import javax.swing.SwingConstants;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

@SuppressWarnings("serial")
public class InnerClassPanel extends JPanel {

    private class ButtonListener implements ActionListener {
	@Override
	public void actionPerformed(final ActionEvent e) {
	    final JButton source = (JButton) e.getSource();
	    InnerClassPanel.this.buttonPush = source.getText();
	    InnerClassPanel.this.label.setText(InnerClassPanel.this.buttonPush);
	    System.out.println(InnerClassPanel.this.buttonPush);
	}
    }

    private class CheckBoxListener implements ItemListener {
	@Override
	public void itemStateChanged(final ItemEvent e) {
	    final JCheckBox source = (JCheckBox) e.getItemSelectable();
	    String label = source.getText();
	    if (e.getStateChange() == ItemEvent.SELECTED) {
		InnerClassPanel.this.checkBoxesSelected.add(label);
	    } else {
		InnerClassPanel.this.checkBoxesSelected.remove(label);
	    }
	    InnerClassPanel.this.label.setText(CheckBoxesSelectedToString());
	    System.out.println(CheckBoxesSelectedToString());
	}
    }

    private class RadioButtonListener implements ActionListener {
	@Override
	public void actionPerformed(final ActionEvent e) {
	    final JRadioButton source = (JRadioButton) e.getSource();
	    InnerClassPanel.this.radioButtonSet = source.getText();
	    InnerClassPanel.this.label.setText(InnerClassPanel.this.radioButtonSet);
	    System.out.println(InnerClassPanel.this.radioButtonSet);
	}
    }

    private class SliderListener implements ChangeListener {
	@Override
	public void stateChanged(final ChangeEvent e) {
	    final JSlider source = (JSlider) e.getSource();
	    if (!source.getValueIsAdjusting()) {
		InnerClassPanel.this.sliderSet = source.getValue();
		InnerClassPanel.this.label.setText(Integer.toString(InnerClassPanel.this.sliderSet));
		System.out.println(InnerClassPanel.this.sliderSet);
	    }
	}
    }

    private class SpinnerListener implements ChangeListener {
	@Override
	public void stateChanged(final ChangeEvent e) {
	    InnerClassPanel.this.spinnerSet = InnerClassPanel.this.spinner.getValue().toString();
	    InnerClassPanel.this.label.setText(InnerClassPanel.this.spinnerSet);
	    System.out.println(InnerClassPanel.this.spinnerSet);
	}
    }

    private class TextFieldListener implements ActionListener {
	@Override
	public void actionPerformed(final ActionEvent e) {
	    final JTextField source = (JTextField) e.getSource();
	    InnerClassPanel.this.textEntry = source.getText();
	    InnerClassPanel.this.label.setText(InnerClassPanel.this.textEntry);
	    System.out.println(InnerClassPanel.this.textEntry);
	}
    }

    private static final int START = 0;
    private static final int END = 100;
    private static final int INC = 5;
    private static final String[] MONTH_STRINGS = new DateFormatSymbols().getMonths();
    private static final SpinnerListModel MONTH_MODEL = new SpinnerListModel(MONTH_STRINGS);

    private String buttonPush = "";
    private String radioButtonSet = "";
    private int sliderSet = START;
    private String spinnerSet = "";
    private String textEntry = "";

    private final JButton button = new JButton("Push Me");
    private final ArrayList<String> checkBoxesSelected = new ArrayList<>();
    private final JCheckBox ketchup = new JCheckBox("Ketchup");
    private final JLabel label = new JLabel();
    private final JCheckBox mustard = new JCheckBox("Mustard");
    private final JCheckBox onions = new JCheckBox("Onions");
    private final JSlider slider = new JSlider(JSlider.HORIZONTAL, START, END, INC);
    private final JSpinner spinner = new JSpinner(MONTH_MODEL);
    private final ButtonGroup starGroup = new ButtonGroup();
    private final JRadioButton starTrek = new JRadioButton("Star Trek");
    private final JRadioButton starWars = new JRadioButton("Star Wars");
    private final JTextField textField = new JTextField();

    public InnerClassPanel() {
	layoutView();
	registerListeners();
    }

    private void layoutView() {
	starGroup.add(starTrek);
	starGroup.add(starWars);
	this.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
	this.setLayout(new GridLayout(17, 1, 5, 5));
	this.add(new JLabel("Button"));
	this.add(button);
	this.add(new JLabel("Slider"));
	this.add(slider);
	this.add(new JLabel("Text Field"));
	this.add(textField);
	this.add(new JLabel("Spinner"));
	this.add(spinner);
	this.add(new JLabel("Radio Buttons"));
	this.add(starTrek);
	this.add(starWars);
	this.add(new JLabel("Check Boxes"));
	this.add(mustard);
	this.add(onions);
	this.add(ketchup);
	this.add(new JSeparator(SwingConstants.HORIZONTAL));
	this.add(label);
    }

    private void registerListeners() {
	button.addActionListener(new ButtonListener());
	slider.addChangeListener(new SliderListener());
	textField.addActionListener(new TextFieldListener());
	spinner.addChangeListener(new SpinnerListener());
	starTrek.addActionListener(new RadioButtonListener());
	starWars.addActionListener(new RadioButtonListener());
	ketchup.addItemListener(new CheckBoxListener());
	mustard.addItemListener(new CheckBoxListener());
	onions.addItemListener(new CheckBoxListener());
    }

    public String CheckBoxesSelectedToString() {
	return Arrays.toString(this.checkBoxesSelected.toArray());
    }

    public String getButtonPush() {
	return this.buttonPush;
    }

    public ArrayList<String> getCheckBoxesSelected() {
	return this.checkBoxesSelected;
    }

    public String getRadioButtonSet() {
	return this.radioButtonSet;
    }

    public int getSliderSet() {
	return this.sliderSet;
    }

    public String getSpinnerSet() {
	return this.spinnerSet;
    }

    public String getTextEntry() {
	return this.textEntry;
    }
}
