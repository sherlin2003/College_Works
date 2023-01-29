package com.example.captcha

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import java.util.*
import android.content.Intent
import android.text.Editable
import android.text.TextWatcher
import android.widget.Toast


class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val phone = findViewById<EditText>(R.id.editTextPhone)
        val cap = findViewById<TextView>(R.id.captcha)
        val ent = findViewById<EditText>(R.id.editTextTextPersonName)
        val but = findViewById<Button>(R.id.button3)
        cap.text = randomString(10)
        ent.addTextChangedListener(object : TextWatcher {
            override fun beforeTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {

            }

            override fun onTextChanged(p0: CharSequence?, p1: Int, p2: Int, p3: Int) {

            }

            override fun afterTextChanged(p0: Editable?) {

                if (cap.text.toString().equals(p0.toString(), true)) {
                    but.setOnClickListener {
                        val intent = Intent(this@MainActivity, MainActivity2::class.java)
                        intent.putExtra("phone", phone.text.toString())
                        Toast.makeText(applicationContext, "Successfully sent", Toast.LENGTH_SHORT)
                            .show()
                        startActivity(intent)
                    }
                }

            }

        })
    }

        fun getRandomNumber(min: Int, max: Int): Int {
            return Random().nextInt((max - min) + 1) + min
        }

        fun randomString(stringLength: Int): String {
            val list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".toCharArray()
            var randomS = ""
            for (i in 1..stringLength) {
                randomS += list[getRandomNumber(0, list.size - 1)]
            }
            return randomS
        }
    }
