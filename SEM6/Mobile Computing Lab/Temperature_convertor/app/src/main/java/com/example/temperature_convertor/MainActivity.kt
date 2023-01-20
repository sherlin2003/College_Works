package com.example.temperature_convertor;
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val showButton = findViewById<Button>(R.id.button3)
        val faren = findViewById<EditText>(R.id.ftoc)
        val cel = findViewById<EditText>(R.id.ctof)

        showButton.setOnClickListener {

            if (cel.isFocused)
            {
                val x = cel.text.toString().toDouble()
                faren.setText((9.toDouble() / 5 * x + 32).toString())
            } else if (faren.isFocused)
            {
                val x = faren.text.toString().toDouble()
                cel.setText(((x - 32) * 5.toDouble() / 9).toString())
            }

        }
    }
}



