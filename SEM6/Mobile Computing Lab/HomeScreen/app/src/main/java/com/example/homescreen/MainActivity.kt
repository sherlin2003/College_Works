package com.example.homescreen

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.content.Intent
import android.view.View.VISIBLE
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val first = findViewById<EditText>(R.id.editTextTextPersonName)
        val last = findViewById<EditText>(R.id.editTextTextPersonName3)
        val phone = findViewById<EditText>(R.id.editTextPhone)
        val email = findViewById<EditText>(R.id.editTextTextEmailAddress)
        val bdate = findViewById<EditText>(R.id.editTextDate)
        val gender= findViewById<EditText>(R.id.editTextTextPersonName6)
        val address = findViewById<EditText>(R.id.editTextTextPersonName7)
        val button = findViewById<Button>(R.id.button)
        button.setOnClickListener {
            val finame = first.text.toString()
            if (first.text.toString() == "" || last.text.toString() == "" || phone.text.toString() == "" || email.text.toString() == "" || bdate.text.toString() == "" || gender.text.toString()== "" || address.text.toString() == "") {
                Toast.makeText(
                    this@MainActivity,
                    "please enter all the details",
                    Toast.LENGTH_LONG
                ).show()
            } else {
                button.visibility = VISIBLE
                val abc = Intent(this@MainActivity, MainActivity2::class.java)
                abc.putExtra("fname", finame)
                startActivity(abc)
            }
        }
    }
}

