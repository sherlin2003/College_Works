package com.example.homescreen

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView

class MainActivity3 : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main3)
        setContentView(R.layout.activity_main2)
        val display=findViewById<TextView>(R.id.tv)
        val name=intent.getStringExtra("fname")
        val msg="hello $name , you are successfully registered"
        display.text=msg
    }
}