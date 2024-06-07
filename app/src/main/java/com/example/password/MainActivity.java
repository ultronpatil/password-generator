package com.example.password;

import android.annotation.SuppressLint;
import android.content.ClipData;
import android.content.ClipboardManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.security.SecureRandom;

public class MainActivity extends AppCompatActivity {

    private EditText passwordEditText;
    private Button generatePasswordButton;
    private Button copyPasswordButton;
    private CheckBox includeNumbersCheckbox;
    private CheckBox includeSymbolsCheckbox;
    private CheckBox includeUppercaseCheckbox;
    private CheckBox includeLowercaseCheckbox;
    private TextView passwordLengthTextView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        passwordEditText = findViewById(R.id.passwordEditText);
        generatePasswordButton = findViewById(R.id.generatePasswordButton);
        copyPasswordButton = findViewById(R.id.copyPasswordButton);
        includeNumbersCheckbox = findViewById(R.id.includeNumbersCheckbox);
        includeSymbolsCheckbox = findViewById(R.id.includeSymbolsCheckbox);
        includeUppercaseCheckbox = findViewById(R.id.includeUppercaseCheckbox);
        includeLowercaseCheckbox = findViewById(R.id.includeLowercaseCheckbox);
        passwordLengthTextView = findViewById(R.id.passwordLengthTextView);

        // Create a new SeekBar programmatically
        SeekBar passwordLengthSeekBar = new SeekBar(this);

        // Set SeekBar attributes
        passwordLengthSeekBar.setId(View.generateViewId()); // Generate a unique ID for the SeekBar
        RelativeLayout.LayoutParams params = new RelativeLayout.LayoutParams(
                RelativeLayout.LayoutParams.MATCH_PARENT,
                RelativeLayout.LayoutParams.WRAP_CONTENT
        );
        params.addRule(RelativeLayout.BELOW, R.id.includeLowercaseCheckbox);
        params.setMargins(20, 0, 20, 0); // Set margins as needed
        passwordLengthSeekBar.setLayoutParams(params);
        passwordLengthSeekBar.setMax(20 - 10); // Set maximum value to the range length
        passwordLengthSeekBar.setProgress(10); // Set initial progress to the minimum value of the range
        // Add SeekBar to the layout
        RelativeLayout layout = findViewById(R.id.parentLayout);
        layout.addView(passwordLengthSeekBar);


        generatePasswordButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (!includeNumbersCheckbox.isChecked() &&
                        !includeSymbolsCheckbox.isChecked() &&
                        !includeUppercaseCheckbox.isChecked() &&
                        !includeLowercaseCheckbox.isChecked()) {
                    Toast.makeText(MainActivity.this, "Select at least two options", Toast.LENGTH_SHORT).show();
                    return;
                }

                int passwordLength = passwordLengthSeekBar.getProgress() + 10; // Add 10 to the progress to get the actual length
                String password = generateRandomPassword(passwordLength,
                        includeNumbersCheckbox.isChecked(),
                        includeSymbolsCheckbox.isChecked(),
                        includeUppercaseCheckbox.isChecked(),
                        includeLowercaseCheckbox.isChecked());

                passwordEditText.setText(password);
            }
        });

        copyPasswordButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String password = passwordEditText.getText().toString();
                if (!password.isEmpty()) {
                    ClipboardManager clipboardManager = (ClipboardManager) getSystemService(CLIPBOARD_SERVICE);
                    ClipData clipData = ClipData.newPlainText("Password", password);
                    clipboardManager.setPrimaryClip(clipData);
                    Toast.makeText(MainActivity.this, "Password copied to clipboard", Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "No password to copy", Toast.LENGTH_SHORT).show();
                }
            }
        });

        passwordLengthSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                int passwordLength = progress + 10; // Add 10 to the progress to get the actual length
                passwordLengthTextView.setText(getString(R.string.password_length, passwordLength));
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
                // Not needed for this implementation
            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
                // Not needed for this implementation
            }
        });
    }

    private String generateRandomPassword(int length, boolean includeNumbers, boolean includeSymbols, boolean includeUppercase, boolean includeLowercase) {
        StringBuilder password = new StringBuilder(length);
        String characters = "";

        if (includeNumbers) {
            characters += "0123456789";
        }
        if (includeSymbols) {
            characters += "!@#$%^&*()-_=+{}[]|:;<>,.?/";
        }
        if (includeUppercase) {
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        }
        if (includeLowercase) {
            characters += "abcdefghijklmnopqrstuvwxyz";
        }

        if (characters.isEmpty()) {
            return "";
        }

        SecureRandom random = new SecureRandom();

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            password.append(characters.charAt(index));
        }

        return password.toString();
    }
}
